import requests
from twilio.rest import Client
import datetime

date = str(datetime.datetime.now())[:10]
print(date)

OWM_Endpoint = "https://cdn.nba.com/static/json/liveData/scoreboard/todaysScoreboard_00.json"

response = requests.get(OWM_Endpoint)

score_stats = response.json()


account_sid = "AC1651b84f6775ce95d2297c4831951df5"
auth_token = "0a2922826d56d582d7204895185384b2"


all_games = score_stats["scoreboard"]["games"]

has_game = False
game_finished = False
result_score = ""
team = "LAL"
for game in all_games:
    if game["homeTeam"]["teamTricode"] == team or game["awayTeam"]["teamTricode"] == team:
        has_game = True
        if game["gameStatusText"] == "Final":
            game_finished = True
        if game["homeTeam"]["teamTricode"] == team:
            result_score += str(f"{team}(H) : {game['awayTeam']['teamTricode']}(A)\n")
            print(f"{team}(H) : {game['awayTeam']['teamTricode']}(A)")
            if int(game["homeTeam"]["score"]) > int(game["awayTeam"]["score"]):
                result_score += str(f"({game['homeTeam']['teamTricode']}){int(game['homeTeam']['score'])} : {int(game['awayTeam']['score'])}({game['awayTeam']['teamTricode']})")
                print(f"({game['homeTeam']['teamTricode']}){int(game['homeTeam']['score'])} : {int(game['awayTeam']['score'])}({game['awayTeam']['teamTricode']})")
            elif int(game["homeTeam"]["score"]) < int(game["awayTeam"]["score"]):
                result_score += str(f"({game['homeTeam']['teamTricode']}){int(game['homeTeam']['score'])} : {int(game['awayTeam']['score'])}({game['awayTeam']['teamTricode']})")
                print(f"({game['homeTeam']['teamTricode']}){int(game['homeTeam']['score'])} : {int(game['awayTeam']['score'])}({game['awayTeam']['teamTricode']})")
            else:
                print(f"Score:{int(game['homeTeam']['score'])} : {int(game['awayTeam']['score'])}")
        if game["awayTeam"]["teamTricode"] == team:
            print(f"{team}(A) : {game['homeTeam']['teamTricode']}(H)")
            result_score += str(f"{team}(A) : {game['homeTeam']['teamTricode']}(H)\n")
            if int(game["awayTeam"]["score"]) > int(game["homeTeam"]["score"]):
                result_score += str(f"({game['awayTeam']['teamTricode']}){int(game['awayTeam']['score'])} : {int(game['homeTeam']['score'])}({game['homeTeam']['teamTricode']})")
                print(f"({game['awayTeam']['teamTricode']}){int(game['awayTeam']['score'])} : {int(game['homeTeam']['score'])}({game['homeTeam']['teamTricode']})")
            elif int(game["awayTeam"]["score"]) < int(game["homeTeam"]["score"]):
                result_score += str(f"({game['awayTeam']['teamTricode']}){int(game['awayTeam']['score'])} : {int(game['homeTeam']['score'])}({game['homeTeam']['teamTricode']})")
                print(f"({game['awayTeam']['teamTricode']}){int(game['awayTeam']['score'])} : {int(game['homeTeam']['score'])}({game['homeTeam']['teamTricode']})")
            else:
                print(f"({game['awayTeam']['teamTricode']}){int(game['awayTeam']['score'])} : {int(game['homeTeam']['score'])}({game['homeTeam']['teamTricode']})")
        break
if has_game == False:
    print(f"{team} do not has game tonight")
elif game_finished == True and has_game == True:
    print(result_score)
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=result_score,
        from_="+16467607418",
        to="+886912167543"
    )
    print(message.sid)
