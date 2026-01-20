# Resume Builder Training Reference

This document establishes the **gold standard** for job description analysis and resume customization. Follow these patterns exactly to ensure consistent, high-quality results.

---

## Keyword Extraction Methodology

### Step 1: Job Metadata Extraction

Extract and present in table format:

| Category      | What to Extract                                      |
| ------------- | ---------------------------------------------------- |
| **Role**      | Exact job title from posting                         |
| **Company**   | Company name                                         |
| **Location**  | City, state, remote/hybrid status                    |
| **Seniority** | Junior (0-2y), Mid (2-5y), Senior (5-8y), Lead (8+y) |
| **Role Type** | AI PM, Healthcare PM, Technical PM, General PM, etc. |
| **Salary**    | If disclosed, include base + bonus + equity          |

---

### Step 2: ATS Keyword Extraction

**Categorize keywords by priority:**

| Priority      | Criteria                                                          | Examples                                   |
| ------------- | ----------------------------------------------------------------- | ------------------------------------------ |
| 🔴 **High**   | Mentioned 2+ times, in requirements section, or industry-specific | "healthcare", "SaaS", "machine learning"   |
| 🟠 **Medium** | Mentioned once in requirements, or common PM tools                | "Jira", "user testing", "cross-functional" |
| 🟢 **Low**    | Nice-to-haves, soft skills, or generic terms                      | "PMP certification", "Excel"               |

**Keyword categories to identify:**

- **Industry**: healthcare, fintech, e-commerce, etc.
- **Technology**: AI, ML, LLM, cloud, IoT, etc.
- **Methodology**: Agile, user research, A/B testing, etc.
- **Tools**: Jira, Figma, SQL, Tableau, etc.
- **Skills**: cross-functional, stakeholder management, etc.
- **Credentials**: PMP, MBA, certifications

---

### Step 3: Requirements Summary

Extract the **Top 5 Requirements** — the non-negotiables that would disqualify a candidate if missing.

Format:

1. **[Requirement]** — brief clarification if needed
2. ...

Also extract **Nice-to-Haves** — explicitly stated as preferred/bonus, not required.

---

## Gold Standard Example: EnsoData

### Job Posting

**Role**: Product Manager - Software Medical Devices SaaS  
**Company**: EnsoData  
**Category**: Healthcare / SaaS PM  
**Date Analyzed**: 2026-01-15

<details>
<summary><strong>Full Job Description (click to expand)</strong></summary>

**Description**

EnsoData is looking for a Product Manager (hybrid preferred), who is passionate about making healthcare better, to help conduct customer research, define new product features, and launch them into the world. This hybrid position in Madison, WI offers a salary of $110,000 to $130,000 along with bonus program, stock options, and benefits, including paid time off and health insurance.

**The Product Manager Role**

We're looking for a new teammate to uncover what product features our customers crave most, define and prioritize them, and work with engineers to bring them to life and marketers to explain them to the world.

On a given day, this could include:

- Managing a discovery process: Researching the sleep industry, discovering and deeply understanding customer problems, and summarizing that research into clear opinions with recommended actions.
- Pitching product opportunities and their supporting evidence to the company and aligning opinions across departments
- Telling the story of the value of product features to the marketing team and reviewing videos and website content focused on product use cases.
- Creating "whiteboard-mockup" designs and testing them out with real users. Working with UX designers to turn these ideas into detailed product requirement specs.
- Breaking down projects into parts. Pulling apart ambiguous problems into releasable slices, and validating the interim steps by reviewing demos.
- Representing EnsoData in partnerships and/or collaborating with product managers at partner companies

**About EnsoData**

EnsoData strives to make healthcare more accurate, efficient, and affordable through waveform artificial intelligence (AI) technology. Using AI and machine learning, our software analyzes billions of data points collected from sensors placed throughout the human body. Our first solution, EnsoSleep, reduces the time clinicians spend analyzing, scoring and managing sleep studies.

**Requirements**

- Bachelor's degree; PMP certification a bonus
- 2-5 year(s) in product management of a shipped/release software product
- Minimum of 1 year of prior work experience in the healthcare space is required, preferably in a digital healthcare SaaS company, a regulated medical device environment, the durable medical equipment (DME) space, or in an organization that focused on clinician workflows.
- Experience with a development issue ticketing system such as Jira, Forecast, or GitHub Issues; and with spreadsheet software (MS Excel or Google Sheets).
- A confident communicator; with strong collaboration, partnering, and presentation skills
- Comfortable working with remote teams and/or hybrid office environments.
- Ability to travel approximately 15% of the calendar year

**Company Culture - Embrace the Pineapple!**

- Make Healthcare Better, Put Customers First, Be a Great Teammate, Gets $#!t Done, Inject a Focus on Quality

**Benefits**

- Remote and flexible schedule (Headquarters in Madison, WI)
- Health, dental, and vision insurance
- Paid time off, 401k, and stock options
- Company Bonus Program
- Team Summits

</details>

---

### Extracted Metadata

| Category      | Extracted                                       |
| ------------- | ----------------------------------------------- |
| **Role**      | Product Manager - Software Medical Devices SaaS |
| **Company**   | EnsoData                                        |
| **Location**  | Madison, WI (Hybrid)                            |
| **Seniority** | Mid-level (2-5 years)                           |
| **Role Type** | Healthcare PM / AI PM                           |
| **Salary**    | $110,000 - $130,000 + bonus + equity            |

### Extracted Keywords

| Priority | Keyword                            | Category           |
| -------- | ---------------------------------- | ------------------ |
| 🔴 High  | **healthcare**                     | Industry           |
| 🔴 High  | **product management**             | Core skill         |
| 🔴 High  | **customer research**              | Methodology        |
| 🔴 High  | **SaaS**                           | Product type       |
| 🔴 High  | **medical devices**                | Industry           |
| 🔴 High  | **AI / machine learning**          | Technology         |
| 🟠 Med   | **Jira**                           | Tool               |
| 🟠 Med   | **user testing**                   | Methodology        |
| 🟠 Med   | **UX design collaboration**        | Skill              |
| 🟠 Med   | **digital health**                 | Industry           |
| 🟠 Med   | **waveform AI**                    | Technology (niche) |
| 🟠 Med   | **cross-functional collaboration** | Skill              |
| 🟢 Low   | **PMP certification**              | Credential (bonus) |
| 🟢 Low   | **Excel/Google Sheets**            | Tool               |
| 🟢 Low   | **GitHub Issues**                  | Tool               |
| 🟢 Low   | **remote/hybrid**                  | Work style         |

### Top 5 Requirements

1. **2-5 years product management** experience with shipped software
2. **Healthcare industry experience** (digital health, medical devices, clinician workflows)
3. **Customer discovery & research** — uncovering needs, summarizing findings
4. **Cross-functional collaboration** with engineering, design, marketing
5. **Communication & presentation skills** for stakeholder alignment

### Nice-to-Haves

- PMP certification
- Experience with partnerships / working with partner PMs
- Sleep/waveform data analysis domain knowledge
- Travel flexibility (~15%)

---

## Example 2: Google (Big Tech)

### Job Posting

**Role**: Product Manager, Fuchsia OS  
**Company**: Google  
**Category**: Big Tech / Platform PM  
**Date Analyzed**: 2026-01-15

<details>
<summary><strong>Full Job Description (click to expand)</strong></summary>

**Company**

At Google, we put our users first. The world is always changing, so we need Product Managers who are continuously adapting and excited to work on products that affect millions of people every day.

**Details**

In this role, you will work cross-functionally to guide products from conception to launch by connecting the technical and business worlds. You can break down complex problems into steps that drive product development.

Fuchsia is a modern, open source operating system that is simple, secure, updatable, and performant. It's a general purpose OS, designed to power an ecosystem of hardware and software.

**Responsibilities**

- Support PRDs by collaborating with partner teams (e.g., engineers, PgMs, UX)
- Define product roadmaps by operationalizing defined strategy
- Articulate defined product ideas to capture attention and influence others
- Validate the market size and opportunity
- Facilitate launches, maintenance, and retirement

**Basic Qualifications**

- Bachelor's degree or equivalent practical experience
- 3 years of experience in product management or related technical role
- 1 year of experience taking technical products from conception to launch
- Experience with low level operating system foundations (kernel, drivers, file systems, networking) or consumer devices

**Preferred Qualifications**

- Master's degree in technology or business
- 2 years of experience in business function (strategic marketing, consulting)
- 2 years of experience delivering technical presentations to senior leadership
- 2 years of experience working cross-functionally
- 1 year of experience in software development or engineering
- Knowledge of accessibility best practices

**Salary**: $132,000-$189,000 + bonus + equity + benefits

</details>

---

### Extracted Metadata

| Category      | Extracted                              |
| ------------- | -------------------------------------- |
| **Role**      | Product Manager, Fuchsia OS            |
| **Company**   | Google                                 |
| **Location**  | Not specified (US, multiple offices)   |
| **Seniority** | Mid-level (3 years PM + 1 year launch) |
| **Role Type** | Technical PM / Platform PM             |
| **Salary**    | $132,000 - $189,000 + bonus + equity   |

### Extracted Keywords

| Priority | Keyword                             | Category        |
| -------- | ----------------------------------- | --------------- |
| 🔴 High  | **product management**              | Core skill      |
| 🔴 High  | **product roadmap**                 | Methodology     |
| 🔴 High  | **cross-functional**                | Skill           |
| 🔴 High  | **PRD**                             | Deliverable     |
| 🔴 High  | **operating system**                | Technology      |
| 🔴 High  | **technical products**              | Product type    |
| 🔴 High  | **conception to launch**            | Skill           |
| 🟠 Med   | **kernel / drivers / file systems** | Technology (OS) |
| 🟠 Med   | **consumer devices**                | Industry        |
| 🟠 Med   | **UX collaboration**                | Skill           |
| 🟠 Med   | **market validation**               | Methodology     |
| 🟠 Med   | **stakeholder management**          | Skill           |
| 🟠 Med   | **technical presentations**         | Skill           |
| 🟢 Low   | **accessibility**                   | Nice-to-have    |
| 🟢 Low   | **software development**            | Preferred       |
| 🟢 Low   | **strategic marketing**             | Preferred       |

### Top 5 Requirements

1. **3 years product management** experience (or related technical role)
2. **Technical product launch** — conception to launch (minimum 1 year)
3. **Low-level OS knowledge** — kernel, drivers, file systems, networking OR consumer devices
4. **Cross-functional collaboration** — engineering, UX, PgM partners
5. **PRD & roadmap ownership** — defining and operationalizing strategy

### Nice-to-Haves

- Master's degree (tech or business)
- Business function experience (marketing, consulting)
- Technical presentations to senior leadership
- Software development background
- Accessibility experience

---

## Example 3: Globus Medical (Traditional Company)

### Job Posting

**Role**: Product Manager, Joint Reconstruction (Robotics/Navigation)  
**Company**: Globus Medical  
**Category**: Traditional / Medical Device PM  
**Date Analyzed**: 2026-01-15

<details>
<summary><strong>Full Job Description (click to expand)</strong></summary>

**Company**

At Globus Medical, we move with a sense of urgency to deliver innovations that improve the quality of life of patients with musculoskeletal disorders. Our Life Moves Us philosophy is built on four values: Passionate About Innovation, Customer Focused, Teamwork, and Driven.

**Details**

Our Joint Reconstruction division is searching for Product Managers who want to make a difference. The Product Manager will develop procedure specific surgical applications used on robotics and navigation systems by working with top surgeons and cross-functional engineering teams. This person will act as the voice of customer on complex, multi-disciplinary development projects.

**Responsibilities**

- Collaborates with management to establish strategic plans
- Creates and manages project plans with product development teams
- Lead UI/UX development efforts for software
- Maintain relationships with Design Team Surgeons
- Performs market analysis to identify new offerings
- Leads coordination of kick-off meetings, design reviews, verification/validation, cadaver labs
- Develops market introduction plans
- Ensures documentation of DHFs, DMRs, and DHRs per quality policy and regulatory requirements
- Obtaining market feedback from surgeons for product specifications
- Partnering with operations for manufacturing/purchasing
- Participating in sales training, customer calls/visits
- Adhering to AdvaMed Code, MedTech Code, and company policies

**Qualifications**

- Bachelor's Degree with 5 years of related experience; or Master's Degree and 3 years
- Excellent verbal and written communication skills
- Advanced project management skills
- Experience with new product introduction and lifecycle management
- Ability to travel up to 20%

</details>

---

### Extracted Metadata

| Category      | Extracted                             |
| ------------- | ------------------------------------- |
| **Role**      | Product Manager, Joint Reconstruction |
| **Company**   | Globus Medical                        |
| **Location**  | Not specified (likely Audubon, PA)    |
| **Seniority** | Mid-Senior (5y + BA or 3y + MA)       |
| **Role Type** | Medical Device PM / Hardware PM       |
| **Salary**    | Not disclosed                         |

### Extracted Keywords

| Priority | Keyword                            | Category          |
| -------- | ---------------------------------- | ----------------- |
| 🔴 High  | **product management**             | Core skill        |
| 🔴 High  | **medical device**                 | Industry          |
| 🔴 High  | **robotics**                       | Technology        |
| 🔴 High  | **cross-functional**               | Skill             |
| 🔴 High  | **new product introduction (NPI)** | Methodology       |
| 🔴 High  | **product lifecycle management**   | Methodology       |
| 🔴 High  | **voice of customer**              | Methodology       |
| 🔴 High  | **regulatory compliance**          | Industry          |
| 🟠 Med   | **UI/UX (software)**               | Skill             |
| 🟠 Med   | **surgeon collaboration**          | Stakeholder       |
| 🟠 Med   | **DHF/DMR/DHR documentation**      | Regulatory        |
| 🟠 Med   | **verification/validation**        | Methodology       |
| 🟠 Med   | **cadaver lab**                    | Industry-specific |
| 🟠 Med   | **project management**             | Skill             |
| 🟠 Med   | **market analysis**                | Methodology       |
| 🟠 Med   | **sales training**                 | Go-to-market      |
| 🟢 Low   | **Microsoft Office**               | Tool              |
| 🟢 Low   | **AdvaMed/MedTech Code**           | Compliance        |
| 🟢 Low   | **inventory management**           | Operations        |

### Top 5 Requirements

1. **5 years experience** (Bachelor's) or **3 years** (Master's)
2. **Medical device / regulated environment** — DHF, DMR, DHR, compliance
3. **New product introduction (NPI)** — full lifecycle management
4. **Surgeon/customer collaboration** — voice of customer, design relationships
5. **Cross-functional project leadership** — engineering, operations, sales, regulatory

### Nice-to-Haves

- Experience attending surgeries/cadaver labs
- Familiarity with AdvaMed/MedTech compliance codes
- Inventory/operations management background
- Travel flexibility (~20%)

---

## Quality Checklist

Before presenting analysis, verify:

- [ ] All 6 metadata fields populated
- [ ] Keywords sorted by priority (High → Med → Low)
- [ ] Each keyword has a category label
- [ ] Top 5 requirements are truly non-negotiables, not nice-to-haves
- [ ] Nice-to-haves are explicitly stated as "preferred" or "bonus" in JD
- [ ] No generic keywords that won't help ATS (e.g., "teamwork", "motivated")
- [ ] Industry-specific terms prioritized higher than generic tools

---

## Anti-Patterns to Avoid

❌ **Don't** include soft skills like "motivated" or "team player" as keywords  
❌ **Don't** mark everything as High priority — be discriminating  
❌ **Don't** guess seniority — derive from years of experience stated  
❌ **Don't** include keywords not actually in the JD  
❌ **Don't** confuse requirements with nice-to-haves
