class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        total = 0
        for n in nums:
            total += n
            self.prefix.append(total)

    def sumRange(self, left: int, right: int) -> int:
        rprefix = self.prefix[right]
        if left > 0:
            lprefix = self.prefix[left-1] 
        else: 
            lprefix = 0
        sum = rprefix - lprefix
        return sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)