# Number Guesser

import random


RoundNum = 1
NumberToGuess = random.randint(1,100)
Guess = 123

print("")
print(">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
print("	")
print("Hello!! Wlecome to Number Guesser.\nIn this game, a random number between 1-100 will be chosen(and not shared with you.)\nYour job is to guess the number.\nAfter each guess the game will tell you if your guess is higher or lower than the randomly generated number.\nA 'GT' after a number means that it was more than the number to guess.\nA 'LT' after a number means that it was less than the number to guess.\n\n Devloped by Ashley Rylander.")
print(">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
print("	")
print(" ")

while Guess != NumberToGuess:
	print("Round", RoundNum,"::")
	Guess = input("Please enter your guess(1-100) or enter q to quit: ")
	if Guess == "Q" or Guess == "q":
		print("Thank you for playing Number Guesser!")
		print("Goodbye!")
		break
	Guess = int(Guess)
	if Guess < NumberToGuess:
		Guess = str(Guess)
		if RoundNum == 1:
			List = [Guess + " (LT)"]
		else:
			List.append(Guess + " (LT)")
		print("")
		print("Your guess is incorrect. The number is more than", Guess)
		Guess = int(Guess)
	if Guess > NumberToGuess:
		Guess = str(Guess)
		if RoundNum == 1:
			List = [Guess + " (GT)"]
		else:
			List.append(Guess + " (GT)")
		print("")
		print("Your guess is incorrect. The number is less than", Guess)
		Guess = int(Guess)
	if Guess == NumberToGuess:
		print("")
		print("! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !")
		print("The number was", NumberToGuess,"! It took you", RoundNum, "guesses!")
		print("Your previous guesses were", List)
		print("! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !")
		print("")
		break
	RoundNum = RoundNum + 1
	print("In the past you tried", List)
	print("")
print("Developed by Ashley Rylander")
Number_Guesser_AR.py
Displaying Number_Guesser_AR.py.
