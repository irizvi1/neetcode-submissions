class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        leftmax, rightmax = height[l], height[r]
        total = 0

        while l < r:
            if height[l] < height [r]:
                l += 1
                leftmax = max(leftmax, height[l])
                if leftmax - height[l] < 0:
                    height[l] = leftmax
                total += leftmax - height[l]
            else: 
                r -= 1
                rightmax = max(rightmax, height[r])
                if rightmax - height[r] < 0:
                    height[r] = rigtmax
                total += rightmax - height[r]
        return total
               