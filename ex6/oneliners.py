#############################################################
# FILE: oneliners.py
# WRITER: Roi Greenberg + roigreenberg + 305571234
# EXERCISE : intro2cs ex6 2013-2014
# Description: implement some tasks in one or few code line.
#############################################################

def is_two_palindrome(string):
    """The function tests if the given string is a “two palindrome” or not.
       A string is a palindrome if reversing it does not change it

    Args:
    - string:String of any length . The string may include punctuation,
             spaces, and other symbols

    The function return True if the string is a “two palindrome” and
    False in not. """
    
    return True if len(string)==1 else \
           string[:len(string)//2]==\
           string[len(string)//2-1::-1]\
           and string[len(string)-(len(string)//2):]==\
           string[:len(string)-(len(string)//2)-1:-1]


def uni_sort(list_1,list_2):
    """The function combines two unsorted lists of integers into one
       sorted list

    Args:
    - list_1:List of integers
    - list_2:List of integers

    The function return a new sorted list with the number from both lists,
    without duplicates"""
    # create a new empty list:
    combine_list=[]
    return combine_list.extend(num for num in (list_1 + list_2)\
                               if num not in combine_list) or \
                               sorted(combine_list)

def dot_product(vector_1,vector_2):
    """The function returns the dot product of two vectors, represented
       as lists

    Args:
    - vector_1:List of integers(representing vector)
    - vector_2:List of integers(representing vector)

    The function return the result of the dot product of the two
    input vectors"""
    
    return sum(num_vector_1*num_vector_2 for num_vector_1,num_vector_2\
               in zip(vector_1,vector_2))

def list_intersection(list_1,list_2):
    """The function combines two unsorted lists of integers into one sorted
       list contain exactly those integers that appear in both input lists.

    Args:
    - list_1:List of integers
    - list_2:List of integers

    The function return a new sorted list only with the number that contain in
    both lists, without duplicates"""
    return sorted(list(set(num for num in list_1+list_2 \
                           if num in list_1 and num in list_2)))

def list_difference(list_1,list_2):
    """The function combines two unsorted lists of integers into one
       sorted list contain only those integers that appear in just one of the
       input lists

    Args:
    - list_1:List of integers
    - list_2:List of integers

    The function return a new sorted list only with the numbers appear in just
    just one of the lists, without duplicates"""
    return sorted(list(set(num for num in list_1+list_2 if \
                           ((num in list_1 and num not in list_2) or\
                            (num in list_2 and num not in list_1)))))

def random_string(number):
    """The function generates a random string of a given length using only
        lower-case characters.

    Args:
    - number: An integer denoting the length of the output random string

    The function return A random string of length N"""
    
    from random import randint
    return ''.join((chr(randint(97,122))) for i in range(number))


def word_mapper(string):
    """The function returns a dictionary mapping from the words in the
       input text to their number appearances

    Args:
    - string: A string of words separated by whitespace and/or punctuation
              marks.

    The function return a dictionary containing a mapping between words
    (as keys) and the number of times they appear in the original input
    string (as value)."""
    
    import re
    # create a list containing only the words converting to lower-case chars
    word_list=re.sub("[\W\_]", " ", string.lower()).split()
    return  dict([(word,word_list.count(word)) for word in word_list])

def gimme_a_value(function,start_value):
    """the function create a generator that gets two inputs, a function(f) and
       a starting point (x0).
    The generator computes a sequence of values (x1,x2...) of the function.
    For all i>=0 The i-th call to the generator returns the value x(i)=f(x(i-1)
    The first call returns x0 (the initial value)

    Args:
    - function: A math function
    - start_value: the initial value, x0

    The function return The next element in the sequence generated by applying
    the function to the previous element. The first returned value is x0"""

    # returns x0 (the initial value)
    yield start_value

    # run endlessly
    while True:
        yield function(start_value)
        # change the start value to the next value
        start_value=function(start_value)
