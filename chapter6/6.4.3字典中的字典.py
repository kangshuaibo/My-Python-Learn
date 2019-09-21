#coding=utf-8
#在字典中将用户名作为键 用户信息存在另一个字典中
print("\n遍历所有用户名")
users = {
	'aeinstein':{
	'first':'albert',
	'last':'einstein',
	'location':'princton',
	},
	'mcurie':{
	'first':'marie',
	'last':'curie',
	'location':'paris',
	},
}

for username,user_info in users.items():	#遍历字典uses 键存username中，关联的字典存user_info中
	print("\nUsername:"+ username)     	#打印用户名

	full_name = user_info['first']+ " " + user_info['last']	 #对每个用户 访问内部字典的键 存在变量中
	location = user_info['location']

	print("\tFull name:" + full_name.title())	#整洁的循环打印出用户 信息
	print("\tLocation:" + location.title())