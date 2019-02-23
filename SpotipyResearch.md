# Spotipy Research

This is a summary of the research done on the Python Spotify API (Spotipy). It highlights how to authorize the application in a Spotify application through Python, which was found to be the largest issue when testing some starting code.

## Authorized Requests

Spotipy supports two from s of authorization to request data from the Spotify servers. These are through Authorization Code Flow and Client Credentials Flow.

### Authorization Code Flow

Spotipy provides a utility method that will attempt to authorize the user.

```python
spotipy.util.prompt_for_user_token(username,scope,client_id='your-app-redirect-url',client_secret='your-app-redirect-url',redirect_uri='your-app-redirect-url')
```

The arguments of this method are described as follows:
username - the username of the user granting access to their account's listening history

scope - the scope in which the application is reading information

client_id - the specific ID of the Spotipy client, gotten from the Spotify developer's dashboard

client_secret - The specific secret assigned to your application, gotten from the Spotify developer's dashboard

redirect_uri - the URI set up with your application, this can be used to redirect the user to whatever URL you have set up for the application

### Client Credentials Flow

Spotipy provides a utility method that will authorize an application to read data from Spotify servers, but not connected to a user's account. This is done through this method.

```python
spotipy.oauth2.SpotifyClientCredentials(client_id='your client ID', client_secret='your client secret', proxies=None)
```

Client credentials flow is appropriate for requests that do not require access to a user's private data.

## IDs, URIs, and URLs

Spotipy supports 3 different ID types. These IDs are for specific tracks, albums, artists, and playlists. In general, any Spotipy method that accepts one of these as an argument will accept any one of these identifiers.

These identifiers are described as follows:

Spotify ID - a base-62 number that signifies a track, album, artist, or playlist Ex. 6rqhFgbbKwnb9MLmUQDhG6

Spotify URI - a resource identifier that signifies a track, album artist, or playlist, the ending of which is its Spotify ID Ex. spotify:track:6rqhFgbbKwnb9MLmUQDhG6

Spotify URL - an HTML link that opens a track, album, artist, or playlist or other Spotify resource in a Spotify client Ex. http://open.spotify.com/track/6rqhFgbbKwnb9MLmUQDhG6

---

Further information on Spotipy and an API Reference can be found [here](https://spotipy.readthedocks.io/en/latest).
