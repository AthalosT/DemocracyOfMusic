import pprint
import sys

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class SpotifyEntry:

    def __init__(self, song_id, name, artist):
        self.song_id = song_id
        self.name = name
        self.artist = artist

    def __repr__(self):
        return str(self)

    def __str__(self):
        return '{} by {}'.format(self.name, self.artist)

pp = pprint.PrettyPrinter(indent=2)

class SpotifyApi:

    def __init__(self):
        client_credentials_manager = SpotifyClientCredentials()
        self.spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    def get_spotify_entries(self, query, limit):
        results = self.spotify.search(query, limit=limit)['tracks']['items']
        spotify_entries = []
        for result in results:
           #result.pop('album', None)
           #result.pop('available_markets', None)
           #pp.pprint(result)
           spotify_entries.append(SpotifyEntry(result['id'], result['name'], result['artists'][0]['name']))
        return spotify_entries

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("I need the name and number of results!")
        sys.exit()

    query = sys.argv[1]
    num_results = int(sys.argv[2])
    for result in SpotifyApi().get_spotify_entries(query, num_results):
        print(result)
