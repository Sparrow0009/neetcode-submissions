class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        # This is the prefix suffix arrays solution
        n = len(height)
        prefix = [0] * n
        suffix = [0] * n
        prefix[0] = height[0]
        suffix[-1] = height[-1]

        total = 0

        for i in range(1, n):
            prefix[i] = max(prefix[i - 1], height[i])
        for i in range(n - 2, -1, -1):
            suffix[i] = max(suffix[i + 1], height[i])

        for i in range(n):
            total += min(prefix[i], suffix[i]) - height[i]
        return total
        '''
        # This is the two pointer solution
        if not height:
            return 0
        l = 0
        r = len(height) - 1

        left_max = height[l]
        right_max = height[r]
        total = 0

        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                total += (left_max - height[l])
            else:
                r -= 1
                right_max = max(right_max, height[r])
                total += (right_max - height[r])
        return total





        