from fetch_data import fetch_players_from_keyword, parse_keyword_search_response
from understat import get_player_stat_per_season
from plot import plot_stats_per_season
from player_stats import PlayerStats

if __name__ == "__main__":
    stat_type = input("Enter the stat based on which you want to compare the players (goals/assists/xG/xA): ")
    
    player_index = 1
    players_stats = []
    add_new_player = True

    while add_new_player:
        player_id_name = {}
        search_string = input(f"Enter the name of player {player_index}: ")
        player_fetch_response = fetch_players_from_keyword(search_string)
        if player_fetch_response:
            player_id_name = parse_keyword_search_response(player_fetch_response)

        player_id = input("Enter your player's ID (The player IDs corresponding to the players suggested based on your search keyword are listed above.): ")
        player_name = player_id_name.get(player_id, None)
        while not player_name:
            print("ERROR: Please enter an ID that is assigned to one of the players suggested above.")
            player_id = input("Enter your player's ID (The player IDs corresponding to the players suggested based on your search keyword are listed above.): ")
            player_name = player_id_name.get(player_id, None)

        player_stats_per_season = get_player_stat_per_season(player_id, stat_type)
        player_stats = PlayerStats(player_id, player_name, stat_type, player_stats_per_season)
        players_stats.append(player_stats)

        add_new_player = ("yes" == input("Do you want to add an another player to the comparison? Enter \"yes\" if you want to: ").lower())
        player_index += 1

    plot_stats_per_season(stat_type, players_stats)