class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        def pivot_index(start,end):
            while start<end:
                mid = (start+end)//2
                if nums[mid]>=nums[0]:
                    start = mid+1
                else:
                    end = mid
            return end
        def binary_search(start,end):
            while start<=end:
                mid = (start+end)//2
                if nums[mid]==target:
                    return mid
                elif target>nums[mid]:
                    start = mid+1
                else:
                    end = mid-1
            return -1
        pivot = pivot_index(start,end)
        if nums[pivot] <= target <= nums[end]:
            return binary_search(pivot,end)
        else:
            return binary_search(start,pivot)
