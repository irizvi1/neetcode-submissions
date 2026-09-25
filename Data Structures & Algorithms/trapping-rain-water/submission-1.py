class Solution:
    def trap(self, height: List[int]) -> int:
        #get a list of the largetr left walls, by iterating normally thru array and updatning the largest left wlal for each index
        #get list of largest right walls by iterating backwards thru, and updating largest right wall for each index
        #for each block find min of leftwall height and right wall height, and subtract height of current index from it, if its negative, leave it

        maxlwall = 0
        maxrwall= 0
        maxl = [0] * len(height)
        maxr = [0] * len(height)
        res = 0

        for i in range(len(height)):
            maxl[i] = maxlwall
            maxlwall = max(maxlwall, height[i])
        for i in range(len(height) -1, -1, -1):
            maxr[i] = maxrwall
            maxrwall = max(maxrwall, height[i])

        for i in range(len(height)):
            pot = min(maxl[i], maxr[i])
            res += max(0, pot - height[i])
        return res

      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
       # l, r = 0, len(height) - 1
       # leftmax, rightmax = height[l], height[r]
        #total = 0

       # while l < r:
            #if height[l] < height [r]:
                #l += 1
                #leftmax = max(leftmax, height[l])
                #if leftmax - height[l] < 0:
                    #height[l] = leftmax
                #total += leftmax - height[l]
            #else: 
                #r -= 1
                #rightmax = max(rightmax, height[r])
                #if rightmax - height[r] < 0:
                    #height[r] = rigtmax
                #total += rightmax - height[r]
        #return total
               