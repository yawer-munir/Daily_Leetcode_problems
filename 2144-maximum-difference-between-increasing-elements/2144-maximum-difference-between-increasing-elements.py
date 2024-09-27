class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_diff = -1
        res = -1
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    max_diff = nums[j] - nums[i]
                    res = max(res,max_diff)
        return res
