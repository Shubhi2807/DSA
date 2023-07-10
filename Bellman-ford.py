# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 18:44:11 2023

@author: Shubhi Tiwari
"""

def bellman_ford(V, edges, S):
         #code here
        dis=[int(1e8)]*(V-1)
        dis[S]=0
        for i in range(V+1):
            for first,second,dist in edges:
                if (dis[first]!=float('inf') and dis[first]+dist<dis[second]):
                    if i==V:
                        return -1
                    else:
                        dis[second]=min(dis[second],dis[first]+dist)
        
       
        return dis
        
print(bellman_ford( V, E, S))    