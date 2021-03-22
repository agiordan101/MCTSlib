from abc import ABCMeta, abstractmethod

class GameEngine(metaclass=ABCMeta):

	def __init__(self):
		pass

	@abstractmethod
	def is_win(self):
		pass

	@abstractmethod
	def apply_move(self, *args, **kwargs):
		pass

	@abstractmethod
	def get_possible_move(self, *args, **kwargs):
		pass

	@abstractmethod
	def reset(self):
		pass

	@abstractmethod
	def no_moves_left(self):
		pass
