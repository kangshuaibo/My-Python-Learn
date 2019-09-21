#coding=utf-8
#将列表储存在字典
print("\n储存所点披萨信息")
pizza = {
	'crust':'thick',
	'toppings':['mushrooms','extra cheese'],	#列表储存到字典中
}
#显示所点披萨的基本信息
print("You ordered a " + pizza['crust'] + "-crust pizza" + "with the following toppings:") #显示字典
for topping in pizza['toppings']: #显示列表
	print("\t" + topping)	#隔行显示


#在字典中嵌套一个列表
print("\n用一个循环遍历字典 另一个遍历列表:")
favorite_languages = {
	'jen':['python','ruby'],
	'sarah':['c'],
	'edward':['ruby','go'],
	'phil':['python','haskell'],
}
for neme,languages in favorite_languages.items():
	print("\n" + neme.title() + "'s favorite languages are:")
	for language in languages:
		print("\t" + language.title()) #隔行输出