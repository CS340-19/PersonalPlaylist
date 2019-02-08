from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import json
import sys

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

uri = sys.argv[1]
username = uri.split(':')[2]
playlist_id = uri.split(':')[4]


def define_song(above_or_below='above', value=.8, mode='danceability'):
    tracks = sp.user_playlist(username, playlist_id)['tracks']['items']
    features = sp.audio_features(track['track']['id'])[0]
    print(track['track']['name']+" // "+track['track']['artists'][0]['name']+" "+str(features[mode]))
define_song(sys.argv[2], float(sys.argv[3]), sys.argv[4])
