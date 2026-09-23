class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        count = set(nums)
        
        res = 0
        cur = 0

        for n in nums:
            if (n - 1) not in count:
                cur = 0
                while (n+cur) in count:
                    cur+=1
                res = max(res, cur)

            
        return res