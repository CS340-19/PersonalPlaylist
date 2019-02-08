import pprint
import sys

import spotipy
import spotipy.util as util
import simplejson as json

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

scope = 'user-top-read'
token = util.prompt_for_user_token(username, scope)

def top_song_screener(above_or_below='above', value=.8, numsongs=50, mode='danceability'):
    if token:
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        ranges = ['short_term', 'medium_term', 'long_term']
        for range in ranges:
            print("range:", range)
            results = sp.current_user_top_tracks(time_range=range, limit=numsongs)
            for i, item in enumerate(results['items']):
                features = sp.audio_features(item['id'])[0]
                if(above_or_below=='above'):
                    if (features[mode]>=value):
                        print(i, item['name'], '//', item['artists'][0]['name'], features[mode])
                if(above_or_below=='below'):
                    if (features[mode]<=value):
                        print(i, item['name'], '//', item['artists'][0]['name'], features[mode])
            print

    else:
        print("Can't get token for", username)

#``top_song_screener('above',.8,50,'danceability')
