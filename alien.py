alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Orginal position: {alien_0['x_position']}")

#Move the alien to the right. 
#Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed']== 'medium':
    x_increment = 2
else:
    #This must be a fast alien
    x_increment = 3

#The new positon is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment 

print(f"New position: {alien_0['x_position']}")

del alien_0['speed']
print(alien_0)

#Different kinds of information about one object.
favorite_languages =  {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite programming ;language is {language}")

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(aliens)