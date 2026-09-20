class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        true_s = "".join(char.lower() for char in s if char.isalnum())
        return true_s == true_s[::-1]'''
        # Solution using two pointers
        left = 0
        right = len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True

