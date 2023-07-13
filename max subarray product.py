# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 18:39:04 2023

@author: Shubhi Tiwari
"""
nums=[2,3,-2,4]
def maxProduct( nums):
        
        """
        :type nums: List[int]
        :rtype: int
        """
        prod1=nums[0]
        prod2=nums[0]
        final=nums[0]
        temp=0
        for i in range(1,len(nums)):
            temp=max(nums[i],nums[i]*prod1,nums[i]*prod2)
           
            prod2=min(nums[i],nums[i]*prod1,nums[i]*prod2)  
           
            prod1=temp
            
            final=max(final,prod1)  
          

        return final
print(maxProduct(nums)    )