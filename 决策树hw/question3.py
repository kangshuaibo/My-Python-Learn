#coding=utf-8

#在2中不在1中
def SumIfNot(list1,list2):
	inter = list(set(list2).difference(set(list1)))
	sum = 0
	for i in inter:
		sum += i
	return sum

#脱掉嵌套列表的外衣 递归方法
def flat(nums):
    res = []
    for i in nums:
        if isinstance(i, list):	#判断两个类型是否相同
            res.extend(flat(i))
        else:
            res.append(i)
    return res


list1 = [[[1],[2]]]
list2 = [[[1],[2]],[[4],[5]],11,[3]]
#print(flat(list1))
#print(flat(list2))

#输出在嵌套列表2中 却不在嵌套列表1中的元素的和
result=SumIfNot(flat(list1),flat(list2))
print(result)

