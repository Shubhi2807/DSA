# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 19:07:23 2023

@author: Shubhi Tiwari
"""

arr=[1 ,3, 5, 8, 9, 2, 6, 7, 6, 8, 9]   
n=len(arr)
def min_jump(arr,n):   	    
   count=0
   num=0
   i=0 
   while( i<n):
       if arr[i]==0:
           return-1
       elif  arr[i]<n:
           
           i=arr[i]
           count=arr[i]
           print(count)
           print(i)
           num=num+1
   return (num)
#arr=[1,3,5,8,9,2,6,7,6,8,9] 
print(min_jump(arr, n))
	            
          