class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cursum = 0
        prefixsums = {0:1}
        diff = 0
        res = 0

        for i in range(len(nums)):
            cursum += nums[i]
            diff = cursum - k
            res += prefixsums.get(diff, 0)
            prefixsums[cursum] = 1 + prefixsums.get(cursum, 0)

        return res