#coding=utf-8
class Dog():
	"""一次模拟小狗的简单尝试"""
	def __init__(self,name,age):	#__init__是一种特殊的方法 每当根据Dog类创建新实例时 会自动运行
		"""初始化属性name和age"""
		self.name = name
		self.age = age

	def sit(self):
		"""模拟小狗被命令时蹲下"""
		print(self.name.title() + " is now sitting.")

	def roll_over(self):
		"""模拟小狗被命令时打滚"""
		print(self.name.title() + "rolled over")
 
my_dog = Dog('while',6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + "years old.") 

my_dog.sit()
my_dog.roll_over()