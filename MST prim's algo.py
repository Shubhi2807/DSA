# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 18:25:23 2023

@author: Shubhi Tiwari
"""

V=3
E= 3
adj=[[0, 1, 5],[1, 2, 3],[0, 2, 1],[1,0,5],[2,1,3],[2,0,1]]

def spanningTree(V, adj):
        #code here
        prio=[]
        visited=[0]*V
        #weight,node
        prio.append([0,0])
        
        count=0
        
        while(prio):
            
            ele=prio.pop()
            
            weight=ele[0]
            node=ele[1]
            
            if visited[node]==1:
                continue
            visited[node]=1
            count+=weight
            for i in adj:
                
                if i[0]==node :
                   
                    if visited[i[1]]==0:
                       prio.append([i[2],i[1]])
        return count    
print(spanningTree( V, adj))    