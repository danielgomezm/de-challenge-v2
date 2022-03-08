import json
import operator
import os
from Team import Team

files = os.listdir('data')
results = {}

# seasons:
for filename in files:
    teams = {}
    season = filename[0:11]
    with open('data/' + filename) as file:
        data = json.load(file)

        for game in data:
            this_game = {}
            home_team = game['HomeTeam']
            away_team = game['AwayTeam']

            # home
            if home_team not in teams.keys():
                teams[home_team] = Team(home_team)
            teams[home_team].goals         += game['FTHG']
            teams[home_team].goals_against += game['FTAG']
            teams[home_team].shots         += game['HST']
            teams[home_team].diff          += game['FTHG'] - game['FTAG']

            # away
            if away_team not in teams.keys():
                teams[away_team] = Team(away_team)
            teams[away_team].goals         += game['FTAG']
            teams[away_team].goals_against += game['FTHG']
            teams[away_team].shots         += game['AST']
            teams[away_team].diff          += game['FTAG'] - game['FTHG']

            # game results
            if game['FTHG'] > game['FTAG']:
                home_pts = 3
                away_pts = 0
            elif game['FTHG'] < game['FTAG']:
                home_pts = 0
                away_pts = 3
            else:
                home_pts = 1
                away_pts = 1

            teams[home_team].pts += home_pts
            teams[away_team].pts += away_pts

    # efectiveness
    for team in teams.keys():
        teams[team].effectiveness = teams[team].goals / teams[team].shots

    # season results
    if not os.path.exists('output'):
        os.mkdir('output')
    results[season] = {}
    results[season]['standings'] = []

    teams_pts = sorted(teams, key = lambda name: (teams[name].pts, teams[name].diff), reverse=True)
    pos = 1
    for team in enumerate(teams_pts):
        results[season]['standings'].append(str(pos) + ': ' + teams[team[1]].getPts())
        pos += 1

    teams_effectiveness = sorted(teams, key = lambda name: (teams[name].effectiveness), reverse=True)
    id = 0
    for team in enumerate(teams_effectiveness):
        results[season]['efectiveness'] = teams[team[1]].getEffectiveness()
        if id == 0: break

    teams_goals_against = sorted(teams, key = lambda name: (teams[name].goals_against), reverse=True)
    id = 0
    for team in enumerate(teams_goals_against):
        results[season]['goals_against'] = teams[team[1]].getGoalsagainst()
        if id == 0: break

# writing to output file
for this_season in results.keys():
    output = open('output/' + this_season + '.txt', 'w')
    print(this_season.upper())
    output.write(this_season.upper() + ':\n')

    output.write('\nstandings:\n')
    for pos in results[this_season]['standings']:
        # print('\t' + pos)
        output.write('\t' + pos + '\n')

    output.write('\nefectiveness:\n')
    output.write('\t' + results[this_season]['efectiveness'] + '\n')
    output.write('\ngoals against:\n')
    output.write('\t' + results[this_season]['goals_against'] + '\n')

