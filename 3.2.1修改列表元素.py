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


