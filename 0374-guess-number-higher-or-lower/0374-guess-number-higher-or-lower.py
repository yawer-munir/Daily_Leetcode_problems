# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        start = 1
        end = n
        while start<=end:
            pick = (start+end)//2
            num = guess(pick)
            if num == 0:
                return pick
            elif num == -1:
                end = pick-1
            else:
                start = pick+1
        