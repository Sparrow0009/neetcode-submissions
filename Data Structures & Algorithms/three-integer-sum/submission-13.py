class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s_nums = sorted(nums)
        len_s = len(s_nums)
        output = []

        for i in range(len_s):
            if i > 0 and s_nums[i] == s_nums[i - 1]:
                continue
            left = i + 1
            right = len_s - 1
            target = -1 * s_nums[i]

            while left < right:
                if s_nums[left] + s_nums[right] == target:
                    output.append([s_nums[left], s_nums[right], -1 * target])
                    left += 1
                    right -= 1
                    while left < right and s_nums[left] == s_nums[left - 1]:
                        left += 1
                elif s_nums[left] + s_nums[right] < target:
                    left += 1
                elif s_nums[left] + s_nums[right] > target:
                    right -= 1

        return output if output else []
            

