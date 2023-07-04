# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 19:16:58 2023

@author: Shubhi Tiwari
"""
m=3
n=2
def uniquePaths( m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        path=m+n-2
        r=m-1
        res=1
        for i in range(1,r+1,1):
            res=res*((path-r+i)/i)
        return res    
print(uniquePaths( m, n))    