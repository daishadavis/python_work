#motorcycles = ['honda', 'yasmaha', 'suzuki']
#print(motorcycles)

#motorcycles[0] = 'ducati'
#print(motorcycles)

#motorcycles = ['honda', 'yasmaha', 'suzuki']
#motorcycles.append('ducati')
#print(motorcycles)

#motorcycles = []
#motorcycles.append('honda')
#motorcycles.append('yamaha')
#motorcycles.append('suzuki')
#print(motorcycles)

#motorcycle = ['honda', 'yasmaga', 'suzuki']
#motorcycle.insert(0, 'ducati')
#print(motorcycle)

#motorcycle = ['honda', 'yamaha', 'suzuki']
#print(motorcycle)

#del motorcycle[0]
#print(motorcycle)

#motorcycle = ['honda', 'yamaha', 'suzuki']
#del motorcycle[1]
#print(motorcycle)

#motorcycles = ['honda', 'yamaha', 'suzuki']
#print(motorcycles)

#popped_motorcycles = motorcycles.pop()
#print(motorcycles)
#print(popped_motorcycles)

#motorcycles = ['honda', 'yamaha', 'suzuki']
#last_owned = motorcycles.pop()
#print("The last motorcycle I owned was a {}".format(last_owned.title()))

#motorcycles = ['honda', 'yamaha', 'suzuki']

#first_owned = motorcycles.pop(0)
#print("The first motorcycle I owned was a {}".format(first_owned.title())) 

#motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
#print(motorcycles)

#motorcycles.remove('ducati')
#print(motorcycles)

#motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
#print(motorcycles)

#too_expensive = 'ducati'
#motorcycles.remove(too_expensive)
#print(motorcycles)
#print("{} is too expensive for me.".format(too_expensive.title()))


guess_list = ['Elon Musk', 'Bill Gates', 'Jay Z']
print("Welcome to my dinner party{}".format(guess_list))
print()

print("{} can't make it to the party".format(guess_list[2]))#adding who won't be coming 
del guess_list[2]#removing the person who won't be coming
print()

guess_list.insert(2, "Allen Turing")#adding the person that will be coming
print("Welcome to my dinner party {}".format(guess_list))#update of who will be coming
print()

print("We have found a bigger table for people to join us.")
print()

guess_list.insert(0, "Sheldon Cooper")
guess_list.insert(1, "Amy Farrah Folwer")
guess_list.append("Penny")

print("Welcome to my dinner party{}".format(guess_list))
print()

print("I can only invite two people")#printing only two people can come to the party

guess_list.pop(0)#Removing sheldon from the list
print("I'm sorry Sheldon you can't come")
guess_list.pop(1)#Removing amy from the list
print("I'm sorry Amy you can't come")
guess_list.pop(0)#Removing Elon from the list
print("I'm sorry Elon you can't come")
guess_list.pop(1)#Removing bill gates from the list
print("I'm sorry Bill you can't come")

print("{0} and {1} are still invited to the party".format(guess_list[0], guess_list[1]))
del guess_list[0]#deleting both litems off the list
del guess_list[0]

print(guess_list)

motorcycle = ['honda', 'yamaha', 'suzkui']
print(motorcycle[2])


motorcycle =['honda', 'yamaha', 'suzkui']
print(motorcycle[-1])
count_motorcycle = len(motorcycle)
print(count_motorcycle)








