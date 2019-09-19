#coding=utf-8
#创建列表 并查看整个列表
print("初始列表:")
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)


#修改列表的第一个元素
print("修改列表的第一个元素:")
motorcycles[0] = 'ducati'	
print(motorcycles)


#方法append()在末尾添加元素
print("末尾添加元素:")
motorcycles.append('ducati') 
print(motorcycles)



#	ex：先创建「空」列表 然后用append()语句插入元素
print("创建空表 插入元素:")
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

#方法insert()在列表中插入元素
print("插入元素:")
motorcycles.insert(0,'ducati') #在第一个位置插入元素 其他元素后移
print(motorcycles)

#del语句 从列表中删除元素
print("从列表中删除元素:")
del motorcycles[0]
del motorcycles[2]
print(motorcycles)

#使用方法pop()删除末尾元素 并使用他的值
print("弹出最后一个元素 并记录他的值")
popped_motorcycle = motorcycles.pop() #变量popped_motorcycle记录弹出的值 方法pop()删除末尾元素
print(motorcycles)
print(popped_motorcycle)

#方法pop()指出最新购买的摩托是哪一款
print("最新购买的摩托是哪一款：")
motorcycles = ['honda','yamaha','suzuki']
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")


#用remove()方法 根据值删除元素
print('根据值删除元素honda')
motorcycles = ['honda','yamaha','suzuki']
motorcycles.remove('honda')
print(motorcycles)



#用remove()方法 删除元素并记录
print("删除元素ducati并记录")
motorcycles = ['honda','yamaha','suzuki','ducati']#初始化
print(motorcycles)

too_expensive = 'ducati'			#先记录这个元素
motorcycles.remove(too_expensive)	#再移除
print(motorcycles)
print("\nA " + too_expensive.title()+" is too expensive for me. ")#方法title() 首字母大写显示他的变量








