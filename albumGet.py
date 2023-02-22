import requests
import APIrequest

access_token = APIrequest.access_token

#Working Example
song_name = 'Matilda'
artist_name = 'PUP'
#Broken Example
#song_name = 'The End of Me feat. Rivers Cuomo'
#artist_name = 'Billy Talent'

search_url = f'https://api.spotify.com/v1/search?q={song_name}+artist:{artist_name}&type=track'

# Step 2: Make a search request
response = requests.get(search_url, headers={'Authorization': f'Bearer {access_token}'})
response_json = response.json()

#Test JSON
track = response_json['tracks']['items']

if len(track)==0:
    print('No Hit')
else:
    track = response_json['tracks']['items'][0]
    print(track)

# Step 3: Get the album ID
#track = response_json['tracks']['items'][0]
#album_id = track['album']['id']


#Set Album URL
#album_url = f'https://api.spotify.com/v1/albums/{album_id}'

# Step 4: Get the album information
#response = requests.get(album_url, headers={'Authorization': f'Bearer {access_token}'})
#response_json = response.json()

#album_name = response_json['name']
#print(album_name)
