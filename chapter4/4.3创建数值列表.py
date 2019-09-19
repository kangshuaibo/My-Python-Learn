#coding=utf-8
#使用函数range() 生成范围内数字
for value in range(1,5):
	print(value)

#使用list()函数将生成的数字转换为列表
print("\n输出的列表为:")
numbers = list(range(1,6))
print(numbers)

#指定range()的步长
print("\n输出偶数：")
even_numbers = list(range(2,11,2))	#范围2～11直到到达11 每次增加2
print(even_numbers)

#两个星号代表乘方**
print("\n创建列表 包含前10个整数的平方：")
squares=[]
for value in range(1,11):	#依次产生10个数
	square = value**2 	    #计算当前值的平方 结果存到变量square中
	squares.append(square)	#将结果附加到列表末尾
print(squares)

#几个处理数据的函数
print("\n找出最大 最小 和：")
digits = [1,2,3,4,5,6,7,8,9,0]
a=min(digits)
b=max(digits)
c=sum(digits)
print(a,b,c)


#列表解析 将for和创建新元素合并
print("\n使用列表解析创建平方数列表:")
squares = [value**2 for value in range(1,11)]
print(squares)
