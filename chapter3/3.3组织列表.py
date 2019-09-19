#coding=utf-8
#使用方法sort() 对列表进行永久排序
print("永久排序")
cars=['bmw','audi','toyota','subaru']
cars.sort()	#永久性的修改汽车列表排序motorcycles = ['honda','yamaha','suzuki']
print(cars)

#向方法sort()中「传递参数」 来进行反向排序
print("\n反向排序")
cars.sort(reverse=True)#反向排序 只需要将方法sort()中传递参数
print(cars)

#使用方法sorted() 按特定顺序显示列表 即临时排序
print("\n临时排序")
cars=['bmw','audi','toyota','subaru']
print("1.Here is the original list:")
print(cars)

print("2.Here is the sorted list")
print(sorted(cars,reverse=True))	#显示临时排序

print("3.Here is the original list again:")
print(cars)

#使用方法reverse() 倒着打印列表 并非排序仅倒打
print("\n倒着打印列表")
cars=['bmw','audi','toyota','subaru']
print(cars)
cars.reverse() #仅仅反转列表
print(cars)

#确定列表长度
print("\n确定列表长度")
cars=['bmw','audi','toyota','subaru']
print(cars)
print("长度为："+ str(len(cars)) ) #用len()方法 向其传递参数:列表
