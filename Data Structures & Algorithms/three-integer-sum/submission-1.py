class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort array
        #check if second number in array is same as first, if so continue (no duplicates)
        #r at len-1, l at a+1, check if all add to zero, if so append res and increment l, if is greater, decrement r, if less increment l
        #check if l is the same as its prev, if so move it forward until it doesnt or doesnt pass r
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0  and a == nums[i-1]:
                continue
            l,r = i+1, len(nums) - 1
            while l < r:
                if a + nums[l] + nums[r] > 0:
                    r-=1
                elif a + nums[l] + nums[r] < 0:
                    l+=1
                else:
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        return res
                


        

            
             
