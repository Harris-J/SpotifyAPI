import requests

access_token = 'YourTokenHere'
song_name = 'Jackson'
artist_name = 'Johnny Cash'

search_url = f'https://api.spotify.com/v1/search?q={song_name}+artist:{artist_name}&type=track'

# Step 2: Make a search request
response = requests.get(search_url, headers={'Authorization': f'Bearer {access_token}'})
response_json = response.json()

# Step 3: Get the album ID
track = response_json['tracks']['items'][0]
album_id = track['album']['id']

album_url = f'https://api.spotify.com/v1/albums/{album_id}'

# Step 4: Get the album information
response = requests.get(album_url, headers={'Authorization': f'Bearer {access_token}'})
response_json = response.json()

album_name = response_json['name']
print(album_name)
