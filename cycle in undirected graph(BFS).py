# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 21:58:13 2023

@author: Shubhi Tiwari
"""

from typing import List
from collections import deque 

    
def detectcycle(node,vis,adj):
    
    vis[node]=1
    q=deque()
    q.append({node,-1})
    while(q):
        node=q.popleft().first
        parent=q.popleft().second
        
        
        for i in adj[node]:
            if vis[i]==0:
                vis[i]=1
                q.append({i,node})
            elif parent!=i:
                return True
    return False        
        
    
    
#Function to detect cycle in an undirected graph.
def isCycle( V: int, adj: List[List[int]]) -> bool:
       	    vis=[0]*V
       	    for i in range(V):
       	        if vis[i]==0:
       	            if detectcycle(i,vis,adj):
       	                return True
       	        
            return False
print(isCycle(V, adj))        