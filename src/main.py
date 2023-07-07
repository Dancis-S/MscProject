""" Main file that is run when the game is executed"""
from src import Calico
from src import Agents


def main():
    agent = Agents.RandomAgent()
    agents = [agent]
    game = Calico.Calico(1, agents)
    game.start_game(1, agents)
    """
     while True:
        num_of_players = int(input("Enter the number of players: "))
        if num_of_players > 4 or num_of_players < 1:
            print("Invalid Number pick ")
        else:
            break

    print("Beginning game for " + str(num_of_players) + " players!")
    game = Calico.Calico(num_of_players)
    game.start_game(num_of_players)  # Calls the method to start the game
    """


main()
