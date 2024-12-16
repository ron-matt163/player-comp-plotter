import json
import requests

def fetch_players_from_keyword(keyword: str):
    """
    Fetches data from the Understat API for the given player name.

    Args:
        player_name (str): The name of the player to query.

    Returns:
        dict: The JSON response from the API if successful.
        None: If the request fails.
    """
    base_url = "https://understat.com/main/getPlayersName/"
    url = f"{base_url}{keyword}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()  # Assumes the API returns JSON
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None    


# Parses the getPlayersName API response to obtain the matched player IDs and names
def parse_keyword_search_response(json_response) -> dict:
    response = json_response['response']
    success = response['success']
    players = response['players']

    player_id_name = {}

    print("Parsing getPlayersName response....")
    if success:

        for player in players:
            print(player["id"], player["player"])
            player_id_name[player["id"]] = player["player"]
    else:
        print("Fetch failed")

    return player_id_name
