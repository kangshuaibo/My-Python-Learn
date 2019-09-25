#coding=utf-8
print("\n导入的类：")
from car import Car 	#从car.py导入Car类

my_new_car = Car('audi','24',2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()