#coding=utf-8
class Car(object):
	"""一次模拟汽车的简单尝试"""
	def __init__(self,make,model,year):
		"""初始化描述汽车的属性"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""返回整洁的描述信息"""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		"""打印一条指出汽车里程的消息"""
		print("This car has " + str(self.odometer_reading) + " miles on it")

	def update_odometer(self,mileage):
		"""2.通过方法修改属性的值
			再加上额外的功能 禁止把里程表往回调整
		"""
		if mileage >= self.odometer_reading:	#如果传进来的值比原来大 就用新的值
			self.odometer_reading = mileage
		else:
			print("\nYou can't rool back an odometer!")

	def increment_odometer(self,miles):
		"""将里程表增加指定的量"""
		self.odometer_reading += miles



my_new_car = Car('audi','24',2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23	#1.直接修改属性的值 通过实例直接修改
my_new_car.update_odometer(20)	#2.调用方法修改属性的值
#读出里程表的数据
my_new_car.read_odometer()




#。假设我们购买了一辆二手车，且从购买到登记期间增加了100英里的里程
print("\n假设买了一个二手车：")
my_used_car = Car('subaru','outback',2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)	#从购买到使用增加了100
my_used_car.read_odometer()



#类的继承
print("\n类的继承：")
class ElectricCar(Car):	#定义子类要在括号中指定父类名称
	"""电动汽车的独特之处"""
	def __init__(self,make,model,year):	#接受创建Car实例的所需信息
		super(ElectricCar,self).__init__(make,model,year)	#连接父类和子类 调用父类的方法init 包含父类的所有属性
		self.battery_size = 70	#初始化电动汽车的特有属性

	def describe_bettery(self):#添加电动车的特有方法
		"""打印描述电池容量的信息"""
		print("this car has a " + str(self.battery_size) + "-KWh battery")

my_tesla = ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())	#继承了原来类的属性
my_tesla.describe_bettery()

