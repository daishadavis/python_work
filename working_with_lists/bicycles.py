#Accessing elements in a list using index
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title()) 

#example of 1 and 3 index
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1])
print(bicycles[3])

#example of -1 index
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])

#using individual values from a list
bicycles = ['trek', 'connondale', 'redline', 'specialized']
message = "My first bicycle was a {}".format(bicycles[0].title())
print(message)

names = ['gabby', 'ella', 'carlos', 'emily']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

print("Hello {} I'm so happy to see you!".format(names[0]))
print("Hello {} I'm so happy to see you!".format(names[1]))
print("Hello {} I'm so happy to see you!".format(names[2]))
print(f"Hello {names[3].title()} I'm so happy to see you!")

transportation = ['car', 'motorcycle', 'plane']
print("My {} is the most expensive thing I own".format(transportation[0]))
print("{} are my favorite mode of transportation".format(transportation[1]))
print(f"I would love to fly an {transportation[2].title()} one day.")