'''
class for client side


'''


class Player():
	''' the player who is playing
	'''

	def __init__(self,name):
		self.name = name
		self.money = 0
		self.cards = []

	def core(self, game,options):
		'''the player must decide here what he is doing here
		game : community cards, total pot, betting in this round,
				round_number, players_status
		options : what the player can do!
		
		'''
		pass



	def get_cards(self, cards):
		self.cards = cards

	def get_money(self, money):
		self.money += money
	def bet_money(self, money):
		self.money -=money

	def showdown():
		'must show you cards'
		return self.cards()

	def refresh(status):
		''' a round has ended,
		analysis it and referesh for next round
		'''
		self.cards = []



Player('foo')
