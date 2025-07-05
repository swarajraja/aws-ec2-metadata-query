import requests    # For making HTTP requests
import sys         # For handling command-line arguments
import json        # For formatting output as JSON

# Base URL for EC2 instance metadata service
METADATA_URL = "http://169.254.169.254/latest/meta-data"

def get_token():
    """
    Obtain a session token from the EC2 Instance Metadata Service v2 (IMDSv2).
    This token is required for all subsequent metadata queries.
    """
    token_url = "http://169.254.169.254/latest/api/token"
    headers = {"X-aws-ec2-metadata-token-ttl-seconds": "21600"}  # Token valid for 6 hours
    resp = requests.put(token_url, headers=headers, timeout=2)   # Send PUT request to get token
    resp.raise_for_status()  # Raise exception if request fails
    return resp.text         # Return the token string

def get_metadata(token, key=None):
    """
    Retrieve metadata from the EC2 instance.
    If a key is provided, fetch only that key's value.
    If no key is provided, fetch all top-level metadata keys and their values.
    """
    headers = {"X-aws-ec2-metadata-token": token}  # Attach token to headers

    if key:
        # If a specific key is provided, construct its URL and fetch its value
        url = f"{METADATA_URL}/{key}"
        resp = requests.get(url, headers=headers, timeout=2)
        if resp.status_code == 200:
            return {key: resp.text}  # Return the key and its value in a dict
        else:
            return {"error": "Key not found or not available"}  # Handle missing key
    else:
        # If no key is provided, fetch all top-level keys
        resp = requests.get(METADATA_URL + "/", headers=headers, timeout=2)
        keys = resp.text.strip().split('\n')  # Get list of keys
        metadata = {}
        for k in keys:
            # Fetch the value for each key
            value_resp = requests.get(f"{METADATA_URL}/{k}", headers=headers, timeout=2)
            metadata[k] = value_resp.text
        return metadata  # Return all key-value pairs as a dict

def main():
    """
    Main function to handle argument parsing, token retrieval,
    metadata fetching, and output formatting.
    """
    # Check if a metadata key is provided as a command-line argument
    key = sys.argv[1] if len(sys.argv) > 1 else None
    try:
        token = get_token()               # Get IMDSv2 token
        data = get_metadata(token, key)   # Fetch metadata (all or specific key)
        print(json.dumps(data, indent=2)) # Print as pretty-formatted JSON
    except Exception as e:
        # Print any errors in JSON format
        print(json.dumps({"error": str(e)}))

# Entry point for the script
if __name__ == "__main__":
    main()
