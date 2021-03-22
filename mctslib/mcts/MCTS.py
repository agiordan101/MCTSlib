from abc import ABCMeta, abstractmethod
from mctslib.game_engine.GameEngine import GameEngine

class MCTS(GameEngine, metaclass=ABCMeta):

	def __init__(self):
		pass

	@abstractmethod
	def selection(self, moves):
		pass

	@abstractmethod
	def expansion(self, moves):
		pass

	@abstractmethod
	def heuristic(self, *args, **kwargs):
		pass

	@abstractmethod
	def get_best_move(self, moves):
		pass

