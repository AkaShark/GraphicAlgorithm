#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 在数组中寻找最小的值 返回了最小值的index
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index

# 排序这个数组 从小到大排列
def selectionSort(arr):
    newArray = [] # 定义一个存放新的排序完成的数组的变量
    for i in range(len(arr)):
        smallest = findSmallest(arr) # 得到最小值的index
        newArray.append(arr.pop(smallest)) # 将这个最小值存放入新的数组中去
    return newArray

print(selectionSort([1,2,3,4,7,4,2,1]))



# python 这个数组的这个pop函数传入index 将数组的这个值弹出 可以获取到
# testArry = [1,21,32,123,123]
# print(testArry.pop(0))