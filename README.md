# Myriad 千面

AI-powered job application toolkit for [Antigravity](https://antigravity.codes/) — resume customization, cover letters, company research, interview prep, and application answers.

> **Myriad** (千面): A master of a thousand faces — countless personas, one candidate. Built on Myriad Pro.

## ✨ What Can Myriad Do?

| Workflow            | What It Does                                                   |
| ------------------- | -------------------------------------------------------------- |
| `/persona-switch`   | Switch users or create a new profile from your existing resume |
| `/resume-builder`   | Tailor your resume to match a specific job posting             |
| `/cover-letter`     | Write a compelling cover letter that sounds human, not AI      |
| `/application-qa`   | Answer short application questions (e.g., "Why this company?") |
| `/company-research` | Research a company before your interview                       |
| `/screen-prep`      | Generate talking points and scripts for your interview         |

---

## 🚀 Getting Started

**Get Antigravity.** Download and install [Antigravity IDE](https://antigravity.codes/). This is the AI coding environment where Myriad runs.

**Open this project.** In Antigravity, open the Myriad folder. All workflows are available via slash commands in the chat.

**Check your profile.** Type `/persona-switch` in the chat to see which profile is active.

**Create your profile (first time only).** Type `/persona-switch --new`, then:

1. Enter your name (lowercase, e.g., "jane")
2. Enter your role (e.g., "pm" for Product Manager, "swe" for Software Engineer)
3. Upload your resume (PDF, Word, or Markdown file)

Myriad will convert your resume to Typst format and generate a PDF.

---

## 📋 How to Use Each Workflow

### Resume Builder — Customize Your Resume for a Job

1. Type `/resume-builder` in chat
2. Paste the **job description** when prompted
3. Review the **gap analysis** (shows which keywords you're missing)
4. Type `Accept all` or `Accept 1, 3` to approve specific edits
5. Your tailored resume is saved in `output/{your-name}/resumes/`

**Example:**

```
User: /resume-builder
Agent: Please paste the job description.
User: [pastes job description]
Agent:
  Gap Analysis: 78% alignment
  Missing: TensorFlow (High), A/B testing (Medium)

  Edit Suggestions:
  1. Add "TensorFlow" to Skills
  2. Mention "A/B testing" in Google bullet

  Commands: Accept all | Accept 1 | Reject 2
```

---

### Cover Letter — Write a Compelling Letter

1. Type `/cover-letter` in chat
2. Paste the **job description**
3. Myriad reads your resume and career profile
4. A PDF cover letter is generated in `output/{your-name}/letters/`

**Tips:**

- The letter avoids clichés like "I am excited to apply..."
- It tells a story connecting your experience to the company

---

### Application Q&A — Answer Short Questions

1. Type `/application-qa` in chat
2. Paste the **question** (e.g., "Why are you interested in this role?")
3. Myriad gives a natural, human-sounding answer
4. Edit and paste into your application

---

### Company Research — Prep for Interviews

1. Type `/company-research` in chat
2. Paste the **job description**
3. Myriad generates 4 research files:
   - Industry landscape
   - Competitors analysis
   - Company deep dive
   - Role fit analysis

Files are saved in `output/company-research/{Company}/`

---

### Screen Prep — Get Interview Scripts

1. Type `/screen-prep {Company}` (e.g., `/screen-prep Google`)
2. Make sure you've run `/company-research` first
3. Myriad generates:
   - **Introduction script** (30-second pitch)
   - **"Why us?" script** (tailored to the company)
   - **Dossier** (comprehensive prep doc with talking points)

---

## 📄 Sample Outputs

See what Myriad can generate:

- **Resume:** [modern_preview.pdf](typst/templates/modern_preview.pdf)
- **Cover Letter:** [letter_preview.pdf](typst/templates/letter_preview.pdf)

---

## 👤 Managing Multiple Profiles

Myriad can store profiles for different people or roles:

```
# See all profiles
/persona-switch

# Switch to a different profile
/persona-switch jane swe

# Create a new profile
/persona-switch --new
```

Each profile has its own:

- Resume file (Typst format)
- Career profile (optional, for stories)
- Output folder for customized resumes

---

## 📁 Where Are My Files?

```
Myriad/
├── personas/
│   └── {your-name}/
│       ├── {name}_{role}_master_resume.typ   ← Your resume (editable)
│       ├── {name}_{role}_master_resume.pdf   ← Compiled PDF
│       └── config.yaml                        ← Settings
├── output/
│   └── {your-name}/
│       ├── resumes/      ← Customized resumes go here
│       └── letters/      ← Cover letters go here
└── .current_persona      ← Currently active profile
```

---

## 🎯 Alignment Scoring

When you run `/resume-builder`, you'll see an alignment score:

| Score   | Meaning              |
| ------- | -------------------- |
| 85-100% | ✅ Excellent match   |
| 70-84%  | 🎯 Good match        |
| 50-69%  | ⚠️ Needs improvement |
| <50%    | ❌ Significant gaps  |

---

## 🔧 Requirements

- [Typst](https://typst.app/) must be installed (for PDF generation)
- Antigravity IDE with AI enabled
- Python environment at `.venv`

**To check if Typst is installed:**

```bash
typst --version
```

**About fonts:** Myriad uses the Myriad Pro font by default. If you don't have it installed:

- Typst will automatically fall back to a similar sans-serif font
- The layout will still work, but the typography may look slightly different
- To use Myriad Pro, install it on your system (it's included with Adobe Creative Cloud)

> **Note:** Myriad Pro is a commercial font and cannot be distributed in this repository. If you need a free alternative, edit `typst/templates/modern.typ` and replace "Myriad Pro" with "Inter" or "Source Sans Pro".

---

## 📝 Quality Checks

Myriad automatically checks your resume for:

| Check                | What It Does                          |
| -------------------- | ------------------------------------- |
| **Page overflow**    | Warns if resume exceeds 1 page        |
| **Orphan detection** | Flags lines with dangling words       |
| **Whitespace check** | Warns if page is less than 60% filled |

---

## 📖 More Documentation

- [`docs/PRD.md`](docs/PRD.md) — Full product requirements
- [`docs/training_reference.md`](docs/training_reference.md) — Examples for ATS analysis
- [`docs/scoring_rules.md`](docs/scoring_rules.md) — How alignment scores work

---

Built with Typst + Gemini AI
