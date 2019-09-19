#coding=utf-8
#打印列表的切片
print("打印列表切片：")
players = ['charles','martina','michael','florence','eli']
print("打印原始：")
print(players)	#打印这个列表
print("切片1到3：")
print(players[1:3]) #输出了1 2号元素
print("切片1到4：")
print(players[1:4]) #输出了1 2 3号元素
print("切片开头到4：")
print(players[:4]) #没有指定初始索引 从头开始打印
print("切片2到结尾：")
print(players[2:]) #从第3个开始一直打到末尾
print("切片最后3个:")
print(players[-3:])
print("切片倒数3～倒数1:")
print(players[-3:-1])


#遍历切片
print("\n遍历前3名:")
players = ['charles','martina','michael','florence','eli']
for player in players[:3]:	#范围从开头到3
	print(player.title())

#复制列表 提取从开头到结尾的切片
print("\n复制列表")
my_foods = ['pizza','falafel','carrot cake']
friend_food = my_foods[:]	#省略前后索引 提取从开头到结尾切片

my_foods.append('cannoli')	#为检验确实为两个列表 每个列表附加一个不同的食品
friend_food.append('ice cream')

print("My:")
print(my_foods)

print("Frinds:")
print(friend_food)

#若只是简单的赋值my_foods给friend_foods,就不能得到两个链表
print("\n错误的复制链表")
my_foods = ['pizza','falafel','carrot cake']
friend_food = my_foods #这行不通

my_foods.append('cannoli')	#为了检验还是同一个列表 两个都附加了
friend_food.append('ice cream')

print("My:")
print(my_foods)
print("Friend:")
print(friend_food)


