class MCTSEngine():

	def __init__(self, game_engine, mcts, mcts_iter=600, sign=None):
		self.mcts_iter = mcts_iter
		self.game_engine = game_engine
		self.mcts = mcts

	def mcts_compute(self):

		move = self.mcts.selection()
		state = self.game_engine.apply_move(move)

		while not self.mcts.is_leaf(state):
			move = self.mcts.selection()
			state = self.game_engine.apply_move(move)

		if not self.game_engine.is_end():
			self.mcts.expansion()

		reward = self.mcts.heuristic(state)
		self.mcts.backprop(state, reward)


	def search(self, sign):
		
		for i in range(self.mcts_iter):
			self.game_engine.reset()
			self.mcts_compute()
		
		return self.mcts.get_best_move()
