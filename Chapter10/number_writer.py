#coding=utf-8
import json

numbers = [2,3,5,7,11,13]

filename = 'numbers.json'	#创建一个文件
with open(filename,'w') as f_obj:	#作为一个对象打开
	json.dump(numbers,f_obj)	#把列表存到对象