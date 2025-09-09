Project AiSRG - Official Documentation
Official Website and Latest Version: https://aisrg.org

Draft Standard Document 1.1

Chapter 1: Introduction
1.1 What is AiSRG?

AiSRG (Ai Service Reference Guide) is an open standard that acts as a "universal translator" between artificial intelligence (AI) and digital service providers (e.g., websites, applications, or various systems).

Simply put, AiSRG is a "manual" that a website can provide, allowing any AI from any developer to read and instantly understand "what this website can do and how to interact with it." This unlocks the potential for AI to evolve from being a mere "information provider" to a true "AI Agent" that can take action.

1.2 Philosophy & Vision

We believe the future is a world where humans, AI, and businesses can collaborate seamlessly. AiSRG's vision is to create an open and democratic infrastructure where even small business owners can make their services "AI-ready" on par with large corporations. It is an innovation born from the collaboration between humans and AI for the benefit of everyone.

1.3 Core Principles

The AiSRG standard is built on three core principles:

👐 Open: An open standard that anyone can use for free, independent of any single company.

📜 Standardized: A clear structure and set of rules ensure that AI and service providers have a mutual understanding.

🔒 Secure: A robust authentication mechanism is in place to protect both users and service providers.

Chapter 2: Quick Start Guide
🏢 For Business Providers

Want to make your website "AI-Ready"? Follow these 3 simple steps:

Create a Guide File: Write a .json file to describe what your service can do, using the AiSRG standard structure (see Chapter 4 for details).

Add a Meta Tag: Add the Meta Tag <meta name="aisrg:location" content="/path/to/your-guide.json"> to the homepage of your website.

Prepare Your API: Create API endpoints ready to receive commands from an AI, as specified in your guide file.

🤖 For AI Developers

Want your AI to be able to "command" various websites?

Discover the Guide: When your AI visits a website, scan for the aisrg:location Meta Tag in the HTML code.

Read and Understand: If the tag is found, download and parse the specified .json file to learn all the capabilities of that website.

Execute Commands: When a user gives a command, your AI will know exactly which API endpoint to send a request to and with what parameters.

Chapter 3: Core Concepts
The Three Pillars of AiSRG

The AiSRG standard is built upon three pillars that work together systemically.

1. Discovery

The heart of discovery is the Meta Tag in the HTML page (<meta name="aisrg:location" content="...">). It acts as a "signpost," letting an AI know that the website supports the AiSRG standard and where to find the .json guide file. This method gives service providers the flexibility to name and store their guide files as they see fit.

2. Specification

The aisrg.json file is the "blueprint" or "contract" that describes all the service's capabilities in a detailed and standardized manner. It includes crucial information such as provider details, supported authentication methods, and a list of all "Actions" the AI can execute. This standardization ensures that AIs from all developers can interpret and interact correctly.

3. Security

AiSRG is designed with security as a priority, supporting two main authentication mechanisms: OTP (suitable for occasional, high-security transactions) and OAuth 2.0 (ideal for continuous use and a better user experience). Service providers can choose the appropriate security level for each Action.

Chapter 4: Specification Reference
This section provides the technical details for every component in the aisrg.json file.

4.1 Root Object

aisrg_version (String, Required): The version of the AiSRG standard this file adheres to (e.g., "1.1").

provider (Object, Required): Information about the service provider.

verification (Object, Optional): The domain ownership verification mechanism.

authentication (Object, Required): Declares the supported authentication methods.

actions (Array, Required): A list of all "Actions" this service can perform.

4.2 The verification Object

method (String, Required): The verification method used. Currently supports "dns-txt".

proof (String, Required): The "proof" used for verification, e.g., aisrg-verification=your-unique-string.

4.3 The authentication Object

methods_supported (Array of Strings, Required): A list of supported methods ("otp", "oauth2").

otp_endpoint (String, Conditional): The URL for requesting an OTP.

oauth2_endpoint (String, Conditional): The URL to start the OAuth 2.0 process.

4.4 The action Object

action_id (String, Required): A unique identifier for the action.

description (String, Required): A description of what the action does.

security_level (String, Required): The required security level ("none", "otp_required", "oauth2_required", "oauth2_preferred").

endpoint (String, Required): The API endpoint URL for this action.

method (String, Required): The required HTTP method ("GET", "POST", etc.).

parameters (Array of Objects, Optional): A list of data required for this action.

responses (Object, Required): Sample response messages for success and failure cases.

4.5 The parameters Object

name (String, Required): The name of the parameter.

type (String, Required): The data type ("string", "integer", "array", etc.).

required (Boolean, Required): Specifies whether the parameter is required.

description (String, Required): A description of the parameter.

format (String, Optional): A specific data format, e.g., "YYYY-MM-DD".

4.6 The responses Object

success (String, Required): The response message for success. May contain {...} placeholders.

failure (String, Required): The response message for failure. May contain {...} placeholders.

Chapter 5: Security Guide
5.1 "User" Authentication

OTP Flow: Used for important, infrequent transactions. The system sends a one-time password to the user for verification.

OAuth 2.0 Flow: Used for continuous sessions. The user logs in and grants consent once, after which the AI Agent uses an Access Token for subsequent verifications.

5.2 "API Caller" (Client/Agent) Authentication

To prevent attacks from malicious scripts, the AiSRG standard recommends using a client authentication mechanism based on Asymmetric Cryptography (e.g., a digitally signed JWT). Each AI Agent vendor should sign its API requests with its private key, and the service provider can verify this signature using the vendor's public key.

5.3 General Best Practices

All communication between the AI and API endpoints must be over HTTPS.

Errors should be handled gracefully, with clear status updates provided to the AI.

5.4 Provider Identity Verification

To prevent phishing from fake websites that mimic a legitimate service's aisrg.json file, the AiSRG standard includes a domain ownership verification mechanism.

Principle: Only the true domain owner can modify its DNS records.

Method:

Create Proof: The service provider adds a specific TXT Record to their domain's DNS.

Declare Proof: The value of that TXT Record is placed in the verification object within the aisrg.json file.

AI Verification: The AI Agent performs a DNS query on the domain to compare the TXT Record value with the one declared in the json file. A match confirms the service's authenticity.

Chapter 6: Examples & Use Cases
6.1 Full Example: "Coffe Zoo"

This is a complete example of an aisrg.json file for the "Coffe Zoo" coffee shop (v1.1), including the verification mechanism.

{
  "aisrg_version": "1.1",
  "provider": {
    "name": "Coffe Zoo",
    "website": "[https://coffezoo.com](https://coffezoo.com)"
  },
  "verification": {
    "method": "dns-txt",
    "proof": "aisrg-verification=a-very-unique-and-random-string-generated-by-coffezoo"
  },
  "authentication": {
    "methods_supported": ["otp", "oauth2"],
    "otp_endpoint": "[https://api.coffezoo.com/v1/auth/request-otp](https://api.coffezoo.com/v1/auth/request-otp)",
    "oauth2_endpoint": "[https://api.coffezoo.com/v1/auth/oauth2](https://api.coffezoo.com/v1/auth/oauth2)"
  },
  "actions": [
    {
      "action_id": "view_menu",
      "description": "View the full menu of drinks and food.",
      "security_level": "none",
      "endpoint": "[https://api.coffezoo.com/v1/menu](https://api.coffezoo.com/v1/menu)",
      "method": "GET",
      "parameters": [],
      "responses": {
        "success": "Here is our recommended menu: {menu_items}",
        "failure": "Sorry, the menu could not be retrieved at this time."
      }
    }
  ]
}

