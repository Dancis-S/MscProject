""" Main file that is run when the game is executed"""
from src import Calico
from src import Agents
from src import Tiles
import csv


def main():
    agent = Agents.RandomAgent()
    agents = [agent]
    average = 0
    highest = 0
    best_board = None
    lowest = 999999999
    for i in range(1, 200001):
        print("Starting Game: " + str(i))
        game = Calico.Calico(1, agents)
        # board = game.players_board[0].board_colour
        # player = game.players_board[0].player_num
        # print(player)
        # print(board)
        score = game.start_game(1, agents)[0][1]
        if score > highest:
            highest = score
        if score < lowest:
            lowest = score
            best_board = game.players_board[0]
        average = calculate_running_average(average, score, i)

    print("\n==== Final Average ====")
    print("     " + str(average))
    print("\n==== Highest Score ====")
    print("     " + str(highest))
    print("\n==== Lowest score ====")
    print("     " + str(lowest))

    print("==== Best Board ====")
    # Save the position of the current board
    layout = []  # (id, colour, pattern)
    requirements = []  # (id, requirement)
    cats = []  # (name, pattern1, pattern2)
    for pus in best_board.cats:
        cats.append((pus.name, pus.pattern_1, pus.pattern_2))
    for tile in best_board.board:
        # tile is the tile object
        if isinstance(tile, Tiles.DesignGoalTile):
            requirements.append((tile.id, tile.requirement))
        else:
            layout.append((tile.tile_id, tile.colour, tile.pattern))
    print("\n==== Layout====")
    print(layout)
    print("==== requirements====")
    print(requirements)
    print("==== Cats ====")
    print(cats)


def human_play():
    while True:
        num_of_players = int(input("Enter the number of players: "))
        if num_of_players > 4 or num_of_players < 1:
            print("Invalid Number pick ")
        else:
            break

    print("Beginning game for " + str(num_of_players) + " players!")
    game = Calico.Calico(num_of_players, [])
    game.start_game(num_of_players, [])  # Calls the method to start the game


def calculate_running_average(previous_avg, new_num, n):
    return ((previous_avg * (n - 1)) + new_num) / n


main()
