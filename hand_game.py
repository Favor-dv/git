#Rules:
	#rocks beats scissors
	#paper beats rocks
	#scissors beats paper 


from random import choice, random

comp_inp_list = ['rock', 'paper', 'scissors']

user_inp = input('Enter your take: ')

if user_inp in comp_inp_list:
	pass
		
else :
	print('Pls enter either rock, paper or scissors')
	quit()
		
comp_Inp = choice(comp_inp_list)

class game (object):

	def __init__(self, user_inp):
		self.user_inp = user_inp

	def rock (self) :
		if user_inp == 'paper':
			if comp_Inp == 'scissors' :
				print('You loose')

		if user_inp == 'scissors' :
			if comp_Inp == 'paper':
				print('You win')
				quit()

	def paper (self) :
		if user_inp == 'scissors' :
			if comp_Inp == 'rock':
				print('You loose')

		if user_inp == 'rock':
			if comp_Inp == 'scissors' :
				print('You win')
				quit()

	def scissors (self) :
		if user_inp == 'rock':
			if comp_Inp == 'paper':
				print('You loose')

		if user_inp == 'paper':
			if comp_Inp == 'rock' :
				print('You win')
				quit()


def calc (self) :
		rock = self.rock()
		paper = self.paper() 
		scissors = self.scissors()

if comp_Inp != user_inp:
	result = game(user_inp)
	print(calc(result))

else:
	print('Tie')

