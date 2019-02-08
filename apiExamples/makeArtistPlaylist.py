import spotipy
import sys
import pprint
import sys
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
if len(sys.argv) > 1:
    urn = sys.argv[1]
    mode = sys.argv[2]
    screen = sys.argv[3]
    tag = sys.argv[4]
else:
    urn = 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'
results = sp.artist_albums(urn, album_type='album')
albums = results['items']
while results['next']:
    results = sp.next(results)
    albums.extend(results['items'])

songs = []
i = 0;
for album in albums:
    for track in sp.album(album['uri'])['tracks']['items']:
        features = sp.audio_features(track['id'])[0]
        if(mode=='above'):
            if float(features[tag])>=float(screen):
                sys.stdout.write(track['name']+" // ")
                for artist in track['artists']:
                    sys.stdout.write(artist['name']+' ')
                print(features[tag])
        if(mode=='below'):
            if float(features[tag])<=float(screen):
                sys.stdout.write(track['name']+" // ")
                for artist in track['artists']:
                    sys.stdout.write(artist['name']+' ')
                print(features[tag])


