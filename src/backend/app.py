from fetch_data import fetch_players_from_keyword, parse_keyword_search_response
from understat import get_player_stat_per_season
from plot import plot_stats_per_season
from player_stats import PlayerStats
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/search-players', methods=['GET'])
def search_players():
    keyword = request.args.get('keyword', '')
    if not keyword:
        return jsonify({"error": "No keyword provided"}), 400

    # Fetch and parse player data
    api_response = fetch_players_from_keyword(keyword)
    if api_response is None:
        return jsonify({"error": "Failed to fetch data from Understat"}), 500

    player_data = parse_keyword_search_response(api_response)
    return jsonify(player_data)


if __name__ == "__main__":
    app.run(debug=True)
    
    # stat_type = input("Enter the stat based on which you want to compare the players (goals/assists/xG/xA): ")
    
    # player_index = 1
    # players_stats = []
    # add_new_player = True

    # while add_new_player:
    #     player_id_name = {}
    #     search_string = input(f"Enter the name of player {player_index}: ")
    #     player_fetch_response = fetch_players_from_keyword(search_string)
    #     if player_fetch_response:
    #         player_id_name = parse_keyword_search_response(player_fetch_response)

    #     player_id = input("Enter your player's ID (The player IDs corresponding to the players suggested based on your search keyword are listed above.): ")
    #     player_name = player_id_name.get(player_id, None)
    #     while not player_name:
    #         print("ERROR: Please enter an ID that is assigned to one of the players suggested above.")
    #         player_id = input("Enter your player's ID (The player IDs corresponding to the players suggested based on your search keyword are listed above.): ")
    #         player_name = player_id_name.get(player_id, None)

    #     player_stats_per_season = get_player_stat_per_season(player_id, stat_type)
    #     player_stats = PlayerStats(player_id, player_name, stat_type, player_stats_per_season)
    #     players_stats.append(player_stats)

    #     add_new_player = ("yes" == input("Do you want to add an another player to the comparison? Enter \"yes\" if you want to: ").lower())
    #     player_index += 1

    # plot_stats_per_season(stat_type, players_stats)