class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        len_s = len(nums)
        output = []

        for i in range(len_s):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len_s - 1
            target = -1 * nums[i]

            while left < right:
                if nums[left] + nums[right] == target:
                    output.append([nums[left], nums[right], -1 * target])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1

        return output if output else []
            

