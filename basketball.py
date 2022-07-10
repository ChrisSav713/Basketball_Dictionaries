from operator import methodcaller


players = [
    {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
    },
    {
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Damian Lillard", 
    "age":33, "position": "Point Guard", 
    "team": "Portland Trailblazers"
    },
    {
    "name": "Joel Embiid", 
    "age":32, "position": "Power Foward", 
    "team": "Philidelphia 76ers"
    },
    {
    "name": "", 
    "age":16, 
    "position": "P", 
    "team": "en"
    }
]

class Player:
    def __init__(self, player):
        self.name = player['name']
        self.age = player['age']
        self.position = player['position']
        self.team = player['team']
    @classmethod
    def get_team(cls, team_list):
        new_team = []
        for player in team_list:
            new_team.append(player)
        return new_team

#challenge 2
# player1 = Player(players[1])
# player2 = Player(players[3])
# player3 = Player(players[2])

#challenge 3
# new_team = []
# for player in players:
#     new_team.append(player)

#bonus
new_team = Player.get_team(players)

for player in new_team:
    print(player)

