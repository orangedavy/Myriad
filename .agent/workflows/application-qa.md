---
description: Answer short-form job application questions authentically
---

# Application Q&A Workflow

Generate natural, human-sounding answers for short-form job application questions.

## Prerequisites

- Persona directory at `personas/{persona}/`
  - Master resume: `{persona}_{role}_master_resume.typ`
  - Career profile: `{persona}_career_profile.md` (optional — story-based answers limited if missing)
- Company research at `output/{persona}/company-research/{Company}/` (optional but helpful)
- Default persona: `davy` with role `pm`

## Trigger

User pastes a question from a job application, optionally with context (company name, role, character limit).

## Voice & Style

**Goal:** Stand out by sounding like a real person, not AI-generated.

**Do:**

- Write conversationally, like you're talking to a recruiter over coffee
- Show genuine enthusiasm without being sycophantic
- Use specific details and numbers from actual experience
- Start sentences differently (not always "I...")
- Include a personal touch or surprising detail
- Be concise, get to the point fast

**Don't:**

- Use bullets, numbered lists, or em dashes
- Use quotes, colons to introduce lists, or formal transitions
- Start with "I am excited to..." or "I believe that..."
- Use corporate buzzwords (synergy, leverage, utilize)
- Sound like every other AI-generated answer

**Tone spectrum:** Casual enough to be memorable, professional enough to be credible.

## Question Types & Approaches

### "Why are you interested in [company]?"

Structure: Hook → Specific connection → What you'd bring

```
Example: The moment I saw [specific thing] about [company], I knew I had to apply. [Personal connection]. Having spent the last [X] years doing [relevant work], I'm excited to bring [skill] to help solve [their problem].
```

### "Do you have experience in [field]?"

Structure: Direct answer → Best example → Transferable angle (if needed)

```
Example: Yes, at [company] I [specific accomplishment with metric]. What I loved most was [insight]. [If bridging] While my background is in [adjacent field], the core challenge is the same: [connection].
```

### "Describe a time when you [situation]."

Structure: Quick context → What you did → Outcome → Reflection

```
Example: When [situation at company], I [action]. The result was [metric]. Looking back, what made it work was [insight that shows self-awareness].
```

### "What's your [salary expectation / availability / etc.]?"

Structure: Direct answer → Brief rationale (if appropriate)

Just answer directly. Don't over-explain.

## Process

1. **Identify question type** from examples above
2. **Pull relevant content** from Career Profile and resume
3. **Check for company research** if question involves the company
4. **Draft answer** following style guidelines
5. **Trim to character limit** if specified (prioritize specifics over generics)
6. **Output** as plain text, ready to copy-paste

## Character Limits

**Default:** Short paragraph (250-500 chars) unless user specifies otherwise.

If user specifies a limit:

- Under 100 chars: One punchy sentence
- 100-250 chars: Two sentences max
- 250-500 chars: Short paragraph ← **default**
- 500+ chars: Full response with one example

Count characters and note if approaching limit.

## Output Format

Output the answer as plain text, ready to copy-paste. No metadata, character counts, or length options unless user asks.

## Examples

**Question:** "Why are you interested in EnsoData?"

When I saw that EnsoData just got FDA clearance to diagnose sleep apnea from a simple pulse oximeter, I got genuinely excited. 54 million Americans have sleep apnea and 80% don't know it. That's exactly the kind of problem I want to spend my time on. My last project at UW Medicine tackled a similar accessibility gap in dialysis care, where I helped patients overcome barriers to home treatment. I'd love to bring that same patient-centered approach to EnsoData's mission.

---

**Question:** "Do you have experience with regulated medical devices?" (250 char limit)

My capstone at UW Medicine required navigating healthcare compliance for an AI therapy chatbot. While not FDA-regulated, I worked closely with clinicians to ensure our solution met clinical safety standards. I'm eager to deepen this experience in a 510(k) environment.

---

**Question:** "Describe a time you used data to make a product decision."

At Samsung, I noticed something odd in our Bixby chatbot data: users were sending almost as many insults as greetings. Instead of dismissing it as noise, I dug in. Through user interviews, I discovered these weren't angry users. They were stressed, lonely people who needed a safe space to vent. So I designed "Tree Hole Mode," where the system recognized emotional distress and responded with empathy instead of deflection. Engagement time jumped 25%. The lesson stuck with me: the most valuable insights often hide in the weirdest data.

## Key Constraints

1. **Sound Human:** If it sounds like ChatGPT wrote it, rewrite it
2. **Be Specific:** Vague answers are forgettable; numbers and names stick
3. **Stay Honest:** Don't invent experiences; bridge from real ones
4. **Respect Limits:** Character counts matter; trim the fluff first
5. **Ready to Paste:** Output should need zero editing
