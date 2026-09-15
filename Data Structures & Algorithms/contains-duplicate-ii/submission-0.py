class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dupes  = {}
        j = 0

        for i in range(len(nums)):
            if (nums[i] in dupes) and (abs(dupes[nums[i]] - i)) <= k:
                return True
            dupes[nums[i]] = i 
        return False