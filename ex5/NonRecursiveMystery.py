#############################################################
# FILE: NonRecursiveMystery.py
# WRITER: Roi Greenberg + roigreenberg + 305571234
# EXERCISE : intro2cs ex5 2013-2014
# Description: Implement a recursive function for sum of
#              divisors in iterative way
#############################################################


def mystery_computation(number):
    '''Implement a recursive function for sum of divisors in iterative way

    A function that sum the divisors of a given number
    (divisors=without remainder)

    Args:
    - number: integer number

    return: sum of all the nember divisors without reminders'''

    # equal the sum to zero
    divisors_sum=0

    # run for all possible divisors
    for divisor in range(1,number//2+1):
        # if no reminders, add to sum
        if number%divisor==0:
            divisors_sum+=divisor
            
    return divisors_sum
