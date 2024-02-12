#Store information abour a pizza being ordered
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

#Summarize the order.
print(f"You order a {pizza['crust']}-crust pizza with the folllowing toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")