# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 20:02:19 2023

@author: Shubhi Tiwari
"""
from queue import Queue

V=5
adj=[[2],[3],[4,5],[2],[]]
def topocycle(V,adj):
    vis=0
    ind=[0]*(V)
    q=Queue()
    
    for i in range(V):
        for j in adj[i]:
            ind[j-1]+=1
            
    for i in range(len(ind)):
        if ind[i]==0:
            q.put(i+1)
            
    while(q.qsize()!=0):
       node=q.get()
       vis+=1
       for i in adj[node-1]:
           ind[i-1]-=1
           if ind[i-1]==0:
               q.put(i)
    if vis==V:
        return False
    return True
print(topocycle(V, adj))     
            
    
    
    