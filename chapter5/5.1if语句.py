#coding=utf-8
#一个简单的条件判断的例子：
cars = ['audi','bmw','subaru','toyota']
for car in cars:
	if car =='bmw':	#是bmw全部大些
		print(car.upper())
	else:			#不是bmw首字母大写
		print(car.title())


#检查是否不相等
print("\n不相等返回true 打印一句话")
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
	print("Hold the anchovies!")


#检查数字
print("\n答案不正确时打印一条消息：")
answer = 17
if answer !=42:
	print("that is not the correct answer. Please try again!")

#检查是否在列表中
print("\n判断是否在列表中:")
requested_toppings=['mushrooms','onions','pineapple']
if 'mushrooms'in requested_toppings:
	print("YES")
if 'pepperoni'in requested_toppings:
	print("Yes")
else:
	print("NO")


#检查是否 不 在列表中
print("\n判断是否 不在列表中")
banned_users = ['andrew','carolina','david']
user = 'marie'
if user not in banned_users:
	print(user.title()+", you can post a respose if you wish")

