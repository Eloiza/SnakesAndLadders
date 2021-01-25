import random
import sys


class GameLog:
	def __init__(self):
		self.rounds = 0		#total rounds in a game 
		self.players = []	#players in their final state
		self.winner = 0 	#index of the player who won

class Die:

	#initialize the die with a random seed
	def __init__(self):
		seedValue = random.randrange(sys.maxsize)  #create a random seed
		random.seed(seedValue)

	#return a random integer between 1 and 6 
	def roll(self):
		return random.randint(1,6)

class Board:
	def __init__(self, s):
		self.size = s 	#number of spaces in the board
		self.board = [i for i in range(self.size + 1)]	#initialize boardgame with indexes numbers


	#add a ladder or a snake to the board
	def add_component(self, index, dest):
		self.board[index] = dest 

	#remove a ladder or a snake to the board
	def remove_component(self, index):
		self.board[index] = index 

	#get some position in the boardgame
	def get_space(self, index):
		return self.board[index]

class Player:
	def __init__(self, player_name, start_position, snk_immunity = 0):
		self.position = start_position			#current player's position in the boardgame
		self.snake_immunity = snk_immunity 		#snake immunity to a x numbers of snakes during the game
		self.snakes = 0 						#total snakes that the player landed during the game 
		self.ladders = 0						#total ladders that the player landed during the game
		self.player_name = player_name			#player name only for print porpouses

	#move a player to some space in boardgame. It also check if the space is a ladder or a snake
	def move_player(self, die_num):
		self.position = self.position + die_num

		#check if the position is greater than the boardgame
		if(self.position > board.size):
			self.position = board.size

		curr_space = board.get_space(self.position)
		if(self.position != curr_space):
			
			#check if it hitted a snake
			if(curr_space < self.position):
				self.snakes += 1

				#check if the player has a snake immunity 
				#if yes the player keeps in the same position 
				if(self.snake_immunity > 0):
					self.snake_immunity = self.snake_immunity - 1
					return;

			#check if it hitted a ladder
			else:
				self.ladders += 1
				if(TOSS_COIN):
					#tossing a coin to take the ladder
					#if one the player stays in the same place
					if(random.randint(0,1)):
						return;

			self.position = curr_space



def game_play(n_players, Players, board_size, n_ladders, ladders ,n_snakes, snakes, toss_coin=0):
	global TOSS_COIN
	TOSS_COIN = toss_coin
	
	#create a die	
	game_die = Die()
	
	#create the board
	global board
	board = Board(board_size)

	#adding ladders
	for i in range(n_ladders):
		board.add_component(ladders[i][0], ladders[i][1])

	#adding snakes
	for i in range(n_snakes):
		board.add_component(snakes[i][0], snakes[i][1])

	#create a gamelog to save some data 
	g_log = GameLog()

	GAME_OVER = 0
	rounds = 0 
	#runs the game
	while(not GAME_OVER):
		rounds+=1
		#do the players turns
		for i in range(n_players):
			rolled_die = game_die.roll()			
			Players[i].move_player(rolled_die)

			#check if some player hitted the last space
			if(Players[i].position == board.size):	
				GAME_OVER = 1
				g_log.winner = i
				break;

	g_log.rounds = rounds
	g_log.players = Players

	return g_log
