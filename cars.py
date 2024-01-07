#Sorting cars into aplhabetical order
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

#Sorting cars in reverse order
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("Here is the original list again:")
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

#Switches the order of the list
cars.reverse()
print(cars)

#returning the numbers of items in a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
x = len(cars)
print(x)

from tkinter.font import names


cities = ['peru', 'paris', 'london', 'spain', 'japan']
print(cities)
print(sorted(cities))
print(cities)
print(sorted(cities, reverse=True))
print(cities)
cities.reverse()
print(cities)
cities.sort()
print(cities)
cities.sort(reverse=True)
print(cities)

inviations = ['Elon Musk', 'Bill Gates', 'Jay Z']
count_inviations = len(inviations)

print("{} people will be coming to dinner tonight".format(count_inviations))

cities = ['paris', 'london', 'africa','toyoko', 'australia']

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
#checking the value of car 

car = 'audi'
if car == 'audi':
    print(car)
#checking for equality 

names = ['allen', 'teddy', 'ray']
for name in names:
    print("Hello {}".format(name))
