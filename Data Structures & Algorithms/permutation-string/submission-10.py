from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        #Solution with Counter
        '''
        need = Counter(s1)
        k = len(s1)

        for i in range(len(s2) - k + 1):
            if Counter(s2[i : i + k]) == need:
                return True
        return False
        '''

        # Solution with Sliding Window
        if len(s1) > len(s2):
            return False
        seen_s1 = Counter(s1)
        k = len(s1)

        window = Counter(s2[:k])
        if window == seen_s1:
            return True
        for i in range(len(s2) - k):
            window[s2[i + k]] += 1
            window[s2[i]] -= 1
            if window[s2[i]] == 0:
                del window[s2[i]]

            if window == seen_s1:
                return True
        return False



            
        

        
        