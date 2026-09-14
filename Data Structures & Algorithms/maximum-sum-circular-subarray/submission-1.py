class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        minsum = nums[0]
        maxsum = nums[0]
        arrsum = 0
        maxcurrsum = 0
        mincurrsum = 0
      
        for num in nums:
            maxcurrsum = max(maxcurrsum, 0)
            maxcurrsum += num
            maxsum = max(maxsum, maxcurrsum)
            
            mincurrsum = min(mincurrsum, 0)
            mincurrsum += num
            minsum = min(minsum, mincurrsum)

            arrsum += num

        if maxsum < 0:
            return maxsum
        return max(maxsum, (arrsum-minsum))

            

