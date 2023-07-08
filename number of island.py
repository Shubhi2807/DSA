# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 18:41:42 2023

@author: Shubhi Tiwari
"""
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

def traversal(row,cols,vis,grid):
        
        
        
        q=[]
        q.append([row,cols])
        
        nrow=0
        ncol=0
        n=len(grid)
        
        m=len(grid[0])
        
        while(q):
            first=q[0][0]
            
            second=q[0][1]
            
            q.pop(0)
            for i in range(-1,2):
                for j in range(-1,2):
                   
                    nrow=row+i
                    ncol=cols+j
                    
                    if (nrow>=0 and nrow<n and ncol>=0 and ncol<m and grid[nrow][ncol]=="1" and vis[nrow][ncol]=="0"):
                        
                        vis[nrow][ncol]=1
                        q.append([nrow,ncol])




def numIslands(grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        n=len(grid)
        m=len(grid[0])
        vis = [["0"]*m]*n
        count=0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (grid[i][j]=="1" and vis[i][j]=="0"):
                    
                    vis[i][j]="1"
                    count+=1
                    traversal(i,j,vis,grid)
        return count  
print(numIslands(grid))     