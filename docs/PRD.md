# Myriad 千面 PRD

## Product Overview

**Myriad** (千面) is an AI-powered job application toolkit that helps candidates customize resumes, research companies, prepare for interviews, and answer application questions — all from a unified persona-based system.

---

## Problem Statement

Job seeking requires juggling multiple tasks: tailoring resumes, researching companies, preparing interview scripts, and answering application questions. Each task is time-consuming and disconnected from the others.

---

## Solution

An integrated workflow system that:

1. Manages multiple personas and roles (e.g., PM, SWE)
2. Ingests existing resumes (PDF/DOCX/MD) and converts to Typst
3. Customizes resumes for specific job descriptions with ATS optimization
4. Generates storytelling-focused cover letters
5. Answers short-form application questions naturally
6. Conducts deep company research for interview preparation
7. Generates interview scripts and dossiers

---

## Target Users

- **Job seekers** applying to multiple positions across different roles
- **Career changers** managing multiple persona profiles
- **Career coaches** helping clients with end-to-end preparation

---

## Core Workflows

### 1. `/persona-switch` — Persona Management

- Switch between personas and roles
- List available profiles
- Create new personas via resume ingestion (PDF/DOCX/MD → Typst)

### 2. `/resume-builder` — Resume Customization

- Extract ATS keywords from job descriptions (🔴 High, 🟠 Med, 🟢 Low)
- Gap analysis with alignment scoring
- **Mandatory diff-style edit suggestions** (always shown, never summarized)
- PDF generation with one-page constraint

### 3. `/cover-letter` — Cover Letter Generation

- Storytelling-focused content (no em dashes, human tone)
- Reads resume and career profile for context
- PDF generation via Typst letter template

### 4. `/application-qa` — Short-Form Answers

- Natural, human-sounding responses (not AI-sounding)
- Adapts to character limits
- Sources from resume and career profile

### 5. `/company-research` — Deep Company Analysis

- **Industry Research:** Landscape, market size (TAM/SAM/SOM), trends
- **Competitive Research:** Direct competitors, adjacent players, advantages
- **Company Research:** Mission/vision, products, culture, pain points
- **Role Analysis:** Fit score, ATS keywords, gap analysis, interview leverage points

### 6. `/screen-prep` — Interview Preparation

- Introduction and "Why Us?" scripts
- Story selection from career profile
- Synthesized dossier with all research

---

## Multi-Persona Architecture

### Naming Convention

`{persona}_{role}_{type}.{ext}`

| File Type      | Example                     |
| -------------- | --------------------------- |
| Resume         | `davy_pm_master_resume.typ` |
| Career Profile | `davy_career_profile.md`    |
| Config         | `config.yaml`               |

### Directory Structure

```
Myriad/
├── personas/
│   ├── davy/
│   │   ├── davy_pm_master_resume.typ
│   │   ├── davy_pm_master_resume.pdf
│   │   ├── davy_career_profile.md (optional)
│   │   └── config.yaml
│   └── {other personas}/
├── output/
│   ├── {persona}/
│   │   ├── resumes/
│   │   ├── letters/
│   │   └── resume-analysis/
│   ├── company-research/{Company}/
│   └── screen-prep/{Company}/
├── typst/templates/
│   ├── modern.typ        ← Resume template
│   └── letter.typ        ← Cover letter template
├── backend/
│   ├── extractors.py     ← PDF/DOCX text extraction
│   ├── generator.py      ← Typst generation (template-rendered)
│   └── monitor.py        ← Quality checks (orphans, page fill)
└── .current_persona      ← Active persona (e.g., "davy pm")
```

---

## Resume Format

### Hybrid Approach (Recommended for New Personas)

Imported resumes use a hybrid format:

- **Styles imported from template** (centralized in `modern.typ`)
- **Content written inline** (click-editable in preview)

```typst
#import "../../typst/templates/modern.typ": page-init, name, heading, entry, main
#show: page-init

#heading[Work]
#entry[*Title, Company* (Location)][Dates]
#main[- Bullet point]
```

---

## Technical Stack

| Component     | Technology                              |
| ------------- | --------------------------------------- |
| Resume Format | Typst                                   |
| AI Engine     | Gemini 3 Pro/Flash, Claude Opus 4.5     |
| Backend       | Python (PyMuPDF for PDF handling)       |
| Workflow      | Antigravity Agent (`.agent/workflows/`) |

---

## Quality Guardrails

Automatic checks during resume ingestion and customization:

| Check                | Threshold               | Action                      |
| -------------------- | ----------------------- | --------------------------- |
| **Page overflow**    | >1 page                 | ⚠️ Ask user to trim content |
| **Orphan detection** | <15 char trailing lines | ⚠️ Suggest rewording        |
| **Whitespace check** | <60% page fill          | ⚠️ Suggest adding content   |

---

## Success Metrics

| Metric                    | Target                       |
| ------------------------- | ---------------------------- |
| Callback Rate Improvement | +15%                         |
| Time per Customization    | < 1 min (manual review)      |
| One-Page Compliance       | 100%                         |
| Interview Script Quality  | Natural, specific, memorable |

---

## Roadmap

### v0.5 — Core Features

- [x] Resume customization with ATS optimization
- [x] Company research workflow (4-step)
- [x] Screen prep with scripts and dossier
- [x] Application Q&A for short-form answers
- [x] Multi-persona support with `/persona-switch`

### v0.6 — Resume Ingestion

- [x] PDF/DOCX/MD → Typst conversion
- [x] Template selection (Modern template)
- [x] New persona onboarding (`/persona-switch --new`)

### v0.7 — Cover Letters

- [x] Cover Letter Generation (`/cover-letter`)
- [x] Storytelling-focused content
- [x] Letter template (`typst/templates/letter.typ`)

### v0.8 — Quality & Polish (Current)

- [x] Hybrid resume format (click-editable)
- [x] Orphan detection in ingestion flow
- [x] Whitespace warning for sparse resumes
- [x] Bold skill categories in template
- [x] Mandatory diff format in resume-builder

### v0.9 — Future

- [ ] Preview/refine loop improvements
- [ ] Web interface

---

## Constraints & Guardrails

1. **One-Page Limit** — All resumes must fit on one page
2. **Fact Flexibility** — Embellishment only for High priority keywords
3. **Character Budget** — ±10% per bullet point
4. **Master Preservation** — Original resume never modified
5. **Career Profile Optional** — Story features limited if missing
6. **Location Fallback** — If no description, use (City, State) in parentheses

---

## Naming Rationale

**Myriad** (千面): In English, "Myriad" means "ten thousand" or "countless" — a direct translation of 千 (Qiān). The Chinese name 千面 means "a thousand faces," evoking a master of disguise who can show different personas for different roles. The name is natively embedded in the project's DNA: Myriad Pro is the default resume font.

🎲 **Bonus pun:** 千面 sounds like 上千个面试 (shàng qiān gè miànshì) — "over a thousand interviews." A lucky omen for job seekers!
