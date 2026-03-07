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

> **Constraint**: Do not target a specific number of keywords (e.g., 7 High, 4 Med). The number of keywords should reflect the complexity of the JD. A complex JD might have 15 High keywords; a simple one might have 5.

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

### Rule 0: Semantic Fit Check (The "Translation vs. Fabrication" Gate)

**Before suggesting ANY keyword integration, apply this framework:**

#### ✅ Safe Translation (Allowed)

You can rename a _process_, _skill_, or _methodology_ using JD terminology if the underlying activity is fundamentally the same.

- _Ex:_ "User research" → "Discovery"
- _Ex:_ "Algorithmic development" → "Model tuning"
- _Ex:_ "Stakeholder alignment" → "Cross-functional collaboration"

#### ❌ Unsafe Fabrication (BANNED)

You CANNOT change the **Business Model**, **Domain**, or **Core Product Type**.

- _Ex:_ "Smart Recorder (Hardware)" → "Call Automation (SaaS)" (Mismatch: Product Type)
- _Ex:_ "Consumer App" → "B2B Platform" (Mismatch: Business Model)
- _Ex:_ "Mobile Game" → "Enterprise Software" (Mismatch: Domain)

**If Unsafe Fabrication detected:**
Do not integrate. Suggest "Bridging" (Rule 1) or skip entirely.

---

### Rule 1: Fact Flexibility ("Bridging" instead of "Claiming")

**Default behavior**: Rephrase existing facts using JD terminology without inventing new claims.

**For 🔴 High Priority keywords with imperfect fit:**
Use **Bridging Phrases** to connect existing experience to the keyword without claiming direct ownership if it doesn't exist.

- **Instead of:** "Built [Keyword]" (when you didn't)
- **Use:** "Applied [Skill] _relevant to_ [Keyword]" or "experience _aligned with_ [Keyword]"

| Priority | Strategy        | Guidance                                                                      |
| -------- | --------------- | ----------------------------------------------------------------------------- |
| 🔴 High  | **Bridging**    | Use "relevant to", "aligned with", "context of" to capture keyword defensibly |
| 🟠 Med   | **Translation** | Only direct synonyms allowed                                                  |
| 🟢 Low   | **Strict**      | Preserve original facts exactly                                               |

**Fabrication Checks:**
❌ **Wrong:** Claiming "B2B SaaS experience" when you only worked on B2C.
✅ **Right (Bridging):** "Launched data products _applicable to_ B2B SaaS contexts..."

❌ **Wrong:** Claiming "FDA regulatory experience" with no exposure.
✅ **Right (Bridging):** "Ensured compliance _aligned with_ regulatory standards..."

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

---

### Rule 6: Core Entity Preservation

**NEVER delete the specific name of the feature, product, or metric you built to make room for a keyword.**

The keyword must _modify_ or _contextualize_ the entity, not replace it.

- ❌ **Bad:** "Optimized data pipelines..." (Deleted "recording scenes")
- ✅ **Good:** "Optimized algorithms _for recording scenes_..."
- ❌ **Bad:** "Launched B2B platform..." (Deleted "Smart Recorder")
- ✅ **Good:** "Launched Smart Recorder _with B2B platform integrations_..."

---

### Rule 7: Strategic Bolding

Do NOT bold keywords just because you inserted them. This looks suspicious and stuffed. Only bold text if it is a **critical metric** (e.g., **\$1.5B** revenue) or the **primary entity** of the resume (e.g., product name).

- ❌ **Bad:** Launched **AI video tools** for **creators** in the **creator economy**...
- ✅ **Good:** Launched AI video tools for creators in the creator economy...

---

## Gap Analysis Output Format

```markdown
## Gap Analysis: [Company Name]

🎯 ██████░░░░ **60%** Fair

### ✓ Matched Keywords

`keyword1` · `keyword2` · `keyword3` · `keyword4` · `keyword5`

### ✗ Missing Keywords

| Priority | Keyword      | Category   | Integration                 |
| :------- | :----------- | :--------- | :-------------------------- |
| 🔴       | **keyword1** | Industry   | → Section, bullet X         |
| 🟠       | **keyword2** | Tool       | → Skills section            |
| 🟠       | ~~keyword3~~ | Niche      | _too niche, skip_           |
| 🟢       | ~~keyword4~~ | Credential | _credential not held, skip_ |
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
