# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 20:39:16 2023

@author: Shubhi Tiwari
"""
import sys
def path(self,ind,W,wt,val,dp):
        if ind==0:
            if wt[0]<=W:
                return val[0]
            else:    
                return 0
            
        if dp[ind][W] != -1:
            return dp[ind][W]  
        not_take=0+self.path(ind-1,W,wt,val,dp)
        take=-sys.maxsize
        if wt[ind]<=W:
            take=val[ind]+self.path(ind-1,W-wt[ind],wt,val,dp)
        dp[ind][W]=max(take,not_take)
        
        return dp[ind][W]
    #Function to return max value that can be put in knapsack of capacity W.
def knapSack(self,W, wt, val, n):
        dp=[[-1 for j in range(W+1)] for i in range(n)]
        
            
        ans=self.path(n-1,W,wt,val,dp)
        return ans