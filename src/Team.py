class Team:
    def __init__(self, name):
        self.name          = name
        self.pts           = 0
        self.goals         = 0
        self.goals_against = 0
        self.shots         = 0
        self.diff          = 0
        self.effectiveness = 0

    def __repr__(self):
        return '{' + self.name + ': ' + str(self.pts) + ', ' + str(self.goals) + ', ' + str(self.goals_against) + ', ' + str(self.shots) + ',' + str(self.effectiveness) + '}'

    def getPts(self):
        return self.name + ': ' + str(self.pts) + ' (' + str(self.diff) + ')'

    def getGoals(self):
        return self.name + ': ' + str(self.goals)

    def getGoalsagainst(self):
        return self.name + ': ' + str(self.goals_against)

    def getDiff(self):
        return self.name + ': ' + str(self.diff)

    def getEffectiveness(self):
        return self.name + ': ' + str(round(self.effectiveness, 2)) + ' [shots-on-target: ' + str(self.shots) + ', goals: ' + str(self.goals) + ']'
