# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 17:00:38 2023

@author: Shubhi Tiwari
"""

def arrange_0_1_2(arr):
    low=0
    mid=0
    high=len(arr)-1
    for i in range(len(arr)):
       if arr[mid]==0:
           arr[mid],arr[low]=arr[low],arr[mid]
           low=low+1
           mid=mid +1
       elif arr[mid]==1:
           mid+=1
       else :
           arr[mid],arr[high]=arr[high],arr[mid]
           high-=1
    return(arr)       
arr=[0,1,2,0,1,2]           
print(arrange_0_1_2(arr))      