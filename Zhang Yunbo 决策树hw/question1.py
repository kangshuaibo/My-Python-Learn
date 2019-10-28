#coding=utf-8

#判断是否是素数
def isprime(num):	#此函数用来判断一个数是否为质数
	if num==1:
		return False
	for i in range(2,num):
		if num % i == 0:
			return False
	return True
	
#脱掉嵌套列表的外衣 递归方法
def flat(nums):
    res = []
    for i in nums:
        if isinstance(i, list):	#判断两个类型是否相同
            res.extend(flat(i))
        else:
            res.append(i)
    return res

#遍历原列表 判断是素数的数 连接到新列表末尾
def readlist_get_prime(original_data):
	final_data = []	
	flated=flat(original_data)
	for i in flated:
		if isprime(i)==True:
			final_data.append(i)
	return final_data

#计算列表有几个素数
def NumberOfPrimes(list):
	length = len(list)
	return length

original_data = [[[1],[2]],[[4],[5],[6]],[[7],[8],[11]],[[2],[7],[7]],23,[7],29]
result=readlist_get_prime(original_data)
result_number = NumberOfPrimes(result)
print(result)
print(result_number)



