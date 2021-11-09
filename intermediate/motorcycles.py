motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('bmw')
print(motorcycles)

motorcycles.insert(0, 'toyota')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

last_motorcycle = motorcycles.pop()
print(f'The last motorcycle I owned was a {last_motorcycle.title()}.')

first_motorcycle = motorcycles.pop(0)
print(f'The first motorcycle I owned was a {first_motorcycle.title()}.')

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)
