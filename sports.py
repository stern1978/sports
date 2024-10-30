#!/usr/bin/python3

import requests
import pickle


today_games = 'https://site.api.espn.com/apis/v2/scoreboard/header'

team_list = ['New York Rangers', 'Arsenal', 'Green Bay Packers', 'United States', 'Milwaukee Brewers', 'United States of America', 'New York Yankees']

def index():
    team_dict = {}
    try:
        sports_couner = 0
        url_get = requests.get(today_games)
        url_data = url_get.json()

        for _ in url_data['sports']:
            sport = url_data['sports'][sports_couner]['slug']
            
            events_counter = 0
            leagues_counter = 0
            for _ in url_data['sports'][sports_couner]['leagues']:
                try:
                    for x in url_data['sports'][sports_couner]['leagues'][leagues_counter]['events']:
                        try:
                            sub_sport = url_data['sports'][sports_couner]['leagues'][leagues_counter]['name']
                            #print(sub_sport)
                            time = url_data['sports'][sports_couner]['leagues'][leagues_counter]['events'][events_counter]['date'] + url_data['sports'][sports_couner]['leagues'][leagues_counter]['events'][events_counter]['id']
                            match_status = url_data['sports'][sports_couner]['leagues'][leagues_counter]['events'][events_counter]['fullStatus']['type']['detail']
                            try:
                                game_status = url_data['sports'][sports_couner]['leagues'][leagues_counter]['events'][events_counter]['fullStatus']['type']['name']
                            except:
                                game_status = 'games_status'
                            try:
                                channel = url_data['sports'][sports_couner]['leagues'][leagues_counter]['events'][events_counter]['broadcast']
                            except KeyError:
                                channel = 'unknown'
                            away_team = url_data['sports'][sports_couner]['leagues'][leagues_counter]['events'][events_counter]['competitors'][0]['displayName']
                            try:
                                away_team_logo = url_data['sports'][sports_couner]['leagues'][leagues_counter]['events'][events_counter]['competitors'][0]['logoDark']
                                home_team_logo = url_data['sports'][sports_couner]['leagues'][leagues_counter]['events'][events_counter]['competitors'][1]['logoDark']
                            except:
                                away_team_logo = url_data['sports'][sports_couner]['leagues'][leagues_counter]['events'][events_counter]['competitors'][0]['logo']
                                home_team_logo = url_data['sports'][sports_couner]['leagues'][leagues_counter]['events'][events_counter]['competitors'][1]['logo']
                            try:
                                away_score = url_data['sports'][sports_couner]['leagues'][leagues_counter]['events'][events_counter]['competitors'][0]['score']
                                home_score = url_data['sports'][sports_couner]['leagues'][leagues_counter]['events'][events_counter]['competitors'][1]['score']
                            except KeyError as e:
                                home_score = 0
                                away_score = 0
                            home_team = url_data['sports'][sports_couner]['leagues'][leagues_counter]['events'][events_counter]['competitors'][1]['displayName']
                            
                            recent = 0
                            season = url_data['sports'][sports_couner]['leagues'][leagues_counter]['events'][events_counter]['group']['name']
                            try:
                                note = url_data['sports'][sports_couner]['leagues'][leagues_counter]['events'][events_counter]['note']
                                #print(note)
                            except KeyError:
                                note = ''
                            try:
                                seriesSummary = url_data['sports'][sports_couner]['leagues'][leagues_counter]['events'][events_counter]['seriesSummary']
                            except KeyError:
                                seriesSummary = ''
                            #print(seriesSummary)
                            events_counter += 1
                            for x in url_data['sports'][sports_couner]['leagues'][leagues_counter]['events']:
                                for team in team_list:
                                    if team == home_team or team == away_team:
                                        team_dict[time] =[]
                                        team_dict[time].append([away_team, away_score, away_team_logo, home_team, home_score, home_team_logo, match_status, game_status, sub_sport, channel, recent, season, sport, note, seriesSummary])
                        except:
                            events_counter = 0  
                    leagues_counter += 1  
                except:
                    pass

            sports_couner += 1
        sort = dict(sorted(team_dict.items(), key=lambda item: item[0]))
        fname = 'pickled.pk'
        #print(sort)

        with open(fname, 'wb') as f:
            pickle.dump(sort, f)

    except IOError as e:
        print(e, 'IndexError end')
        pass


if __name__ == '__main__':
    index()