def sandwich_toppings(*toppings):
    """Accepts a list of toppings someone wants on a sandwich"""
    print("\nMaking a sandwich with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


sandwich_toppings('Honey glazed turkey', 'Lettuce', 'Tomato', 'Mayo', 'Onions', 'American cheese')
sandwich_toppings('Roast beef', 'Colby jack cheese', 'Lettuce', 'Tomato', 'Mayo') 
sandwich_toppings('Fried chicken', 'Lettuce', 'Tomato', 'American cheese')