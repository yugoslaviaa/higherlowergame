import random


def intchecker(number):
    valid = False
    while not valid:
        error = "Whoops! Please enter a valid option. (1, 2, or 3 if on main menu)"
        try:
            response = int(input(number))
            if response:
                return response
            else:
                print(error)
                print()

        except ValueError:
            print(error)


def quit(): 
	confirmation = intchecker("Are you sure you wish to exit? (1 for yes, 2 for no")
	if confirmation == 1:
		print("Quitting game..")
		print("Thanks for playing!")
	elif confirmation == 2: 
		main()



def main(): 
	print()
	print("Would you like to: ")
	print()
	print("1  Play the game")
	print("2  Open the instructions")
	print("3  Exit the game")
	print()
	global selection
	selection = intchecker(">> ")
	if selection == 1: 
		print("\nStarting the game...")
		print()
		generator = random.randint(1, 13) 
	elif selection == 2: 
		print("-" * 70)	
		print()
		print("HOW TO PLAY:")
		print()
		print("The computer will generate a random number between 1 and 13.")
		print("Your job is to guess whether or not the next number the computer chooses is higher or lower.")
		print("If you guess right, you get to keep playing.")
		print("If you guess wrong, you lose and have to start over.")
		print()
		print("-" * 70)
	elif selection == 3: 
		quit()
	
	

# Main Routine 
print("-" * 70)
print()
print("Welcome to the higher lower game!")
print("Created by Shaun Reynolds 2/08/2021")
print()
print("-" * 70)

while selection != 3: 
	main()