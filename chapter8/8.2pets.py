#coding=utf-8
#传递实参数
def describe_pet(animal_type,pet_name):
	"""显示宠物信息"""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() +".")
#调用函数
describe_pet('hamster','harry')	#调用函数一次
describe_pet('dog','willie')	#又调用了一次 位置实参
describe_pet(pet_name='harry',animal_type='hamster')	#关键字实参数


print("\n定义函数使用默认值：")
def describe_pet(pet_name,animal_type='dog'):
	"""显示宠物信息"""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name = 'willie')	#关键字实参
describe_pet('willie')	#位置实参 依然默认位置1
describe_pet(pet_name='harry',animal_type='hamster')#提供了参数 忽略默认值
