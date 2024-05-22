class LargestRectangleInHistogram:
    def __init__(self, heights):
        self.heights = heights

    def largest_rectangle_in_histogram_stack(self):
        stack = []
        maxArea = 0

        for i, h in enumerate(self.heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i-index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(self.heights) - i))
        return maxArea
           
