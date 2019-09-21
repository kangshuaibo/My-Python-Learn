#coding=utf-8
#使用函数int()将input()获取的默认字符串转换为数字
height = input("How tall are you, in inches? ")
height = int(height)	#input默认返回为字符串

if height >= 36:
	print("\nYou're tall enough to ride !")
else:
	print("\nYou'll be able to ride when you're a little older.")