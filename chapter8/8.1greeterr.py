#coding=utf-8
#定义函数
def greet_user():
	"""显示简单的问候语"""
	print("Hello!")
#调用函数
greet_user()	


#向函数传递参数
def greet_user(username):
	"""显示简单的问候语"""
	print("Hello, " + username.title() + "!")
#调用函数并传递参数
greet_user('jesse')