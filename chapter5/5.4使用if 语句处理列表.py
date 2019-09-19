#coding=utf-8
#每添加一种配料打印一条消息
requested_toppings = ['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
	print("Adding "+ requested_topping + ".")
print("\nFinished making your pizza!")

#然而 青椒用完了
print("\n然而 青椒用完了：")
requested_toppings = ['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
	if requested_topping == 'green peppers': #青椒用完了
		print("Sorry,we are mout of green peppers right now.")
	else:		#确保其他原料都添加到披萨中
		print("Adding "+requested_topping+ ".")
print("Finished making your pizza!")

#确定列表不是空的
print("\n确定列表不是空的")
requested_toppings = []
if requested_toppings:	#如果不是空的
	for requested_topping in requested_toppings:
		print("Adding"+requested_topping+".")
	print("Finished making your pizza")
else:
	print("Are you sure you want a plain pizza?")

#使用多个列表
print("\n使用多个列表:")
available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']
for requested_topping in requested_toppings:	#顾客点的 披萨店有原料
	if requested_topping in available_toppings:
		print("Adding " + requested_topping+ ".")
	else:
		print("Sorry,we don't have "+ requested_topping +".")
print("@Finished making your pizza")
