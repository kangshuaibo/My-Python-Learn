#coding=utf-8
#使用break退出循环
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"
#break循环 不需要初始
while True:	#这样程序不断运行
	city = input(prompt)

	if city == 'quit':
		break	#直到遇到break跳出循环
	else:
		print("I'd love to go to " + city.title() + "!")