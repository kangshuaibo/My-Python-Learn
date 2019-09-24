#coding=utf-8
#预先不知道传递给函数会是什么样的信息
#接受任意数量的 键-值 对
def build_profile(first,last,**user_info):	#以字典的形式保存
	"""创建一个字典，其中包含我们知道的有关用户的一切"""
	profile = {}	#创建一个空字典
	profile['first_name'] = first #字典分别获取值
	profile['last_name'] = last
	for key,value in user_info.items():	#把最后一项参数 所有的值依次循环存到字典
		profile[key] = value
	return profile

user_profile = build_profile('albert','einstein',location = 'princeton', field = 'physics')	#向函数传递参数 返回值存到变量
print(user_profile)

