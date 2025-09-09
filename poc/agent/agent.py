import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin

def discover_aisrg_guide(url):
    """
    Scans a URL for the AiSRG meta tag and returns the URL of the guide file.
    """
    print(f"\n[INFO] Scanning {url} for AiSRG meta tag...")
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise an exception for bad status codes
        soup = BeautifulSoup(response.text, 'html.parser')
        
        meta_tag = soup.find('meta', {'name': 'aisrg:location'})
        
        if meta_tag and meta_tag.get('content'):
            guide_path = meta_tag.get('content')
            guide_url = urljoin(url, guide_path) # Properly join the base URL and the path
            print(f"[SUCCESS] Found AiSRG guide at: {guide_url}")
            return guide_url
        else:
            print("[FAIL] This website does not support the AiSRG standard.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Could not fetch URL: {e}")
        return None

def fetch_and_parse_guide(guide_url):
    """
    Fetches and parses the AiSRG JSON guide file.
    """
    print(f"\n[INFO] Fetching and parsing the guide from {guide_url}...")
    try:
        response = requests.get(guide_url, timeout=5)
        response.raise_for_status()
        guide_data = response.json()
        print("[SUCCESS] Guide parsed successfully.")
        return guide_data
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Could not fetch guide file: {e}")
        return None
    except json.JSONDecodeError:
        print("[ERROR] Failed to decode JSON from the guide file.")
        return None

def execute_action(base_url, action, guide):
    """
    Gathers parameters and executes a selected action.
    """
    print(f"\n[ACTION] Preparing to execute '{action['action_id']}'...")
    print(f"Description: {action['description']}")
    
    params = {}
    if 'parameters' in action and action['parameters']:
        for param in action['parameters']:
            user_input = input(f"Please enter {param['name']} ({param['description']}): ")
            params[param['name']] = user_input
            
    endpoint_url = urljoin(base_url, action['endpoint'])
    method = action['method'].upper()
    
    print(f"\n[EXEC] Sending {method} request to {endpoint_url} with data: {params}")
    
    try:
        if method == 'GET':
            response = requests.get(endpoint_url, params=params, timeout=5)
        elif method == 'POST':
            response = requests.post(endpoint_url, json=params, timeout=5)
        else:
            print(f"[ERROR] Unsupported HTTP method: {method}")
            return
            
        response.raise_for_status()
        response_data = response.json()
        
        # Use the response template from the guide
        success_template = action['responses']['success']
        formatted_response = success_template.format(**response_data)
        
        print("\n------------------ RESULT ------------------")
        print(f"[SUCCESS] {formatted_response}")
        print("------------------------------------------")

    except requests.exceptions.RequestException as e:
        print(f"[ERROR] API request failed: {e}")
    except KeyError as e:
         print(f"[ERROR] Response data is missing a key needed for the template: {e}")


def main():
    print("--- AiSRG AI Agent PoC ---")
    
    # 1. Discovery
    base_url = input("Please enter a website URL to check for AiSRG compatibility: ")
    if not base_url.endswith('/'):
        base_url += '/'
        
    guide_url = discover_aisrg_guide(base_url)
    if not guide_url:
        return

    # 2. Understanding
    guide = fetch_and_parse_guide(guide_url)
    if not guide:
        return
        
    print("\n[INFO] Provider:", guide.get('provider', {}).get('name', 'N/A'))
    print("       Standard Version:", guide.get('aisrg_version', 'N/A'))

    # 3. User Intent
    actions = {action['action_id']: action for action in guide.get('actions', [])}
    if not actions:
        print("\n[WARN] No actions found in the guide.")
        return
        
    print("\nAvailable actions:")
    for action_id in actions.keys():
        print(f"- {action_id}")
        
    chosen_action_id = input("Which action would you like to perform? ")
    
    if chosen_action_id in actions:
        execute_action(base_url, actions[chosen_action_id], guide)
    else:
        print("[ERROR] Invalid action selected.")

if __name__ == "__main__":
    main()

