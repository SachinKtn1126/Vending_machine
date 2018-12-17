# Title:                            Candy vending machine
# Author:                           Sachin Kotian
# Created date (DD-MM-YYYY):        17-12-2018
# Last modified date (DD-MM-YYYY):  17-12-2018
#
# ABOUT:
# This code acts as a candy vending machine
# It takes input from the user of how many candies he/she wants,
# checks the stock and prints the candies

# initialising the function
candy_stock = 5                                                 # set initial available stock in the vending machine
x = int(input("Please enter the number of candies you want"))   # get user input for number of candies he/she wants
i = 1                                                           # variable to be incremented while executing loop

while candy_stock:
    while i <= x:
        if x > candy_stock:                                     # if the user input is more than the stock
            print("Available stock =" + str(candy_stock))
            # get input from user if her/she wants to get all the candies from stock
            response = input("do you want to take all candies from stock? y: yes OR n: no")
            if response.lower() == "y":
                x = candy_stock                                 # set user input to available candy_stock
                continue
            else:
                break                                           # if user says 'no', end the loop
        else:
            print("candy")
            i += 1

    candy_stock = candy_stock - x                               # update candy_stock
    print("Available stock = " + str(candy_stock))

    if candy_stock != 0:                                        # if stock available, check if user wants more candies
        repeat = input("Repeat? yes or no")
        if repeat.lower() == "y":
            x = int(input("Please enter the number of candies you want"))  # initialise values of variable
            i = 1
        else:
            print("Thank you, visit again")
            break
    else:
        print("\nStock over! Thank you, visit again")
        break



