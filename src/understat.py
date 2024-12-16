from understatapi import UnderstatClient
from constants import PERMITTED_STAT_TYPES

understat = UnderstatClient()

def get_player_all_seasons_stats(player_id: str) -> list:
    player_seasons_stats = understat.player(player_id).get_season_data().get("season", None)
    if not player_seasons_stats:
        return []
    else:
        return player_seasons_stats

# Returns the stat provided as argument to the function for each season
def get_player_stat_per_season(player_id: str, stat_type: str):
    if stat_type not in PERMITTED_STAT_TYPES:
        print("ERROR: Required stat type not found in the understat API library response")
        return None
    
    player_seasons_stats = get_player_all_seasons_stats(player_id)

    player_stats_per_season = {}
    for season_stats in player_seasons_stats:
        player_stats_per_season[season_stats["season"]] = season_stats.get(stat_type, 0)
    
    return player_stats_per_season


