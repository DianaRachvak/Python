#num = float(input("enter a price: "))
#print("Total price: ", round(num+0.35*num), "\n Sales Tax: ", 0.35*num)

import random
winnum = random.randint(0,99)
guess = int(input("Enter your lottery pick(2digits): "))
winnumD1 = winnum//10
winnumD2 = winnum%10
guessD1 = guess//10
guessD2 = guess%10
while(guess != winnum or guess != -1):


	
	if guess == winnum:
		print('Exact Match, you win $1000000')
		break

	elif (guessD2 == winnumD1) and (guessD1 == winnumD2):
		print('Match all digits, you win $700000')
		break
	elif (guessD1 == winnumD1 or guessD1 == winnumD2 or guessD2 == winnumD1
		or guessD2 == winnumD2):
	    print('Match one digit, you win $3000')
	    break
	elif guess < winnum:
		print("Please guess a higher number: ")
		guess = int(input("Enter your lottery pick(2digits): "))
	elif guess > winnum:
		print("Please guess a lower number: ")
		guess = int(input("Enter your lottery pick(2digits): "))

	guessD1 = guess//10
	guessD2 = guess%10
print("Congrats on the correct num")