class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # merging
        nums = nums1+nums2
        nums.sort()
        total = len(nums)
        if total%2:#odd
            return (nums[total//2])
        return (nums[total//2]+nums[total//2-1])/2