class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'The restaurant name: {self.restaurant_name}\n')
        print(f'Cuisine type: {self.cuisine_type}\n')

    def open_restaurant(self):
        print(f'The restaurant is open!\n')

restaurant_1 = Restaurant('One', 'Burger')
restaurant_2 = Restaurant('Two', 'Sausage')
restaurant_3 = Restaurant('Three', 'Pie')
print(restaurant_1.describe_restaurant())
print(restaurant_2.describe_restaurant())
print(restaurant_3.describe_restaurant())
