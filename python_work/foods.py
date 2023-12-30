my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

foods = ['pizza', 'falafel', 'carrot cake', 'ice cream', 'hot dog']
print("The first three in the list are:")
for food in foods[:3]:
    print(food.title())

print("\nThree items from the middle of the list are:")
for food in foods[1:4]:
    print(food.title())

print("\nThe last three items in the list are:")
for food in foods[2:]:
    print(food.title())

my_pizzas =['cheese', 'pepperoni', 'beef', 'chicken']
friend_pizzas = my_pizzas[:]

my_pizzas.append('peppers')
friend_pizzas.append('olives')

print("My favorite pizzas are:")
for pizza in my_pizzas[:]:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas[:]:
    print(pizza)

