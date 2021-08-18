import requests
import json
import pymongo
from pymongo import MongoClient
import ssl
import datetime
import pandas as pd
import os

pl_data_api = os.environ.get("pl_data_key")

def update_fixture_tracker():

    f = open("fixtures.json",'w')  # write in text mode
    url = "https://api-football-v1.p.rapidapi.com/v2/fixtures/league/2790"
    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': pl_data_api
        }

    fixture_data = requests.request("GET", url, headers=headers).text
    f.write(fixture_data)
    f.close()

def create_fixture_data_struct():

    fixture_data_list = []

    with open('fixtures.json') as f:
        dict_of_countries = json.load(f)

    fixtures = dict_of_countries['api']['fixtures']

    for fixture in fixtures:
        home_score=fixture['goalsHomeTeam']
        if str(home_score).lower() =="none":
            continue
        away_score=fixture['goalsAwayTeam']
        if str(away_score).lower() == "none":
            continue

        fixture_data_dict = {}
        fixture_data_dict['home team'] = fixture['homeTeam']['team_name']
        fixture_data_dict['away team'] = fixture['awayTeam']['team_name']
        fixture_data_dict['home goals'] = home_score
        fixture_data_dict['away goals'] = away_score
        fixture_data_dict['timestamp'] = fixture['event_date']
        fixture_data_list.append(fixture_data_dict)

    return fixture_data_list

def fixture_data_to_csv(fixture_data_list):

    out_file = open("fixtures_stats.csv",'w')
    out_file.write('home team,away team,home score,away score,date\n')

    for fixture_data_dict in fixture_data_list:
        out_file.write(fixture_data_dict['home team']+","+fixture_data_dict['away team']+","+str(fixture_data_dict['home goals'])+","+str(fixture_data_dict['away goals'])+","+fixture_data_dict['timestamp']+"\n")

    out_file.close()

    read_file = pd.read_csv (r'fixtures_stats.csv')
    read_file.to_excel (r'fixtures_stats.xlsx', index = None, header=True)
    print(fixture_data_list)


def fixture_data_to_mongodb(fixture_data_list):

    client = MongoClient('mongodb+srv://topher-thompson:Topher^0316@cluster-pldata.ezii8.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', ssl_cert_reqs=ssl.CERT_NONE)
    db = client.fixtureData
    fixtures_collection = db["2021-2022"]
    fixtures_collection.drop()
    fixtures_collection = db["2021-2022"]

    for fixture in fixture_data_list:

        fixtures_collection.insert_one(fixture)

def main():
    #Change this variable to 'false' if there have been no new fixture results
    call_api = 'true'
    if call_api.lower() == 'true':
        update_fixture_tracker()

    fixture_data_list = create_fixture_data_struct()
    fixture_data_to_csv(fixture_data_list)
    fixture_data_to_mongodb(fixture_data_list)

if __name__ == '__main__':
    main()