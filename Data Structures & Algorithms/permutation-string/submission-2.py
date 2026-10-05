from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        k = len(s1)

        for i in range(len(s2) - k + 1):
            if Counter(s2[i : i + k]) == need:
                return True
        return False

        
        