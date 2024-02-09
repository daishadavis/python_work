from pickle import FALSE, TRUE


banned_users =['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title}, you can post a response if you wish.")

#Boolean Expressions
game_active = TRUE
can_edit = FALSE


car = 'subaru'
print("Is car =='subaru'? I predict true.")
print(car == 'subaru')

print("\nIs car == 'audi' I predict false")
print(car == 'audi')

food = 'burger'
print("Is food == 'burger'? I predict true")
print(food == 'burger')

print("\nIs food == 'phone'? I predict false")
print(food == 'phone')

animal = 'bear'
print("Is animal == 'bear'? I predict true")
print(animal == 'bear')

print("\nIs animal == 'red'? I predict false")
print(animal == 'red')

color = 'purple'
print("Is color == 'purple'? I predict true")
print(color == 'purple')

print("\nIs color == 'sandwich'? I predict false")
print(color == 'sandwich') 

car = 'tesla'
print(car == 'tesla') 
