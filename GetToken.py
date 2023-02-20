import base64
import requests

client_id = 'YourClientID'
client_secret = 'YourClientSecret'

# Step 1: Encode the client ID and client secret as base64
encoded_auth = base64.b64encode(f'{client_id}:{client_secret}'.encode('ascii')).decode('ascii')

# Step 2: Make a POST request to the Spotify Accounts service to retrieve the access token
token_url = 'https://accounts.spotify.com/api/token'
response = requests.post(token_url, 
                         headers={
                            'Authorization': f'Basic {encoded_auth}',
                            'Content-Type': 'application/x-www-form-urlencoded'
                         },
                         data={
                            'grant_type': 'client_credentials'
                         })

response_json = response.json()

access_token = response_json['access_token']
print(access_token)
