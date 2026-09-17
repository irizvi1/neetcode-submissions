class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            total += num
        leftsum = 0
        
        for i in range(len(nums)):
            rightsum = total - (leftsum + nums[i])
            if leftsum == rightsum:
                return i
            leftsum += nums[i]

        return -1