from elec_car import ElectricCar

my_ele_car = ElectricCar('tesla', 'model s', 2019)
print(my_ele_car.get_descriptive_name())

my_ele_car.describe_battery()
my_ele_car.read_odometer()

my_ele_car.update_odometer(23)
my_ele_car.read_odometer()

my_ele_car.increment_odometer(100)
my_ele_car.read_odometer()
