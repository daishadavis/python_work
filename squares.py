squares = []
for value in range(1, 11):
    square = value ** 2 
    squares.append(square)

print(squares)

squares = []
for value in range(1, 11):
    squares.append(value**2)

print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

squares = [value**2 for value in range(1, 11)]
print(squares)

for value in range(1, 21):
    print(value)

numbers = list(range(1, 1_000_001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

for value in range(1, 20, 3):
    print(value)

for value in range(3, 33, 3):
    print(value)

for value in range(1, 11):
    print("{} cubed is {}".format(value, value**2))

squares = [value**2 for value in range(1, 11)]
print(squares)