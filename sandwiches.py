#sandwich maker

import pyinputplus as pyip


def sandwich():
    cost = 0
    print("Welcome to the Sandwich shop. I will now take your order.")
    #bread:
    print("What type of bread would you like? ")
    bread = pyip.inputMenu(["Wheat", "White", "Sourdough"], numbered=True)
    cost += 1.50
    #protein:
    print("What type of protein would you like? ")
    protein = pyip.inputMenu(["Chicken", "Turkey", "Ham", "Tofu"])
    cost += 2.00
    #ifcheese:
    ask_cheese = "Would you like cheese on your sandwich? "
    cheese = pyip.inputYesNo(ask_cheese)
    if cheese == "yes":
        cheese_type = pyip.inputMenu(["Cheddar", "Swiss", "Mozzarella"])
        cost += 1.00
    else:
        pass
    mayo = pyip.inputYesNo("Would you like mayo on your sandwich? ")
    if mayo == "yes":
        cost += 0.25
    else:
        pass
    mustard = pyip.inputYesNo("Would you like mustard on your sandwich? ")
    lettuce = pyip.inputYesNo("Would you like lettuce on your sandwich? ")
    if lettuce == "yes":
        cost += 0.25
    else:
        pass
    tomato = pyip.inputYesNo("Would you like tomato on your sandwich? ")
    if tomato == "yes":
        cost += 0.25
    else:
        pass
    howmany = pyip.inputInt("How many sandwiches do you want?", min=1)
    total_cost = (howmany * cost)
    return("Your total is " + str(total_cost) + ".")



    #if extras:
    #howmany:

print(sandwich())

