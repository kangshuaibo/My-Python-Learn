#coding=utf-8
#结合使用位置实参和任意数量实参数
#将任意实参要放到最后
def make_pizza(size,*toppings):
	"""概述要制作的披萨"""
	print("\nMaking a " + str(size) +" -inch pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)

make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','exter cheese')
