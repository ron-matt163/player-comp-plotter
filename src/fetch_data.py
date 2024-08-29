import json

def fetch_players_from_keyword(keyword):
    return

def parse_keyword_search_response(response):
    parsed_response = json.loads(response)
    response = parsed_response['response']
    success = response['success']
    players = response['players']

    if success:
        for player in players:
            print(player["id"], player["player"])
    else:
        print("Fetch failed")


if __name__ == "__main__":
    RESPONSE = '{"response":{"success":true,"players":[{"id":"2097","player":"Lionel Messi","team":"Paris Saint Germain"},{"id":"8838","player":"Junior Messias","team":"Genoa"}]}}'

    parse_keyword_search_response(RESPONSE)