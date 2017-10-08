#Dice rolling program

print ("Welcome to my dice rolling program!")
print ("Press enter to roll")


#While True statement & assigning breaks

while True:

	play = input()

	
	if play == "q":
		break
		
	from random import *

	number = randint(1,6)
	

	if (number == 1):
		print (" [-------------]")
		print (" [             ]")
		print (" [      O      ]")
		print (" [             ]")
		print (" [-------------]")
		print ("Type 'q' to quit")

		
	if (number == 2):
		print (" [-------------]")
		print (" [             ]")
		print (" [   O     O   ]")
		print (" [             ]")
		print (" [-------------]")
		print ("Type 'q' to quit")
	
		
	if (number == 3):
		print (" [-------------]")
		print (" [   O     O   ]")
		print (" [             ]")
		print (" [      O      ]")
		print (" [-------------]")
		print ("Type 'q' to quit")

		
	if (number == 4):
		print (" [-------------]")
		print (" [   O     O   ]")
		print (" [             ]")
		print (" [   O     O   ]")
		print (" [-------------]")
		print ("Type 'q' to quit")

		
	if (number == 5):
		print (" [-------------]")
		print (" [   O     O   ]")
		print (" [      O      ]")
		print (" [   O     O   ]")
		print (" [-------------]")
		print ("Type 'q' to quit")

		
	if (number == 6):		
		print (" [-------------]")
		print (" [   O     O   ]")
		print (" [   O     O   ]")
		print (" [   O     O   ]")
		print (" [-------------]")
		print ("Type 'q' to quit")
		
	

	

