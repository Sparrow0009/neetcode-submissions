class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = []
        for i in range(len(position)):
            combined.append([position[i], speed[i]])

        combined.sort(reverse=True)

        stack = []

        for i in range(len(combined)):
            time = (target - combined[i][0]) / combined[i][1]
            if  not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)