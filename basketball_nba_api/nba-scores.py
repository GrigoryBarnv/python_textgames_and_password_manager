from requests import get

BASE_URL = "https://cdn.nba.com/static/json/liveData"
ALL_JSON = "/scoreboard/todaysScoreboard_00.json"


def get_scoreboard_data():
    data = get(BASE_URL + ALL_JSON).json()
    return data


def get_scoreboard():
    data = get_scoreboard_data()
    games = data.get("scoreboard", {}).get("games")

    if games is None:
        games = data.get("games", [])

    if not games:
        print("No games found.")
        return

    for game in games:
        home_team = game["homeTeam"]
        away_team = game["awayTeam"]
        clock = game['gameTimeUTC']
        period = game['period']
        print("----------------------------------------")
        print(f"{away_team['teamTricode']} vs {home_team['teamTricode']}")
        print(f"{away_team['score']} - {home_team['score']}")
        print(f"{clock} - Period is {period}")
        
def get_stats():
    data = get_scoreboard_data()
    games = data.get("scoreboard", {}).get("games")

    if games is None:
        games = data.get("games", [])

    if not games:
        print("No games found.")
        return

    teams = []

    for game in games:
        home_team = game["homeTeam"]
        away_team = game["awayTeam"]

        teams.append(home_team)
        teams.append(away_team)

    teams.sort(key=lambda team: (team["teamCity"], team["teamName"]))

    for team in teams:
        print(
            f"{team['teamCity']} - {team['teamName']} - "
            f"wins: {team['wins']}, losses: {team['losses']}, score: {team['score']}"
        )


def print_detailed_table():
    data = get_scoreboard_data()
    games = data.get("scoreboard", {}).get("games")

    if games is None:
        games = data.get("games", [])

    if not games:
        print("No games found.")
        return

    for game in games:
        home_team = game["homeTeam"]
        away_team = game["awayTeam"]
        clock = game.get("gameTimeUTC", "")
        period = game.get("period", "")

        print("========================================")
        print(f"[{away_team['teamTricode']} vs {home_team['teamTricode']}]")
        print(f"{away_team['score']} - {home_team['score']}")
        print(f"{clock} - Period is {period}")
        print("----------------------------------------")
        print(
            f"{away_team['teamCity']} {away_team['teamName']} | "
            f"wins: {away_team['wins']}, losses: {away_team['losses']}, score: {away_team['score']}"
        )
        print(
            f"{home_team['teamCity']} {home_team['teamName']} | "
            f"wins: {home_team['wins']}, losses: {home_team['losses']}, score: {home_team['score']}"
        )


print_detailed_table()
