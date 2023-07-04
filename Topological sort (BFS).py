# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 22:11:53 2023

@author: Shubhi Tiwari
"""
V=5
adj=[[],[],[3],[1],[0,1],[0,2]]

from collections import deque

    
#Function to return list containing vertices in Topological order.
def topoSort( V, adj):
    # Code here
    ind=[0]*(V+1)
    ans=[]
    for i in range(V+1):
        for j in adj[i]:
            ind[j]+=1 
    
    q=deque() 
    for i in range(len(ind)):
        if ind[i]==0:
            q.append(i)
    
    while(q):
        node=q.popleft()
        ans.append(node)
        for i in adj[node]:
            ind[i]-=1
            if ind[i]==0:
                q.append(i)
    return ans  
print(topoSort(V, adj))