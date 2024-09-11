class Solution:
    def mySqrt(self, x: int) -> int:
        start = 0
        end = x
        while start<=end:
            mid = (start+end)//2
            square = mid*mid
            if square==x:
                return mid
            elif square<x:
                ans = mid
                start = mid+1
            elif square>x:
                end = mid-1
        return ans