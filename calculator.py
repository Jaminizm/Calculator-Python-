#Returns the sum of num1 and num2
def add(num1, num2):
	return num1 + num2
	
def subtract(num1, num2):
	return num1 - num2

def multiply(num1, num2):
	return num1 * num2

def divide(num1, num2):
	return num1 / num2

#+, *, -, /

def main():
	operation = input("what do you want to do (+,-,*,/): ")
	if((operation != "+") and (operation != "-") and (operation != "/") and (operation != "*")): 
		#invalide operation
		print("You must enter a valid operation")
		#valid operation
	else:
		num1 = int(input("Enter num1: "))
		num2 = int(input("Enter num2: "))
		#Plus
		if(operation == '+'):
			print(add(num1, num2))
			
		#Minus
		if(operation == '-'):
			print(subtract(num1, num2))
			
		#multiply
		if(operation == '*'):
			print(multiply(num1, num2))
			
		#divide
		if(operation == '/'):
			print(divide(num1, num2))
			

main()