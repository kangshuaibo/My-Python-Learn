#coding=utf-8
#简单的if语句只有一个测试和一个操作
age = 19
if age>=18:
	print("You are old enough to votel!")
	print("Have you registered to vote yet?")
else:
	print("Sorry, you are too young to vote.")
	print("Please register to vote as soon as you turn 18!")


#if-elif-else结构
print("\n多个条件if语句：")
age = 12
if age<4:
	print("You admission cost is $0.")
elif age < 18:
	print("Your admission cost is $5.")
else:
	print("Your admission cost is $10.")

#化简上述代码
print("化简代码：")
age = 12

if age < 4:
	price = 0
elif age < 18:
	price=5
else:
	price = 10

print("Your admission cost is $" + str(price) + ".")


#使用多个elif代码块
print("使用多个代码块")
age = 12
if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age < 65:
	price = 10
elif age >= 65:
	price = 5

print("Your admission cost is$" + str(price) + ".")


#if测试多个条件
print("\n测试多个条件：")
requested_toppings = ['mushrooms','extra cheese']
if 'mushrooms'in requested_toppings:
	print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:	#没有这个 不执行
	print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
	print("Adding extra cheese.")
print("@Finished making your pizza!")

#elif通过一个后其余不执行
print("\n测试elif多个条件")
requested_toppings = ['mushrooms','extra cheese']
if 'mushrooms'in requested_toppings:	#这个成功了 其他的不执行了
	print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:	
	print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
	print("Adding extra cheese.")
print("@Finished making your pizza!")

