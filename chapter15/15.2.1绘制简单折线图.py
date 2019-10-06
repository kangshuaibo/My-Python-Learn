#coding=utf-8
#使用平方数序列1 4 9 16 15来绘制这个图表
import matplotlib.pyplot as plt 


input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]	#默认x轴为0 1 2 3 4
plt.plot(input_values,squares,linewidth=5) #把列表传递给函数plot() 这个函数来绘制图形 参数指定线的宽度

#设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)	#为x y轴设置标题
plt.ylabel("Square of Value",fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis='both',labelsize=14) #设置刻度的样式 实参both同时影响x y轴
plt.show()
