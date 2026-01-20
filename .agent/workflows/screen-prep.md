---
description: Prepare scripts for initial screen interview using company research
---

# Screen Prep Workflow

Prepare tailored interview scripts for initial screen interviews. Requires `/company-research` to be completed first.

## Prerequisites

- Persona directory at `personas/{persona}/`
  - Career profile: `{persona}_career_profile.md` (optional — story features limited if missing)
- Company research at `output/company-research/{Company}/`
- Default persona: `davy`

## Workflow Steps

### Step 1: Verify Company Research Exists

Ask user for the **Company Name** they want to prepare for.

Check if research exists:

// turbo

```bash
if [ ! -d "/Volumes/T7-APFS/Myriad/output/company-research/{COMPANY}" ]; then
  echo "❌ ERROR: Company research not found for {COMPANY}"
  echo "Please run /company-research first."
  exit 1
fi
```

> [!CAUTION]
> If research is missing, **STOP** and inform user to run `/company-research` first.

### Step 2: Load Research Context

Read all prior research files:

- `output/company-research/{Company}/1_industry.md`
- `output/company-research/{Company}/2_competitive.md`
- `output/company-research/{Company}/3_company.md`
- `output/company-research/{Company}/4_role_analysis.md`

### Step 3: Create Output Directory

// turbo

```bash
mkdir -p "/Volumes/T7-APFS/Myriad/output/screen-prep/{COMPANY}"
```

## Script Preparation Phase

### Step 4: Scripts + Story Selection

**Role:** Career Strategist + Behavioral Interview Specialist

**Constraints:**

- Follow templates ~80%, use ~20% flexibility for company-specific insights
- **Word count:** 200-250 words per script (spoken ~1.5-2 min)
- **Bold all customizations:** Company names, changed sentences, unfamiliar content
- Be creative, passionate, yet professional

**Input:**

- Role Analysis + Company Research
- Career Profile at `typst/Career_Profile.md`

---

#### Introduction Script

Keep static parts unchanged. Bold all customizations. ~80% fixed, ~20% company-specific.

**Fixed parts:**

- Opening (summary, passion origin)
- Experience examples paragraph

**Flexible parts (must customize):**

- Recent application paragraph: **[Industry]** space + **1-sentence bridge**
- Alignment paragraph: **[alignment with role]**, **[company]**, **[product]**
- Hook ending: **[vision/goal]** + **3 specific story applications** (not generic summaries)

---

#### Why Us Script

**MUST be fully written, not templated.** Three points:

1. **[Experience]:** Specific experiences relevant to role. Use fixed statements about dialysis project and smart recorder.

2. **[Mission]:** Company mission + personal connection. Include compelling stat if available (e.g., "54M Americans have sleep apnea, 80% undiagnosed").

3. **[Challenge]:** Express excitement about learning opportunity. Format:
   > What excites me most is the opportunity to blend my experience with a fresh challenge. **[Specific learning area]** promises a refreshing experience. Exploring this new space — helping you solve **[specific problem]** — would allow me to grow with **[company]**.

**Hook:** Write a specific hook (not [HOOK] placeholder). Example: recent news, product announcement, technology breakthrough.

---

#### Story Selection

Select 3-4 stories from Career Profile that address JD requirements.

| Story                                    | Addresses                                       |
| ---------------------------------------- | ----------------------------------------------- |
| **[Exact title from Career_Profile.md]** | [Requirement addressed] — [Why this story fits] |

**Format:** No summary column. Expand "Addresses" to include justification for why story maps to requirement.

---

**Context Required:** Role Analysis + Company Research + Career Profile

// turbo

```bash
cat > "/Volumes/T7-APFS/Myriad/output/screen-prep/{COMPANY}/scripts.md" << 'EOF'
{CONTENT}
EOF
```

### Step 6: Final Synthesis

**Role:** Data Synthesizer and Executive Editor

Compile all research and scripts into a single dossier:

```markdown
# {Company Name}

JD - {Role Title}

## Fit Analysis

**Top Matches:**

- [Match 1]
- [Match 2]
- [Match 3]
- [Match 4]

**Gap Strategy:**

- [Gap 1] → [Bridge]
- [Gap 2] → [Bridge]
- [Gap 3] → [Bridge]

**Key Terminology:** `keyword` · `keyword` · `keyword`

## Market Intelligence

### Landscape

[From 1_industry.md — no explicit 20/80 labels]

### Market Size

[TAM/SAM/SOM table with relevance column]

### Trends

[Top 3 trends]

## Competitive Landscape

[Table: Competitor | Archetype | Flagship | Moat | Vulnerability]

## Company Research

### Executive Summary

~200 words as company analysis. Structure:

1. What they do (1-2 sentences)
2. Market position (competitive landscape context)
3. Recent momentum (news, funding)
4. Strategic bet (where they're heading)
5. Why it matters for PM role (optional but recommended)

### Strategy

[2025 Goals as numbered list + Pain Points as table with Confirmed/Inferred]

### Recent News

[Top 2 events with interview implications as blockquote]

### Mission/Vision

[Two bullet points: Mission = stated purpose, Vision = long-term aspiration]

### Products

[Table: Product | Description | Status]

### Target Users

[Bullets with segment + description]

### Business Model

[Table: Revenue Stream | Description]

### Culture

[Bullets: **Value** — Description. Include slogan as final bullet.]

## Introduction

[Insert Intro script verbatim from 2_scripts.md]

## Why us?

[Insert Why Us script verbatim from scripts.md]

## Stories

[For each confirmed story, create a `<details>` block with full STAR content from Career_Profile.md:]

<details>
<summary><strong>[Story Title]</strong> — [1-line summary with key metric]</summary>

### Overview

[From Career_Profile.md]

### Situation

[From Career_Profile.md]

### Task

[From Career_Profile.md]

### Action

[Bullets from Career_Profile.md]

### Result

[From Career_Profile.md]

</details>

## Quick Reference

**Intro Key Points:**

- [Point 1]
- [Point 2]

**Story Key Points:**

- [Story 1]: [Key point to hit]
- [Story 2]: [Key point to hit]
- [Story 3]: [Key point to hit]

## Questions

[Leave blank for user to fill]
```

// turbo

```bash
cat > "/Volumes/T7-APFS/Myriad/output/screen-prep/{COMPANY}/{COMPANY}_dossier.md" << 'EOF'
{CONTENT}
EOF
```

---

## Completion

Notify user:

```
✅ Screen prep complete: {Company} - {Role}

📁 Files saved to: output/screen-prep/{Company}/
   • scripts.md ← Review scripts & stories
   • {Company}_dossier.md ← Final dossier

🎯 Ready for your screen interview!
```

---

## Key Constraints

1. **Dependency Check**: MUST verify `/company-research` output exists first.
2. **Template Fidelity**: Scripts should ~80% match templates, ~20% customization.
3. **Context Chaining**: Read all research files before generating scripts.
4. **Script Integrity**: Keep Introduction and Why Us scripts verbatim in final dossier.
5. **Markdown Format**: All outputs use strict Notion-compatible Markdown.
