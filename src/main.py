""" Main file that is run when the game is executed"""
from src import MCTSGreedy
from src import Calico
from src import Agents
import mcts


def main():
    test_out_mcts()


def test_out_mcts():
    agent = mcts.MCTS(0,100)
    game = Calico.Calico(1, [agent])
    game.start_game(1, [agent])
    print(game.single_player_give_game_info())

def MCTS_10_to_1000():
    """
    This function will run 100 games of mcts at different intervals, and then give the average
    of each, to see how the number of iterations affects the gameplay of the agent
    """
    intervals = [10, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

    for number in intervals:
        mcts_agent = mcts.MCTS(0, number)

        for i in range(100):  # Play the 100 games with those intervals

            game = Calico.Calico(1, [mcts_agent])


def normal_MCTS_vs_Greedy_MCTS():
    player1 = 0
    player2 = 0
    for i in range(1, 101):
        greedy_agent = MCTSGreedy.MCTSGreedy(0, 20)
        mcts_agent = mcts.MCTS(1, 20)
        game = Calico.Calico(2, [greedy_agent, mcts_agent])
        score = game.start_game(2, [greedy_agent, mcts_agent])
        if score == 1:
            player1 += 1
        else:
            player2 += 1
    print("Player 1: " + str(player1))
    print("Player 2: " + str(player2))

def greedy_vs_mcts():

    for i in range(1, 11):
        greedy_agent = Agents.GreedyAgentRandom(0)
        mcts_agent = mcts.MCTS(1, 10)
        game = Calico.Calico(2, [greedy_agent, mcts_agent])
        score = game.start_game(2, [greedy_agent, mcts_agent])
        print(score)


def greedy_vs_greedy():
    player1 = 0
    player2 = 0
    for i in range(10001):
        greedy_agent_1 = Agents.GreedyAgentRandom(0)
        greedy_agent_2 = Agents.GreedyAgentRandom(1)
        game = Calico.Calico(2, [greedy_agent_1, greedy_agent_2])
        game.select_board_colour(0, 1)
        game.select_board_colour(1, 1)
        score = game.start_game(2, [greedy_agent_1, greedy_agent_2])
        if score == 1:
            player1 += 1
        else:
            player2 += 1
    print("Player 1: " + str(player1))
    print("Player 2: " + str(player2))


def MCTS_Greedy_agent_play():
    average = 0
    highest = 0
    best_board = None
    lowest = 999999999
    for i in range(1, 2):
        print("Starting Game: " + str(i))
        agent = MCTSGreedy.MCTSGreedy(0, 1000)
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
    for i in range(1, 1001):
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


def mcts_agent_play():
    average = 0
    highest = 0
    best_board = None
    lowest = 999999999
    for i in range(1, 10):
        print("Starting Game: " + str(i))
        agent = mcts.MCTS(0, 1000)
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
        game.select_board_colour(0, 3)
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


def display_solo_info():
    """
    Function for solo games, to display the information about the games that occurred
    """
    pass


main()
