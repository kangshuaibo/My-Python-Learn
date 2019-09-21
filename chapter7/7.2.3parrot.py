#coding=utf-8
#设置标志
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the prograr. "

active = True #设置一个标志	外有初始
while active:				#中有条件
	message = input(prompt)	#内有增量

	if message == 'quit':	#用户输入quit就退出循环
		active = False
	else:
		print(message)