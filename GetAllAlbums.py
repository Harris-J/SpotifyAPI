import csv
import requests
import APIrequest
#import GetToken

#Get Token needs to run first to get this varible. I'm sure it could all be called here more elegantly
access_token = APIrequest.access_token
#access_token = GetToken.access_token

#I have a local file called APIrequest with my real credential - saving this so I don't forget I did that. Future me will figure out a better way to work with API credentials and tokens (har har)

with open('input.csv', encoding='utf-8', mode='r') as f:
    reader = csv.reader(f)
    data = list(reader)

for row in data:
    artist_name = row[0]
    song_name = row[1]

    search_url = f'https://api.spotify.com/v1/search?q={song_name}+artist:{artist_name}&type=track'

    response = requests.get(search_url, headers={'Authorization': f'Bearer {access_token}'})
    response_json = response.json()

    track = response_json['tracks']['items'][0]
    album_id = track['album']['id']

    album_url = f'https://api.spotify.com/v1/albums/{album_id}'

    response = requests.get(album_url, headers={'Authorization': f'Bearer {access_token}'})
    response_json = response.json()

    album_name = response_json['name']

    row.append(album_name)

with open('output.csv', encoding='utf-8', mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)
