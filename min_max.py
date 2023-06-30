# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 19:53:13 2023

@author: Shubhi Tiwari
"""

N=int(input("ENTER N:"))
arr=[]
print("arr element:")
for i in range(N):
    a=int(input())
    arr.append(a)
print(arr)    

min_ele=[]
max_ele=[]

def min_max_element(min_index,max_index,arr):
    if N==1:
        min_ele=arr[min_index]
        max_ele=arr[max_index]
    elif N==2:
        if arr[min_index]>arr[max_index]:
            min_ele=arr[max_index]
            max_ele=arr[min_index]
        else:
            min_ele=arr[min_index]
            max_ele=arr[max_index]
    else:
        mid=int((min_index+max_index)/2)
        max_ele,min_ele=min_max_element(min_index,mid,arr)
        
        