class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Solution after actually understanding how the algo works

        stack = [] # (index, height)
        m_a = 0 # max area we can get

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                m_a = max(m_a, height * (i - index))
                start = index
            stack.append((start, h))
        for i, h in stack:
            m_a = max(m_a, h * (len(heights) - i))
        return m_a

        