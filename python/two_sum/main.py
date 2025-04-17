# https://neetcode.io/problems/two-integer-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        opp = {}
        for i, n in enumerate(nums):
            o = target - n
            if n in opp:
                return [opp[n], i]
            else:
                opp[o] = i
            
        
