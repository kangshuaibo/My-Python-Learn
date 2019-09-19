#coding=utf-8
#定义元组
print("定义元组 其值不可修改")
dimensions=(200,50)	#定义元组 元组与列表差不多 只是其中元素不可以修改
print(dimensions[0])
print(dimensions[1])

#遍历元组中的所有值
print("\n遍历元组中的值")
dimensions = (200,50)
for dimension in dimensions:
	print(dimension)

#修改元组变量
print("\n虽然不能修改元组， 但可以重新定义这个元组")
dimensions=(200,50)
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)

dimensions = (400,100)	#重新定义元组 一个新的元组储存到变量dimensions中 即可修改元组变量
print("Modifid dimensions:")
for dimension in dimensions:
	print(dimension)