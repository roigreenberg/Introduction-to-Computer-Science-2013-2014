######################################################################
# FILE: GetToTheZero.py
# WRITER: Roi Greenberg + roigreenberg + 305571234
# EXERCISE : intro2cs ex5 2013-2014
# Description: Check if James Bond can pass the corridor undetected
######################################################################

def is_solvable(start,corridor):
    '''return a function that Check if James Bond can pass the corridor

    Args:
    - start: the start position. non negative integer smaller than corridor
             length
    - corridor: A list with positive integer except for the last place
                that hold zero.

    return: True if solvable, else False

    In case of bad input: values are out of range
    returns False'''

    ## verifies the position is in the corridor
    if start not in range(len(corridor)):
        return False

    END=0
    ## create empty list for used positions
    used_position=[]
    def get_to_zero(position,corridor):
        '''Check if James Bond can pass the corridor undetected

        A function that check if a given corridor is possible to solve by
        moving forward and backward according to the number in the current
        position in order to get to the last position that hold 'zero'.

        Args:
        - start: the start position. non negative integer smaller than corridor
                 length
        - corridor: A list with positive integer except for the last place
                    that hold zero.

        return: True if solvable, else False

        In case of bad input: values are out of range
        returns False'''

        # difine the value of the finish value
        END=0

        # check if position already checked
        if position in used_position:
            return False

        # add position to used positions list
        used_position.append(position)

        # check if the position is at the finish position
        if corridor[position]==END:
            return True

        # search the corridor forward and backward(if possible)
        return (False if position+corridor[position]>=len(corridor) \
                else get_to_zero(position+corridor[position],corridor)) \
                or \
               (False if position-corridor[position]<0 else\
                get_to_zero(position-corridor[position],corridor))
    
    return get_to_zero(start,corridor)
