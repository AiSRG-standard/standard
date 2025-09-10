# AiSRG - Proof of Concept (PoC)

This directory contains a working proof of concept for the AiSRG standard. It is designed to demonstrate the full lifecycle of an AI Agent discovering, understanding, and executing a service's capabilities.

## Example Conversation Flow
To understand the power of AiSRG, imagine the following conversation between a user and an AI Agent that supports the standard.

### User:

    "Hey, can you help me book a table at Coffe Zoo?"

### AI Agent (Internal monologue):

🔍 Discover: I'll find the Coffe Zoo website and scan it for an aisrg:location meta tag. Found it!

📖 Understand: I'll download the aisrg.json file. I see a book_table action is available.

🧠 Analyze: The action requires name, phone_number, date, time, and guests. I need to ask the user for this information.

### AI Agent (to User):

"Of course! To book your table at Coffe Zoo, what is your name and phone number, and for what date, time, and number of guests?"

### User:

"My name is Somchai, phone is 081-123-4567. For tomorrow at 2:30 PM, just for me."

### AI Agent (Internal monologue):

📦 Format: I'll structure this data into a JSON payload.

🚀 Execute: I'll send a POST request to the API endpoint specified in the guide.

📨 Receive: I've received a success response from the server with a booking ID.

💬 Translate: Now, I'll translate this result into a human-friendly message.

### AI Agent (to User):

"All set! I've successfully booked a table for you, Somchai. Your booking ID is #8412. You can contact Coffe Zoo directly at 02-xxxxxxx for any further questions."

## Components
This PoC consists of two main parts:

coffezoo/: A simulated service provider website.

agent/: A simulated AI Agent client.

## How to Run This PoC

### Prerequisites

A local web server with PHP support (e.g., XAMPP, MAMP, or Python's built-in server).

Python 3 installed on your machine.

Required Python libraries: requests and beautifulsoup4.

### Step 1: Set up the Service Provider (coffezoo)

Place the coffezoo directory in the root of your local web server.

Make sure your web server is running. You should be able to access the homepage at an address like http://localhost/coffezoo/.

### Step 2: Install Python Libraries

Open your terminal or command prompt and run the following command:

pip install requests beautifulsoup4

### Step 3: Run the AI Agent

Navigate to the poc/agent/ directory in your terminal.

Run the script with the following command:

python agent.py

The script will prompt you for the URL of the service provider. Enter the address from Step 1 (e.g., http://localhost/coffezoo/).

Follow the on-screen instructions to test the available actions.
