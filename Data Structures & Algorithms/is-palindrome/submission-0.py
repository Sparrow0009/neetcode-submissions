class Solution:
    def isPalindrome(self, s: str) -> bool:
        true_s = "".join(char.lower() for char in s if char.isalnum())
        return true_s == true_s[::-1]