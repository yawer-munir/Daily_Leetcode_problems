class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        window = set()
        l = 0
        res = s = 0
        for r in range(len(nums)):
            while nums[r] in window:
                window.remove(nums[l])
                s-=nums[l]
                l+=1
            window.add(nums[r])
            s+=nums[r]
            if len(window)>k:
                window.remove(nums[l])
                s-=nums[l]
                l+=1
            if len(window)==k:
                res = max(res,s)
        return res
        