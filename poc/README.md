AiSRG - Proof of Concept (PoC)
This directory contains a working proof of concept for the AiSRG standard. It is designed to demonstrate the full lifecycle of an AI Agent discovering, understanding, and executing a service's capabilities.

Components
This PoC consists of two main parts:

coffezoo/: A simulated service provider website for a coffee shop named "Coffe Zoo".

index.html: The homepage containing the AiSRG discovery meta tag.

aisrg.json: The standard-compliant guide file that describes the service's capabilities.

api/index.php: A simple API endpoint that simulates backend actions like view_menu and book_table.

agent/: A simulated AI Agent client.

agent.py: A Python script that acts as an AI Agent. It discovers, reads, and interacts with the "Coffe Zoo" service based on the aisrg.json guide.

How to Run This PoC
Prerequisites

A local web server with PHP support (e.g., XAMPP, MAMP, or Python's built-in server).

Python 3 installed on your machine.

Required Python libraries: requests and beautifulsoup4.

Step 1: Set up the Service Provider (coffezoo)

Place the coffezoo directory in the root of your local web server.

Make sure your web server is running. You should be able to access the homepage at an address like http://localhost/coffezoo/.

Step 2: Install Python Libraries

Open your terminal or command prompt and run the following command:

pip install requests beautifulsoup4

Step 3: Run the AI Agent

Navigate to the poc/agent/ directory in your terminal.

Run the script with the following command:

python agent.py

The script will prompt you for the URL of the service provider. Enter the address from Step 1 (e.g., http://localhost/coffezoo/).

Follow the on-screen instructions to test the available actions.
