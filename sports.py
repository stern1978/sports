#!/usr/bin/python3

import datetime
import requests
import pickle


mlb_url = 'https://site.api.espn.com/apis/site/v2/sports/baseball/mlb/scoreboard'
nhl_url = 'http://site.api.espn.com/apis/site/v2/sports/hockey/nhl/scoreboard'
epl_url = 'https://site.api.espn.com/apis/site/v2/sports/soccer/eng.1/scoreboard'
uefa_champions = 'https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.champions/scoreboard'
uefa_europa = 'https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.europa/scoreboard'
club_friendly = 'https://site.api.espn.com/apis/site/v2/sports/soccer/CLUB.FRIENDLY/scoreboard'
nfl_url = 'https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard'
world_cup = 'https://site.api.espn.com/apis/site/v2/sports/soccer/fifa.world/scoreboard'
mls = 'https://site.api.espn.com/apis/site/v2/sports/soccer/usa.1/scoreboard'
community_shield = 'https://site.api.espn.com/apis/site/v2/sports/soccer/eng.charity/scoreboard'

url_list = [nhl_url, nfl_url, mlb_url, uefa_champions, uefa_europa, club_friendly, epl_url, world_cup, mls, community_shield]
team_list = ['New York Rangers', 'Arsenal', 'Milwaukee Brewers', 'New York Yankees', 'Green Bay Packers', 'United States']

def index():
   sport_dict = {}
   team_dict = {}
   try:
      for url in url_list:
         counter = 0
         url_get = requests.get(url)
         url_data = url_get.json()
         now_espn = datetime.datetime.now().strftime('%Y-%m-%dT%H:%MZ')
         tomorrow = datetime.datetime.now() + datetime.timedelta(hours= -48)
         tomorrow_espn = tomorrow.strftime('%Y-%m-%dT%H:%MZ')
         if url_data['leagues'][0]['season']['type']['id'] != '4': #removes offseason games
            if url_data['events'][counter]['competitions'][0]['startDate'] > tomorrow_espn:
               sport_name = url_data['leagues'][0]['name']
               sport_dict[sport_name] = []
               for events in url_data:
                  try:
                     for _ in events:
                        try:               
                           teams_playing = url_data['events'][counter]['name']
                           for team in team_list:
                              if team in teams_playing:
                                 recent = url_data['events'][counter]['competitions'][0]['recent']
                                 home_team =  url_data['events'][counter]['competitions'][0]['competitors'][0]['team']['name']
                                 away_team =  url_data['events'][counter]['competitions'][0]['competitors'][1]['team']['name']
                                 match_status = url_data['events'][counter]['competitions'][0]['status']['type']['shortDetail']
                                 home_score = url_data['events'][counter]['competitions'][0]['competitors'][0]['score']
                                 away_score = url_data['events'][counter]['competitions'][0]['competitors'][1]['score']
                                 home_logo = url_data['events'][counter]['competitions'][0]['competitors'][0]['team']['logo']
                                 away_logo = url_data['events'][counter]['competitions'][0]['competitors'][1]['team']['logo']
                                 game_status = url_data['events'][counter]['competitions'][0]['status']['type']['name']
                                 time = url_data['events'][counter]['date']
                                 try:
                                    channel = '- On ' + url_data['events'][counter]['competitions'][0]['broadcasts'][0]['names'][0]
                                 except:
                                    channel = ''
                                 slug = url_data['events'][counter]['season']['slug'].replace('-', ' ')
                                 team_dict[time] =[]
                                 team_dict[time].append([away_team, away_score, away_logo, home_team, home_score, home_logo, match_status, game_status, sport_name, channel, recent, slug.title()])
                                    
                                 sport_dict[sport_name].append([away_team, away_score, away_logo, home_team, home_score, home_logo, match_status, game_status, time, channel, recent, slug])
                           counter+=1
                        except KeyError as e:
                           print(e)
                  except IndexError:
                     pass   
               if not sport_dict[sport_name]:
                  del sport_dict[sport_name]
      sort = dict(sorted(team_dict.items(), key=lambda item: item[0]))
      fname = 'pickled.pk'

      with open(fname, 'wb') as f:
         pickle.dump(sort, f)
   
   except KeyError as e:
      print(e)

if __name__ == '__main__':
   index()
