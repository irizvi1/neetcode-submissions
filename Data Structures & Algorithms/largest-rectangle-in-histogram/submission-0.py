class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #pop from stack if current heiht is less than height at top of stack, then potentially update maxarea (height of top of stack * i-index(distance btween the bars)), if cuurent height is larger, append to stack with the indez of the last popped bar

        stack = []
        maxarea = 0
        index = 0
        height = 0

        for i, h in enumerate(heights):
            index = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxarea = max(maxarea, height * (i - index))
            stack.append((index, h))

        for i, h in stack:
            maxarea = max(maxarea, h * (len(heights) - i))
        return maxarea