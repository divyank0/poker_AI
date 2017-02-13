"""
this is table for 
playing a poker game

cards n
1-13: Hearts
14-26: diamonds
27:39 spades

40: 52 clubs

1- Ace
2- 2
10- 10
11- J
12- Q
13- K
"""


import random
import sys
print(sys.version)




class Deck():
	'''this is deck of cards, with shuffle inbuild
		to get new cards,
		call distribute with number of cards'''

	def __init__(self):
		self.cards = random.shuffle(list(range(52)))

	def distribute(self,count):
		temp = []
		for i in range(count):
			temp.append(self.cards.pop())
		return temp


class Player():
	''' the player who is playing
	'''

	def __init__(name, api):
		self.name = name
		self.api = api
		self.cards = []

	def core(self):
		# decide what player whats to do
		# heavy algo

	def get_cards(self, cards):
		self.cards = cards

	def showdown():
		return self.cards()






states = {0:'dealing',1:'flop',2:'turn',3:'river',4:'showing'}

class Table():
	'''table which deals the card to players
	and manages the game'''

	def __init__(self):
		self.deck = Deck()
		self.players = []
		self.state = 0    # 0, 1, 2,3,4
		self.community_card =[]

	def add_players(self, player):
		if len(players) < 6:
			self.players.append(player)
		else:
			print('number of players exeded 5, hence ignoring')

	def deal(self):
		'deal the cards to n players'
		
		if self.state == 0:
			'deal start'
			card_dealts={}
			#deal cards
			for i in self.players:
				card_dealts[i] = self.deck().distribute(1)
			for i in self.players:
				card_dealts[i].extend(self.deck().distribute(1))
			#distriubte cards
			for player in self.players:
				player.get_cards(card_dealts[player])
		else:
			print('some issue in dealing')
		self.state +=1




	def open_cards(self):
		'add cards to community_card'
		if self.state == 1:
			self.community_card.extend(self.deck.distribute(3))
		elif self.state ==2:
			self.community_card.extend(self.deck.distribute(1))
		elif self.state ==3:
			self.community_card.extend(self.deck.distribute(1))
		else:
			print('some issue iwith adding community cards')
		self.state +=1


	def showdown():
		'ask each player to reveal cards'
		assert self.state == 4
		players_cards ={}
		for i in self.players:
			players_cards[i] = self.players[i].showdown()

		winner = find_winner(self.community_cards, players_cards)

		print('winner is ', winner.name)



class pot():
	'''pot on the table
	this will maintain the betting status of the table'''

	def __init__(self):
		self.money = 0
		self.bets = []



def find_winner(community_cards, players_cards):
	'''input:  community_cards [1,2,3,4,5]
	output: players_cards = {1:[1,2]}'''








print(1)

'''
todo:
	- message exchange protocol
	- community_cards
		- pot total
		- players status, raise, call, check , fold
	- 'all in for one player'
	- 
		- 


'''