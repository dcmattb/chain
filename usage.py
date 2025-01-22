# Show API Usage and test connection to Chainalysis IAPI
import secrets
import requests, datetime, json

# Set the API KEY in the headers
headers = {
  "token": secrets.API_KEY,
  "accept": "application/json"
}

# Use today's date in ISO format
today = datetime.date.today().isoformat()

# The IAPI URL
url = f"https://iapi.chainalysis.com/usage/user/2025-01-01/{today}"

# Send the request
response = requests.get(url, headers=headers)

if response.status_code == 200:
  # Successful response
  print(json.dumps(response.json(), indent=2))
else:
  # Error
  print(f"Error {response.status_code}")
