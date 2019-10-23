import numpy as np
import pandas as pd
from math import log  
# step1 自定义信息熵计算函数，用于计算数据集的信息熵

"""
建立一个字典，对数据集各数据的类别计数，
从而计算各类别出现频率(作为概率pi)，
最后调用信息熵公式计算 H(D)=-求和(pi*logpi)
"""

def calEntropy(dataset):
    n=len(dataset)
    labelCounts={}
    
    #对数据集各数据的类别计数
    for data in dataset:
        datalabel=data[-1] #取data最后一列，类别列
        if datalabel not in labelCounts.keys():
            labelCounts[datalabel]=0
        labelCounts[datalabel]+=1
    entropy=0.0
    
    #计算各类别出现频率(作为概率pi),调用信息熵公式计算 H(D)=-求和(pi*logpi)
    for key in labelCounts.keys():
        prob=float(labelCounts[key])/n
        entropy -= prob*log(prob,2)
    return entropy

#step2 自定义数据划分函数，用于根据指定特征的指定取值，划分数据集
"""
输入：数据集、特征所在列索引、特征取值
输出：满足指定特征等于指定取值的数据子集
"""
def splitDataset(dataset,index,value):
    subDataset=[]
    for data in dataset:
        if data[index]==value:
            #抽取除了data[index]的内容(一个特征用于计算其对数据集的经验条件熵时，不需要此特征在子数据集中)
            splitData=data[:index] #取索引之前的元素
            splitData.extend(data[index+1:]) #再合并索引之后的元素
            subDataset.append(splitData)
    return subDataset

#step3~6 选择信息增益最大的特征作为数据集划分特征
"""
输入：数据集
输出：该数据集的最佳划分特征
"""
def chooseFeature(dataset):
    #初始化
    numFeature=len(dataset[0])-1 #因为最后一列是类别
    baseEntropy=calEntropy(dataset) #H(D)
    bestInfoGain=0.0
    bestFeatureIndex=-1
    
    #创建特征A各取值a的列表
    for i in range(numFeature):
        featureList=[data[i] for data in dataset]
        uniqueValue=set(featureList)
        empEntropy=0.0 #初始化特征A对数据集D的经验条件熵H(D|A)
        
        #计算特征A各取值a的信息熵H(Di)和样本概率|Di|/|D|，并相乘
        for value in uniqueValue:
            subDataset=splitDataset(dataset,i,value) #(列索引为i的特征)特征A取value值所划分的子数据集
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
    classCount={}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote]=0
        classCount[vote]+=1
    
    #对classCount按value降序排序
    sortedClassCount=sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0] #返回类别最大的类别名

"""
输入：数据集(list类型)，数据集特征列表(按在数据集的位置排序)(list类型)
输出：该数据集的决策树
思路：【递归】
    1. 若数据集属于同一类，则返回该类别，划分停止
    2. 若数据集所有特征已经遍历，返回当前计数最多的类别为该结点类别，划分停止
    3. 否则继续分支，调用chooseFeature()函数，选择当前数据集最优特征
    4. 遍历当前最优特征各属性值，划分数据集，并递归调用自身createTree()构建子数据集的决策树
    5. 完成
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
        subData=splitDataset(dataset,bestFeatureIndex,value) 
        desitionTree[bestFeature][value]=createTree(subData,subFeatureLabels)
    return desitionTree
def main():
	data_input=pd.read_csv(r"data.txt",sep=" ")
	data_input_list = np.array(data_input).tolist()
	features = data_input.columns.tolist()[0:-1]
	my_tree = createTree(data_input_list,features)
	print (my_tree)

if __name__  == "__main__":
	main()