import requests
from datetime import datetime, timedelta
import smtplib
from email.message import EmailMessage


my_email = "davidho041860@gmail.com"
password = "hqcyrpugcskwowmo"

receiever = ["davidho041860@gmail.com"]
date = str(datetime.now())[:10]
print(date)

#API endpoint
OWM_Endpoint = "https://cdn.nba.com/static/json/liveData/scoreboard/todaysScoreboard_00.json"

response = requests.get(OWM_Endpoint)

score_stats = response.json()

all_games = score_stats["scoreboard"]["games"]

has_game = False
game_finished = False
result_score = ""
#Change the team name to search different team score result
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
#If the team has game, then send the game result to your cellphone
if has_game == False:
    print(f"{team} do not has game tonight")
elif game_finished == True and has_game == True:

	print(result_score)
	m = EmailMessage()

	m['X-Priority'] = '1'
	m['Subject'] = "Game result"
	m.set_content(f"Hi \nHere is the game result,\n\n{result_score}")

	with smtplib.SMTP("smtp.gmail.com") as connection:
		connection.starttls()  ##Make secure
		connection.login(user=my_email, password=password)
		connection.sendmail(my_email,
							receiever,
							m.as_string())
