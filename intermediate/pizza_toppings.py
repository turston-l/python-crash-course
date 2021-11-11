topping_added = ''

while True:
    
    topping_added = input('Add a pizza topping: \nOr press quit to exit.')
    if topping_added == 'quit':
        break
    else:
        print(f'You have added {topping_added}')