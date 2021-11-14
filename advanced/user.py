user_name = input('\nEnter your name: \n')

file_object = 'guests.txt'

with open(file_object, 'a'):
    file_object.write('user_name')