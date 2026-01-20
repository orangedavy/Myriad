// Cover Letter Template
// Header: Phone (left) | Email (right)
// Title: "Cover Letter" (centered, bold)
// Body: Block paragraphs with salutation and closing
//
// Usage: #import "letter.typ": render
//        #render(data)

// --- Configuration ---

#let text-color = rgb("#5E5E5E")
#let weight-regular = 480
#let weight-semibold = 300
#let weight-bold = 600
#let weight-light = 300

// --- Render Function ---

#let render(data) = {
  set page(
    paper: "us-letter",
    margin: (left: 75pt, right: 75pt, top: 75pt, bottom: 75pt),
  )
  set text(
    font: "Myriad Pro",
    size: 12pt,
    fill: text-color,
    weight: weight-regular,
    ligatures: true,
  )
  set par(
    justify: true,
    leading: 0.75em,
    spacing: 1.5em,
  )

  // Header: Phone (left) | Email (right)
  grid(
    columns: (1fr, 1fr),
    align(left)[#data.contact.at("phone", default: "")],
    align(right)[#data.contact.email],
  )

  v(1em)

  // Title: Cover Letter
  align(center)[
    #text(size: 24pt, weight: weight-bold)[Cover Letter]
  ]

  v(1em)

  // Salutation
  if data.at("recipient", default: none) != none and data.recipient.at("name", default: none) != none {
    [Dear #data.recipient.name,]
  } else if data.at("recipient", default: none) != none and data.recipient.at("company", default: none) != none {
    [Dear #data.recipient.company Recruiter,]
  } else {
    [Dear Hiring Manager,]
  }

  v(1em)

  // Body
  data.body

  v(1.5em)

  // Closing (right-aligned)
  align(right)[
    Best regards,\
    #data.contact.name
  ]
}

// --- Sample Data ---
// Alex Chen applying to Samsung for a Product Manager role

#let sample-data = (
  contact: (
    name: "Alex Chen",
    email: "alex.chen@gmail.com",
    phone: "415-555-8820",
  ),
  recipient: (
    company: "Samsung",
  ),
  body: [
Growing up in Seoul, I spent countless hours tinkering with my parents' first Samsung TV remote. I remember the exact moment the power button stopped working and I figured out how to fix it with a paperclip. That spark of curiosity about how devices work has never left me.

When I saw the Product Manager role at Samsung Research, I immediately thought about how far that little remote has come. Today, Samsung is building the AI-powered ecosystem I dreamed about as a kid. From Bixby to SmartThings to the devices that connect them all, you are creating experiences that feel like magic. I want to be part of building that magic.

At Stripe, I led the Checkout redesign that serves 10 million consumers monthly. I learned that great products are not about features. They are about removing friction so completely that users forget there was ever a barrier. At Airbnb, I ran 50+ user research sessions and discovered that the best insights come from listening to what people do not say. These experiences taught me how to translate complex technology into simple, delightful moments.

What excites me most about Samsung is the opportunity to apply these lessons at a scale few companies can match. Building products that ship to hundreds of millions of users requires a different kind of rigor. It means obsessing over every interaction, every edge case, every moment where technology meets real life. That challenge is exactly what I have been preparing for. My background in payments, travel, and consumer AI has taught me how to balance speed with quality, and I am eager to bring that discipline to your team.

I would be honored to contribute to Samsung Research. Whether it is refining Bixby's voice experience or imagining the next generation of connected devices, I am ready to roll up my sleeves and build products that make people's lives a little more magical.

Thank you for considering my application.
  ],
)

// Render Preview
#render(sample-data)
