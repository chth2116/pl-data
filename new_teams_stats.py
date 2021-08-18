import requests
import json
import pymongo
from pymongo import MongoClient
import ssl
import datetime
import pandas as pd
import os

pl_data_api = os.environ.get("pl_data_key")

def update_team_list():

    f = open("new_teams.json",'w')  # write in text mode

    url = "https://api-football-v1.p.rapidapi.com/v3/teams"

    querystring = {"id":"33", "league":"39"}

    headers = {
        'x-rapidapi-key': "e7b358e304msh801d4f6823af534p1fe851jsn91d5039ce9cc",
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com"
        }

    teams = requests.request("GET", url, headers=headers, params=querystring).text
    f.write(teams)
    f.close()

# def update_player_list():
#     team_data_list = []
#
#     with open('teams.json') as f:
#         dict_of_teams = json.load(f)
#
#     # teams = '33'
#     teams = dict_of_teams['api']['teams']
#     # create for loop through each team, grab every player from each team, create list of each players stats
#     # push team and player list of stats to db
#     for team in teams:
#
#         url = "https://api-football-v1.p.rapidapi.com/v2/players/squad/"+str(team["team_id"])+"/2021-2022"
#         headers = {
#             'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
#             'x-rapidapi-key': pl_data_api
#             }
#         team_name = team["name"]
#         print(team_name)
#
#
#         player_data = json.loads(requests.request("GET", url, headers=headers).text)['api']['players']
#         # print(player_data)
#         #
#         # client = MongoClient('mongodb+srv://topher-thompson:Topher^0316@cluster-pldata.ezii8.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', ssl_cert_reqs=ssl.CERT_NONE)
#         # db = client.teams
#         # teams_collection = db["2022-2022"]
#         #
#         # personDocument = {
#         #   "team": team_name,
#         #   "players": player_data
#         # }
#         # teams_collection.insert_one(personDocument)
#
#
#
#
#
#         #
#         # player_data_list = []
#         player_list = []
#         for player in player_data:
#             url = "https://api-football-v1.p.rapidapi.com/v2/players/player/"+str(player['player_id'])+"/2021-2022"
#             headers = {
#                 'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
#                 'x-rapidapi-key': pl_data_api
#                 }
#             player_stats_response = json.loads(requests.request("GET", url, headers=headers).text)['api']['players']
#             print(player_stats_response)
#
#
#
#
#             player_dict = {}
#             player_dict['name'] = player['player_id']
#             player_dict['stats'] = player_stats_response
#             player_list.append(player_dict)
#
#         client = MongoClient('mongodb+srv://topher-thompson:Topher^0316@cluster-pldata.ezii8.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', ssl_cert_reqs=ssl.CERT_NONE)
#         db = client.teams
#         teams_collection = db["2021-2022"]
#         personDocument = {
#           "team": team_name,
#           "player": player_list
#         }
#         teams_collection.insert_one(personDocument)
#         # #         player_data_dict1['Stats'] = player_stats_response
#         #         print(player_stats_response)
#         #     except:
#         #         print("error")
#         #         continue
#         #
#         #     player_data_dict = {}
#         #     player_data_dict['_id'] = player['player_id']
#         #     player_data_dict['Name'] = player['player_name']
#         #     player_data_dict['Firstname'] = player['firstname']
#         #     player_data_dict['Lastname'] = player['lastname']
#         #     player_data_dict['Position'] = player['position']
#         #     player_data_dict['Age'] = player_data_dict1
#         #
#         #     player_data_dict['Weight'] = player['weight']
#         #     player_data_dict['Nationality'] = player['nationality']
#         #     player_data_dict['Stats'] = player_stats_response
#         #
#         #
#         #
#         #     player_data_list.append(player_data_dict)
#         #
#         # client = MongoClient('mongodb+srv://topher-thompson:Topher^0316@cluster-pldata.ezii8.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', ssl_cert_reqs=ssl.CERT_NONE)
#         # db = client.teams
#         # teams_collection = db["2022-2022"]
#         #
#         # personDocument = {
#         #   "team": team_name,
#         #   "players": player_data_list
#         # }
#         # teams_collection.insert_one(personDocument)
#
#
#
#
# def main():
#     update_team_list()
#     update_player_list()
#
# if __name__ == '__main__':
#     main()
