class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_set = set()

        for i in nums:
            seen_set.add(i)
        return len(seen_set) != len(nums)
        