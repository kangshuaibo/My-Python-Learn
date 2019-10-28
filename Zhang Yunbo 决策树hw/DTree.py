#coding=utf-8
import numpy as np
import pandas as pd
from math import log  


# step1 计算数据集的信息熵
"""
建立一个字典，对数据集各数据的类别计数，
从而计算各类别出现频率(作为概率pi)，
最后调用信息熵公式计算H(D)=-求和(pi*logpi)
""" 
def calEntropy(dataset):
    n=len(dataset)
    labelCounts={}  #对数据集类别计数的字典
    
    #对数据集各数据的类别计数
    for data in dataset:
        datalabel=data[-1] #取data最后一列（类别列）
        if datalabel not in labelCounts.keys(): #如果最后一列key不在上面那个字典
            labelCounts[datalabel]=0 #把这个key放到字典 并value置0
        labelCounts[datalabel]+=1 #这个key再次出现 就计数

    entropy=0.0
    #计算各类别出现频率(作为概率pi),调用信息熵公式计算H(D)= -求和(pi*logpi)
    for key in labelCounts.keys():
        prob=float(labelCounts[key])/n  #出现的概率是 这个结果出现的次数/总数据
        entropy -= prob*log(prob,2)
    return entropy


#step2 根据特征值划分数据集 返回一个子集
"""
输入：数据集、特征所在列索引、特征取值
输出：除去特征值的数据子集
"""
def devideDataset(dataset,index,value):

    subDataset=[]
    for data in dataset:
        if data[index]==value:
            #提取除了索引以外的 即索引之前和之后的合并数据集
            #一个特征用于计算其对数据集的经验条件熵时，不需要此特征data[index]在子数据集中
            devideData=data[:index] #取索引之前的元素
            devideData.extend(data[index+1:]) #再合并索引之后的元素

            subDataset.append(devideData)   #连接到要返回的数据集 即数据子集(不包含index的数据)
    return subDataset

#step3~6 选择信息增益最大的特征作为数据集划分特征
"""
输入：数据集 调用划分数据集函数
输出：该数据集的最佳划分特征
"""
def chooseFeature(dataset):
    #初始化
    numFeature=len(dataset[0])-1 #因为最后一列是类别
    baseEntropy=calEntropy(dataset) #H(D) 调用信息熵函数
    bestInfoGain=0.0
    bestFeatureIndex=-1
    
    #创建特征A各取值a的列表
    for i in range(numFeature):
        featureList=[data[i] for data in dataset]
        uniqueValue=set(featureList) #创建无序不循环的元素集
        empEntropy=0.0 #初始化特征A对数据集D的经验条件熵H(D|A)
        
        #计算特征A各取值a的信息熵H(Di)和样本概率|Di|/|D|，并相乘
        for value in uniqueValue:
            subDataset=devideDataset(dataset,i,value) #(列索引为i的特征)特征A取value值所划分的子数据集
            prob=len(subDataset)/float(len(dataset)) #计算|Di|/|D|
            empEntropy += prob*calEntropy(subDataset) #H(D|A)
        
        #取信息增益最大的特征为最佳划分特征
        infoGain=baseEntropy-empEntropy #信息增益
        if infoGain>bestInfoGain:
            bestInfoGain=infoGain
            bestFeatureIndex=i
    return bestFeatureIndex

#step7~8 递归构建决策树
def majorClass(classList):
    classCount={}   #给每个类别出现记数
    for item in classList:
        if item not in classCount.keys():
            classCount[item]=0  #没出现过 就放到字典中 并值为0
        classCount[item]+=1 #出现过就记数
    
    #对classCount按value降序排序 operator获取第几个对象的值 sorted可以对list或者iterator进行排序 True为降序
    sortedClassCount=sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0] #返回类别最大的类别名 即讲序排列的第一个

"""
输入：数据集(list类型)，数据集特征列表(按在数据集的位置排序)(list类型)
输出：该数据集的决策树
"""
def createTree(dataset,featureLabels):
    classList=[data[-1] for data in dataset] #取数据集各数据类别
    
    #若数据集属于同一类，则返回该类别，划分停止
    if classList.count(classList[0])==len(classList):
        return classList[0]
    
    #若数据集所有特征已经遍历，返回当前计数最多的类别为该结点类别，划分停止
    if len(dataset[0])==1:
        return majorClass(classList)
    
    #否则继续分支，调用chooseFeature()函数，选择当前数据集最优特征
    bestFeatureIndex=chooseFeature(dataset)
    bestFeature=featureLabels[bestFeatureIndex]
    
    #用于存储决策树，字典结构存储树的所有信息，并可体现包含关系
    desitionTree={bestFeature:{}} 
    del(featureLabels[bestFeatureIndex]) #删除已被用于划分数据的特征
    
    #得到当前最优划分特征的各属性值
    featureValues=[data[bestFeatureIndex] for data in dataset]
    uniqueValues=set(featureValues)
    
    #遍历当前最优特征各属性值，划分数据集，并递归调用自身createTree()构建子数据集的决策树
    for value in uniqueValues:
        #得到已删除当前最优划分特征的特征列表,用于递归调用
        subFeatureLabels=featureLabels[:] 
       
        #用当前最优划分特征的指定值分割子数据集，用于递归调用
        subData=devideDataset(dataset,bestFeatureIndex,value) 
        desitionTree[bestFeature][value]=createTree(subData,subFeatureLabels)
    return desitionTree
def main():
	data_input=pd.read_csv(r"data.txt",sep=" ")    #输入数据 数据元素以空格分开
	data_input_list = np.array(data_input).tolist()
	features = data_input.columns.tolist()[0:-1]
	my_tree = createTree(data_input_list,features)
	a=str(my_tree) #把输出的整个转换为字符串类型
	b=convert(a)   #按照题目要求输出为‘（’
	print("("+b+")") 

def convert(str):
	string=str.replace("{","(").replace("}",")").replace(":","").replace("'","")
	return string



if __name__  == "__main__":
	main()