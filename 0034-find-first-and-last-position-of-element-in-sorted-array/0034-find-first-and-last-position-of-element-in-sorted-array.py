class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums)-1
        def first(start,end):
            ans = -1
            while start<=end:
                mid = (start+end)//2
                if nums[mid]==target:
                    ans = mid
                    end = mid-1
                elif target<nums[mid]:
                    end = mid-1
                else:
                    start = mid+1
            return ans
        def last(start,end):
            ans = -1
            while start<=end:
                mid = (start+end)//2
                if nums[mid]==target:
                    ans = mid
                    start = mid+1
                elif target<nums[mid]:
                    end = mid-1
                else:
                    start = mid+1
            return ans
        result = []
        result.append(first(start,end))
        result.append(last(start,end))
        return result