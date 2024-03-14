filename1 = 'files_exceptions/cats.txt'
filename2 = 'files_exceptions/dogs.txt'

print("Cats:")
try:
    with open(filename1, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    pass
else:
    print(contents)

print("\nDogs: ")
try:
    with open(filename2, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    pass
else:
    print(contents)