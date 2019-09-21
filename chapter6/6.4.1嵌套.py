#coding=utf-8
#字典列表 创建一个外星人列表 每个外星人都是一个字典
alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}

aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
	print(alien)


#用随机函数range()生成30个外星人
print("\n随机产生30个外星人")
aliens = []	#创建一个储存外星人的空列表
for alien_number in range(30):	#循环30次 产生30个外星人
	new_alien = {'color':'green','point':5,'speed':'slow'}
	aliens.append(new_alien)	#每生产一个 就依次添加到列表

for alien in aliens[:5]:	#只打印从开始到5
	print(alien)
print("...")	#后面就省略了

print("Total number of aliens :" + str(len(aliens)))	#len()函数求出列表长度

#前三个外星人变成黄色 速度为中等 值10个点
print("\n前三个外星人修改值:")
for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10

for alien in aliens[0:5]:	#显示前5个外星人
	print(alien)
print("...")

#继续修改 将黄色的外星人 改为移动速度快 且值15个点的红色外星人
print("\n将黄色修改为速度快：")
for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15

for alien in aliens[0:10]:
	print(alien)
print("...")