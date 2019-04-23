from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpRequest
from .forms import UsernameForm
import spotipy.oauth2 as oauth2
import spotipy
import os
import random

SPOTIPY_CLIENT_ID = 'b15385ab56f944d0b0fb57fe4ec457db'
SPOTIPY_CLIENT_SECRET = '98018551dff340bbbffe87487726b7bb'
SPOTIPY_REDIRECT_URI = 'http://127.0.0.1:8000/rcode'
SCOPE = 'user-top-read'

global user_token

def index(request):
    context = {}

    print('Making Spotify client credentials')
    client_credentials = oauth2.SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID,
                                                         client_secret=SPOTIPY_CLIENT_SECRET)

    if 'username' in request.session:
        print('Username found')
        sp_oauth = oauth2.SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                       client_secret=SPOTIPY_CLIENT_SECRET,
                                       redirect_uri=SPOTIPY_REDIRECT_URI,
                                       scope=SCOPE,
                                       cache_path="user_caches/.cache-" + request.session['username'])

        token_info = sp_oauth.get_cached_token()

        sp = spotipy.Spotify(auth=token_info['access_token'],
                             client_credentials_manager=client_credentials)

        results = sp.current_user_top_artists(limit=1)

        seed_artists = list()
        for artist in results['items']:
            seed_artists.append(artist['id'])

        recommended = sp.recommendations(seed_artists=seed_artists,
                                         limit=30,
                                         target_accousticness=0.5,
                                         target_danceability=0.5,
                                         target_energy=0.5,
                                         target_instrumentalness=0.5,
                                         target_liveness=0.5,
                                         target_loudness=0.5,
                                         target_speechiness=-30,
                                         target_valence=0.5,
                                         target_tempo=125)

        context['logged_in'] = True
        context['username'] = sp.current_user()['display_name']
    else:
        sp = spotipy.Spotify(client_credentials_manager=client_credentials)

        results = sp.recommendation_genre_seeds()

        seed_genres = list()
        for i in range(0,5):
            genre_index = random.randint(0, len(results['genres']))
            seed_genres.append(results['genres'][genre_index])

        recommended = sp.recommendations(seed_genres=seed_genres,
                                         limit=30,
                                         target_accousticness=0.5,
                                         target_danceability=0.5,
                                         target_energy=0.5,
                                         target_instrumentalness=0.5,
                                         target_liveness=0.5,
                                         target_loudness=0.5,
                                         target_speechiness=-30,
                                         target_valence=0.5,
                                         target_tempo=125)

    j = 0
    tracks = list()
    track_row = list()
    for track in recommended['tracks']:
        track_row.append(track)
        j += 1

        if j == 3:
            print(track_row)
            print()
            tracks.append(track_row)
            track_row = list()
            j = 0

    context['tracks'] = tracks

    return render(request, 'PPMaker/index.html', context)

def login(request):
    if request.method == "POST":
        form = UsernameForm(request.POST)

        if form.is_valid():
            request.session['username'] = form.cleaned_data['username']

    if 'username' in request.session:
        sp_oauth = oauth2.SpotifyOAuth(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI,
                                       scope=SCOPE, cache_path="user_caches/.cache-" + request.session['username'])
        token_info = sp_oauth.get_cached_token()

        if token_info:
            print('Found cached token')
            return render(request, 'PPMaker/login.html', {'logged_in': True})
        else:
            auth_url = sp_oauth.get_authorize_url()

            print('Redirecting to Spotify authorization')
            return redirect(auth_url)

    form = UsernameForm()

    print('Prompting for username')
    return render(request, 'PPMaker/login.html', {'form': form})

def rcode(request):
    if 'username' not in request.session:
        return redirect('login')

    sp_oauth = oauth2.SpotifyOAuth(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI,
                                   scope=SCOPE, cache_path="user_caches/.cache-" + request.session['username'])
    url = request.build_absolute_uri()
    code = sp_oauth.parse_response_code(url=url)
    token_info = sp_oauth.get_access_token(code)

    if token_info:
        print('Received user token')
        return render(request, 'PPMaker/login.html', {'logged_in': True})
    else:
        print('Failed to receive user token')
        del request.session['username']
        return redirect('login')

def logout(request):
    if 'username' not in request.session:
        return redirect('index')

    cache_path = "user_caches/.cache-" + request.session['username']
    os.remove(cache_path)
    del request.session['username']
    print('Removed user\'s saved data')

    return redirect('index')
