---
description: Switch between personas for resume and interview workflows
---

# Persona Switch Workflow

Manage and switch between personas for all resume and interview workflows.

## Current Persona

Stored in: `.current_persona` (simple text file with `persona role` format)

// turbo

```bash
cat .current_persona 2>/dev/null || echo "davy pm"
```

## Commands

### View Current

```
/persona-switch
```

Output:

```
Current: davy (pm)
Available: davy [pm], jane [pm, swe]
```

### Switch Persona

```
/persona-switch davy
/persona-switch davy pm
/persona-switch jane swe
```

// turbo

```bash
echo "{PERSONA} {ROLE}" > .current_persona
```

### List Available

// turbo

```bash
for dir in personas/*/; do
  persona=$(basename "$dir")
  roles=$(ls "$dir"/*.typ 2>/dev/null | sed 's/.*_\([^_]*\)_master_resume.typ/\1/' | tr '\n' ', ' | sed 's/,$//')
  echo "$persona [$roles]"
done
```

### Create New Persona

```
/persona-switch --new
```

Triggers the resume ingestion flow using the Python backend.

#### Step 1: Prompt for Details

Ask the user for:

1. **Persona name** (lowercase, alphanumeric) — e.g., "john", "jane"
2. **Role** (lowercase) — e.g., "pm", "swe", "ds"
3. **Resume file** — Accept PDF, DOCX, or MD

#### Step 2: Preview Extraction

// turbo

```bash
cd . && .venv/bin/python -c "
from backend.extractors import extract_text, parse_resume_preview

text = extract_text('{FILE_PATH}')
preview = parse_resume_preview(text)

print(f'📄 Extracted {len(text)} characters')
print(f'📋 Detected sections: {preview[\"detected_sections\"]}')
print()
print('Sample:')
print(preview['sample_content'][:300])
"
```

Show preview to user and ask to confirm.

#### Step 3: Agent Parsing & Validation

**Role:** Resume Parser Agent

1. **Extract Text:** Re-run extraction if needed.
2. **Parse to JSON:** Use the **ResumeData** schema to parse the text into a valid JSON structure.
3. **Save JSON:** Write the parsed JSON to `temp_resume.json` in the current directory.

```json
{
  "contact": { "name": "..." },
  "work": [ ... ],
  "..."
}
```

> [!IMPORTANT]
> Verify that `contact.email` and `contact.name` are present. Only proceed if valid JSON is saved.

#### Step 4: Select Template

Ask user to choose:

1. **modern** (default) — Clean Myriad Pro style
2. **classic** — Traditional Times New Roman
3. **minimal** — Ultra-clean, maximum whitespace

#### Step 5: Generate and Compile

// turbo

```bash
cd . && .venv/bin/python -m backend.ingest \
  --json temp_resume.json \
  --persona "{PERSONA}" \
  --role "{ROLE}" \
  --template "{TEMPLATE}"
```

**Cleanup:**

```bash
rm temp_resume.json
```

#### Step 6: Review Output

If successful, show:

- ✅ Typst file path
- ✅ PDF file path
- ⚠️ Any warnings (e.g., page overflow)

**Orphan Detection** (run automatically):

// turbo

```bash
cd . && .venv/bin/python -c "
from backend.monitor import detect_runts
runts = detect_runts('personas/{PERSONA}/{PERSONA}_{ROLE}_master_resume.pdf')
if runts:
    print('⚠️ Orphans detected:')
    for r in runts:
        print(f'  - Page {r[\"page\"]}: \"{r[\"text\"]}\"')
    print('Suggest rewording these bullets to avoid dangling words.')
else:
    print('✅ No orphans detected')
"
```

**Whitespace Check** (run automatically):

// turbo

```bash
cd . && .venv/bin/python -c "
from backend.monitor import check_page_fill
result = check_page_fill('personas/{PERSONA}/{PERSONA}_{ROLE}_master_resume.pdf')
print(f'Page fill: {result[\"fill_percent\"]}%')
if result['warning']:
    print(f'⚠️ {result[\"suggestion\"]}')
else:
    print('✅ Good page density')
"
```

If orphans or whitespace warnings detected: Show user issues before confirming.

If page count > 1:

- Ask user which sections to trim
- Re-run generation with reduced content

#### Step 7: Update Current Persona

// turbo

```bash
echo "{PERSONA} {ROLE}" > .current_persona
echo "✅ Switched to: {PERSONA} ({ROLE})"
```

#### Optional: Add Career Profile

After successful ingestion, ask user if they want to add a career profile:

```
Would you like to add a career profile for story-based features?
This enables /screen-prep and /application-qa to use your work experiences.

Upload a career profile markdown file, or type stories directly.
```

If yes, save to `personas/{PERSONA}/{PERSONA}_career_profile.md` and update config.yaml.

## Validation

When switching, verify files exist:

// turbo

```bash
PERSONA="{PERSONA}"
ROLE="{ROLE}"
RESUME="personas/$PERSONA/${PERSONA}_${ROLE}_master_resume.typ"

if [ ! -f "$RESUME" ]; then
  echo "❌ Resume not found: $RESUME"
  echo "Available roles for $PERSONA:"
  ls personas/$PERSONA/*.typ 2>/dev/null | sed 's/.*_\([^_]*\)_master_resume.typ/  - \1/'
  exit 1
fi

echo "✅ Switched to: $PERSONA ($ROLE)"
```

## Integration

Other workflows read current persona from `.current_persona`:

```bash
read PERSONA ROLE < .current_persona
```

Affected workflows:

- `/resume-builder`
- `/company-research`
- `/screen-prep`
- `/application-qa`
