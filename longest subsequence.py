# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 20:51:49 2023

@author: Shubhi Tiwari
"""

import sys

def path(self,ind1,ind2,text1,text2,dp):
        if ind1<0 or ind2<0:
            return 0
        if dp[ind1][ind2]!=-1:
            return dp[ind1][ind2]
             
        if text1[ind1]==text2[ind2]:
             dp[ind1][ind2]=1+self.path(ind1-1,ind2-1,text1,text2,dp)
        else:     
             dp[ind1][ind2]=0+max(self.path(ind1-1,ind2,text1,text2,dp),self.path(ind1,ind2-1,text1,text2,dp))
        
        return dp[ind1][ind2]         
def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        n=len(text1)
        m=len(text2)
        dp=[[-1 for i in range(m)] for i in range(n)]
        ans=self.path(n-1,m-1,text1,text2,dp)
        return ans