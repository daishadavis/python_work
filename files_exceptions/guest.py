guest = input("What is your name?: ")

filename = 'files_exceptions/guest.txt'

with open(filename, 'w') as file_object:
    file_object.write(f"{guest}\n")