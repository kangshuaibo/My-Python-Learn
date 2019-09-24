#coding=utf-8
#传递列表
def greet_users(names):
	"""向列表中的每一位用户都发出简单的问候"""
	for name in names:	#从列表中依次访问每个元素
		msg = "Hello, " + name.title() + "!"
		print(msg)

username = ['hannah','ty','margot']	#是一个列表
greet_users(username)	#调用函数 向其中传递参数（列表）