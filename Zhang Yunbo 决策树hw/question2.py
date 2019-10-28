#脱掉嵌套列表的外衣 递归方法
def flat(nums):
    res = []
    for i in nums:
        if isinstance(i, list):	#判断两个类型是否相同
            res.extend(flat(i))
        else:
            res.append(i)
    return res

#遍历原列表 判断是偶数的数 连接到新列表末尾
def even(original_data):
	final_data = []	
	flated=flat(original_data)
	for i in flated:
		if i%2==0:
			final_data.append(i)
	return final_data

original_data = [[[1],[2]],[[-4],[5],[6]],[[7],[8],[11]],[[2],[7],[7]],23,[7],29]
result=even(original_data)
print(result)
