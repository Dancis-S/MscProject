import random
import math
import copy


class Node:
    def __init__(self, player_id, parent=None, move=None, state=None):
        self.parent = parent
        self.move = move
        self.state = state
        self.untried_moves = MCTS.get_legal_moves(player_id, state)
        self.children = []
        self.wins = 0
        self.visits = 0

    def add_child(self, move, state, player_id):
        node = Node(player_id, parent=self, move=move, state=state)
        self.untried_moves.remove(move)
        self.children.append(node)
        return node

class MCTS:
    def __init__(self, agents_id, itermax):
        self.itermax = itermax
        self.player_id = agents_id
        self.player_name = "MCTS Agent"

    def get_action(self, given_node):
        root_node = Node(self.player_id, state=self.clone_state(given_node))

        for _ in range(self.itermax):
            node = root_node
            state = self.clone_state(given_node)

            # Selection
            while node.untried_moves == [] and node.children != []:
                node = self.select_child(node)
                state = self.make_move(state, node.move)

            # Expansion
            if node.untried_moves:
                move = random.choice(node.untried_moves)
                state = self.make_move(state, move)
                node = node.add_child(move, state, self.player_id)

            # Simulation
            while not self.is_game_over(state):
                state = self.make_move(state, random.choice(self.get_legal_moves(self.player_id, state)))

            # Backpropagation
            while node is not None:
                node.visits += 1
                node.wins += self.get_score(state)
                node = node.parent

        return sorted(root_node.children, key=lambda c: c.visits)[-1].move

    @classmethod
    def select_child(cls, node):
        s = sorted(node.children, key=lambda c: c.wins / c.visits + math.sqrt(2 * math.log(node.visits) / c.visits))[-1]
        return s

    @classmethod
    def get_legal_moves(cls, player_id, state):
        """
        Returns the legal moves for the given state
        :return:
        """
        board = state.get_my_board(player_id)
        open_positions = board.open_positions
        legal_moves = []
        for location in open_positions:
            for i in range(0, 3):
                for k in range(0, 3):
                    legal_moves.append((location, i, k))

        return legal_moves

    def make_move(self, state, move):
        new_state = state
        # Move is going to come in form (location, stack indx, shop indx)
        location = move[0]
        stack_indx = move[1]
        my_stack = new_state.get_my_stack(self.player_id)
        colour = my_stack[stack_indx][0]  # Gets the colour
        pattern = my_stack[stack_indx][1]  # Gets the pattern
        shop_indx = move[2]

        # Add the tile
        my_board = new_state.get_my_board(self.player_id)
        my_board.add_tile(location, colour, pattern)

        # Take selected tile from shop add to stack, and randomly add new tile to shop
        my_stack.append(new_state.shop.pop(shop_indx))  # Pop the shop indx
        new_state.shop.append(state.tiles_bag.pop())

        return new_state

    def is_game_over(self, state):
        """
        Checks whether the game is over by looking at the open pos
        :param state:
        :return:
        """
        if not state.get_my_board(self.player_id).open_positions:
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

    def get_score(self, state):
        return state.get_my_board(self.player_id).get_score()



