class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        started = 0
        
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                continue
            elif nums[i] < nums[i + 1]:
                if started == 1:
                    return False
                started = 2
            elif nums[i] > nums[i+1]:
                if started ==2:
                    return False
                started = 1
        return True