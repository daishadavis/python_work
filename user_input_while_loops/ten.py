number = input("Give me any number you want and I'll tell you if its a multiple of ten. ")
number = int(number)

if number % 10 == 0:
    print("\nThis number is a mulitple of ten.")
else:
    print("\nThis number is not a mulitple of ten.")