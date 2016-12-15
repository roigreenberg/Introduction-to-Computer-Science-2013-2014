#####################################################################
# FILE : ex1.py
# WRITER : Roi Greenberg + roigreenberg + 305571234
# EXERCISE : intro2cs ex1 20013-2014
# DESCRIPTION:
# Einstein game
#####################################################################


print("Welcome to the Einstein puzzle")  # welcoming line
input_number = int(input("Please enter a three digit number:"))  # receive number
reverse_number = input_number//100 + ((input_number//10)%10)*10 + (input_number%10)*100  # calculate the reverse number 
print("For the number:", input_number, "the reverse number is:", reverse_number)
difference = max(input_number,reverse_number) - min(input_number,reverse_number)  # calculate the difference between the numbers
print("The difference between", input_number, "and", reverse_number, "is", difference)
reverse_difference = difference//100 + ((difference//10)%10)*10 + (difference%10)*100  # calculate the reverse difference number
print("The reverse difference is:", reverse_difference)
print("The sum of:", difference, "and", reverse_difference, "is:", difference+reverse_difference)






    


