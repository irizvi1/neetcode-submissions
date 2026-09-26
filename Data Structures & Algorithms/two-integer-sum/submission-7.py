class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = 0
        hash = {}
        same = []

        
        for i in range(len(nums)):
            hash[nums[i]] = i

        for i in range(len(nums)):
            if target - nums[i] == nums[i]:
                same.append(i)
            elif target - nums[i] in hash:
                return [i,hash[(target - nums[i])] ]
        if same:
            return same

        