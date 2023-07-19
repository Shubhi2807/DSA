# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 09:48:00 2023

@author: Shubhi Tiwari
"""

def path(self,i,j,grid,dp):
        if i==0 and j==0:
            return grid[i][j]
        if i<0 or j<0 :
            return 1000000000
        if dp[i][j]!=-1:
            return dp[i][j]
        up=grid[i][j]+self.path(i-1,j,grid,dp)         
        left=grid[i][j]+self.path(i,j-1,grid,dp)
        dp[i][j]=min(up,left)  

        return dp[i][j]     
def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n=len(grid)
        m=len(grid[0])
        dp=[[-1 for _ in range(m)] for _ in range(n)]
        ans=self.path(n-1,m-1,grid,dp)
        return ans