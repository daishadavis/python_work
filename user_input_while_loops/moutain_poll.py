responses = {}

#Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    #Prompt for the person's name and reponse.
    name = input("\nWhat is your name? ")
    response = input("Which moutain would you like to climb someday? ")

    #Store response in the dictionary.
    responses[name] = response

    #Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no)")
    if repeat == 'no':
        polling_active = False

#Polling is complete. Show result.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like climb {response}.")