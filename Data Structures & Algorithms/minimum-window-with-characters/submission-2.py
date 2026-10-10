# we set the 2 pointers at the start of the string
# we move the right pointer until counter of that window contains count_t
# then we start shrinking the left window until the count_t still exists and store the shortest string
# if in an iteration, the window stops containing count_t, we start moving the right.
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        count_t = Counter(t)
        shortest = [0, float('inf')]

        left = 0
        window = Counter()

        need = len(count_t)
        have = 0
        for right in range(len(s)):
            window[s[right]] += 1

            if (s[right] in count_t) and (window[s[right]] == count_t[s[right]]):
                have += 1

            while have == need:
                if (right - left + 1) < (shortest[1] - shortest[0] + 1):
                    shortest = [left, right]
                window[s[left]] -= 1
                if (s[left] in count_t) and (window[s[left]] < count_t[s[left]]):
                    have -= 1
                left += 1
        return s[shortest[0]: shortest[1] + 1] if shortest[1] != float('inf') else ""











        
        
        