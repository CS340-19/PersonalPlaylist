<h1>Authorization and Examples in the Terminal</h1> <br>
<p>Here is a brief description of how to authorize and use the functions to sort music by its tags</p><br>
<h2>Authorization</h2><br>

  1. In order to authorize your terminal to use these programs, you must enter the contents of credentials into the terminal.
```
export SPOTIPY_CLIENT_ID='a07dc742b8de49b0b470138f9a036e38'
export SPOTIPY_CLIENT_SECRET='880b02ebc3864d7ab6a5e028f846b137'
export SPOTIPY_REDIRECT_URI='http://google.com/'
```
  SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET are found in my dashboard for our webserver holding "Custom Concert" https://developer.spotify.com/dashboard/applications/a07dc742b8de49b0b470138f9a036e38.
  2. To search and screen music on a playlist you use:
  ```
  python3 read_a_playlist.py [uri] [above or below] [tag value: 0-1] [mode: i.e. 'danceability]
  ```
