#Writing clear prompts 
name = input("Please enter your name: ")
print(f"\nHello, {name}!")

#Adding aditional text to a prompt
prompt = "If you tell me who you are we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")

age = input("How old are you?")
