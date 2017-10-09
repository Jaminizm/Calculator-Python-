#Dice rolling program

print ("Welcome to my dice rolling program!")
print ("Press enter to roll")


#While True statement & assigning breaks

while True:

	play = input()

	
	if play == "q":
		break
		
	from random import *

#Beating number
	bnumber = randint(1,6)
	
	number = randint(1,6)
	

	if (bnumber == 1):
		print ("Player 1 Rolls: ")
		print (" [-------------]")
		print (" [             ]")
		print (" [      O      ]")
		print (" [             ]")
		print (" [-------------]")
		print ("Press Enter to Roll")
		play = input ()

		
	if (bnumber == 2):
		print ("Player 1 Rolls: ")
		print (" [-------------]")
		print (" [             ]")
		print (" [   O     O   ]")
		print (" [             ]")
		print (" [-------------]")
		print ("Press Enter to Roll")
		play = input ()
		
	if (bnumber == 3):
		print ("Player 1 Rolls: ")
		print (" [-------------]")
		print (" [   O     O   ]")
		print (" [             ]")
		print (" [      O      ]")
		print (" [-------------]")
		print ("Press Enter to Roll")
		play = input ()
		
	if (bnumber == 4):
		print ("Player 1 Rolls: ")
		print (" [-------------]")
		print (" [   O     O   ]")
		print (" [             ]")
		print (" [   O     O   ]")
		print (" [-------------]")
		print ("Press Enter to Roll")
		play = input ()
		
	if (bnumber == 5):
		print ("Player 1 Rolls: ")
		print (" [-------------]")
		print (" [   O     O   ]")
		print (" [      O      ]")
		print (" [   O     O   ]")
		print (" [-------------]")
		print ("Press Enter to Roll")
		play = input ()
			
	if (bnumber == 6):		
		print ("Player 1 Rolls: ")
		print (" [-------------]")
		print (" [   O     O   ]")
		print (" [   O     O   ]")
		print (" [   O     O   ]")
		print (" [-------------]")
		print ("Press Enter to Roll")
		play = input ()
		
	
	if (number == 1):
		print (" [-------------]")
		print (" [             ]")
		print (" [      O      ]")
		print (" [             ]")
		print (" [-------------]")
		print ("Press Enter to Roll")

		
	if (number == 2):
		print (" [-------------]")
		print (" [             ]")
		print (" [   O     O   ]")
		print (" [             ]")
		print (" [-------------]")
		
	
		
	if (number == 3):
		print (" [-------------]")
		print (" [   O     O   ]")
		print (" [             ]")
		print (" [      O      ]")
		print (" [-------------]")
	

		
	if (number == 4):
		print (" [-------------]")
		print (" [   O     O   ]")
		print (" [             ]")
		print (" [   O     O   ]")
		print (" [-------------]")
	

		
	if (number == 5):
		print (" [-------------]")
		print (" [   O     O   ]")
		print (" [      O      ]")
		print (" [   O     O   ]")
		print (" [-------------]")
	

		
	if (number == 6):		
		print (" [-------------]")
		print (" [   O     O   ]")
		print (" [   O     O   ]")
		print (" [   O     O   ]")
		print (" [-------------]")
	

	if (bnumber < number):
		print ("Congratulation! You won!")
		print ("Type 'q' to quit")
	
		
	elif (int(bnumber) == int(number)):
		print ("Draw! Roll Again!")
		print ("Type 'q' to quit")
		
	else:
		print ("Too bad, better luck next time!")
		print ("Type 'q' to quit")
		

