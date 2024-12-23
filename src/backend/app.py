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

@app.route('/generate-plot', methods=['POST'])
def generate_plot():
    try:
        if not request.is_json:
            return jsonify({"error": "Request must be in JSON format"}), 400
        data = request.get_json()
        print(data)
        players_ids = data.get("players", [])
        stat_type = data.get("stat_type", "")
        # request_id = data.get("request_id", "")

        players = []

        for player_id in players_ids:
            player_stats_per_season = get_player_stat_per_season(player_id["id"], stat_type)
            player = PlayerStats(player_id["id"], player_id["name"], stat_type, player_stats_per_season)
            players.append(player)

        plot_base64 = plot_stats_per_season(stat_type, players)
        return jsonify({"image_base64": plot_base64})

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)