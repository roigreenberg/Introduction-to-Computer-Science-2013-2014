#############################################################
# FILE: ex3.py
# WRITER: Roi Greenberg + roigreenberg + 305571234
# EXERCISE : intro2cs ex4 2013-2014
# Description:  retirement calculation (expenses and houses)
# and sorting function
#############################################################

# calculate pension with variable growth rates
def variable_pension(salary, save, growth_rates):
    """ calculate retirement fund assuming constant pesnion

    A function that calculates the value of a retirement fund in each year
    based on the worker salary, savings, working years and assuming constant
    growthRate of the fund

    Args:
    - salary: the amount of money you earn each year,
           a non negative float.
    - save: the percent of your salary to save in the investment account
            each working year -  a non negative float between 0 and 100
    - growth_rate: the annual percent increase/decrease in your investment
           account, a float larger than or equal to -100 (minus 100)
    - years: number of years to work - non negative int

    return: a list whose values are the size of your retirement account at
      the end of each year.

    In case of bad input: values are out of range
    returns None

    You can assume that the types of the input arguments are correct. """
    GROWTH = 0.01
    # verifies the input
    for rate in growth_rates:
        if float(rate) < -100:
            return
    if salary < 0 or save < 0 or save > 100:
        return

    if not growth_rates: # return empty list if no growth rates given 
        return []
    
    # calculate the pention
    pension = [salary * save * GROWTH]
    
    # run for the length of the growth rates list
    for i in range(1, len(growth_rates)):
        pension.append(pension[i - 1]*(1 + float(growth_rates[i])*\
                       GROWTH) + salary*save*GROWTH)
        
    return pension  # return list of the pension value for each year

    

# calculate the retirement savings
def post_retirement(savings, growth_rates, expenses):
    """ calculates the account status after retirement

    A function that calculates the account status after retirement, assuming
    constant expenses and no income
    Args:
    -savings: the initial amount of money in your savings account.
    A float larger than 0
    - growth_rates: a list of annual growth percentages in your investment
    account - a list of floats larger than or equal to -100.
    -expenses: the amount of money you plan to spend each year during
    retirement. A non negative float

    return: a list of your retirement account value at the end of each year.

    Note in case of a negative balance - the growth rate will change into
    rate on the debt
    In case of bad input: values are out of range returns None

    You can assume that the types of the input arguments are correct."""

    GROWTH = 0.01
    
    # verifies the input
    if not growth_rates:
        return []
    for rate in growth_rates:
        if rate < -100:
            return
    if savings < 0 or expenses < 0:
        return

    # Calculate the retirement saving
    # and put the into the new list
    retirement = [savings*(1+float(growth_rates[0])*GROWTH)-expenses]
    for i in range(1, len(growth_rates)):
        retirement.append(retirement[i-1]*(1+float(growth_rates[i])\
                                           *GROWTH)-expenses)
        
    return retirement  # return list of the retirement saving in each year


    


# Find the maximal expenses you may expend during your lifetime
def live_like_a_king(salary, save, pre_retire_growth_rates,
                  post_retire_growth_rates, epsilon):
    """ Find the maximal expenses you may expend during your lifetime

    A function that calculates what is the maximal annual expenses you may
    expend each year and not enter into debts
    You may Calculate it using binary search or using arithmetics
    Specify in your README in which method you've implemnted the function

    Args:  
    -salary: the amount of money you make each year-a non negative float.
    -save: the percent of your salary to save in the investment account
    each working year -  a non negative float between 0 and 100
    -pre_retire_growth_rates: a list of annual growth percentages in your
    investment account - a list of floats larger than or equal to -100.
    -post_retire_growth_rates: a list of annual growth percentages
    on investments while you are retired. a list of floats larger
    than or equal to -100. In case of empty list return None
    - epsilon: an upper bound on the money must remain in the account
    on the last year of retirement. A float larger than 0

    Returns the maximal expenses value you found (such that the amount of
    money left in your account will be positive but smaller than epsilon)

    In case of bad input: values are out of range returns None

    You can assume that the types of the input arguments are correct."""
    GROWTH = 0.01
    # verifies the input
    for rate in pre_retire_growth_rates:
        if rate < -100:
            return
    for rate in post_retire_growth_rates:
        if rate < -100:
            return
    if salary < 0 or save < 0 or save > 100 or epsilon <= 0:
        return
    # return None if no growth rates given 
    if len(post_retire_growth_rates) == 0: 
        return
    # return "0.0" if no growth rates given 
    if len(pre_retire_growth_rates) == 0: 
        return 0.0

    # calculate your savings in your retirement day
    savings = variable_pension(salary, save, pre_retire_growth_rates)[-1]

    # calculate the maximun expenses so you wont get in debts
    sum1, sum2 = savings*(1+float(post_retire_growth_rates[0])*GROWTH), 1
    for rate in post_retire_growth_rates[1:]:
        sum1=sum1*(1+rate*GROWTH)
        sum2=sum2*(1+rate*GROWTH)+1
    expenses = float(sum1)/float(sum2)
    return expenses


   





def bubble_sort_2nd_value(tuple_list):
    """sort a list of tuples using bubble sort algorithm

    Args:
    tuples_list - a list of tuples, where each tuple is composed of a string
    value and a float value - ('house_1',103.4)

    Return: a NEW list that is sorted by the 2nd value of the tuple,
    the numerical one. The sorting direction should be from the lowest to the
    largest. sort should be stable (if values are equal, use original order)

    You can assume that the input is correct."""
    
    reordered_list=tuple_list[:] # copy the value to new list
    for i in range(len(reordered_list)):  # bubble sort according to 2nd value
        for  j in range (0,len(reordered_list)-i-1):
            if reordered_list[j][1] > reordered_list[j+1][1]:
                reordered_list[j+1], reordered_list[j] =  \
                reordered_list[j], reordered_list[j+1]

    return reordered_list    





def choosing_retirement_home(savings,growth_rates,retirement_houses):
    """Find the most expensive retirement house one can afford.

    Find the most expensive, but affordable, retiremnt house.
    Implemnt the function using binary search

    Args:
    -savings: the initial amount of money in your savings account.
    -growth_rates: a list of annual growth percentages in your
    investment account - a list of floats larger than or equal to -100.
    -retirement_houses: a list of tuples of retirement_houses, where
    the first value is a string - the name of the house and the
    second is the annual rent of it - nonnegative float.

    Return: a string - the name of the chosen retirement house
    Return None if can't afford any house.

    You need to test the legality of savings and growth_rates
    but you can assume legal retirement_house list 
    You can assume that the types of the input are correct"""


    # verifies the input
    if not growth_rates:
        return
    for rate in growth_rates:
        if rate < -100:
            return
    if savings < 0 or not retirement_houses:
        return

    # sort the houses according to their annual rental
    reorder_houses = bubble_sort_2nd_value(retirement_houses)

    # return None if no house affordable
    if post_retirement(savings, growth_rates, reorder_houses[0][1])[-1] < 0:
        return
    # check if all the houses affordable. if so, choose the last house
    elif post_retirement(savings, growth_rates, reorder_houses[-1][1])[-1] > 0:
        best_house = len(reorder_houses)-1
    else:   
        # search for the best affordable house using binary-search                   
        cheap_house, exp_house = 0, len(reorder_houses)
        best_house = (cheap_house+exp_house)//2
        while best_house != cheap_house:
            saving_last_year = post_retirement(savings, growth_rates, \
                                     reorder_houses[best_house][1])[-1]
            best_house_cost = reorder_houses[best_house]
            if saving_last_year >= 0:
                cheap_house = best_house
            elif saving_last_year < 0:
                exp_house = best_house
            best_house = (cheap_house+exp_house)//2

    # check for former house with same annual rental
    while reorder_houses[best_house][1] == reorder_houses[best_house-1][1] \
          and best_house!=0:
        best_house -= 1
        
    return reorder_houses[best_house][0]
 
        

def get_value_key(value=0):
    """returns a function that calculates the new value of a house


    #Args:
    -value: the value added per opponent - a float - the default value is 0

    This function returns a function that accepts triple containing
    (house ,anntual rent,number of opponents) and returns the new value of
    this house - annual_rent+value*opponents

    You can assume that the input is correct."""
    
    def new_rent(house):
        """return the fun value of the house

        #Args:
        -house:(tuple), where  the first value
        is a string - the name of the house,
        the second is the annual rent on it - a non negative float, and the
        third is the number of battleship opponents the home hosts - non
        negative int"""

        return house[1]+value*house[2]
    
    return new_rent
    
    
    

   
def choose_retirement_home_opponents(budget,key,retirement_houses):
    """ Find the best retiremnt house that is affordable and fun

    A function that returns the best retiremnt house to live in such that:
    the house is affordable and
    his value (annual_rent+value*opponents) is the highest

    Args:
    -annual_budget: positive float. The amount of money you can
    expand per year.
    -key: a function of the type returned by get_value_key
    -retirement_houses: a list of houses (tuples), where  the first value
    is a string - the name of the house,
    the second is the annual rent on it - a non negative float, and the third
    is the number of battleship opponents the home hosts - non negative int
    
    Returns the name of the retirement home which provides the best value and
    which is affordable.

    You need to test the legality of annual_budget,
    but you can assume legal retirement_house list 
    You can assume that the types of the input are correct"""
    
    # verifies the input
    if budget <= 0:
        return
    if not retirement_houses:
        return

    # sort the houses according to their fun value
    sorted_retirement_houses=sorted(retirement_houses, key=key)
    # search and return the most fun house that affordable
    # return None if none affordable
    for best_house in range(len(sorted_retirement_houses)):
        if sorted_retirement_houses[-1 - best_house][1] < budget:
            return sorted_retirement_houses[-1-best_house][0]

