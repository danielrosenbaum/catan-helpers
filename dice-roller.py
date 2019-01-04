# Random Catan Dice Roller
import random

all_numbers = []
players = []
turn = 0
true_vals = [3, 6, 8, 11, 14, 17, 14, 11, 8, 6, 3]

# Randomly roll the dice
def roll_dice():
    global turn, all_numbers
    turn = turn % len(players)
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    roll = dice_1 + dice_2
    print ("\n", players[turn], "rolled a", roll, "\n")
    
    # keep track of all numbers and turn
    all_numbers.append(roll)
    turn += 1

# Print all the results from the game
def get_results():
    total = len(all_numbers)
    print("Total Rolls:", total)
    print("#   # of Rolls\t\t%\t       Exp. %")
    for i in range(2,13):
        count = all_numbers.count(i)
        percent = round((count/total) * 100)
        print(str(i) + ":\t" + str(count) + "\t|\t" + str(percent) + "%\t|\t" + str(true_vals[i-2]) + "%")

# Redo a roll
def redo_roll():
    global turn, all_numbers
    turn -= 1
    # remove the last entry from all_numbers
    all_numbers = all_numbers[:-1]
    roll_dice()
