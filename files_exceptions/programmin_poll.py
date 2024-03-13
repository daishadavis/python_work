filename = 'files_exceptions/programming_poll.txt'

print("Thank you for taking our survey!")
print("Enter 'q' when your done with your responses.")

while True:
    responses = input("Why do you like programming?: ")

    if responses == 'q':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(f"{responses}\n")