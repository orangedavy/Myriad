// Modern Resume Template
// Based on Myriad Pro aesthetic with clean layout
//
// Usage Option 1 (Template-rendered):
//   #import "modern.typ": render
//   #render(data)
//
// Usage Option 2 (Hybrid - click-editable):
//   #import "modern.typ": page-init, name, heading, entry, main
//   #show: page-init
//   #align(center)[#name[Your Name] ...]

// --- Configuration ---

#let text-color = rgb("#5E5E5E")
#let weight-regular = 480
#let weight-semibold = 300
#let weight-bold = 600
#let weight-light = 300

// --- Styles ---

// 1. Name
#let name(body) = {
  text(size: 20pt, weight: weight-bold, stretch: 87.5%, body)
  v(-0.75em)
}

// 2. Section Heading
#let heading(body) = {
  v(0em)
  text(size: 14pt, weight: weight-light, stretch: 112.5%, body)
  v(-0.5em)
}

// 3. Entry Header
// Note: Location parameter removed per user preference
#let entry(left, right) = {
  v(0em)
  set text(size: 11pt, weight: weight-light, stretch: 87.5%)
  show strong: set text(weight: weight-semibold)
  
  grid(
    columns: (1fr, auto),
    left,
    right
  )
  v(-0.25em)
}

// 4. Body Text
#let main(body) = {
  set text(weight: weight-regular)
  set par(leading: 0.875em)
  show strong: set text(weight: weight-semibold)
  pad(left: 20pt, right: 15pt, body)
}

// 5. Bullet Formatter
// Handles markdown rendering within bullets (bold only for now to avoid eval issues)
#let format-bullets(bullets) = {
  for bullet in bullets {
    let parts = bullet.split("*")
    let content = []
    for (i, part) in parts.enumerate() {
      if calc.odd(i) {
        content = [#content#strong(part)]
      } else {
        content = [#content#part]
      }
    }
    list.item(content)
  }
}

// 6. Page Initialization (for hybrid usage)
#let page-init(body) = {
  set page(
    paper: "a4",
    fill: white,
    margin: (left: 50pt, right: 50pt, top: 25pt, bottom: 25pt),
  )
  set text(font: "Myriad Pro", fill: text-color, size: 10pt, ligatures: true)
  set list(marker: [•], body-indent: 8pt, spacing: 1em)
  body
}

// --- Render Function ---

#let render(data) = {
  set page(
    paper: "a4",
    fill: white,
    margin: (left: 50pt, right: 50pt, top: 25pt, bottom: 25pt),
  )

  set text(font: "Myriad Pro", fill: text-color, size: 10pt, ligatures: true)
  set list(marker: [•], body-indent: 8pt, spacing: 1em)

  // Header
  // Note: Contact details laid out to match user preference (2 lines of header info)
  align(center)[
    #name[#data.contact.name]
    #main[
      #if data.contact.at("location", default: none) != none [Location: *#data.contact.location*; ]
      #if data.contact.at("phone", default: none) != none [Phone: *#data.contact.phone*; ]
      Email: *#data.contact.email*; 
      #if data.contact.at("linkedin", default: none) != none [LinkedIn]\
      
      #if data.at("summary", default: none) != none [#data.summary]
    ]
  ]

  // Work Experience
  if data.at("work", default: ()).len() > 0 {
    heading[Work]
    for job in data.work {
      let company-text = if job.at("url", default: none) != none {
        link(job.url)[#job.company]
      } else {
        job.company
      }
      
      let title-part = [*#job.title, #company-text*]
      if job.at("description", default: none) != none {
        title-part = [#title-part (#job.description)]
      }
      
      entry(title-part, job.dates)
      
      main[
        #format-bullets(job.bullets)
      ]
    }
  }

  // Projects
  if data.at("projects", default: ()).len() > 0 {
    heading[Projects]
    for project in data.projects {
      let title-text = if project.at("url", default: none) != none {
        link(project.url)[#project.title]
      } else {
        project.title
      }
      
      let entry-left = [*#title-text*]
      if project.at("description", default: none) != none {
        entry-left = [#entry-left (#project.description)]
      }

      entry(entry-left, project.dates)
      
      main[
        #format-bullets(project.bullets)
      ]
    }
  }

  // Education
  if data.at("education", default: ()).len() > 0 {
    heading[Education]
    for edu in data.education {
      let inst-text = if edu.at("url", default: none) != none {
        link(edu.url)[#edu.institution]
      } else {
        edu.institution
      }
      
      entry([*#edu.degree, #inst-text*], edu.dates)
      
      if edu.at("bullets", default: ()).len() > 0 {
        main[
          #format-bullets(edu.bullets)
        ]
      }
    }
  }

  // Skills
  if data.at("skills", default: (:)).len() > 0 {
    heading[Skills]
    main[
      #for (category, items) in data.skills [
        - *#category:* #items.join(", ")
      ]
    ]
  }
}

// --- Sample Data (For Preview) ---
// This maintains the Master Template visual reference

#let sample-data = (
  contact: (
    name: "Alex Chen",
    location: "San Francisco, CA",
    phone: "415-555-8820",
    email: "alex.chen@gmail.com",
    linkedin: "https://linkedin.com/in/alexchen",
  ),
  summary: [
    Customer-obsessed product leader with *8+* years building consumer and B2B products at big tech.\
    Launched *6* products from *0* to *1* for *3M+* users and drove *\$150M+* revenue via data-driven roadmaps.
  ],
  work: (
    (
      title: "Senior Product Manager",
      company: "Stripe",
      url: "https://stripe.com",
      description: "Consumer payments and checkout",
      dates: "2022.03 – Present",
      bullets: (
        "Launched Stripe Checkout redesign serving *10M+* consumers monthly, increasing payment completion rates by *23%* and reducing cart abandonment by *18%* across e-commerce partners.",
        "Built one-click payment experience using Link, growing consumer adoption to *5M+* saved accounts and boosting repeat purchase rates by *40%* for participating merchants.",
        "Led consumer trust initiatives including receipt redesign and dispute resolution flow, improving customer satisfaction scores by *15* points and reducing support tickets by *30%.",
        "Drove international expansion of consumer-facing checkout to *12* new markets, adapting UX for local payment preferences and achieving *95%* localization satisfaction scores.",
      ),
    ),
    (
      title: "Product Manager",
      company: "Airbnb",
      url: "https://airbnb.com",
      description: "Global travel marketplace",
      dates: "2019.06 – 2022.02",
      bullets: (
        "Spearheaded the development of dynamic pricing algorithms that increased host revenue by *22%* while maintaining guest satisfaction scores above *4.7* stars across *2M+* listings.",
        "Launched Airbnb Experiences booking flow redesign, improving conversion rates by *28%* and reducing drop-off by *40%* through iterative A/B testing with *100k+* users.",
        "Conducted *50+* user research sessions to identify pain points in the checkout process, leading to a streamlined design that increased bookings by *18%* quarter-over-quarter.",
      ),
    ),
    (
      title: "Associate Product Manager",
      company: "Google",
      url: "https://google.com",
      description: "Search and Ads",
      dates: "2017.08 – 2019.05",
      bullets: (
        "Owned end-to-end product lifecycle for Google Ads reporting features used by *1M+* advertisers, increasing feature adoption by *32%* through intuitive dashboard redesigns.",
        "Collaborated with engineering to reduce page load times by *45%* using performance optimization techniques, directly improving advertiser engagement metrics.",
        "Analyzed data from *10+* sources to identify opportunities in small business advertising, launching a self-serve campaign builder that acquired *80k+* new advertisers.",
      ),
    ),
  ),
  projects: (
    (
      title: "Open Source Analytics Platform",
      url: none,
      description: "Personal project",
      dates: "2021.01 – 2021.06",
      bullets: (
        "Built a real-time analytics dashboard using React and Python, gaining *5k+* GitHub stars and adoption by *200+* startups for product metrics tracking.",
      ),
    ),
    (
      title: "AI-Powered Interview Coach",
      url: none,
      description: "Hackathon winner",
      dates: "2020.09 – 2020.10",
      bullets: (
        "Developed an LLM-based interview preparation tool that provides personalized feedback, winning *1st place* at TechCrunch Disrupt Hackathon among *150+* teams.",
      ),
    ),
  ),
  education: (
    (
      degree: "MBA",
      institution: "UC Berkeley Haas School of Business",
      url: "https://haas.berkeley.edu",
      dates: "2015.08 – 2017.05",
      bullets: (
        "Concentration in Technology Leadership; PM Club President; Berkeley Case Competition Finalist",
      ),
    ),
    (
      degree: "BS in Computer Science",
      institution: "Stanford University",
      url: "https://stanford.edu",
      dates: "2011.09 – 2015.06",
      bullets: (
        "Magna Cum Laude, GPA 3.85/4.0; Coursework: Machine Learning, HCI, Databases, Distributed Systems",
      ),
    ),
  ),
  skills: (
    "Tools": ("Python", "SQL", "Figma", "Amplitude", "Mixpanel", "Looker", "JIRA", "Notion", "Miro", "Dovetail", "A/B Testing"),
    "Credentials": ("PMP", "Certified Scrum Product Owner (CSPO)", "Six Sigma Green Belt"),
  ),
)

// Render Preview
#render(sample-data)
