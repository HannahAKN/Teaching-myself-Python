#This program is to practice if/elif/else statements. This program will give you the menu of an food truck. It will let you choose Items and then give you the total for your order.
print("Welcome to the Lusty Loot Food Truck!")
print("What can we get for you today?\n\n")

food_item = input("Would you like Pizza or Tacos, Or would you just like to skip to Ice cream? Type the name of the item you want: ")


pizza_size = input("What Pizza size do you want? S or M: ")
pizza_extra_cheese = input("Do you want extra cheese on you pizza? Y for yes, or N for no: ")
pizza_pepperoni = input("Do you want pepperoni? Y or N: ")

taco_type = input("Do you want chicken or beef tacos? Type the name of the preferred meat: ")
taco_number = input("How many tacos do you want? 2, 4 or 6: ")
taco_mix = input(" Do you want all to be the same meet type? Y or N: ")

ice_cream_flavour = input("Do you want Strawberry, Chocolate or vanilla ice cream? Type the name of the flavour: ")
ice_cream_scoops = input("How many scoops do you want? 1, 2 or 3: ")
ice_cream_sprinkles = input("Do you want sprinkles? Y or N: ")
bill = 0

if food_item == "Pizza":
    if pizza_size == "M":
        bill += 20
        print("One medium pizza.")
    else:
        bill += 15
        print("One small pizza.")

    if pizza_extra_cheese == "Y":
        bill += 2
        print("Adding extra cheese!")
    else:
        print("No extra cheese.")
