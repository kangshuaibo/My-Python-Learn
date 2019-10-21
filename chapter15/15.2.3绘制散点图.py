#coding=utf-8
#使用函数scatter() 向它传递一对x和y坐标，在指定位置绘制一个点
import matplotlib.pyplot as plt 

plt.scatter(2,4,s=200)

#设置图表标题并给坐标轴加上标签
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of value",fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis='both',which='major',labelsize=14)	
#which一共3个参数['major' ， 'minor'，'both'] 
#默认是major表示主刻度，后面分布为次刻度及主次刻度都显示。
plt.show()
