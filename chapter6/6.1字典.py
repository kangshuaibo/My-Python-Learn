#coding=utf-8
alien_0 = {'color':"green",'points':5}	#字典alien_0储存了外星人的颜色和点数
print(alien_0['color'])			#指定键 来访问字典中的值
print(alien_0["points"])

#假如玩家射杀了外星人
print("\n假如射杀了外星人:")
alien_0 = {'color':'green','points':5}	#首先定义字典
new_points = alien_0['points']		#从字典中获取键points的值	储存在新变量new_points中
print("You just earned " + str(new_points) + " points！")		#将数字转化成字符串 打印消息

#添加 键-值 对
print("\n向字典中添加xy:")
alien_0 = {'color':'green','points':5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print("添加后：")
print(alien_0)

#创建一个空字典
print("\n创建空字典后添加：")
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)


#修改字典中的值
print("\n修改字典中的值：")
alien_0 = {'color':'green'}
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'	#直接修改键的值
print("The alien is now " + alien_0['color'] + "." )


#以不同速度移动的外星人的位置进行跟踪
print("\n确定外星人移动多远:")
alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
print("Original x_position：" + str(alien_0['x_position']))
#向右移动外星人
#据外星人当前速度决定将其移动多远
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3
#新位置等于老位置加上增量
alien_0['x_position'] = alien_0['x_position'] = x_increment
print("New x_position:" + str(alien_0['x_position']))

