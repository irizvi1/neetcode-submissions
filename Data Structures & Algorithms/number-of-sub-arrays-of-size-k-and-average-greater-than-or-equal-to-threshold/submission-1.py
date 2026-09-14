
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        #have a counter to keep track of number of subarrs when both conditions are met
        #everytime a subrr is eclipses 3, clear the first num in set
        
        count = 0
        sum = 0
        L = 0
        R = 0

        for R in range(len(arr)):
            sum += arr[R]
            if ((R - L) + 1) > k:
                sum -= arr[L]
                L += 1
            
            if (R == L + (k-1)) and (sum/k >= threshold):
                 count += 1
            
        return count


