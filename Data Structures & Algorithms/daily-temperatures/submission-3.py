class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        """ # Inefficient Solution - O(n^2)
        stack = [0] * len(temperatures)  
        for i in range(len(temperatures)):
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    stack[i] = (j - i)
                    break
                else:
                    continue
        return stack
        """
        output = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                result = i - j
                output[j] = result
            stack.append(i)
        return output    




        