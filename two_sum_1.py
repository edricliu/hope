#!/usr/bin/env python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_with_idx = [(x, i) for i, x in enumerate(nums)]
        nums_with_idx = sorted(nums_with_idx, key = lambda p: p[0])
        i = 0;
        j = len(nums) - 1

        res = None
        while i < j:
            cur_sum = nums_with_idx[i][0] + nums_with_idx[j][0]
            if cur_sum < target:
                i += 1
            elif cur_sum > target:
                j -= 1
            else:
                res = [nums_with_idx[i][1], nums_with_idx[j][1]]
                break

        return sorted(res)



s = Solution()
print s.twoSum([3, 2, 4], 6)