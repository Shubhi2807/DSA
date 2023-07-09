# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 22:47:18 2023

@author: Shubhi Tiwari
"""
class Solution:
    def dfs(self,start,vis,arr,adj):
        vis[start]=1
        for i in adj[start]:
            if vis[i]==0:
                self.dfs(i,vis,arr,adj)
        arr.append(start) 
        
    def trans(self,V,adj):
        t=[[] for _ in range(V)]
        for i in range(V):
            for j in adj[i]:
                t[j].append(i)
                
        return t        
    def revdfs(self,node,Gt,vis): 
        vis[node]=1
        for i in Gt[node]:
            if vis[i]==0:
                self.revdfs(i,Gt,vis)
                
    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        # code here
        vis=[0]*V
        arr=[]
        for i in range(V):
            if vis[i]==0:
                self.dfs(i,vis,arr,adj)
                
        Gt=self.trans(V,adj)
        
        vis=[0]*V
        com=0
        while(arr):
            node=arr.pop()
            if vis[node]==0:
                com+=1
                self.revdfs(node,Gt,vis)
        return com       
