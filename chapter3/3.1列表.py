#coding=utf-8
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles[0].title()) #输出第一个元素 方法titile()大写每个单词

print(bicycles[1])
print(bicycles[3])

print(bicycles[-1]) #指定-1返回列表的最后一个元素
print(bicycles[-2]) #指定-2返回列表倒数第二个元素

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)