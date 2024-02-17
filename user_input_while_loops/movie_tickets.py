prompt = "\nHow old are you?"
prompt += "\n(Type 'quit' to stop)"

active = True

while active:
    age = input(prompt)

    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            price = 0
        elif age < 13:
            price = 10
        else:
            price = 15
        
        print(f"The ticket price is ${price}.")