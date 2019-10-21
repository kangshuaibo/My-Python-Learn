#coding=utf-8
#使用scatter()绘制一系列点
import matplotlib.pyplot as plt 

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]	#遍历x值 计算平方储存到列表

plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolor='none',s=40)	#用c传递根据每个点的y值设置颜色。默认为蓝色点 黑色轮廓 我们删掉轮廓

#设置图表标题并给坐标轴指定标签
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of value",fontsize=14)

#设置每个坐标轴的取值范围
plt.axis([0,1100,0,1100000])	#分别为x坐标0到1100，y坐标0到1100000 给最右边留一个空好看

#设置刻度标记的大小
plt.tick_params(axis='both',which='major',labelsize=14)	
#which一共3个参数['major' | 'minor' | 'both'] 
#默认是major表示主刻度，后面分布为次刻度及主次刻度都显示。
plt.show()