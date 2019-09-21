#coding=utf-8
#一个列表新注册但还没有验证，把他们移动到已经验证的列表

#创建一个待验证用户列表 和一个用于储存已验证用户的空列表
unconfirmed_users = ['alice','brian','candace']
confirmed_users = []

#验证每个用户，直到没有未验证的为止
#移动经过验证的用户
while unconfirmed_users:	#处理列表 一直到空
	current_user = unconfirmed_users.pop()	#弹出一个未验证的

	print("Verifying user:" + current_user.title())	#打印这个未验证的
	confirmed_users.append(current_user)	#放到已经验证的

#显示所有已经验证的用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
	 print(confirmed_user.title())
