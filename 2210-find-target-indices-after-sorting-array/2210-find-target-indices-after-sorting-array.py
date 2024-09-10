class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        start = 0
        end = len(nums)-1
        def first(start,end):
            first = -1
            while start<=end:
                mid = (start+end)//2
                if nums[mid]==target:
                    first = mid
                    end = mid-1
                elif nums[mid]<target:
                    start = mid+1
                elif nums[mid]>target:
                    end = mid-1
            return first
        def last(start,end):
            last = -1
            while start<=end:
                mid = (start+end)//2
                if nums[mid]==target:
                    last = mid
                    start = mid+1
                elif nums[mid]<target:
                    start = mid+1
                elif nums[mid]>target:
                    end = mid-1
            return last
        first_occurrence = first(start,end)
        last_occurrence = last(start,end)
        if first_occurrence==-1:
            return []
        return list(range(first_occurrence,last_occurrence+1))
        
