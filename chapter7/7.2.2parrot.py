#coding=utf-8
#让用户选择何时退出
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
message = ""	#1外有初始变量 只要不是下面条件就行
while message != 'quit':	#中间有条件
	message = input(prompt)	#内有增量（等待用户输入）
	if message !='quit':	#防止打印出quit
	print(message) 	#不管输入什么都直接打印出来