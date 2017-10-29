from collections import defaultdict

class SongSet:

    def __init__(self):
        self.votes = defaultdict(set)

    def add_request(self, user_id, song_id):
        self.votes[song_id].add(user_id)

    def grab_top_k_songs(self, k):
        pairs = [(song_id, len(voters)) for song_id, voters in self.votes.items()]
        pairs = sorted(pairs, key=lambda votes: votes[1], reverse=True)
