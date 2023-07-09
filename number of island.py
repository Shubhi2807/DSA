# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 18:41:42 2023

@author: Shubhi Tiwari
"""
grid=[["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]

def traversal(row,cols,arr,grid):
        arr[row][cols]="1"
       
        
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
                   
                    nrow=first+i
                    ncol=second+j
                    
                    if (nrow>=0 and nrow<n and ncol>=0 and ncol<m and grid[nrow][ncol]=="1" and arr[nrow][ncol]=="0"):
                        
                        arr[nrow][ncol]="1"
                        q.append([nrow,ncol])
                    



def numIslands(grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        n=len(grid)
        m=len(grid[0])
        count=0
        vis=[]
        arr=[]
        for i in range(n):
            for j in range(m):
                vis.append("0")
            arr.append(vis) 
            vis=[]
           
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (grid[i][j]=="1" and arr[i][j]=="0"):
                    
                    count+=1
                    traversal(i,j,arr,grid)
        return count  
print(numIslands(grid))     