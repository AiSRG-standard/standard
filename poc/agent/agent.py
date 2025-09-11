import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin

def discover_aisrg_guide(url):
    """Scans a URL for the AiSRG meta tag and returns the URL of the guide file."""
    print(f"\n[INFO] 🕵️  Scanning {url} for AiSRG meta tag...")
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        meta_tag = soup.find('meta', {'name': 'aisrg:location'})
        if meta_tag and meta_tag.get('content'):
            guide_path = meta_tag.get('content')
            guide_url = urljoin(url, guide_path)
            print(f"[SUCCESS] ✅ Found AiSRG guide at: {guide_url}")
            return guide_url
        else:
            print("[FAIL] ❌ This website does not support the AiSRG standard.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] 💥 Could not fetch URL: {e}")
        return None

def fetch_and_parse_guide(guide_url):
    """Fetches and parses the AiSRG JSON guide file."""
    print(f"\n[INFO] 📖 Fetching and parsing the guide from {guide_url}...")
    try:
        response = requests.get(guide_url, timeout=5)
        response.raise_for_status()
        guide_data = response.json()
        print("[SUCCESS] ✅ Guide parsed successfully.")
        return guide_data
    except (requests.exceptions.RequestException, json.JSONDecodeError) as e:
        print(f"[ERROR] 💥 Failed to fetch or parse guide file: {e}")
        return None

def execute_action(base_url, action):
    """Gathers parameters and executes a selected action."""
    print(f"\n[ACTION] ▶️  Preparing to execute '{action['action_id']}'...")
    print(f"   Description: {action['description']}")

    params = {}
    if action.get('parameters'):
        print("\n[INFO] ✍️  This action requires the following information:")
        for param in action['parameters']:
            user_input = input(f"   Please enter {param['name']} ({param['description']}): ")
            params[param['name']] = user_input

    endpoint_url = urljoin(base_url, action['endpoint'])
    method = action['method'].upper()

    print(f"\n[EXEC] 🚀 Sending {method} request to {endpoint_url} with data: {params}")

    try:
        if method == 'GET':
            response = requests.get(endpoint_url, params=params, timeout=5)
        elif method == 'POST':
            response = requests.post(endpoint_url, json=params, timeout=5)
        else:
            print(f"[ERROR] ❌ Unsupported HTTP method: {method}")
            return

        response.raise_for_status()
        response_data = response.json()

        success_template = action['responses']['success']
        formatted_response = success_template.format(**response_data)

        print("\n" + "="*40)
        print("🎉 ACTION SUCCEEDED! 🎉")
        print(f"   {formatted_response}")
        print("="*40)

    except requests.exceptions.RequestException as e:
        print(f"\n[ERROR] 💥 API request failed: {e}")
    except KeyError as e:
         print(f"\n[ERROR] 💥 Response data is missing a key for the template: {e}")

def main():
    print("--- AiSRG AI Agent PoC (v2) ---")
    base_url = input("Please enter a website URL (e.g., http://localhost/coffezoo/): ")
    if not base_url.endswith('/'):
        base_url += '/'

    guide_url = discover_aisrg_guide(base_url)
    if not guide_url: return

    guide = fetch_and_parse_guide(guide_url)
    if not guide: return

    print("\n[INFO] ✅ Provider Verified:", guide.get('provider', {}).get('name', 'N/A'))

    actions = {action['action_id']: action for action in guide.get('actions', [])}
    if not actions:
        print("\n[WARN] ⚠️ No actions found in the guide.")
        return

    print("\nAvailable actions:")
    for action_id in actions.keys():
        print(f"- {action_id}")

    chosen_action_id = input("\nWhich action would you like to perform? ")

    if chosen_action_id in actions:
        execute_action(base_url, actions[chosen_action_id])
    else:
        print("[ERROR] ❌ Invalid action selected.")

if __name__ == "__main__":
    main()

    
