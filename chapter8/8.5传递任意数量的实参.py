#coding=utf-8
#一个带星号的形参*toppings 不管调用语句提供了多少实参 都生成一个元组
def make_pizza(*toppings):
 	"""概述要制作的披萨"""
	print("\nMaking a pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')