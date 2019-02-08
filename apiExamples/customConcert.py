import spotipy
import os
import sys
import spotipy.util as util

# User ID: 12125553997

username = '12125553997'

os.remove(f".cache-{username}")
token = util.prompt_for_user_token(username)

sp = spotipy.Spotify(auth=token)

user = sp.current_user()

print(user)
