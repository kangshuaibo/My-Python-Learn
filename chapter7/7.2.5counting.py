#coding=utf-8
#从1数到10 只打印奇数
current_number = 0	#非break 外一定有初始
while current_number < 10:	#中有条件
	current_number += 1		#内有增量
	
	if current_number %2 == 0:	#遇到偶数 忽略后面的代码 回到循环开头判断是否继续进行
		continue
	print(current_number)