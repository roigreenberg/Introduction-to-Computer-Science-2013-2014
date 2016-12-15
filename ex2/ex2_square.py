#####################################################################
# FILE : ex2_square.py
# WRITER : Roi Greenberg + roigreenberg + 305571234
# EXERCISE : intro2cs ex2 20013-2014
# DESCRIPTION: Print square of '#' with  rhombus of '*' inside it
######################################################################

#!/usr/bin/env python3
def square_printing(n):
    number = n
    index = 1
    for i in range(1, 2*n+2):  # for all the lines
        if i==1 or i==2*n+1:  # check for the first and last lines
            print ("#" * (2 * n + 1))
        else:
            print ("#", end="")
            for k in range(1, 2*n):  # for every line
                if k == number or k == (2*n - number): 
                    print ("*", end="")
                else:
                    print (" ", end="")
            print ("#", end="")
            number -= index  # change the indicator for '*'
            if number == 1:  
                index = -1
            print ("")  # start in new line

#Here to help you test your code.
if __name__=="__main__":  #If we are the main script, and not imported
    from sys import argv
    try:
        n = int(argv[1])
    except:
        n = int(input("Please enter a positive integer: "))
    square_printing(n)
