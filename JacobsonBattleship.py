#Mia Jacobson
#CS2 - "Dot Wars (Battleship)"
#Description: This assignment is a simplified version of the board game "battleship". In this game, two players- the user and the computer- battle to guess where their opponent's randomly placed ships, or in this case, dots, are on the other's board. The game is played with 10 turns each, or until there is a winner.
#4/30/24
#Bonuses:(1)Make dots into shapes, 

import random
def main():
#main function
#instructions
    print("Welcome to Battleship! Here are the rules:")
    print("You will be asked 4 times to input coordinates (row and column) that indicate where to place your ships.")
    print("Your opponent (the computer) will randomly choose input 4 coordinates to place their ships.")
    print("Throughout the course of 10 turns each, each player will guess where their opponent's ship is.")
    print("Before each of your turns, you will get to see your guess board for optimal guessing. \n")
    print("Key:")
    print("💥 = Hit")
    print("❌ = Miss")
    print("🚢 = Where your ships are \n")
    print("Good luck!\n")


    #sets up boards for user & computer
    computer_board_placements = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    computer_board_guesses = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    user_board_placements = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    user_board_guesses = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

    rand_computer_initial_placements(computer_board_placements) #computer's initial ship placement (random)
    user_initial_placements(user_board_placements)#user's initial ship placement
    print("Your ship board:\n")
    show_board(user_board_placements)

   #counters for user and computer ships that have been sunk, once they reach 4, game ends
    ccounter = 0
    ucounter = 0
    
    for turn in range(10):#sets game to 10 turns each
        print("\n")
        print("Your guesses board:\n")
        show_board(user_board_guesses)
        computer_board_placements, user_board_guesses, ucounter = user_guesses(computer_board_placements, user_board_guesses, ucounter)
        print(f"You have {10-turn} turns left.")#tells user how many turns they have left

        if ucounter == 4:
            print("Game Over. \nCongratulations! You won.")
            break
        user_board_placements, user_board_guesses,computer_board_guesses, ccounter = rand_computer_guesses(user_board_placements, user_board_guesses,computer_board_guesses,ccounter)
        if ccounter == 4:
            print("Game Over. \nSorry, you lost.")
            break

#displays boards
def show_board(user_board):
    for i in user_board:
        print(i)
    
    print("")

#takes in user input for where they want to place ships, returns placements on the board
def user_initial_placements(user_board_placements):
    counter = 0
    while counter < 5:
        while True:
            try:
                row = int(input("What row do you want to place your ship in?"))         
                col = int(input("What column do you want to place your ship in?"))
                print("\n")
            
            except:
                print("Invalid response. Please enter an integer from 0 to 4.")
                continue

            #checks for invalid user inputs
            if (0 > row or row > 4 or 0 > col or col > 4):
                print("Invalid response. Please enter an integer from 0 to 4.")
                continue

            if user_board_placements[row][col] != '🚢':
                break
            else:
                print("There is already a ship in this spot. Please enter different coordinates.")


        user_board_placements[row][col] = '🚢'
        counter = counter +1
    
#takes in user guesses for where opponent's ships are, returns either "hit" or "miss" message
def user_guesses(computer_board_placements, user_board_guesses, ucounter):
    while True:
        try:
            row = int(input("What is the row of the coordinate would you like to guess?"))
            col = int(input("What is the column of the coordinate would you like to guess?"))
        
        except:
                print("Invalid response. Please enter an integer from 0 to 4.")
                continue

            
        #checks for invalid user inputs
        if (0 > row or row > 4 or 0 > col or col > 4):
            print("Invalid response. Please enter an integer from 0 to 4.")
            continue
       
        if user_board_guesses[row][col] not in ['💥', '❌']:
            break
        else:
            print("You already guessed this spot. Please enter different coordinates.")

    if computer_board_placements[row][col] == '🚢':
        computer_board_placements[row][col] = '💥'
        user_board_guesses[row][col] = '💥'
        print("\n")
        print("Yay! You hit one of your opponent's ships. :)")
        ucounter = ucounter + 1
    elif computer_board_placements[row][col] == 0:
        user_board_guesses[row][col] = '❌'
        print("\n")
        print("Sorry, you did not hit one of your opponents' ships. :(")
    return computer_board_placements, user_board_guesses, ucounter

#random computer placement of ships, happens once at the beginning of the game
def rand_computer_initial_placements(computer_board_placements):
    counter = 0
    while counter < 4:
        row, col = random.randrange(0,4), random.randrange(0,4)
        if computer_board_placements[row][col] == '🚢':
            continue
        else:
            computer_board_placements[row][col] = '🚢'
            counter = counter + 1

def rand_computer_guesses(user_board_placements, user_board_guesses,computer_board_guesses, ccounter):
    # this function is where the computer guesses where the user's ships are
    # it happens once a turn, and randomly
    while True:
        row, col = random.randrange(0,4), random.randrange(0,4)
        if computer_board_guesses[row][col] in ["💥","❌"]:
            continue
        else:
            if user_board_placements[row][col] == '🚢':
                computer_board_guesses[row][col] = '💥'
                user_board_placements[row][col] = '💥'
                print("Uh oh. One of your ships has been hit and sunk! :(")
                ccounter = ccounter +1
            elif user_board_placements[row][col] == 0:
                computer_board_guesses[row][col] = '❌'
                print("You are safe. The computer did not hit one of your ships. :)")
            break
    return user_board_placements, user_board_guesses,computer_board_guesses, ccounter
      

    
if __name__ == '__main__':
    main()