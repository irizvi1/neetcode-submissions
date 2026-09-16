class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        L = 0
        R = len(numbers) -1

        while L < R:
            cursum = numbers[L] + numbers [R] 

            if cursum < target:
                L+=1
            elif cursum > target:
                R -= 1
            else:
                return [L + 1,R + 1]
      