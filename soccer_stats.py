import requests
import json
import pymongo
from pymongo import MongoClient
import ssl
import datetime
import pandas as pd
import os

# fixtures_stats = {}
pl_data_api = os.environ.get("pl_data_key")

def update_fixture_tracker():

    f = open("fixtures.json",'w')  # write in text mode
    url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"

    querystring = {"league":"39","season":"2021"}

    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': pl_data_api
        }


    fixture_data = requests.request("GET", url, headers=headers, params=querystring).text
    f.write(fixture_data)
    f.close()


def create_fixture_data_struct():

    fixture_data_list = []

    with open('fixtures.json') as f:
        dict_of_countries = json.load(f)

    fixtures = dict_of_countries['response']
    fixture_stats = []

    for fixture in fixtures:
        home_score=fixture['goals']['home']
        if str(home_score).lower() =="none":
            continue
        away_score=fixture['goals']['away']
        if str(away_score).lower() == "none":
            continue

        fixture_data_dict = {}
        fixture_data_dict['home team'] = fixture['teams']['home']['name']
        fixture_data_dict['away team'] = fixture['teams']['away']['name']
        fixture_data_dict['home goals'] = home_score
        fixture_data_dict['away goals'] = away_score
        fixture_data_dict['timestamp'] = fixture['fixture']['date']
        fixture_data_list.append(fixture_data_dict)

        url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"

        querystring = {"id":str(fixture['fixture']['id'])}

        headers = {
            'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
            'x-rapidapi-key': pl_data_api
            }


        fixture_stat = json.loads(requests.request("GET", url, headers=headers, params=querystring).text)
        fixture_stats.append(fixture_stat)

    print(fixture_stats)

    return fixture_data_list, fixture_stats

def fixture_data_to_csv(fixture_data_list):

    out_file = open("fixtures_stats.csv",'w')
    out_file.write('home team,away team,home score,away score,date\n')

    for fixture_data_dict in fixture_data_list:
        out_file.write(fixture_data_dict['home team']+","+fixture_data_dict['away team']+","+str(fixture_data_dict['home goals'])+","+str(fixture_data_dict['away goals'])+","+fixture_data_dict['timestamp']+"\n")

    out_file.close()

    read_file = pd.read_csv (r'fixtures_stats.csv')
    read_file.to_excel (r'fixtures_stats.xlsx', index = None, header=True)
    # print(fixture_data_list)


def fixture_data_to_mongodb(fixture_data_list, fixture_stats):

    client = MongoClient('mongodb+srv://topher-thompson:Topher^0316@cluster-pldata.ezii8.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', ssl_cert_reqs=ssl.CERT_NONE)
    db = client.fixtureData
    fixtures_collection = db["2021-2022"]
    fixtures_collection.drop()
    fixtures_collection = db["2021-2022"]
    i = 0
    for fixture in fixture_data_list:

        fixture_document = {
            "Home Team": fixture['home team'],
            "Away Team": fixture['away team'],
            "Home Score": fixture['home goals'],
            "Away Score": fixture['away goals'],
            "Timestamp": fixture['timestamp'],
            "fixture stats": fixture_stats[i]['response']['fixture']
        }
        i = i + 1
        # for fixture in fixture_data_list:
        #
        fixtures_collection.insert_one(fixture_document)

def main():
    #Change this variable to 'false' if there have been no new fixture results
    call_api = 'true'
    if call_api.lower() == 'true':
        update_fixture_tracker()

    fixture_data_list, fixture_stats = create_fixture_data_struct()
    # fixture_data_to_csv(fixture_data_list)
    fixture_data_to_mongodb(fixture_data_list, fixture_stats)

if __name__ == '__main__':
    main()
