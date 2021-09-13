import random
import os


def intchecker(number):
    ''' '''
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
    print()
    print("Are you sure you wish to exit? (1 for yes, 2 for no)")
    print()
    confirmation = intchecker(">> ")
    if confirmation == 1:
        print("\nQuitting game..")
        print()
        print("Thanks for playing!")
        print()
        print("-" * 70)
    elif confirmation == 2:
        print()
        print("-" * 70)
        main()


# difficulty selection function
def difficulty_selector():
    ''' '''
    global amount_of_cards
    amount_of_cards = 0
    print()
    print("Select your difficulty: ")
    print()
    print("E for easy")
    print("H for hard")
    print("There is also a secret mode you can try to figure out if you want.")
    print()
    my_secret = os.environ['secret_difficulty']
    # lolol you thought
    global difficulty_user
    difficulty_user = input(">> ").upper()
    print()
    print(f"You have chosen {difficulty_user}")
    if difficulty_user == "E":
        amount_of_cards += 5
    elif difficulty_user == "H":
        amount_of_cards += 10
    elif difficulty_user == my_secret:
        amount_of_cards += 30
        print("Nice! You found my secret difficulty.")

    return amount_of_cards


# Main menu
def main():
    print("Would you like to: ")
    print()
    print("1  Play the game")
    print("2  Exit the game")
    print()
    print("-" * 70)
    global selection
    selection = intchecker(">> ")
    if selection == 1:
        print("\nStarting the game...")
        
				diff_number = difficulty_selector()

        global ai_list
        global cards
        global points

        #  Game Variables
        ai_list = []
        cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        points = 0
        i = 0

        while len(ai_list) != amount_of_cards:
            gen = random.choice(cards)
            ai_list.append(gen)

        print()
        print(f"Your card is {ai_list[i]}.\n")
        print("Do you wish to go higher or lower?")
        print()

        user_guess = input(">> ").upper()
        while i != amount_of_cards:
            if user_guess[0] == "H":
                if ai_list[i] < ai_list[i + 1]:
                    print()
                    print("Correct!")
                    points += 1
                elif ai_list[i] > ai_list[i + 1]:
                    print()
                    print("Wrong!")
                    print()
                    print(f"You had {points} points.")
                    print()
                    return False
           	if user_guess[0] == "L":
                if ai_list[i] > ai_list[i + 1]:
                    print()
                    print("Correct!")
                    points += 1
                elif ai_list[i] < ai_list[i + 1]:
                    print()
                    print("Wrong!")
                    print()
                    print(f"You had {points} points.")
                    print()
                    return False
      print("\nCongratulations! You won.")
      print()
      print(f"You have {points} points.")
      print()
  	  print("Do you wish to play again? (Y/N)")
      print()
      retry = input(">> ").upper()
      if retry[0] == "Y":
          return True
      elif retry[0] == "N":
          quit()
      else:
          print("\nAssuming what you meant is quit then.")
          quit()

    elif selection == 2:
        quit()


# Main Routine
print("-" * 70)
print()
print("Welcome to the higher lower game!")
print("Created by Shaun Reynolds 2/08/2021")
print()
print("-" * 70)
print()
print("HOW TO PLAY:")
print()
print("The computer will generate a random number between 1 and 13.")
print(
    "Your job is to guess whether or not the next number the computer chooses is higher or lower."
)
print("If you guess right, you get to keep playing.")
print("If you guess wrong, you lose and have to start over.")
print()
print("-" * 70)
print()

while menu != True: 
	menu = main()

if menu = True: 
	main()