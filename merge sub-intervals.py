# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 21:58:57 2023

@author: Shubhi Tiwari
"""

intervals = [[1,3],[2,6],[8,10],[15,18]]
def merge(intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        #print(intervals)
        ans=[]
        ans.append(intervals[0])
        k=0
        for j in range(1,len(intervals)):
            
           #print(ans[k][1],"ans")
           #print(intervals[j][0])
           if intervals[j][0] <= ans[k][1]:
               
               #print(intervals[j][1])
               #print(ans[k][1])
               if intervals[j][1] < ans[k][1]:
                  ans[k][1]=ans[k][1]
               else:
                   ans[k][1]=intervals[j][1]
                   
           else:
               ans.append(intervals[j])
               k=k+1    
                  
        return(ans)
                  
                

print(merge(intervals))             