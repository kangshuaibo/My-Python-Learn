#coding=utf-8
#9.5导入python标准库
from collections import OrderedDict	#导入排序类
favorite_language = OrderedDict()	#创建一个实例 是一个排序的空字典

favorite_language['jen'] = 'python'
favorite_language['sarah'] = 'c'
favorite_language['edward'] = 'ruby'
favorite_language['phil'] = 'python'

for name,language in favorite_language.items():	#返回可遍历的(键, 值) 元组数组。
	print(name.title() + "'s favorite language is " + language.title() + ".")