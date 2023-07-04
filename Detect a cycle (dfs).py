# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 22:42:05 2023

@author: Shubhi Tiwari
"""

from typing import List
from queue import Queue

    
def detectcycle(self,node,parent,vis,adj):
        
        vis[node]=1
        for i in adj[node]:
            if vis[i]==0:
                if self.detectcycle(i,node,vis,adj):
                   return True
            elif parent!=i:
                return True
        return False        
            
        
        
    #Function to detect cycle in an undirected graph.
def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    vis=[0]*V
	    for i in range(V):
	        if vis[i]==0:
	            if self.detectcycle(i,-1,vis,adj):
	                return True
        return False
	        
         