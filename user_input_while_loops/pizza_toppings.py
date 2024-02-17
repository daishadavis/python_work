prompt = "\nWhat topping would you like on your pizza?"
prompt += "\n(Enter 'quit' when you have finished) "

active = True
while True:
    topping = input(prompt)
    
    if topping == 'quit':
        break
    else:
        print(f"We'll add {topping} to your pizza. Is there anything else?")
