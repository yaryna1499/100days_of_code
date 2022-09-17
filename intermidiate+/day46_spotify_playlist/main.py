import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

CLIENT_ID = "f5c73356d6ba407e8bcd9f5606bee919"
CLIENT_SECRET = "bb8d0b9e7add48da86dc2781e2216e99"

date = input("What year would you like to travel? Please, type the date in this format YYYY-MM-DD:")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")

soup = BeautifulSoup(response.text, "html.parser")
songs = [title.getText().strip("\n\t") for title in soup.select(selector="h3.c-title.a-no-trucate")]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
