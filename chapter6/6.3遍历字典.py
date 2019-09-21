#coding=utf-8
#遍历所有键-值 对
print("遍历所有键-值 对：")
use_0 = {
	'username':'efermi',
	'first':'enrico',
	'last':'fermi',
}
for key,value in use_0.items():	#函数itmes()返回键值对列表 然后依次存到两个变量中
	print("\nKey:" + key)
	print("Value:" + value)



#储存的是不同人的同一种信息
print("\n遍历不同人的同一种信息：")
favorite_langusages = {
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
}

for name,language in favorite_langusages.items():
	print(name.title() + "'s favorite_langusages is " +language.title() + ".")



#遍历字典中所有的键
favorite_langusages = {
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
}
for name in favorite_langusages.keys():	#只遍历键值 使用函数keys()
	print(name.title())


#使用当前键访问相关联的值
print("\n访问键关联的值：")
favorite_langusages = {	#定义字典
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',	
}
friends = ['phil','sarah']	#定义列表
for name in favorite_langusages.keys():	#循环键 输出每个人的名字
	print(name.title())	#打印键
	if name in friends:	#判断键值是否在指定列表中 （for只包括缩进 可以有空行） 
		print(" Hi " + name.title() + ",I see your favorite language is " + favorite_langusages[name].title() + "!") #打印键相关联的value值


#去定某个人是否接受了调查
print("\n判断是否接受了调查：")
if 'erin' not in favorite_langusages.keys():
	print("Erin,please take our poll!")


#按顺序遍历字典中所有的键
print("\n按顺序遍历字典中所有的键：")
for name in sorted(favorite_langusages.keys()):
	print(name.title() + ",thank you for taking the poll.")


#遍历字典中所有的值
print("\n遍历字典中所有的值")
favorite_langusages = {
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'pill':'python',
}
print("The following languages have been mentioned:")
for language in favorite_langusages.values():
	print(language.title())

#剔除重复项 向集合set()传递参数 提取不同的语言
print("\n剔除重复项")
print("The following languages have been mentioned:")
for language in set(favorite_langusages.values()):
	print(language.title())











