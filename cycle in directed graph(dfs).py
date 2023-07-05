# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 21:22:00 2023

@author: Shubhi Tiwari
"""

from queue import Queue

V=4
adj=[[2],[3],[4],[1]]
def topopath(node,vis,ans,adj):
        vis[node-1]=1
        for i in adj[node-1]:
            topopath(i,vis,ans,adj)
        ans.append(node)    
    #Function to return list containing vertices in Topological order.
def topoSort( V, adj):
        # Code here
        vis=[0]*V
        ans=[]
        for i in range(V):
            if (vis[i]==0):
                topopath(i,vis,ans,adj)
        ls=[]
        for i in range(len(ans)-1,-1,-1):
            ls.append(ans[i])
            ans.pop()
            
        if len(vis)==V:
            return False
        
        return True
print(topoSort(V, adj))    