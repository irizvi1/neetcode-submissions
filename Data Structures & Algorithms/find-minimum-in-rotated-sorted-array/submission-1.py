class Solution:
    def findMin(self, nums: List[int]) -> int:
        #check if array is sorted or not (num[l] < num[r] ?), if it is return the nums[l]

        #if not set mid, and check whether mid is greater than or nums[l], if it is then the min is in the right side, so move l to m+1 and update min with nums[l]
        # if not, min is in the right side, so move r to m-1 and update min with nums[l]

        l = 0
        r= len(nums) - 1
        res = float('inf')

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            else:
                mid =  l+ (r-l)//2
                res = min(nums[mid], res)
                if nums[mid] >= nums[l]:
                    l = mid+1
                else:
                    r = mid-1
        return res