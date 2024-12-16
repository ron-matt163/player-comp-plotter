from fetch_data import fetch_players_from_keyword, parse_keyword_search_response
from understat import get_player_stat_per_season
from plot import plot_stats_per_season

if __name__ == "__main__":
    stat_type = input("Enter the stat based on which you want to compare the players (goals/assists/xG/xA): ")
    player1_id_name, player2_id_name = {}, {}

    # Obtaining player 1 stats
    search_string_1 = input("Enter the name of player 1: ")

    player1_fetch_response = fetch_players_from_keyword(search_string_1)
    if player1_fetch_response:
        player1_id_name = parse_keyword_search_response(player1_fetch_response)
    
    player1_id = input("Enter your player's ID (The player IDs corresponding to the players suggested based on your search keyword are listed above.): ")
    player1_name = player1_id_name.get(player1_id, None)
    while not player1_name:
        print("ERROR: Please enter an ID that is assigned to one of the players suggested above.")
        player1_id = input("Enter your player's ID (The player IDs corresponding to the players suggested based on your search keyword are listed above.): ")
        player1_name = player1_id_name.get(player1_id, None)       

    player1_stats_per_season = get_player_stat_per_season(player1_id, stat_type)

    # Obtaining player 2 stats
    search_string_2 = input("Enter the name of the player 2: ")

    player2_fetch_response = fetch_players_from_keyword(search_string_2)
    if player2_fetch_response:
        player2_id_name = parse_keyword_search_response(player2_fetch_response)
    
    player2_id = input("Enter your player's ID (The player IDs corresponding to the players suggested based on your search keyword are listed above.): ")
    player2_name = player2_id_name.get(player2_id, None)
    while not player2_name:
        print("ERROR: Please enter an ID that is assigned to one of the players suggested above.")
        player2_id = input("Enter your player's ID (The player IDs corresponding to the players suggested based on your search keyword are listed above.): ")
        player2_name = player2_id_name.get(player2_id, None)

    player2_stats_per_season = get_player_stat_per_season(player2_id, stat_type)    

    plot_stats_per_season(stat_type, player1_stats_per_season, player2_stats_per_season, player1_name, player2_name)