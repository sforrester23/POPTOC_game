# Define functions for POPTOC here

# Define a function that outputs true if number inputted is divisible by 3 and false if it's not
def div_3(number):
    if number%3 == 0:
        return True
    else:
        return False

# Define a function that outputs true if number inputted is divisible by 5 and false if it's not
def div_5(number):
    if number%5 == 0:
        return True
    else:
        return False
# Define a function that outputs, based on the number inputted:
# POPTOC if it's divisible by 3 AND 5
# POP if it's divisible by 3
# TOC if it's divisible by 5
def POPTOC(number):
    if div_3(number) and div_5(number):
        return 'POPTOC'
    elif div_3(number):
        return 'POP'
    elif div_5(number):
        return 'TOC'
    else:
        return 'Neither POP nor TOC'









# Write some pseudo code

# Write a function to check if divisible by 3
# Write a function to check if divisible by 5
# Write a function to check if divisible by 3 AND 5???