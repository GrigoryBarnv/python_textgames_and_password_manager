from requests import get
from pprint import PrettyPrinter

printer = PrettyPrinter()

BASE_URL = "https://cdn.nba.com/static/json/liveData"
ALL_JSON = "/scoreboard/todaysScoreboard_00.json"

response = get(BASE_URL + ALL_JSON).json()

printer.pprint(response)