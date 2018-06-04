import random

name = input('Hello. What is your name? ')

print('Well, ' +name+ ', I am thinking of a number from 1 to 20')
secretN = random.randint(1, 20)

for i in range(1, 7):
	guess = int(input('Take a guess: '))
	if guess<secretN:
		print('Your guess is too low')
	elif guess>secretN:
		print('Your guess is too high')
	else:
		break # correct answer


if guess == secretN:
	print('Good job, ' +name+ ', you guessed my # in ' +str(i)+ ' guesses')
else:
	print('Nope, the # I was thinking of was ' + str(secretN))


