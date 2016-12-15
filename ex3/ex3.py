#############################################################
# FILE: ex3.py
# WRITER: Roi Greenberg + roigreenberg + 305571234
# EXERCISE : intro2cs ex3 2013-2014
# Description: pension, growth rates and retirement
# caculations.
#############################################################

# calculate pension with constant growth rate
def constant_pension(salary, save, growth_rate, years):
    # verifies the input
    if salary < 0 or growth_rate < -100 or years < 0\
       or save < 0 or save > 100:
        return

    if years == 0:  # return empty list if years is 0 
        return []
    # calculate the pention
    pension = [salary * save * 0.01]
    # run for the length of the years given
    for i in range(1, years):
        pension.append(pension[i - 1]*(1 + growth_rate*0.01)\
                       + salary*save*0.01)
    return pension  # return list of the pension value for each year

# calculate pension with variable growth rates
def variable_pension(salary, save, growth_rates):
    # verifies the input
    for i in growth_rates:
        if float(i) < -100:
            return
    if salary < 0 or save < 0 or save > 100:
        return

    if len(growth_rates) == 0: # return empty list if no growth rates given 
        return []
    
    # calculate the pention
    pension = [salary * save * 0.01]
    
    # run for the length of the growth rates list
    for i in range(1, len(growth_rates)):
        pension.append(pension[i - 1]*(1 + float(growth_rates[i])*0.01)\
                       + salary*save*0.01)
        
    return pension  # return list of the pension value for each year

# finding the fund with the best pention
def choose_best_fund(salary,save,funds_file):
    if salary < 0 or save < 0 or save > 100: # verifies the input
        return
    
    file = open(funds_file)  # open the given file
    funds = file.readlines()  # create list of the file lines
    for i in range(len(funds)):  # divide the Fund name from the growth rates
        funds[i] = funds[i].split(",", 1)
    if len(funds[0]) == 1:  # return empty list in no growth rates given
        return []

    # Create list from the growth rates and strip the fund name and the last
    # growth rate from unnessary chars ('#' "\n")
    for i in range(len(funds)):
        funds[i][1] = funds[i][1].strip("\n").split(",")
        funds[i][0] = funds[i][0].strip("#")

    # create new list of every fund and it value in the last year
    funds_compare = []
    
    # Calculate the pension values the takes only the name and the last value
    # and put the into the new list
    for i in range(len(funds)):
        pension_values = variable_pension(salary,save,funds[i][1]) 
        fund_last_value = [funds[i][0], pension_values[len(funds[i][1]) - 1]]
        funds_compare.append(fund_last_value)

    # reorder the funds from the highest value to the lowest
    for i in range(len(funds)-1):
        for  j in range (i,len(funds)):
            if funds_compare[i][1] < funds_compare[j][1]:
                funds_compare[i], funds_compare[j] =\
                funds_compare[j], funds_compare[i]
    file.close()
    
    return tuple(funds_compare[0]) # return a tuple with the best fund

# find the growth rate in a given yaer
def growth_in_year(growth_rates,year):
    # verifies the input
    if len(growth_rates) == 0 or year < 0:
        return 
    for i in growth_rates:
        if float(i) < -100:
            return
    if len(growth_rates) <= year:
        return
 

    return growth_rates[year]  # return the growth rate in the given yaer
    

# update the growth rates list with inflation value 
def inflation_growth_rates(growth_rates,inflation_factors):
    # verifies the input
    if len(inflation_factors) == 0:
        return growth_rates
    for i in growth_rates:
        if float(i) < -100:
            return
    for i in inflation_factors:
        if float(i) <= -100:
            return
        
    # return empty list in no growth rates given
    if len(growth_rates) == 0:
        return []
    
    update_rates = []  # create new list of the update rates
    
    # run for the shortest list and calculate the update rates
    for i in range(min(len(growth_rates),len(inflation_factors))):
            update_rates.append(100*((100+float(growth_rates[i]))/\
                                     (100+float(inflation_factors[i]))-1))
            
    # added the rates from the original rates that didn't update
    if len(growth_rates)>len(inflation_factors):
        for i in range(len(growth_rates)-len(inflation_factors)+1,\
                       len(growth_rates)+1):
            update_rates.append(float(growth_rates[i-1]))
            
    return update_rates  # return list of the updated rates

# calculate the retirement savings
def post_retirement(savings, growth_rates, expenses):
    # verifies the input
    if len(growth_rates) == 0:
        return []
    for i in growth_rates:
        if float(i) < -100:
            return
    if savings <= 0 or expenses < 0:
        return

    # Calculate the retirement saving
    # and put the into the new list
    retirement = [savings*(1+float(growth_rates[0])*0.01)-expenses]
    for i in range(1, len(growth_rates)):
        retirement.append(retirement[i-1]*(1+float(growth_rates[i])\
                                           *0.01)-expenses)
        
    return retirement  # return list of the retirement saving in each year

