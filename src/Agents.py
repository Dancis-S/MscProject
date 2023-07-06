""" File that contains the different AI agents"""

class RandomAgent:
    def getAction(self, GameState):
        openPositions = GameState.getOpenPositions
