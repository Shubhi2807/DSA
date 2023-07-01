# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 08:59:20 2023

@author: Shubhi Tiwari
"""
nums=[3,2,1]
def nextPermutation(nums):
        
        # Find non-increasing suffix
        i = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
            
        if i <= 0:
            for i in range(len(nums)-1):
                min_num=i
                
                for j in range(i+1,len(nums)):
                    if nums[j]<nums[min_num]:
                        min_num=j
                        
                nums[min_num],nums[i]=nums[i],nums[min_num]
            return nums
        
        # Find successor to pivot
        j = len(nums) - 1
        print(nums[j],nums[i-1])
        while nums[j] <= nums[i - 1]:
            j -= 1
            
        nums[i - 1], nums[j] = nums[j], nums[i - 1]
        
        # Reverse suffix
        nums[i : ] = nums[len(nums) - 1 : i - 1 : -1]
        return( nums)
print(nextPermutation(nums))          