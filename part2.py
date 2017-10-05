import argparse
import csv


class Player(object):
    def __init__(self, name, team, position, height, weight, age):
        self.name = name
        self.team = team
        self.position = position
        self.height = float(height)
        self.weight = float(weight)
        self.age = float(age)

    def get_last_name(self):
        return self.name.split(' ')[-1]


class Team(object):
    def __init__(self, name=None):
        self.name = name
        self.players = []

    def set_name(self, name):
        self.name = name

    def add_player(self, player):
        self.players.append(player)

    def get_players(self, position=None):
        """
        Get players on the team

        :param position: Player position
        :rtype: list
        """
        if not position:
            return self.players
        return [player for player in self.players if player.position == position]

    def get_pos_avg_height(self, position):
        """
        Get the average height of of all team players who play the given position
        :param position: Player position
        :rtype: float
        """
        players = self.get_players(position)
        avg = sum([player.height for player in players]) / len(players)
        return avg

    def get_max_age(self):
        """
        Get the max age of of all team players
        :rtype: float
        """
        age = max([player.age for player in self.players])
        return age

    def get_players_start_with(self, letter):
        """
        Get the number of team players whose last name begins with the given letter
        :param letter: Letter to check
        :rtype: int
        """
        last_names = [player for player in self.players if player.get_last_name()[0].startswith(letter)]
        return len(last_names)


def read_file(file_name):
    """
    Rea a csv file and return a list of the contents
    :param file_name: path to csv file
    :return: team object
    """
    team = Team()
    with open(file_name, 'rb') as data:
        header = data.next()  # pull out the header row
        reader = csv.reader(data, delimiter=',')
        for row in reader:
            player_name, team_name, player_pos, player_height, player_weight, player_age = \
                [attr.strip() for attr in row]  # pull out the player attrs

            # set the team name to the first player's team
            if not team.name:
                team.set_name(team_name)

            # create new player and add them to the team
            player = Player(player_name, team_name, player_pos, player_height, player_weight, player_age)
            team.add_player(player)
    return team


def challenge(file_name):
    """
    Challenge function to analyze a csv file
    :param file_name: path to csv file
    :return: Avg Height, Max Age, Number of players with last names starting with 'B'
    """
    team = read_file(file_name)
    avg_height = team.get_pos_avg_height('Outfielder')
    max_age = team.get_max_age()
    players_b = team.get_players_start_with('B')
    return avg_height, max_age, players_b


if __name__ == '__main__':
    file_name = 'data.csv'
    # setup arguments for running through the terminal. an error will be raised if there are not enough arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name", help="Path to csv data file", type=str)
    args = parser.parse_args()
    result = challenge(args.file_name)
    print result
