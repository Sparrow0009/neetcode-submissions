class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_dict = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen_dict:
                return [seen_dict[complement], i]
            seen_dict[nums[i]] = i
        return False
        