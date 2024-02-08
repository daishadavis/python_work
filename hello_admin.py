usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print(f"Hello {username.title()}, would you like to see a status report?")
        else:
            print(f"Hello {username.title()} thank you for loggin in again")
else:
    print("We need to find some users!")


current_users = ['admin', 'sarah', 'jaden', 'amy', 'nathan']

new_users = ['michelle', 'daniel', 'scott', 'jaden', 'louis']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"Hello, {new_user.title()}. The username is already in use, please use a different one.")
    else:
        print(f"Hello {new_user.title()}. This username is available.")


numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")