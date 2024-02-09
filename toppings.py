requested_toppings = 'mushrooms'

if requested_toppings != 'anchovies':
    print("Hold the anchovies")

age = 18
print(age == 18)

print(age == 19)
print(age > 21)
print(age <= 21)
print(age > 21)
print(age >= 21)

age_0 = 22
age_1 = 18

if age_0 >= 21 and age_1 >=21:
    print("True")
    

if age_0 >= 21 or age_1 >= 21:
    print("True")

requested_toppings = ['mushrooms', 'onions', 'pineapple']

print('mushrooms' in requested_toppings)


print('pepperoni' in requested_toppings)
    

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinsihed making your pizza")

alien_color = 'red' 

if alien_color == 'green':
    print("You earned 5 points")
elif alien_color == 'yellow':
    print("You earned 10 points")
elif alien_color == 'red':
    print("You earned 15 points")


age = 3

if age < 2:
    print("Your a baby")
elif age == 2 or age < 4:
    print("Your a toddler")
elif age == 4 or age < 13:
    print("Your a kid")
elif age == 13 or age < 20:
    print("Your a teenager")
elif age == 20 or age < 65:
    print("Your an adult")
else:
    print("Your an elder")

favorite_fruits = ['apple', 'banana','pineapple']

if 'apple' in favorite_fruits:
    print("You really like apples!")
if 'oranges' in favorite_fruits:
    print("You really like oranges!")
if 'pineapple' in favorite_fruits:
    print("Youe really like pineapples!")
if 'grapes' in favorite_fruits:
    print("You really like grapes!")
if "banana" in favorite_fruits:
    print("You really like bananas!")

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping == 'green peppers':
            print("Sorry, we are out of green peppers right now")
        else:
            print(f"Adding {requested_topping}")

    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plan pizza?")


available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")

