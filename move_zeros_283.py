#!/usr/bin/env python

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = -1;
        while i + 1 < len(nums) and nums[i+1] != 0:
            i += 1

        j = i + 1

        while j < len(nums):
            if nums[j] != 0:
                i += 1
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
            j += 1