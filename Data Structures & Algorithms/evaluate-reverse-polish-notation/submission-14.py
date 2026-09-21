class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ["+", "-", "*", "/"]
        for char in range(len(tokens)):
            if tokens[char] not in operations :
                stack.append(int(tokens[char]))
            elif tokens[char] in operations:
                a = stack.pop()
                b = stack.pop()
                if tokens[char] == "+":
                    stack.append(b + a)
                elif tokens[char] == "-":
                    stack.append(b - a)
                elif tokens[char] == "*":
                    stack.append(b * a)
                elif tokens[char] == "/":
                    stack.append(int(b / a))
        return stack[-1]



        