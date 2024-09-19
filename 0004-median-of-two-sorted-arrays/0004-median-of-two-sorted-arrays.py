class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1.copy()
        nums+= nums2.copy()
        nums.sort()
        start = 0
        end = len(nums)-1
        if len(nums)%2:
            return (nums[(start+end)//2])
        else:
            mid1 = (start+end)//2
            mid2 = mid1+1
            mid = nums[mid1]+nums[mid2]
            return (mid/2)