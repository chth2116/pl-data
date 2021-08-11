import requests
import json

# f = open("countries.json",'w')  # write in text mode
# url = "https://api-football-v1.p.rapidapi.com/v2/countries"
# headers = {
#     'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
#     'x-rapidapi-key': "322779bdffmshe98543268d8f262p11eab0jsnfd6df521d919"
#     }
#
# countries_data = requests.request("GET", url, headers=headers).text
# f.write(countries_data)
# f.close()

# f2 = open("pl.json",'w')  # write in text mode
# url = "https://api-football-v1.p.rapidapi.com/v2/leagues/country/england/2020"
# headers = {
#     'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
#     'x-rapidapi-key': "322779bdffmshe98543268d8f262p11eab0jsnfd6df521d919"
#     }
#
# pl_data = requests.request("GET", url, headers=headers).text
# f2.write(pl_data)

# 2790

# url = "https://api-football-v1.p.rapidapi.com/v2/teams/league/2790"

f3 = open("fixtures_stats.json",'w')  # write in text mode
url = "https://api-football-v1.p.rapidapi.com/v2/statistics/fixture/592157/"
headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "322779bdffmshe98543268d8f262p11eab0jsnfd6df521d919"
    }

fixture_data = requests.request("GET", url, headers=headers).text
f3.write(fixture_data)
f3.close()

# f3 = open("fixtures.json",'w')  # write in text mode
# url = "https://api-football-v1.p.rapidapi.com/v2/fixtures/league/2790"
# headers = {
#     'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
#     'x-rapidapi-key': "322779bdffmshe98543268d8f262p11eab0jsnfd6df521d919"
#     }
#
# fixture_data = requests.request("GET", url, headers=headers).text
# f3.write(fixture_data)
# f3.close()
