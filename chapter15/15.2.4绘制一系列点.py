#coding=utf-8
#使用scatter()绘制一系列点
import matplotlib.pyplot as plt 

x_value = [1,2,3,4,5]
y_value = [1,4,9,16,25]

plt.scatter(x_value,y_value,s=100)

#设置图表标题并给坐标轴指定标签
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of value",fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis='both',which='major',labelsize=14)	
#which一共3个参数['major' ， 'minor'，'both'] 
#默认是major表示主刻度，后面分布为次刻度及主次刻度都显示。
plt.show()