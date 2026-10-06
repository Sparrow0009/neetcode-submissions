class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Trying to solve this again to see if I actually remember
        seen = set(nums)
        max_streak = 0
        for num in seen:
            if (num - 1) not in seen:
                length = 1
                while (num + length) in seen:
                    length += 1
                max_streak = max(max_streak, length)
        return max_streak

        # [2,20,4,10,3,4,5] - nums array
        # [2,20,4,10,3,5] - seen set
