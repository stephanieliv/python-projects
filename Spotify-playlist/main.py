from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


##SCRAPING BILLBOARD
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
bb_web_page = response.text
soup = BeautifulSoup(bb_web_page, "html.parser")
song_names = [a.getText().strip() for a in soup.select("li #title-of-a-story")]

##SPOTIFY AUTHENTICATION
sp = spotipy.Spotify(
                  auth_manager=SpotifyOAuth(
                  client_id="3c39992cc94c4f56a7daaab8f97b0ab6",
                  client_secret="49654561aad2423b91169bbc5c9cddac",
                  redirect_uri="https://www.example.com",
                  scope="playlist-modify-private",
                  show_dialog=True,
                  cache_path="token.txt")
                  )

user = sp.current_user()["id"]
print(user)

##SEARCHING SPOTIFY FOR SONG TITLES
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

##CREATING A PLAYLIST
playlist = sp.user_playlist_create(user=user,
                                   name=f"{date} Billboard 100",
                                   public=False,
                                   collaborative=False,
                                   description="top100")


##ADDING SONGS TO PLAYLIST
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
