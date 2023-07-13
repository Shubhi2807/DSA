# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 20:44:49 2023

@author: Shubhi Tiwari
"""

def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sub = []
        for x in nums:
            if len(sub) == 0 or sub[-1] < x:
                sub.append(x)
            else:
                idx = bisect_left(sub, x)  # Find the index of the first element >= x
                sub[idx] = x  # Replace that number with x
        return len(sub)