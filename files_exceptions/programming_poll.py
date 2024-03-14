filename = 'files_exceptions/programming_poll.txt'

print("Enter a reason why you like programming.")
print("Enter 'q' when your done with your responses.")

while True:
    responses = input("Why do you like programming?: ")

    if responses == 'q':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(f"{responses}\n")