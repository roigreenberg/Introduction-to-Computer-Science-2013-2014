#####################################################################
# FILE : ex2_rpsls.py
# WRITER : Roi Greenberg + roigreenberg + 305571234
# EXERCISE : intro2cs ex2 20013-2014
# DESCRIPTION: Playing Rock-Paper-Scissors-Lizard-Spock game against
# for set of rounds the player want until one's win.
#####################################################################

#!/usr/bin/env python3
import random
from ex2_rpsls_helper import get_selection

def who_win(player, comp):  # find who win
    if player == comp:
        return ("draw")
    elif player == 1 and (comp == 4 or comp == 3):
        return ("Player")
    elif player == 2 and (comp == 1 or comp == 5):
        return ("Player")
    elif player == 3 and (comp == 2 or comp == 4):
        return ("Player")
    elif player == 4 and (comp == 5 or comp == 2):
        return ("Player")
    elif player == 5 and (comp == 3 or comp == 1):
        return ("Player")
    else:
        return ("Computer")
    
def rpsls_game():  # the game function
    player_win = comp_win = draws = 0  # reset counters
    while -2<(player_win - comp_win)<2:
        # player input
        player_sel = int(input("    Please enter your selection:" \
                               + " 1 (Rock), 2 (Paper), 3 (Scissors),"\
                               + " 4 (Lizard) or 5 (Spock): "))
        # make sure the number is correct
        while player_sel < 1 or player_sel > 5:
            # player input
            print("    Please select one of the available options.\n")
            player_sel = int(input("    Please enter your selection:"\
                               + " 1 (Rock), 2 (Paper), 3 (Scissors),"\
                               + " 4 (Lizard) or 5 (Spock): "))
        print ("    Player has selected: "
               +"{}.".format(get_selection(player_sel)))
        comp_sel = random.randint(1,5)  # computer selection
        print ("    Computer has selected: "\
               +"{}.".format(get_selection(comp_sel)))
        winner = who_win(player_sel, comp_sel)  # find who won
        if winner != "draw":  # declare the result
            print ("    The winner for this round is: {}\n".format(winner))
        else:
            print ("    This round was drawn\n")
        if winner == "Player":  # count the sum of the winning
            player_win += 1
        elif winner == "Computer":
            comp_win += 1
        else:
            draws += 1
    # find out who win and announce the winner
    game_winner = "Player" if player_win > comp_win else "Computer" 
    print ("The winner for this game is:", game_winner)
    print ("Game score: Player {},".format(player_win)\
           +" Computer {}, draws {}".format(comp_win, draws))
    return (1 if game_winner == "Player" else -1)    

       
def rpsls_play():
    choice = 2
    # welcoming line
    print ("Welcome to the Rock-Scissors-Paper-Lizard-Spock game!")
    while choice == 2:  # run until player choose to quit
        sets = sets_won = 0
        choice = 3
        N = int(input("Select set length: "))
        while choice == 3:  # run until player choose to reset
            player_game = comp_game = 0  # reset counters
            sets += 1
            for ii in range(1, N+1):  # run for N rounds
                print ("Now beginning game", ii)
                game_winner = rpsls_game()  # get the round's winner
                if game_winner == 1:  # count the winning
                    player_game += 1
                else:
                    comp_game += 1
                print ("Set score: Player {},".format(player_game)\
                       +" Computer {}".format(comp_game))
                # break the loop if one have won more than N/2 games
                if (player_game > (N/2)) or (comp_game > (N/2)):
                    break
            if player_game == comp_game:  # run if draw after N games
                num = N +1
                # run until one have 2 wins more than the other
                while -2<(player_game - comp_game)<2:
                    print ("Now beginning game", num)
                    num += 1
                    game_winner = rpsls_game()  # get the round's winner
                    if game_winner == 1:  # count the winning
                        player_game += 1
                    else:
                        comp_game += 1
                    print ("Set score: Player {}, ".format(player_game)\
                           +"Computer {}".format(comp_game))
            # announce the player status
            if player_game > comp_game:
                print ("Congratulations! You have won "\
                       +"in", player_game + comp_game, "games.")
                sets_won += 1
            else:
                print("Too bad! You have lost"\
                      +" in", player_game + comp_game, "games.")
            # sum the set score
            print ("You have played {} sets, and ".format(sets)
                   + "won {}!\n".format(sets_won))
            # ask the player how he want to continue
            print ("Do you want to: 1 - quit, 2 - reset "
                   +"scores or 3 - continue? ", end="")
            while True:  # confirm the right input
                try:
                    choice = int(input())
                    break
                except ValueError:
                    pass
            if choice == 1:  # if player want to quit
                break
            if choice == 2:  # if player want to reset
                print ("Resetting scores")

#Here to help you test your code.
#When debugging, it is helpful to be able to replay with the computer
# repeating the same choices.
if __name__=="__main__": #If we are the main script, and not imported
    from sys import argv
    try:
        random.seed(argv[1]) # as a string is good enough
    except:
        pass

    rpsls_play()
