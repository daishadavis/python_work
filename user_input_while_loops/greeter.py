#Writing clear prompts 
#name = input("Please enter your name: ")
#print(f"\nHello, {name}!")

#Adding aditional text to a prompt
#prompt = "If you tell me who you are we can personalize the messages you see."
# += "\nWhat is your first name? "

#name = input(prompt)
#print(f"\nHello, {name}!")

#age = input("How old are you?")

#def greet_user(username):
    #"""Display a simple greeting."""
    #print(f"Hello, {username.title()}!")##

#greet_user('jesse')

#def get_formatted_name(first_name, last_name):
    #"""Return a full name, neatly formatted"""
    #full_name = f"{first_name} {last_name}"
    #return full_name.title()

#This is an infinite loop
#while True:
    #print("\nPlease print your name:")
    #print("(enter 'q' at any time to quit)")
    #f_name = input("First name: ")
    #if f_name == 'q':
        #break
    #l_name = input("Last_name: ")
    #if l_name == 'q':
        #break

    #formatted_name = get_formatted_name(f_name, l_name)
    #print(f"\nHello, {formatted_name}!")

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)