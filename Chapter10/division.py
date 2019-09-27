#coding=utf-8
try:
	print(5/0)
except ZeroDivisionError:
	print("You can't divide by zero")

#一个除法运算的简单计算器
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit")

while True:	#条件为true 内有break
	first_number = input("\nFirst number:")
	if first_number == 'q':
		break

	second_number = input("second_number")
	if second_number =='q':
		break

	try:
		answer = int(first_number)/int(second_number)
	except ZeroDivisionError:
		print("You can't divide by 0!")
	else:
		print(answer)