---
description: Generate a tailored cover letter using AI storytelling
---

# Cover Letter Generator

Generate a storytelling-focused cover letter that sounds human, not AI-generated.

## Prerequisites

- Persona directory at `personas/{persona}/`
  - Master resume: `{persona}_{role}_master_resume.typ`
  - Career profile: `{persona}_career_profile.md` (optional but helpful for stories)
- Typst installed (`typst --version`)

## Default Persona

Default: Varies (set via `/persona-switch`)

## Workflow Steps

### Step 0: Load Persona

Read current persona from `.current_persona`:

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
  echo "❌ Resume not found. Run /persona-switch first."
  exit 1
fi
```

### Step 1: Collect Job Description

Ask the user to paste the **Job Description**.

Extract the **Company Name** from the JD (the agent identifies this automatically).

### Step 2: Read Source Files

Read the following files to understand the candidate:

1. **Master Resume**: `personas/{PERSONA}/{PERSONA}_{ROLE}_master_resume.typ`
2. **Career Profile** (if exists): `personas/{PERSONA}/{PERSONA}_career_profile.md`
3. **Config**: `personas/{PERSONA}/config.yaml`

Extract key context: name, email, phone, work history, notable projects, skills.

### Step 3: Generate Cover Letter Body

Write the cover letter body following the Voice & Style guidelines below.

### Step 4: Create Typst File

Create directory and write the letter:

// turbo

```bash
read PERSONA ROLE < .current_persona
mkdir -p "output/$PERSONA/letters"
```

Write to `temp_cover_letter.typ` (in root) using the template:

```typst
#import "../../../typst/templates/letter.typ": render

#let data = (
  contact: (
    name: "[NAME]",
    email: "[EMAIL]",
    phone: "[PHONE]",
  ),
  recipient: (
    company: "[COMPANY]",
  ),
  body: [
    [GENERATED BODY - multiple paragraphs]
  ],
)

#render(data)
```

### Step 5: Compile PDF

// turbo

```bash
read PERSONA ROLE < .current_persona
cd .
typst compile --root . "temp_cover_letter.typ" "output/$PERSONA/letters/${COMPANY}_Cover_Letter.pdf"
rm "temp_cover_letter.typ"
```

### Step 6: Notify User

```
✅ Cover letter saved: output/{PERSONA}/letters/{COMPANY}_Cover_Letter.pdf
```

---

## Voice & Style

**Goal:** Stand out by sounding like a real person, not AI-generated.

**Do:**

- Start with a specific moment, belief, or origin story
- Connect your personal journey to the company's mission
- Write conversationally, like talking to a friendly hiring manager
- Use specific details and numbers from actual experience
- Start sentences differently (not always "I...")
- Include a personal touch or surprising detail
- Keep it to 3-4 paragraphs, 250-400 words

**Don't:**

- Use bullets, numbered lists, or em dashes
- Use quotes, colons to introduce lists, or formal transitions
- Start with "I am writing to apply for..." or "I am excited to..."
- Use corporate buzzwords (synergy, leverage, utilize)
- Repeat bullet points from the resume
- Sound like every other cover letter
- Use exaggerating contrasts (e.g., "It's not about X, it's about Y") - just say what it is

**Tone:** Casual enough to be memorable, professional enough to be credible.

---

## Structure (4-5 Short Paragraphs)

1. **Hook**: A specific moment or belief (2-3 sentences)
2. **Connection**: Why this specific mission resonates with you
3. **Evidence**: Relevant experience #1 (focus on the _approach_, not just results)
4. **Evidence**: Relevant experience #2 (focus on ecosystem/collaboration)
5. **Close**: Simple, forward-looking wrap-up

---

## Key Constraints

1. **Sound Human**: If it sounds like ChatGPT wrote it, rewrite it
2. **Be Specific**: Vague letters are forgettable; specific stories stick
3. **Stay Honest**: Don't invent experiences; connect real ones to the company
4. **No Em Dashes**: Use commas or periods instead
5. **Ready to Send**: Output should need minimal editing

---

## Example Interaction

```
User: /cover-letter
[Pastes job description for EnsoData Product Manager role]

Agent: [Reads resume and career profile silently]

Agent: I'll write a cover letter connecting your dialysis project experience to EnsoData's sleep diagnostics mission.

[Agent creates temp_cover_letter.typ]
[Agent compiles PDF and deletes temp file]

Agent: ✅ Cover letter saved: output/alex/letters/EnsoData_Cover_Letter.pdf
```
