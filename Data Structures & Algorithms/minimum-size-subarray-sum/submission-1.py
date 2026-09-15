class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum = 0
        R = 0 
        L = 0
        min_length = len(nums)
        curr_length = (R - L) + 1
        

        for R in range(len(nums)):
            
            sum+=nums[R]
            while sum >= target:
                min_length = min(min_length, curr_length)
                sum = sum - nums[L]
                L += 1
                curr_length -= 1
            if curr_length == len(nums):
                return 0    
            curr_length += 1
        
        return min_length

            
