class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_longest = 0
        seen = set()
        left = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            len_longest = max(len_longest, (right - left + 1))
        return len_longest

        