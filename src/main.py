""" Main file that is run when the game is executed"""
import keras.models
from src import MCTSGreedy
from src import Calico
from src import Agents
from src import Tiles
import mcts
import os


def main():
    greedy_vs_mcts()


def greedy_vs_mcts():
    mcts_wins = 0
    greedy_wins = 0

    for i in range(1,11):
        greedy_agent = Agents.GreedyAgentRandom(0)
        mcts_agent = mcts.MCTS(1, 10)
        game = Calico.Calico(2, [greedy_agent, mcts_agent])
        score = game.start_game(2, [greedy_agent, mcts_agent])
        print(score)

def MCTS_Greedy_agent_play():
    average = 0
    highest = 0
    best_board = None
    lowest = 999999999
    for i in range(1, 2):
        print("Starting Game: " + str(i))
        agent = MCTSGreedy.MCTSGreedy(0, 10)
        game = Calico.Calico(1, [agent])
        score = game.start_game(1, [agent])[0][1]
        if score > highest:
            highest = score
            best_board = game.players_board[0]
        if score < lowest:
            lowest = score
        average = calculate_running_average(average, score, i)

    print("\n==== Final Average ====")
    print("     " + str(average))
    print("\n==== Highest Score ====")
    print("     " + str(highest))
    print("\n==== Lowest score ====")
    print("     " + str(lowest))
    # Save the position of the current board
    layout = []  # (id, colour, pattern)
    requirements = []  # (id, requirement)
    cats = []  # (name, pattern1, pattern2)

    for pus in best_board.cats:
        cats.append((pus.name, pus.pattern_1, pus.pattern_2))

    for tile in best_board.board:
        # tile is the tile object
        if tile.normal_tile:
            layout.append((tile.tile_id, tile.colour, tile.pattern))
        else:
            requirements.append((tile.id, tile.requirement))

    print("\n==== Layout====")
    print(layout)
    print("==== requirements====")
    print(requirements)
    print("==== Cats ====")
    print(cats)


def greedy_agent_play():
    average = 0
    highest = 0
    best_board = None
    lowest = 999999999
    for i in range(1, 101):
        print("Starting Game: " + str(i))
        agent = Agents.GreedyAgentRandom(0)
        game = Calico.Calico(1, [agent])
        score = game.start_game(1, [agent])[0][1]
        if score > highest:
            highest = score
            best_board = game.players_board[0]
        if score < lowest:
            lowest = score
        average = calculate_running_average(average, score, i)

    print("\n==== Final Average ====")
    print("     " + str(average))
    print("\n==== Highest Score ====")
    print("     " + str(highest))
    print("\n==== Lowest score ====")
    print("     " + str(lowest))
    # Save the position of the current board
    layout = []  # (id, colour, pattern)
    requirements = []  # (id, requirement)
    cats = []  # (name, pattern1, pattern2)

    for pus in best_board.cats:
        cats.append((pus.name, pus.pattern_1, pus.pattern_2))

    for tile in best_board.board:
        # tile is the tile object
        if tile.normal_tile:
            layout.append((tile.tile_id, tile.colour, tile.pattern))
        else:
            requirements.append((tile.id, tile.requirement))

    print("\n==== Layout====")
    print(layout)
    print("==== requirements====")
    print(requirements)
    print("==== Cats ====")
    print(cats)


def dqn_agent_play():
    path_to_model = None
    for file in os.listdir(os.getcwd()):
        if file.endswith(".keras"):
            path_to_model = file

    agent = Agents.DQNPlayer(0, path_to_model)
    agents = [agent]
    average = 0
    highest = 0
    best_board = None
    lowest = 999999999
    for i in range(1, 100):
        print("Starting Game: " + str(i))
        game = Calico.Calico(1, agents)
        score = game.start_game(1, agents)[0][1]
        if score > highest:
            highest = score
            best_board = game.players_board[0]
        if score < lowest:
            lowest = score
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
        if tile.normal_tile:
            layout.append((tile.tile_id, tile.colour, tile.pattern))
        else:
            requirements.append((tile.id, tile.requirement))
    print("\n==== Layout====")
    print(layout)
    print("==== requirements====")
    print(requirements)
    print("==== Cats ====")
    print(cats)


def mcts_agent_play():
    average = 0
    highest = 0
    best_board = None
    lowest = 999999999
    for i in range(1, 2):
        print("Starting Game: " + str(i))
        agent = mcts.MCTS(0, 2000)
        game = Calico.Calico(1, [agent])
        score = game.start_game(1, [agent])[0][1]
        if score > highest:
            highest = score
            best_board = game.players_board[0]
        if score < lowest:
            lowest = score
        average = calculate_running_average(average, score, i)

    print("\n==== Final Average ====")
    print("     " + str(average))
    print("\n==== Highest Score ====")
    print("     " + str(highest))
    print("\n==== Lowest score ====")
    print("     " + str(lowest))
    # Save the position of the current board
    layout = []  # (id, colour, pattern)
    requirements = []  # (id, requirement)
    cats = []  # (name, pattern1, pattern2)

    for pus in best_board.cats:
        cats.append((pus.name, pus.pattern_1, pus.pattern_2))

    for tile in best_board.board:
        # tile is the tile object
        if tile.normal_tile:
            layout.append((tile.tile_id, tile.colour, tile.pattern))
        else:
            requirements.append((tile.id, tile.requirement))

    print("\n==== Layout====")
    print(layout)
    print("==== requirements====")
    print(requirements)
    print("==== Cats ====")
    print(cats)


def random_agent_play():
    agent = Agents.RandomAgent(0)
    agents = [agent]
    average = 0
    highest = 0
    best_board = None
    lowest = 999999999
    for i in range(1, 50000):
        print("Starting Game: " + str(i))
        game = Calico.Calico(1, agents)
        score = game.start_game(1, agents)[0][1]
        if score > highest:
            highest = score
            best_board = game.players_board[0]
        if score < lowest:
            lowest = score
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
        if tile.normal_tile:
            layout.append((tile.tile_id, tile.colour, tile.pattern))
        else:
            requirements.append((tile.id, tile.requirement))
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
