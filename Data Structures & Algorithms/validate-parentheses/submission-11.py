class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"}": "{", ")": "(", "]": "["}

        for i in range(len(s)):
            if s[i] in ["(", "[", "{"]:
                stack.append(s[i])
            elif s[i] in pairs:
                if stack and stack.pop() == pairs[s[i]]:
                    continue
                return False
        return True if not stack else False


        