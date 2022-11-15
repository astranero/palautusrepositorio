from player import Player
import requests
from datetime import datetime

class PlayerReader:
    def __init__(self, url):
        self.url = url

    def read(self):
        return requests.get(self.url).json()

    def get_players(self):
        players = []
        response = self.read()
        for player_dict in response:
            player = Player(
                player_dict['name'],
                player_dict["nationality"],
                player_dict["assists"],
                player_dict["goals"],
                player_dict["penalties"],
                player_dict["team"],
                player_dict["games"]
            )
            players.append(player)
        return players

class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()
    
    def top_scorers_by_nationality(self, nation):
        national_players = []
        for player in self.players:
            if player.nationality == nation:
                national_players.append(player)
        national_players.sort(key=Player.score, reverse=True)
        return national_players

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")
   
    print(f"Players from FIN {datetime.now()}")
    print()
    for player in players:
        print(player)
    
if __name__ == "__main__":
    main()
