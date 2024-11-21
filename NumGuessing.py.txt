# Number Guessing Game using python

from random import uniform



def startGame(randNum):
	print("I have Choosen an random Number between 1 - 100, try guessing it within 3 attempts.")
	count = 0
	while count < 3:  # issue 1
		n = int(input("Enter the Number : "))
		if(randNum == n):
			print(f"You guessed it right! The number was {randNum}")
			return 1  # whenever an function returns something it will terminate itself.
		elif(randNum > n) :
			print("Your Number is smaller. TRY AGAIN")
			count+=1
		elif(randNum < n):
			print("Your Number is Bigger. TRY AGAIN")
			count+=1
	return 0
		
			
		
			
	


randNum = int(uniform(1,100)) # issue 3	
r = startGame(randNum)
if(r == 0):
	print(f"Sorry your all 3 attempts are done. The correct Number was {randNum}") #issue 4

