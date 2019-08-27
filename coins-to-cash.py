# Create a function called calc_dollars. In the function body, define a dictionary and store it in a variable named piggyBank. The dictionary should have the following keys defined.
# quarters
# nickels
# dimes
# pennies
# For each coin type, give yourself as many as you like.
# piggyBank = {
#     "pennies": 342,
#     "nickels": 9,
#     "dimes": 32
# }
# Once you have given yourself a large stash of coins in your piggybank, look at each key and perform the appropriate math on the integer value to determine how much money you have in dollars. Store that value in a variable named dollarAmount and print it.

# Given the coins shown above, the output would be 7.07 when you call calc_dollars()

def calc_dollars():
    piggy_bank = {
        "quarters" : 472,
        "nickels" : 33,
        "dimes" : 24,
        "pennies" : 10
    }

    dollar_amount = (piggy_bank["quarters"] / 4) + (piggy_bank["nickels"] / 20) + (piggy_bank["dimes"] / 10) + (piggy_bank["pennies"] / 100)

    print(f'${dollar_amount}')

calc_dollars()

# Now do the reverse. Convert the dollar amount into the coins that make up that dollar amount. The final result is an object with the correct number of quarters, dimes, nickels, and pennies.

# dollarAmount = 8.69

# piggyBank = {
#     "pennies": 0,
#     "nickels": 0,
#     "dimes": 0,
#     "quarters": 0
# }

# # Your magic Python code here
# That should produce the following output.

# >>> print(piggyBank)
# { 'quarters': 34, 'nickels': 1, 'dimes': 1, 'pennies': 4 }

def calc_coins():
    dollar_amount = 8.69

    piggy_bank ={
        "pennies" : 0,
        "nickels" : 0,
        "dimes" : 0,
        "quarters" : 0
    }

    piggy_bank["quarters"] = dollar_amount // .25
    no_quarters = dollar_amount % .25
    piggy_bank["dimes"] = no_quarters // .10
    no_dimes = no_quarters % .10
    piggy_bank["nickels"] = no_dimes // .05
    no_nickels = no_dimes % .05
    piggy_bank["pennies"] = no_nickels // .01

    print(piggy_bank)

calc_coins()



