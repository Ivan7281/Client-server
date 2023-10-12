def create_array(array):
    for i in range(32):
        array.append(i ** 2)
    for i in range(11):
        array.append(i ** 3)


def create_teams(players, teams):
    for i in range(len(players)):
        for j in range(i + 1, len(players)):
            team = (players[i], players[j])
            teams.append(team)


array_a = []
create_array(array_a)
array_a = list(set(array_a))
array_a.sort()
print(array_a, "\n")

players_a = ["Emily", "Alexander", "Sophia", "Benjamin", "Olivia", "William", "Ava", "James"]
teams_a = []
create_teams(players_a, teams_a)
print(teams_a)
