# The New User's Guide to Myriad

Welcome! If you are new to coding, terminals, or "AI agents," this guide is for you. It covers everything from installing the software to customizing your resume.

---

## 🛠️ Step 1: Getting Set Up

Before you can run the agent, you need to set up your environment.

### 1. Install Antigravity (The App)

Antigravity is the "brain" where Myriad lives.

1. Download the app from [antigravity.codes](https://antigravity.codes/).
2. Drag the app to your **Applications** folder.
3. Open it. You might need to sign in with your Google account.

### 2. Get the Code (Cloning)

You need to download the Myriad project files to your computer.

1. Open Antigravity.
2. In the "Welcome" screen or command palette (`Cmd+Shift+P`), look for **Git: Clone**.
3. Paste the repository URL: `https://github.com/orangedavy/Myriad.git`
4. Choose a folder to save it (e.g., `Documents/Myriad`).
5. Click **Open**.

### 3. Install Dependencies (The Engine)

Myriad needs a few tools to work: **Python** (for logic) and **Typst** (for PDFs).

#### Installing Typst (PDF Generator)

**If you have Homebrew (Mac users):**
Open the terminal (view > Terminal) and type:

```bash
brew install typst
```

**If you DON'T have Homebrew:**

1. Go to the [Typst GitHub Releases](https://github.com/typst/typst/releases).
2. Download `typst-x86_64-apple-darwin.tar.xz` (for Intel Macs) or `typst-aarch64-apple-darwin.tar.xz` (for M1/M2/M3 Macs).
3. Unzip the file.
4. Move the `typst` binary to a folder in your path (like `/usr/local/bin`) OR just keep note of where it is.

#### Setting up Python

Antigravity comes with Python, but this project needs specific add-ons (like PDF readers) to work. Run this command to install them:

1. Open the **Terminal** tab in Antigravity (bottom panel).
2. Run this "magic command":
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
   _(If you see errors, ask the agent for help!)_

---

## 🖥️ Step 2: The Workspace

### Extensions to Install

To make editing easier, install these extensions (click the "Blocks" icon on the left sidebar):

1. **Tinymist Typst** - Intelligent formatting and highlighting for Typst.
2. **vscode-pdf** - To view PDF files directly in the editor.

### Understanding the Folder Structure

Don't be overwhelmed by the files! Here is the map:

- **`personas/`** → 🏠 **Your Home.**
  - Go here to find your resume (`master_resume.typ`).
  - This is where you make permanent changes (fixing typos, adding jobs).
- **`output/`** → 📤 **The Outbox.**
  - The AI puts all generated files here (Tailored Resumes, Cover Letters).
  - _Don't edit files here; they will be overwritten next time you run a command._
- **`docs/`** → 📚 **The Manual.**
  - Read `tips.md` (this file!) and `scoring_rules.md`.

---

## 📝 Step 3: Editing Your Master Resume

Your "Master Resume" is the source of truth. The AI reads this to create tailored versions.

### Finding It

1. Open the file explorer (left sidebar).
2. Go to `personas` > `[your_name]` > `[your_name]_[role]_master_resume.typ`.

### Editing It (Typst Crash Course)

Typst files look a lot like simple text. You don't need to know code to edit it.

**Basic Formatting:**

- **Bold**: `*text*` → **text**
- **Italic**: `_text_` → _text_
- **Links**: `#link("url")[Display Text]`

**Editing Content:**
Just find the text you want to change and type!

```typ
// Example Entry
#entry(
  title: "Product Manager",
  company: "Tech Corp",
  dates: "2020 - Present",
  location: "Remote",
  bullets: (
    "Led cross-functional teams...",
    "Launched 3 new products...",
  )
)
```

**Adding a New Job:**
Copy and paste an entire `#entry(...)` block and fill in the new details.

---

## 🤖 Step 4: Running the Agent

### Switching Personas

Typing `/persona-switch` tells the agent who you are.

- "I am Davy, the PM" -> loads Davy's PM resume.
- "I am Jane, the Designer" -> loads Jane's Designer resume.

### "Feeding" the Agent

When the agent asks for a Job Description (JD) or Resume:

1. **Drag and Drop:** You can drag a PDF or text file directly from your computer's folder into the chat window.
2. **Paste:** Just copy the text and paste it.

### Common Commands

- `/resume-builder` - Create a tailored resume.
- `/cover-letter` - Write a cover letter.
- `/company-research` - Do deep research on a company.

---

## 🎨 Design & Fonts

### Installation (Myriad Pro)

The template uses **Myriad Pro** by default.

- If you have Adobe Creative Cloud, you likely already have it.
- If not, you can install it (`.otf` or `.ttf` files) by double-clicking them on your Mac.
- **Restart Antigravity** if fonts don't appear immediately.

### Using a Different Font

If you don't want to install fonts, you can change the template to use a system font (like Arial or Helvetica).

1. Open `typst/templates/modern.typ`.
2. Find the line: `text(font: "Myriad Pro", ...)`
3. Change it to: `text(font: "Helvetica", ...)`

---

## 💡 Pro Tips

### Notion Compatibility

When copying content to Notion:

1. **Don't use Cmd+V.** It messes up code blocks.
2. **Use Cmd+Shift+V** (Paste and Match Style). This keeps the markdown structure perfect.

### "It's Broken!" Checklist

If something isn't working:

1. **Did you activate the environment?** (`source .venv/bin/activate`)
2. **Is in the right folder?** (You should be in `Myriad`)
3. **Is Typst installed?** (Type `typst --version` in terminal)
4. **Is the file path right?** (Use relative paths like `.` instead of `/Users/...`)
