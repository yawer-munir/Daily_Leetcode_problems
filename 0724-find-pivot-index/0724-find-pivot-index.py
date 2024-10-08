class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum, right_sum = 0,sum(nums)
        for index,num in enumerate(nums):
            right_sum-=num
            if left_sum==right_sum:
                return index
            left_sum+=num
        return -1
