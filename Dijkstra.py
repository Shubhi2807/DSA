# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 20:24:19 2023

@author: Shubhi Tiwari
"""
from queue import Queue

def dijkstra(V, adj, S):
        #code here
        dist=[100000]*V
        q=[]
        parent=[]
        for i in range(V):
            parent.append(i)
           
        q.append([0,S])
        
        dist[S]=0
        while(q):
            ele=q.pop()
           
            dis=ele[0]
            
            node=ele[1]
           
            for i in adj[node]:
                
                adjnode=i[0]
                edw=i[1]
                if dis+edw<dist[adjnode]:
                    dist[adjnode]=dis+edw
                    q.append([dis+edw,adjnode])
                    parent[adjnode]=node
                  
        
        return dist
print(dijkstra( V, adj, S))    
    