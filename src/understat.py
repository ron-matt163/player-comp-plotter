from understatapi import UnderstatClient
from helper import write_dict_to_json
understat = UnderstatClient()

def get_player_all_seasons_stats(player_id: str):
    return understat.player(player_id).get_season_data()

if __name__ == "__main__":
    player_season_stats = get_player_all_seasons_stats("7322")
    write_dict_to_json(player_season_stats, "../data/sample_season_data.json")
    

