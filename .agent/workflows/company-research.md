---
description: Conduct comprehensive company research for interview preparation
---

# Company Research Workflow

Conduct deep research on a target company to prepare for interviews. This is the foundation for `/screen-prep`.

## Prerequisites

- Persona directory at `personas/{persona}/`
  - Master resume: `{persona}_{role}_master_resume.typ`
  - Career profile: `{persona}_career_profile.md` (optional)
- Default persona: `davy` with role `pm`

## Workflow Steps

### Step 0: Load Persona

Read current persona from `.current_persona`:

// turbo

```bash
read PERSONA ROLE < /Volumes/T7-APFS/Myriad/.current_persona
echo "Using: $PERSONA ($ROLE)"
```

### Step 1: Collect Job Description

Ask the user to providing the job description. They can either:

- Paste it directly in chat
- Provide a URL to scrape
- Point to a file

Extract **Company Name** and **Role Title** from the JD.

### Step 2: Create Output Directory

// turbo

```bash
read PERSONA ROLE < /Volumes/T7-APFS/Myriad/.current_persona
mkdir -p "/Volumes/T7-APFS/Myriad/output/$PERSONA/company-research/{COMPANY}"
```

---

## Research Phase

Execute all 4 research steps. Use **web search** for up-to-date information. **Pass context between steps** — each subsequent step should reference prior research for coherence.

> [!IMPORTANT]
> Don't hallucinate. If unsure about something, say so explicitly.

### Step 3: Industry Research

**Role:** Strategic Market Analyst

**Scope Technique (20/80 Rule):**

- **20% Context (Broad):** The macro industry — major shifts, regulatory changes, macro headwinds
- **80% Focus (Specific):** The company's niche segment — who has the best product, fastest growth, deepest integrations

**Output Structure:**

1. **Landscape** — current state of the industry (broad) → company's segment (specific)
2. **Market Size** — use TAM/SAM/SOM filter:
   - Show divergence between sources ("$22B to $38B depending on scope")
   - Explain why: "The $38B includes wellness apps; the $22B clinical diagnostics figure is more relevant for [Company]"
   - Your value-add: Define the playing field, don't just recite a number
3. **Growth Drivers & Barriers** — table format: Driver/Barrier | Impact | So What?
4. **Disruptive Tech/Regulation** — technologies or laws reshaping the sector (include CMS/RPM codes if relevant)
5. **Trends** — top 3 shifting trends
6. **Future Outlook** — 3-5 year projection with confidence levels

**Formatting:**

- Interview implications as blockquote italic: `> _Ask about their...?_`
- Do NOT explicitly label broad/specific percentages in output

**Context Required:** Job Description

// turbo

```bash
read PERSONA ROLE < /Volumes/T7-APFS/Myriad/.current_persona
cat > "/Volumes/T7-APFS/Myriad/output/$PERSONA/company-research/{COMPANY}/1_industry.md" << 'EOF'
{CONTENT}
EOF
```

### Step 4: Competitive Research

**Role:** Competitive Intelligence Specialist

**Output Structure:**

**Direct Competitors (3):** Transposed table with companies as columns:

```markdown
|                   | [Company 1](url) | [Company 2](url) | [Company 3](url) |
| ----------------- | ---------------- | ---------------- | ---------------- |
| **Archetype**     | Tech Innovator   | Premium Niche    | Agile Startup    |
| **Flagship**      | Product          | Product          | Product          |
| **Moat**          | ...              | ...              | ...              |
| **Vulnerability** | ...              | ...              | ...              |
```

**Adjacent Players (2-3):** Table with Company | Relationship | Notes

**Competitive Advantage:** Target Company's key differentiators as table: Differentiator | Why It Matters

**Archetypes:** Legacy Giant, Low-Cost Disruptor, Premium Niche, Tech Innovator, Agile Startup

**Formatting:**

- Link company names in table headers
- Clean section headers (no "Tier 1 —" or "EnsoData's" prefixes)
- End with interview implication as blockquote italic

**Context Required:** Job Description + Industry Research

// turbo

```bash
read PERSONA ROLE < /Volumes/T7-APFS/Myriad/.current_persona
cat > "/Volumes/T7-APFS/Myriad/output/$PERSONA/company-research/{COMPANY}/2_competitive.md" << 'EOF'
{CONTENT}
EOF
```

### Step 5: Company Research

**Role:** Corporate Strategist (Critical Optimist tone)

**Tone:** 20% validation (what they do well), 80% constructive problem-solving (where they can go next).

**Output Structure:**

**Part 1: Foundational Knowledge**

1. **Mission & Vision** — Mission (stated purpose) and Vision (long-term aspirational goal, not just current focus). Format as two bullet points.
2. **Products** — table: Product | Description | Status
3. **Business Model** — table: Revenue Stream | Description
4. **Culture** — bullet list with format: `- **Value** — Description`. Include slogan as final bullet if applicable.

> [!NOTE]
> **Culture Verification Protocol:** Cross-reference stated values with Glassdoor/Blind. Do NOT present reviews as facts — use them to generate interview questions.
>
> - If reviews say "decisions are top-down," reframe as: _"How has decision-making evolved as the company scaled?"_
> - Glassdoor = marketing-positive, Blind = venting-negative. Truth is in the middle.

**Part 2: Insider Context**

1. **Strategic Goals** — this year's "North Star"
2. **Pain Points** — label as `Confirmed` or `Inferred`:
   - `Confirmed`: From earnings calls, press releases, CEO interviews
   - `Inferred`: From industry trends, competitive pressure
3. **Strategic Challenges** — headwinds the company faces (regulatory, competitive, operational)
4. **Recent News** — 2 significant recent events (not minor updates)

**Part 3: Stakeholder Map** _(if interviewing)_

Research likely interviewers on LinkedIn:

- **Background**: Engineer → talk tech. MBA → talk market sizing.
- **Tenure**: 10 years = values stability. 6 months = hired to shake things up.
- **Shared Ground**: Common employers, industries, interests.

**Context Required:** Job Description + Industry + Competitive Research

// turbo

```bash
read PERSONA ROLE < /Volumes/T7-APFS/Myriad/.current_persona
cat > "/Volumes/T7-APFS/Myriad/output/$PERSONA/company-research/{COMPANY}/3_company.md" << 'EOF'
{CONTENT}
EOF
```

### Step 6: Role Analysis

**Role:** Executive Career Coach

**Input:** Read `typst/master_resume.typ` for candidate background.

**Output Structure:**

**Job Metadata** — Table with Role, Company, Location, Seniority, Role Type, Salary

**Fit Score** — Multi-line format:

```
🎯 ████████░░ **78%** Good
**Edge:** [strength]
**Risk:** [gap]
```

**ATS Keywords** — Table: Priority | Keyword | Category | ✔/✘

**Key Requirements** — Top 5 numbered, with business rationale in italics

**Nice-to-Haves** — Bulleted list of preferred qualifications

**Gap Analysis** — Table: Gap | Bridge Strategy (no emojis for soft gaps)

**Interview Leverage Points** — Numbered list with format:
`1. **Topic:** Statement with specifics.`

**Context Required:** Job Description + All prior research + Master Resume

// turbo

```bash
read PERSONA ROLE < /Volumes/T7-APFS/Myriad/.current_persona
cat > "/Volumes/T7-APFS/Myriad/output/$PERSONA/company-research/{COMPANY}/4_role_analysis.md" << 'EOF'
{CONTENT}
EOF
```

---

## Completion

Notify user:

```
✅ Company research complete: {Company}

📁 Files saved to: output/company-research/{Company}/
   • 1_industry.md
   • 2_competitive.md
   • 3_company.md
   • 4_role_analysis.md

🎯 Ready for /screen-prep to generate interview scripts.
```

---

## Key Constraints

1. **Don't Hallucinate**: Use web search. If unsure, say so.
2. **Honest & Unbiased**: Present objective analysis. Don't flatter the candidate or the company — include risks, challenges, and potential red flags.
3. **Context Chaining**: Each step MUST read prior outputs for coherence.
4. **Up-to-date**: Research must be current — search for recent news.
5. **Dollar Signs**: Do NOT escape dollar signs ($). Use standard $ for currency to enable easy copy-pasting to Notion.
6. **Markdown Format**: All outputs use strict Notion-compatible Markdown.

---

## Data Source Priorities

| Data Type            | Primary Sources                           |
| -------------------- | ----------------------------------------- |
| **Product/Features** | G2, Capterra, TrustRadius                 |
| **Strategy/Vision**  | Company website (Press/About), LinkedIn   |
| **Financials/Scale** | Crunchbase (free), press releases         |
| **User Sentiment**   | Reddit, "Company A vs Company B" searches |

> [!TIP]
> If a paid source (e.g., CB Insights) is blocked, triangulate: if 2 free sources confirm a number, that is sufficient.

## Citation Format

Include sources for key claims:

- In tables: Add `Source` column
- Inline: "Estimated $50M revenue (Source: TechCrunch 2024)"
