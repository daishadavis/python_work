responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat's your name? ")
    response = input("What's your dream vacation? ")

    responses[name] = response

    repeat = input("Would you like to let another person repond (yes/no)? ")
    if repeat == 'no':
        polling_active = False

print("--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()}'s dream vacation is {response.title()}.")