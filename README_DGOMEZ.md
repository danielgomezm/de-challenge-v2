## ETL Process
The implemented ETL process loads English soccer data, obtaining a series of statistics. The data source is a set of data files, which have the statistics of all the matches of the seasons to be analyzed. This data is coded according to a series of variables, which include goals, cards, shots and predictions for the matches.

The ETL process corresponds to a program developed in Python, which reads each of these files and processes their data in memory, calculating each of the required results. These are: standings, the team with the best shots on goal, and the team with the most goals, by season. The results are finally written to a text file, with the information for each result presented by season.

## Running the program
To run the program, Python version 3 is required and you need to run:
`> python english_premier_league.py`

## Results
I each output-file, we have:
- standings: the standigns for each team of the season, presenting place, team, points and goal difference.
- efectiveness: the ratio between shots on goal and goals scored.
- goals against: the team with the most goals against.
