---
description: Customize resume for a job description using AI analysis
---

# Resume Customization Workflow

This workflow helps you tailor your resume for a specific job posting using Gemini AI.

## Prerequisites

- Persona directory at `personas/{persona}/`
  - Master resume: `{persona}_{role}_master_resume.typ`
  - Career profile: `{persona}_career_profile.md` (optional)
  - Config: `config.yaml`
- Typst installed (`typst --version`)
- Virtual environment at `.venv`
- **Training Reference**: See `docs/training_reference.md` for gold standard examples
- **Scoring Rules**: See `docs/scoring_rules.md` for alignment calculation and integration rules

## Default Persona

Default: Varies (set via `/persona-switch`)

## Workflow Steps

### Step 0: Load Persona

Read current persona from `.current_persona` (set via `/persona-switch`):

// turbo

```bash
read PERSONA ROLE < .current_persona
echo "Using: $PERSONA ($ROLE)"
```

**Validate resume exists:**

// turbo

```bash
read PERSONA ROLE < .current_persona
if [ ! -f "personas/$PERSONA/${PERSONA}_${ROLE}_master_resume.typ" ]; then
  echo "❌ Resume not found. Run /persona-switch to set persona."
  exit 1
fi
```

> To change persona, use `/persona-switch [persona] [role]`

### Step 1: Collect Job Description

Ask the user to provide the job description. They can either:

- Paste it directly in chat
- Provide a URL to scrape
- Point to a file

### Step 1.5: Select Mode (Default: Manual Review)

Ask: **"Quick auto-generate or manual review?"** (default: manual)

| Mode                             | Behavior                                                               |
| -------------------------------- | ---------------------------------------------------------------------- |
| **🔍 Manual Review** _(default)_ | Analyze → Show gap analysis → Present edit options → Wait for approval |
| **🚀 Autonomous**                | Analyze → Apply all High/Med edits → Generate PDF → Notify             |

**Trigger Autonomous mode only if** user explicitly says "auto", "quick", "just do it".
Otherwise, default to Manual Review.

### Step 2: Analyze Job Description (Background)

**Follow the methodology in `docs/training_reference.md` exactly.**

Extract silently and **save to log file** `output/{PERSONA}/resume-analysis/{Company}_analysis.md`:

1. **Job Metadata**: Role, Company, Location, Seniority, Role Type, Salary
2. **ATS Keywords**: Prioritized as 🔴 High, 🟠 Medium, 🟢 Low with category labels
3. **Top 5 Requirements**: Non-negotiable qualifications only
4. **Nice-to-haves**: Explicitly stated as preferred/bonus

**Constraint**: Do NOT artificially limit the number of keywords (e.g. to 7 High/4 Med). Extract ALL keywords that materially impact ATS ranking. A typical list might have 10-20 High, 5-10 Med, and 5-10 Low.

// turbo

```bash
read PERSONA ROLE < .current_persona
mkdir -p "output/$PERSONA/resume-analysis"
```

**Do not display to user** — proceed directly to Gap Analysis.

### Step 3: Gap Analysis (User-Facing)

**Follow the scoring formula in `docs/scoring_rules.md`.**

Compare extracted requirements against `personas/{PERSONA}/{PERSONA}_{ROLE}_master_resume.typ`:

- **Matched Keywords**: Inline list with backticks
- **Missing Keywords**: Table with **4 columns**: `Priority` (Emoji), `Keyword`, `Category`, `Integration`
- **Alignment Score**: Battery-style with emoji and edit count

Present this analysis to the user — this is the **first output they see**.

**Also append to** `output/resume-analysis/{Company}_analysis.md`:

```markdown
## Gap Analysis

🎯 ████████░░ **XX%** [Status] (N edits)

### ✓ Matched Keywords

`keyword` · `keyword` · ...

### ✗ Missing Keywords

| Priority | Keyword     | Category | Integration       |
| :------- | :---------- | :------- | :---------------- |
| 🔴       | **keyword** | Industry | → Skills section  |
| 🟠       | **keyword** | Tool     | → Work exp bullet |
```

### Step 4: Suggest Edits — MANDATORY DIFF FORMAT

> ⚠️ **You MUST show diffs for EVERY suggested edit. Do not summarize. Show only the changed portion.**

**Follow `docs/scoring_rules.md` for all edit rules:**

- **Rule 0**: Translation Allowed, Fabrication BANNED (Do not change domain/product type)
- **Rule 1**: Fact Flexibility — use "Bridging" phrases for High priority keywords
- **Rule 2**: ±10% character length constraint
- **Rule 3**: Prioritize High → Med → Low
- **Rule 4**: One keyword per bullet
- **Rule 5**: Match JD terminology exactly
- **Rule 6**: Core Entity Preservation — NEVER delete feature names

**Negative Constraints:**

- ❌ Do not invent B2B SaaS experience if only B2C exists.
- ❌ Do not rename hardware products to software platforms.
- ❌ Do not delete specific feature names (e.g., "recording scenes") to make space.

Format using diff style (see `docs/scoring_rules.md` § Edit Suggestion Output Format):

```diff
# Section, Bullet X
- ...original text...
+ ...modified text...
```

↳ Adds **keyword** (🔴 High) | +X chars

### Step 5: User Approval

Present all suggestions and ask user to:

- Accept individual edits: "Accept 1, 3, 5"
- Accept all: "Accept all"
- Reject specific: "Reject 2"
- Request revision: "Revise 4 to focus more on..."

### Step 6: Apply Edits (Copy-First Approach)

Create a temporary copy, apply edits, export PDF, then delete the temp file.

// turbo

```bash
cd .
cp personas/{PERSONA}/{PERSONA}_{ROLE}_master_resume.typ personas/{PERSONA}/temp_customized.typ
```

Apply approved changes to `typst/temp_customized.typ` only. Master remains untouched.

**Also append to** `output/resume-analysis/{Company}_analysis.md`:

```markdown
## Edits Applied

| #   | Keyword     | Section  | Accepted     |
| --- | ----------- | -------- | ------------ |
| 1   | **keyword** | Bullet X | ✔            |
| 2   | **keyword** | Skills   | ✘ (rejected) |

### Diff

\`\`\`diff

# Section, Bullet X

- original text...

* modified text...
  \`\`\`
```

### Step 6.5: Page Count Validation

Before final compile, verify the resume fits on one page:

// turbo

```bash
cd .
typst compile personas/{PERSONA}/temp_customized.typ /tmp/resume_check.pdf
PAGE_COUNT=$(.venv/bin/python -c "import fitz; print(len(fitz.open('/tmp/resume_check.pdf')))")
if [ "$PAGE_COUNT" -gt 1 ]; then
  echo "⚠️ Overflow detected ($PAGE_COUNT pages). Trimming required."
  rm personas/{PERSONA}/temp_customized.typ /tmp/resume_check.pdf
  exit 1
fi
rm /tmp/resume_check.pdf
```

If validation fails, abort and suggest specific bullets to shorten.

### Step 6.6: Runt/Orphan Validation

After page count check, verify no "runts" (dangling short words) exist.

// turbo

```bash
cd .
RUNTS=$(.venv/bin/python -c "from backend.monitor import detect_runts; import json; print(json.dumps(detect_runts('/tmp/resume_check.pdf')))")
if [ "$RUNTS" != "[]" ]; then
  echo "⚠️ Runts detected!"
  echo "$RUNTS" | jq -r '.[] | "- Page \(.page): \"\(.text)\""'

  # Auto-fix attempt
  echo "🔄 Attempting auto-fix..."
  FIXES=$(.venv/bin/python -c "from backend.fixer import fix_runts; import json, sys; runts=json.loads(sys.argv[1]); print(json.dumps(fix_runts(runts)))" "$RUNTS")

  # Apply fixes to the temp file (complex sed/replacement needed, or simpler: just notify user for now in manual mode)
  # For MVP: We show the suggested fixes
  echo "💡 Suggested changes:"
  echo "$FIXES" | jq -r 'to_entries[] | "Change: \(.key)\nTo:     \(.value)\n"'

  # TODO: Implement auto-apply logic by matching strings in the .typ file
fi
```

### Step 7: Compile & Cleanup

// turbo

```bash
cd .
typst compile personas/{PERSONA}/temp_customized.typ "output/{PERSONA}/resumes/{COMPANY}_{JOBROLE}_{NAME}.pdf"
```

**Do not auto-open PDF.** After compile, immediately cleanup:

// turbo

```bash
rm "personas/{PERSONA}/temp_customized.typ"
```

Notify user with confirmation:

```
✅ Resume saved: output/{PERSONA}/resumes/{COMPANY}_{JOBROLE}_{NAME}.pdf
```

**Naming convention**: `{COMPANY}_{JOBROLE}_{NAME}.pdf`

Variables:

- `{PERSONA}` = selected persona (e.g., alex)
- `{COMPANY}` = from JD analysis
- `{JOBROLE}` = from JD analysis (e.g., Product Manager)
- `{NAME}` = from config.yaml (e.g., Alex Chen)

Examples:

- `EnsoData_Product Manager_Alex Chen.pdf`
- `Google_AI PM_Alex Chen.pdf`
- `Globus Medical_Product Manager_Alex Chen.pdf`

---

## 🚀 Autonomous Mode Flow

If user selects autonomous mode, execute Steps 2-8 without pausing for approval:

1. Analyze JD → extract keywords
2. Run gap analysis → identify missing High/Med keywords
3. Generate edits for all missing High and Med priority keywords
4. Apply edits to temp file (skip Low priority)
5. Compile PDF with naming convention
6. Delete temp file
7. Notify user with single message:

```
✅ Resume generated: Company_Role_Alex Chen.pdf

Alignment: 🎯 ██████░░░░ 64% Fair
Edits applied: 5 (medical device, Jira, cross-functional, FDA, ISO 13485)
```

---

## 📦 Batch Mode

Process multiple job descriptions at once. Always uses Autonomous mode.

### Trigger

User provides multiple JDs in one of these formats:

- Multiple text blocks separated by `---`
- List of URLs
- Folder path containing `.txt` or `.md` JD files

### Flow

1. Parse all JDs
2. For each JD, run full autonomous flow:
   - Analyze → Gap analysis → Generate edits → Apply → Export PDF
3. Summarize results in single notification:

```
✅ Batch complete: 5 resumes generated

| Company | Role | Alignment | PDF |
|---------|------|-----------|-----|
| EnsoData | Product Manager | 🎯 74% | [View](file://...) |
| Google | AI PM | ⚠️ 68% | [View](file://...) |
| Globus | Medical Device PM | ⚠️ 60% | [View](file://...) |
| Meta | Healthcare PM | 🎯 82% | [View](file://...) |
| Amazon | Technical PM | ✅ 88% | [View](file://...) |
```

### Batch Commands

```bash
# Compile all in sequence
for jd in jd_files/*.txt; do
  company=$(basename "$jd" .txt)
  cp typst/master_resume.typ typst/temp_customized.typ
  # Apply edits...
  typst compile typst/temp_customized.typ "output/resumes/${company}_Alex Chen.pdf"
  rm typst/temp_customized.typ
done
```

---

## Key Constraints

1. **Length Preservation**: Edited bullets should stay within ±10% character count
2. **Fact Flexibility**: May embellish for High priority keywords only (see `docs/scoring_rules.md`)
3. **Format Stability**: Don't add/remove sections, just modify content
4. **One Page**: Resume must remain a single page — track character budget
5. **Font Consistency**: Always use Myriad Pro

## Example Interaction

```
User: /resume

Agent: Please paste the job description. Quick auto-generate or manual review? (default: manual)

User: [pastes JD]

Agent: ## Gap Analysis: Google

🎯 ██████████ **82%** Good (1 edit)

### ✓ Matched Keywords
`LLM` · `cross-functional` · `roadmap` · `product management`

### ✗ Missing Keywords
| Priority | Keyword | Category | Integration |
| :--- | :--- | :--- | :--- |
| 🔴 | **TensorFlow** | Technology | → Skills section |
| 🟠 | **technical presentations** | Skill | → Samsung bullet 2 |

### Suggested Edits

\`\`\`diff
# Skills
- Technical: Python, Figma, SQL, Git, Jira, ROS...
+ Technical: Python, TensorFlow, Figma, SQL, Git, Jira, ROS...
\`\`\`
↳ Adds **TensorFlow** (🔴 High) | +12 chars

**Commands:** `Accept all` | `Accept 1` | `Reject 1` | `More options`
```
