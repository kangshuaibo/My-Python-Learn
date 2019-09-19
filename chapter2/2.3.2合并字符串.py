#coding=utf-8
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

#直接输出拼接
print("Hello"+" "+last_name)

#调用方法首字母大写 把字符串存到变量中
message = "Hello,"+full_name.title()+"!"
print(message)