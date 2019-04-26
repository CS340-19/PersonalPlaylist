from django.shortcuts import render, redirect
import spotipy.oauth2 as oauth2
import spotipy
import os
import random
import json

SPOTIPY_CLIENT_ID = 'b15385ab56f944d0b0fb57fe4ec457db'
SPOTIPY_CLIENT_SECRET = '98018551dff340bbbffe87487726b7bb'
SPOTIPY_REDIRECT_URI = 'http://127.0.0.1:8000/rcode'
SCOPE = 'user-top-read playlist-modify-public'


def index(request):
    context = {}

    print('Making Spotify client credentials')
    client_credentials = oauth2.SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID,
                                                         client_secret=SPOTIPY_CLIENT_SECRET)

    if 'user_id' in request.session:
        print('User ID found')
        sp_oauth = oauth2.SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                       client_secret=SPOTIPY_CLIENT_SECRET,
                                       redirect_uri=SPOTIPY_REDIRECT_URI,
                                       scope=SCOPE,
                                       cache_path="user_caches/.cache-" + request.session['user_id'])

        token_info = sp_oauth.get_cached_token()
        if not token_info:
            cache_path = "user_caches/.cache-" + request.session['user_id']
            os.remove(cache_path)
            del request.session['user_id']
            return redirect('login')


        sp = spotipy.Spotify(auth=token_info['access_token'],
                             client_credentials_manager=client_credentials)

        context['logged_in'] = True
        context['username'] = sp.current_user()['display_name']
    else:
        sp = spotipy.Spotify(client_credentials_manager=client_credentials)

    if request.method == 'POST':
        request.session['accousticness'] = float(request.POST.getlist('accousticness')[0])
        request.session['danceability'] = float(request.POST.getlist('danceability')[0])
        request.session['energy'] = float(request.POST.getlist('energy')[0])
        request.session['instrumentalness'] = float(request.POST.getlist('instrumentalness')[0])
        request.session['liveness'] = float(request.POST.getlist('liveness')[0])
        request.session['loudness'] = float(request.POST.getlist('loudness')[0])
        request.session['speechiness'] = float(request.POST.getlist('speechiness')[0])
        request.session['valence'] = float(request.POST.getlist('valence')[0])
        request.session['tempo'] = float(request.POST.getlist('tempo')[0])
        request.session['genre'] = request.POST.getlist('genre')[0]
        return redirect('index')

    results = sp.recommendation_genre_seeds();

    genres = {}
    for genre in results['genres']:
        genres[genre] = genre.capitalize()

    context['genres'] = genres

    if 'attributes_set' not in request.session:
        request.session['accousticness'] = 0.5
        request.session['danceability'] = 0.5
        request.session['energy'] = 0.5
        request.session['instrumentalness'] = 0.5
        request.session['liveness'] = 0.5
        request.session['loudness'] = 0.5
        request.session['speechiness'] = -30
        request.session['valence'] = 0.5
        request.session['tempo'] = 125
        request.session['genre'] = results['genres'][random.randint(0, len(results['genres'])-1)]
        request.session['attributes_set'] = True

    context['attributes'] = {
        'accousticness': request.session['accousticness'],
        'danceability': request.session['danceability'],
        'energy': request.session['energy'],
        'instrumentalness': request.session['instrumentalness'],
        'liveness': request.session['liveness'],
        'loudness': request.session['loudness'],
        'speechiness': request.session['speechiness'],
        'valence': request.session['valence'],
        'tempo': request.session['tempo'],
        'genre': request.session['genre']
    }

    recommended = sp.recommendations(seed_genres=[request.session['genre']],
                                     limit=30,
                                     target_accousticness=request.session['accousticness'],
                                     target_danceability=request.session['danceability'],
                                     target_energy=request.session['energy'],
                                     target_instrumentalness=request.session['instrumentalness'],
                                     target_liveness=request.session['liveness'],
                                     target_loudness=request.session['loudness'],
                                     target_speechiness=request.session['speechiness'],
                                     target_valence=request.session['valence'],
                                     target_tempo=request.session['tempo'])

    j = 0
    tracks = list()
    track_row = list()
    for track in recommended['tracks']:
        track_row.append(track)
        j += 1

        if j == 3:
            tracks.append(track_row)
            track_row = list()
            j = 0

    request.session['tracks'] = json.dumps(recommended['tracks'])

    context['tracks'] = tracks

    return render(request, 'PPMaker/index.html', context)


def login(request):
    if 'user_id' in request.session:
        sp_oauth = oauth2.SpotifyOAuth(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI,
                                       scope=SCOPE, cache_path="user_caches/.cache-" + request.session['user_id'])
        token_info = sp_oauth.get_cached_token()

        if token_info:
            print('Found cached token')
            return redirect('index')
        else:
            auth_url = sp_oauth.get_authorize_url()

            print('Redirecting to Spotify authorization')
            return redirect(auth_url)
    else:
        sp_oauth = oauth2.SpotifyOAuth(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI, scope=SCOPE)
        auth_url = sp_oauth.get_authorize_url()
        return redirect(auth_url)


def rcode(request):
    if 'user_id' in request.session:
        return redirect('login')

    sp_oauth = oauth2.SpotifyOAuth(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI, scope=SCOPE)
    url = request.build_absolute_uri()
    code = sp_oauth.parse_response_code(url=url)
    token_info = sp_oauth.get_access_token(code)

    if token_info:
        print('Received user token')

        sp = spotipy.Spotify(auth=token_info['access_token'])
        user = sp.current_user()

        cache_path = 'user_caches/.cache-' + user['id']
        f = open(cache_path, "w+")
        f.write(json.dumps(token_info))
        f.close()

        request.session['user_id'] = user['id']

        return redirect('login')
    else:
        print('Failed to receive user token')
        del request.session['user_id']
        return redirect('login')


def logout(request):
    if 'user_id' not in request.session:
        return redirect('index')

    cache_path = "user_caches/.cache-" + request.session['user_id']
    os.remove(cache_path)
    del request.session['user_id']
    print('Removed user\'s saved data')

    return redirect('index')

def add(request):
    if 'user_id' not in request.session:
        return redirect('index')

    context = {}

    client_credentials = oauth2.SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID,
                                                         client_secret=SPOTIPY_CLIENT_SECRET)

    print('User ID found')
    sp_oauth = oauth2.SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                   client_secret=SPOTIPY_CLIENT_SECRET,
                                   redirect_uri=SPOTIPY_REDIRECT_URI,
                                   scope=SCOPE,
                                   cache_path="user_caches/.cache-" + request.session['user_id'])

    token_info = sp_oauth.get_cached_token()

    sp = spotipy.Spotify(auth=token_info['access_token'],
                         client_credentials_manager=client_credentials)

    context['username'] = sp.current_user()['display_name']

    if request.method == "POST":
        playlist_name = request.POST.getlist('playlist_name')[0]
        user_id = sp.current_user()['id']

        playlist = sp.user_playlist_create(user_id, playlist_name)
        track_list = json.loads(request.session['tracks'])
        track_ids = list()
        for track in track_list:
            track_ids.append(track['id'])

        sp.user_playlist_add_tracks(user_id, playlist['id'], track_ids)

        return redirect('index')

    return render(request, 'PPMaker/add.html', context)
