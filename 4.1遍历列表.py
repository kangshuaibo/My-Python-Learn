#coding=utf-8
#打印列表中的魔术师
print("打印列表中魔术师")
magicians=['alice','david','carolina']
for magician in magicians: #取出列表magicians中的元素 存在变量magician中
	print(magician)


#对每位魔术师都打印消息
print("\n对于每位魔术师都打印消息")
magicians=['alice','david','carolina']
for magician in magicians:
	print(magician.title() + ", that was a great trick!")


#没缩进的代码都只执行一次
print("\n没缩进的代码都只执行一次")
magicians=['alice','david','carolina']
for magician in magicians:	#冒号容易漏掉
	print(magician.title()+", that was a great trick")
	print("I can't wait to see your next trick,"+ magician.title())
print("@Thank you, everyone. That was a great magic show!")


