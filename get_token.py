import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="",
    client_secret="",
    redirect_uri="http://localhost:8088",
    scope="user-library-modify user-read-currently-playing"
))

# This will open a browser window to log in
token = sp.auth_manager.get_access_token()
print("Token:", token)