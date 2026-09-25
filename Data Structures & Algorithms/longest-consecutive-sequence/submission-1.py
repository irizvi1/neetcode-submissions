class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       
       #put entire array ina  set
       #start loop thru array
       # if current nums[i] - 1 not in set set lenght = 1, next = num+1, then check the sequence lenght via second loop(while) by looping if num+1 is in set, and incrementing lengh and next if os
       #exit loop and max(longest, lenght)

        s = set(nums)
        length = 0
        longest = 0

        for i in range(len(nums)):
            if (nums[i] -1) not in s:
                length = 1
                next = nums[i] + 1
                while next in s:
                    length +=1
                    next +=1
            longest = max(longest, length)
        return longest

       
       
       
       
       
       
       
       
       
       
       
       
       
       
       # if len(nums) == 0:
            #return 0
        #count = set(nums)
        
        #res = 0
        #cur = 0

        #for n in nums:
            #if (n - 1) not in count:
                #cur = 0
               # while (n+cur) in count:
                    #cur+=1
                #res = max(res, cur)

            
        #return res