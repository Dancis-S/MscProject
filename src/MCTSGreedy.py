import random
import math
import Calico
import copy
from src import Agents


class API:
    @classmethod
    def get_legal_moves(cls, state):
        """
        Returns the legal moves for the given state
        :return:
        """
        board = state.players_board[0]
        open_positions = board.open_positions
        legal_moves = []
        for location in open_positions:
            for i in range(0, 3):
                for k in range(0, 3):
                    legal_moves.append((location, i, k))

        return legal_moves

    @classmethod
    def make_move(cls, state, move):
        new_state = state
        # Move is going to come in form (location, stack indx, shop indx)
        location = move[0]
        stack_indx = move[1]
        colour = new_state.players_stack[0][stack_indx][0]  # Gets the colour
        pattern = new_state.players_stack[0][stack_indx][1]  # Gets the pattern
        shop_indx = move[2]

        # Add the tile
        new_state.players_board[0].add_tile(location, colour, pattern)

        # Take selected tile from shop add to stack, and randomly add new tile to shop
        new_state.players_stack[0].append(new_state.shop.pop(shop_indx))  # Pop the shop indx
        new_state.shop.append(state.tiles_bag.pop())

        return new_state

    @classmethod
    def is_game_over(cls, state):
        """
        Checks whether the game is over by looking at the open pos
        :param state:
        :return:
        """
        if not state.players_board[0].open_positions:
            return True
        else:
            return False

    @staticmethod
    def clone_state(root_state):
        """
        Given the root state return a copy of the state for further simulation
        :param root_state:
        :return:
        """
        clone = copy.deepcopy(root_state)
        return clone

    @classmethod
    def get_score(cls, state):
        return state.players_board[0].get_score()


class Node:
    def __init__(self, parent=None, move=None, state=None):
        self.parent = parent
        self.move = move
        self.state = state
        self.untried_moves = API.get_legal_moves(state)
        self.children = []
        self.wins = 0
        self.visits = 0


class MCTSGreedy:
    def __init__(self, agents_id, itermax):
        self.itermax = itermax
        self.id = agents_id

    def get_action(self, given_node):
        root_node = Node(state=API.clone_state(given_node))

        for _ in range(self.itermax):
            node = root_node
            state = API.clone_state(given_node)

            # Selection
            while node.untried_moves == [] and node.children != []:
                node = self.select_child(node)
                state = API.make_move(state, node.move)

            # Expansion
            if node.untried_moves:
                move = random.choice(node.untried_moves)
                state = API.make_move(state, move)
                node = node.add_child(move, state)

            # Simulation
            while not API.is_game_over(state):
                agent = Agents.GreedyAgentRandom(self.id)
                move = agent.get_action(state)
                state = API.make_move(state, move)

            # Backpropagation
            while node is not None:
                node.visits += 1
                node.wins += API.get_score(state)
                node = node.parent

        return sorted(root_node.children, key=lambda c: c.visits)[-1].move

    def select_child(self, node):
        s = sorted(node.children, key=lambda c: c.wins / c.visits + math.sqrt(2 * math.log(node.visits) / c.visits))[-1]
        return s


def add_child(self, move, state):
    node = Node(parent=self, move=move, state=state)
    self.untried_moves.remove(move)
    self.children.append(node)
    return node


Node.add_child = add_child
