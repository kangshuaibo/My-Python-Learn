#coding=utf-8
def get_formatted_name(first_name,last_name):	
	"""返回整洁的姓名"""
	full_name = first_name + ' ' + last_name
	return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)

#让参数变可选的
print("\n让参数变成可选的")	
def get_formatted_name(first_name,last_name,middle_name=' '):	#把可选参数定义在最后
	"""返回整洁的姓名"""
	if middle_name:	#检查是否有提供中间名
		full_name = first_name + ' ' + middle_name + ' ' +last_name
	else:
		full_name = first_name +' '+last_name
	return full_name.title()

musician = get_formatted_name('join','lee')#调用函数 少传递一个参数
print(musician) 

musician = get_formatted_name('join','hooker','lee')#调用函数 传递完整参数	（若有中间名 必须确保它是最后一个实参）
print(musician)

#返回一个字典
print("\n返回一个字典：")
def build_person(first_name,last_name,age=''):
	"""返回一个字典，其中包含有关一个人的信息"""
	person = {'first':first_name,'last':last_name}
	if age:
		person['age']=age	#在字典中添加
	return person

musician = build_person('jimi','hendrix',27)	#调用函数 传递参数
print(musician)



	