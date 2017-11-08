from songset import Songset

class Session:

    def __init__(self):
        self.users = {}
        self.user_id = 0
        self.songset = Songset()

    def _next_user(self):
        self.user_id += 1

    def add_user(self):
        new_user = User(self.user_id)
        self.users[self.user_id] = new_user
        self._next_user_id()
        return new_user

    def add_vote(self, user_id, song_id):
        self.songset.add_request(user_id, song_id)

    def remove_vote(self, user_id, song_id):
        self.songset.remove_request(user_id, song_id)

    def restart(self):
        self.__init__()
