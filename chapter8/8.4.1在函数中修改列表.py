#coding=utf-8
#题目：需要打印的设计存储在一个列表中，打印后移到另一个列表中

#首先创建一个列表，其中包含一些要打印的设计
unprinted_designs = ['iphont case','robot pendant','dodecahedron']
completed_models = []

#模拟打印每个设计，直到没有未打印的设计为止
#打印每个设计后，都将其移动到列表completed_models中
while unprinted_designs:
	current_design = unprinted_designs.pop()

	#模拟根据设计制作3D打印模型的过程
	print("Printing model: " + current_design)
	completed_models.append(current_design)

#显示打印好的所有模型
print("\nThe following models have been printed:")
for completed_model in completed_models:
	print(completed_model)



#变成两个函数处理以上
#负责处理打印设计工作
def  print_models(unprinted_designs,completed_models):
	"""
	模型打印每个设计，直到没有未打印的设计为止
	打印每个设计后，都将其移到列表completed_models中
	"""

	while unprinted_designs:
		current_design = unprinted_designs.pop()

		#模拟根据设计制作3D打印模型的过程
		print("Pringing model:" + current_design)
		completed_models.append(current_design)

#打印了哪些设计
def show_completed_models(completed_models):
	"""显示打印好的所有模型"""
	print("\nThefollowing models have been printed:")
	for completed_model in completed_models:
		print(completed_model)

unprinted_designs = ['iphone case','pendant','dodecahedron']
completed_models =[]

	print_models(unprinted_designs,completed_models)
	show_completed_models(completed_models)

