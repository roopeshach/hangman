import random

def welcome():
	name = str(input("Enter you name ::"))
	print("Welcome to the game",name)
	print("#####################################")
	print("Try to guess the word or hanged")
	hangman()
	print()

def hangman():
	lines = open("dictionary.txt").readlines() 
	line = lines[0] 

	word = line.split() 
	words = random.choice(word)
	# words = random.choice(["roopesh", "acharya", "deepesh", "cucumber", "fruits"])
	#random word chanxa paxi chai ma auta text file wa word list halxu
	acceptedLetters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUPWXYZ'

	turns = 6
	enteredWord = ' ' #user bata0 aaune word

	#word generation
	while (len(words)> 0):
		message= " " 
		fails = 0 #fails chai 6 huna ko lagi declaration
		for char in words:
			if char in enteredWord:
				message = message+char
			else:
				message = message + "_" + " "
				fails += 1 #adding errors
		if message == words: #user le deko word milemaa
			print(message)
			#real word pani output haldim na
			print("You entered the right word. The word was:", ranGenWord)
		break # word guess garepaxi exit
		#natra feri word ko input magam na
		print("Guess the word:", message)
		guess = input()

		#accepted letters ma user le deko word xa ki nai vanera check garna lako
		if guess in acceptedLetters:
			enteredWord = enteredWord + guess
		else:
			#accepted letters ma xaina vane valid letter magna ko lagi use lai vanne
			print("Enter a valid character:")
			#eri user sanga input liney
			guess = input()

		#Yesso hangman ni banaidim na gaaro xa haha
		#1st guess mile vane tauko ani haat ani sarir ani khutta total 6 gess to be wrong
		if guess not in words:
			turns = turns - 1
			if turns == 5: #tauko print hanna lai O haldim na
				print("   O  ")
			if turns == 4:
				print("   O  ")
				print("   |")
			if turns == 3:
				print("   O")
				print("  /|")
			if turns == 2:
				print("   O  ")
				print("  /|\\")
			if turns == 1:
				print("   O  ")
				print("  /|\\")
				print("  /")
			if turns == 0:
				print("   O  ")
				print("  /|\\")
				print("  / \\")
			print("You couldn't guess the word", words)
			break
welcome()




