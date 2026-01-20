# Keyword Matching & Scoring Rules

This document defines the rules for calculating alignment scores and determining when/how to integrate keywords into the resume.

---

## Alignment Score Calculation

### Formula

```
Alignment Score = (Matched High × 3 + Matched Med × 2 + Matched Low × 1) / (Total High × 3 + Total Med × 2 + Total Low × 1) × 100
```

### Score Interpretation

| Score       | Rating    | Action                                             |
| ----------- | --------- | -------------------------------------------------- |
| **85-100%** | Excellent | Minor tweaks only, focus on phrasing               |
| **70-84%**  | Good      | Integrate 2-3 missing High keywords                |
| **50-69%**  | Fair      | Significant edits needed, prioritize High keywords |
| **< 50%**   | Poor      | Consider if role is a good fit                     |

---

## Keyword Priority Definitions

### 🔴 High Priority — Must integrate if missing

**Criteria** (any of the following):

- Mentioned 2+ times in JD
- Appears in "Required Qualifications" section
- Industry-specific term (e.g., "healthcare", "SaaS", "medical device")
- Core methodology for the role (e.g., "product roadmap", "user research")

**Integration urgency**: Critical — ATS will likely filter without these

---

### 🟠 Medium Priority — Integrate if natural fit exists

**Criteria**:

- Mentioned once in requirements
- Common PM tools (e.g., "Jira", "Figma")
- Transferable skills (e.g., "cross-functional", "stakeholder management")
- Domain-adjacent terms (e.g., "UX collaboration")

**Integration urgency**: Important — strengthens application but not dealbreakers

---

### 🟢 Low Priority — Integrate only if space allows

**Criteria**:

- Listed in "Nice-to-have" or "Preferred" sections
- Generic tools (e.g., "Excel", "Microsoft Office")
- Soft skill adjacent (e.g., "communication skills")
- Credentials not required (e.g., "PMP certification a bonus")

**Integration urgency**: Optional — deprioritize if resume is tight on space

---

## Keyword Categories

Use these categories to label each keyword:

| Category        | Description             | Examples                                                   |
| --------------- | ----------------------- | ---------------------------------------------------------- |
| **Industry**    | Sector/vertical         | healthcare, fintech, e-commerce, medical devices           |
| **Technology**  | Technical domains/tools | AI, ML, LLM, robotics, operating system                    |
| **Methodology** | PM frameworks/processes | Agile, user research, A/B testing, NPI, lifecycle          |
| **Tool**        | Specific software       | Jira, Figma, SQL, Tableau, GitHub                          |
| **Skill**       | Competencies            | cross-functional, stakeholder management, UX collaboration |
| **Deliverable** | Artifacts produced      | PRD, roadmap, market analysis                              |
| **Credential**  | Certifications/degrees  | PMP, MBA, Master's degree                                  |
| **Stakeholder** | People you work with    | surgeons, engineers, customers                             |
| **Regulatory**  | Compliance/legal        | FDA, DHF/DMR/DHR                                           |

---

## Integration Rules

### Rule 0: Semantic Fit Check (GATE)

**Before suggesting ANY keyword integration, ask:**

> "Does this keyword describe something the candidate _actually did_ in that role, even if phrased differently?"

If NO → **Do not integrate.** Mark as `~~keyword~~ _no semantic fit_` and skip.

**Semantic fit means:**

- The keyword describes the _same type of work_, not just similar-sounding words
- Adding the keyword doesn't change _what the bullet claims you did_
- A hiring manager reading both versions would understand them as the same accomplishment

**Examples of BAD semantic fit:**

| Original                             | Keyword                    | Why It Fails                                                 |
| ------------------------------------ | -------------------------- | ------------------------------------------------------------ |
| "Built a smart recorder OS"          | **content curation**       | Recorder captures audio, doesn't curate content from sources |
| "Integrated with Uber, Spotify apps" | **third-party content**    | Apps ≠ content publishers/news sources                       |
| "Optimized onboarding funnel"        | **recommendation systems** | Funnel optimization ≠ ML-based content ranking               |
| "Conducted user research"            | **quality signals**        | Research methods ≠ content trustworthiness signals           |

**Examples of GOOD semantic fit:**

| Original                        | Keyword              | Why It Works                        |
| ------------------------------- | -------------------- | ----------------------------------- |
| "Deployed LLMs through APIs"    | **Generative AI**    | Same technology, different phrasing |
| "Aligned 8+ stakeholders"       | **cross-functional** | Same collaboration, JD terminology  |
| "Created go-to-market strategy" | **GTM strategy**     | Exact same deliverable              |

**When semantic fit fails for most High-priority keywords:**

- Warn user: `⚠️ Low semantic fit (~X%). This role may not be a strong match.`
- Suggest skipping or applying minimal transferable-skill edits only

---

### Rule 1: Fact Flexibility by Priority

**Default behavior**: Rephrase existing facts using JD terminology without inventing new claims.

**Exception for 🔴 High Priority keywords**: When a High priority requirement is missing and critical for ATS passage, you may **strategically embellish** metrics, experiences, or accomplishments — provided they:

1. **Pass Rule 0** — semantic fit check must be satisfied first
2. **Look plausible** given the candidate's background
3. **Are relevant** to the actual work performed
4. **Cannot be easily disproved** in an interview
5. **Enhance rather than fabricate** — stretch existing experience, don't invent from scratch
6. **NEVER fabricate domain expertise** — Do not add specific clinical conditions (e.g., "metabolic health", "cardiology"), niche industries, or technical certifications (e.g., "FDA compliance") if not in the candidate's background. Focus on **Methodology Alignment** instead.

| Priority | Invention Allowed?   | Guidance                                            |
| -------- | -------------------- | --------------------------------------------------- |
| 🔴 High  | ✅ Yes, if plausible | Stretch existing experience to match JD terminology |
| 🟠 Med   | ⚠️ Minimal           | Only rephrase, don't add new claims                 |
| 🟢 Low   | ❌ No                | Preserve original facts exactly                     |

**Examples**:

❌ Wrong: Adding "robotics experience" when you've never touched robotics  
✅ Right: Rephrasing "IoT device development" → "embedded systems and robotics-adjacent development"

❌ Wrong: Claiming "FDA regulatory experience" with no exposure  
✅ Right: Expanding "worked with legal/compliance teams" → "ensured compliance with regulatory requirements"

---

### Rule 2: Character Length Constraint

Edited bullets must stay within **±10% character count** of the original.

| Original Length | Min | Max |
| --------------- | --- | --- |
| 100 chars       | 90  | 110 |
| 150 chars       | 135 | 165 |
| 200 chars       | 180 | 220 |

---

### Rule 3: Prioritize High → Med → Low

When integrating keywords, always prioritize:

1. Missing 🔴 High keywords first
2. Then 🟠 Medium if natural fit
3. Only 🟢 Low if space allows and highly relevant

---

### Rule 4: One Keyword Per Bullet

Avoid stuffing multiple keywords into a single bullet. Spread them across different bullets for natural reading.

❌ Wrong: "Led cross-functional, agile, data-driven product roadmap..."  
✅ Right: Integrate one keyword per bullet across 3 separate bullets

---

### Rule 5: Match Terminology Exactly

Use the **exact phrasing** from the JD when possible.

| JD Says                    | Resume Should Say                                 |
| -------------------------- | ------------------------------------------------- |
| "voice of customer"        | "voice of customer" (not "customer feedback")     |
| "new product introduction" | "new product introduction" (not "product launch") |
| "cross-functional"         | "cross-functional" (not "interdisciplinary")      |

## Gap Analysis Output Format

```markdown
## Gap Analysis: [Company Name]

🎯 ██████░░░░ **60%** Fair

### ✓ Matched Keywords

`keyword1` · `keyword2` · `keyword3` · `keyword4` · `keyword5`

### ✗ Missing Keywords

|     | Keyword      | Integration                 |
| --- | ------------ | --------------------------- |
| 🔴  | **keyword1** | → Section, bullet X         |
| 🟠  | **keyword2** | → Skills section            |
| 🟠  | ~~keyword3~~ | _too niche, skip_           |
| 🟢  | ~~keyword4~~ | _credential not held, skip_ |
```

### Alignment Format

```
🎯 ████████░░ **75%** Good (3 edits)
✅ ██████████ **92%** Excellent (1 edit)
⚠️ ██████░░░░ **58%** Fair (5 edits)
❌ ████░░░░░░ **42%** Poor (8 edits)
```

### Alignment Emoji Scale

| Score   | Emoji | Rating    |
| ------- | ----- | --------- |
| 85-100% | ✅    | Excellent |
| 70-84%  | 🎯    | Good      |
| 50-69%  | ⚠️    | Fair      |
| <50%    | ❌    | Poor      |

---

## Edit Suggestion Output Format

Show only the **changed portion** of each bullet, not the full sentence.

```markdown
### Suggested Edits

\`\`\`diff

# UW Medicine #2

- ...emerging technologies, like Generative AI, by deploying...

* ...Generative AI with RAG architecture, deploying...
  \`\`\`
  ↳ Adds **RAG** (🔴) | +3 chars

\`\`\`diff

# OnePlus #2

- Defined success metrics and conducted...

* Defined OKRs and success metrics, conducted...
  \`\`\`
  ↳ Adds **OKR** (🔴) | +10 chars

---

**Commands:** `Accept all` | `Accept 1` | `Reject 2` | `More options`
```

Always ask user to Accept/Reject before applying.

---

## Format Rules

1. **Battery-style alignment** — Use emoji + progress bar + edit count in parentheses
2. **Show ALL suggested edits** — Every missing keyword marked for integration must have a corresponding edit
3. **Compact diffs for partial changes** — If only sentence ending changes, show only that portion
4. **Full diffs for complete rewrites** — If entire bullet changes, show full before/after
5. **No redundant acronyms** — Write "new product introduction" not "new product introduction (NPI)"
6. **Check Education section** — Skills mentioned in Education (e.g., Robotics) count as matched
7. **Explain skipped keywords** — Mark as ~~strikethrough~~ with _italicized reason_
8. **One-page constraint** — Edits must not cause line overflow. Track character budget:
   - Before editing, ensure new length ≤ original OR compensate by trimming elsewhere
   - Warn user if edit would cause overflow: `⚠️ +15 chars may overflow line`
9. **3 options max per keyword** — When user requests alternatives, show at most 3 options in diff style grouped by keyword
10. **Job Analysis → Log file** — Save full analysis to `output/logs/{Company}_analysis.md`, show only Gap Analysis to user
11. **No auto-open PDF** — Generate silently, cleanup temp file after edits confirmed
12. **Net-zero character budget** — Track cumulative character changes across all edits:
    - Display running total after each edit: `Net: +45 chars`
    - If total additions > **50 characters**, require compensatory trimming elsewhere
    - Suggest trimmable bullets when suggesting additions
13. **Pre-compile validation** — Before finalizing PDF, compile and verify page count = 1:
    - If overflow detected, abort and warn user: `⚠️ Overflow detected (2 pages). Trimming required.`
    - Suggest specific bullets to shorten
