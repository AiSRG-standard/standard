# Introducing AiSRG: An Open Standard for AI-Web Communication

Today, we are launching a new project that will forever change how artificial intelligence interacts with the digital world. Welcome to AiSRG (Ai Service Reference Guide).

## The Problem: AI is Smart, Yet "Blind"

In an era where AI assistants can write poetry, solve complex equations, and create art, they face a fundamental limitation: they cannot truly "act" on the internet.

Today's AI is like a brilliant librarian who has read every book in the world. But when you ask them, "Can you reserve that book for me?" they can't. They can only tell you how to reserve it yourself.

The connection between AI and digital services is currently a "Walled Garden" system, requiring special, custom integrations for each service. This stifles innovation and excludes smaller providers.

## The Solution: A "Universal Manual" for AI

AiSRG is an open standard that functions as an "Ai Service Reference Guide."

Simply put, AiSRG is a simple set of rules that allows any website or service to create an aisrg.json file—a "manual" that tells an AI:

"Hello! I am the Coffe Zoo website."

"Here are the services I can perform for you: view the menu, book a table."

"To book a table, here is the information you need and the back door (API Endpoint) you need to send it to."

For example, a simplified aisrg.json looks like this:
    ```{
    "aisrg_version": "1.1",
    "provider": {
    "name": "Coffe Zoo"
    },
    "actions": [
        {
          "action_id": "view_menu",
          "description": "View the menu",
          "endpoint": "api/",
          "method": "GET"
        },
        {
          "action_id": "book_table",
          "description": "Book a table",
          "endpoint": "api/",
          "method": "POST",
          "parameters": [
            { "name": "date", "type": "string" },
            { "name": "time", "type": "string" },
            { "name": "guests", "type": "integer" }
          ]
        }
    ]
    }

Through a simple discovery mechanism using a <meta> Tag, any AI that supports this standard can automatically discover and learn the capabilities of millions of websites.

🎯 AiSRG Advantages
✳️ No Hard Coding - AI automatically learns new services.
✳️ Standardized - Developers know how to implement them.
✳️ Extensible - Unlimited new services can be added.
✳️ Human-Friendly - Natural conversation.

## Our Vision: "The Open Kitchen"

We are not building a product; we are building an "Open Kitchen" where everyone can participate:

Service Providers can use our open "recipe" to make their services accessible to AI-powered customers.

AI Developers can build smarter and more useful "kitchen appliances" (AI Agents).

End-Users enjoy a seamless, truly automated experience.

We have chosen the Apache License 2.0 to ensure this standard remains open and secure for everyone, forever.

## Quickstart
1. Add an aisrg.json file to your service's web root.
2. Add the discovery <meta> tag to your HTML <head>:

    <meta name="aisrg:location" content="/aisrg.json">

3. Any AI Agent that supports AiSRG can now discover and interact with your service automatically.


## Roadmap
✅ Draft standard & initial documentation
🔄 Build reference implementation (SDK + AI connector)
🔄 Publish proof of concept integrations (e.g., Coffee zoo,Booking site)
🔜 Community discussion forum
See our docs/project_aisrg_documentation.md for more details.

## Contributing
We welcome contributors! 🚀
Try our Proof of Concept: poc/README.md
Open an issue or pull request in GitHub
Discuss ideas in our community forum (coming soon)
Help translate documentation (see README.th.md)


## License
AiSRG is released under the Apache License 2.0.
This ensures the standard remains open, free, and protected for the entire community.

## Links
🌐 Official Website: https://aisrg.org
💻 GitHub Repository: https://github.com/AiSRG-standard/standard

## We Invite You to Build the Future

AiSRG is a community-driven project, and this is just the beginning. We believe the real power will come from everyone who participates.
Let's build the next-generation infrastructure for the internet together—one where humans and AI can collaborate to their fullest potential.
