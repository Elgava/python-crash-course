from electric_car import ElectricCar as EC
from car_class import Car as C
import battery

my_tesla = EC('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.get_range()

my_nissan = C('nisan', 'GTR', 2020)
print(my_nissan.get_descriptive_name())