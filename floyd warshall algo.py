# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 20:48:34 2023

@author: Shubhi Tiwari
"""

def shortest_distance(self, matrix):
		#Code here
		for i in range(len(matrix)):
		    for j in range(len(matrix)):
		        if matrix[i][j]==-1:
		            matrix[i][j]=100000000
		        if i==j:
		            matrix[i][j]=0
		            
		for k in range(len(matrix)):
		    for i in range(len(matrix)):
		        for j in range(len(matrix)):
		            matrix[i][j]=min(matrix[i][j],matrix[i][k]+matrix[k][j])
		            
		for i in range(len(matrix)):
		    for j in range(len(matrix)):
		        if matrix[i][j]==100000000:
		            matrix[i][j]=-1
		        if i==j:
		            matrix[i][j]=0            
    