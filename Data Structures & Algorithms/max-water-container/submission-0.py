class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights) - 1
        max_area = 0
        curr_area = 0

        while L < R:
            curr_area = min(heights[L], heights[R]) * (R-L) 
            max_area = max(max_area, curr_area)
            if heights[L] < heights[R]:
                L+=1
            else:
                R -= 1

            

        return max_area
