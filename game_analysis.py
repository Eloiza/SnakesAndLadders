import game_source as gs

def main():

	n_times = 10000
	n_players = 2

	#board_game setup 
	board_size = 36
	ladder_spaces = [(3,16), (5,7), (15,25), (18,20), (21,32)]
	snake_spaces  = [(12,2), (14,11), (17,4), (31,19), (35,22)] 

	####### QUESTION 1 AND 2 ####### 
	wins = [0 for i in range(n_players)]	#a list to save how many times a player has won
	total_snakes = 0 	#to save total snakes landed in a game

	#running the 10.000 games 
	for i in range(n_times):
		#set the default players
		plyrs = [gs.Player("Player1", start_position= 1), gs.Player("\tPlayer2", start_position=1)]

		#run the game with a default parameters
		log = gs.game_play(n_players= 2, Players=plyrs, board_size= 36, n_ladders= 5, ladders=ladder_spaces,  n_snakes= 5, snakes=snake_spaces)

		#save wins of each player
		wins[log.winner] += 1	

		#save total snakes landed during the game
		for i in range(len(log.players)):
			total_snakes += log.players[i].snakes

	print("QUESTION 1: \nProbability that the first player wins: %.2f\n" %( (wins[0]/n_times)*100) )
	print("QUESTION 2: \nAverage amount of landed snakes: %.0f\n" %( (total_snakes/n_times) ) )

	
	####### QUESTION 3 #######
	total_rounds = 0 
	for i in range(n_times):
		#set default players to each game
		plyrs = [gs.Player("Player1", start_position= 1), gs.Player("\tPlayer2", start_position= 1)]

		#run the game with a coin toss when a player lands a ladder
		log = gs.game_play(n_players= 2, Players=plyrs, board_size= 36, n_ladders= 5, ladders=ladder_spaces,  n_snakes= 5, snakes=snake_spaces, toss_coin = 1)

		#sum the total of rounds
		total_rounds += log.rounds

	print("QUESTION 3: \nAverage amount of rolls to complete the game: %.0f\n" %(total_rounds/n_times))

	####### QUESTION 4 #######
	final_results = []

	#run a for to change the player's 2 position 
	for i in range(1, board_size):
		wins = [0 for i in range(len(plyrs))]	#save how many times a player has won 

		#run 10.000 games for each posible position
		for j in range(n_times):

			#set default players with a diferent start position 
			plyrs = [gs.Player("Player1", start_position= 1), gs.Player("\tPlayer2", start_position= i)]
			
			#run the default game
			log = gs.game_play(n_players= 2, Players=plyrs, board_size= 36, n_ladders= 5, ladders=ladder_spaces,  n_snakes= 5, snakes=snake_spaces)

			#save winner
			wins[log.winner] += 1
		
		#save the absolute value of the diference between how many times each player has won
		final_results.append(abs(wins[0] - wins[1]))

	#the best position is the position that has the smallest diference
	best_position = final_results.index(min(final_results)) + 1
	print("QUESTION 4: \nThe best Player's 2 start position: %i\n" %(best_position))


	####### QUESTION 5 #######
	wins = [0 for i in range(len(plyrs))] #save how many times a player has won

	#run 10.000 games
	for i in range(n_times):
		#set a default player (Player 1) and a player with immunity to the first snake (Player 2)
		plyrs = [gs.Player("Player1", start_position= 1), gs.Player("\tPlayer2", start_position=1, snk_immunity=1)]

		#run the game
		log = gs.game_play(n_players= 2, Players=plyrs, board_size= 36, n_ladders= 5, ladders=ladder_spaces,  n_snakes= 5, snakes=snake_spaces)

		#save winner
		wins[log.winner] += 1 

	print("QUESTION 5: \nProbability of Player1 winning: %.2f\n" %((wins[0]/n_times)*100 ))
 
if '__main__':
	main()