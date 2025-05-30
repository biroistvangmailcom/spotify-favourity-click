#!/data/data/com.termux/files/usr/bin/python3
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="", #your Spotify user ID#
    client_secret="", #your Spotify API Secret#
    redirect_uri="http://127.0.0.1:8088",
    scope="user-library-modify user-read-currently-playing"
))

# Get the current track
current_track = sp.currently_playing()
if current_track and current_track['is_playing']:
    track_id = current_track['item']['id']
    sp.current_user_saved_tracks_add([track_id])
    print(f"Added to favorites: {current_track['item']['name']}")
else:
    print("No track playing or not available.")