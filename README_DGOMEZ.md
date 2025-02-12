## ETL Process
The implemented ETL process loads English soccer data, obtaining a series of statistics. The data source is a set of data files, which have the statistics of all the matches of the seasons to be analyzed. This data is coded according to a series of variables, which include goals, cards, shots and predictions for the matches.

The ETL process corresponds to a program developed in Python, which reads each of these files and processes their data in memory, calculating each of the required results. These are: standings, the team with the best shots on goal, and the team with the most goals, by season. The results are finally written to text files, with the information for each result presented by season.

## Running the program
To run the program, Python version 3 is required and you need to run:

`python src/english_premier_league.py`

## Results
The results are written to files in the output folder. For each output-file, one per season, we have:
- **standings**: the standings for each team of the season, presenting place, team, points and goal difference.
- **efectiveness**: the team with the best ratio of shots on goal finishing in goal.
- **goals against**: the team with the most goals against.
