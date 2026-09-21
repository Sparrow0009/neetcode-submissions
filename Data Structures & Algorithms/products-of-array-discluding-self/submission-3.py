class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        # With division operator
        output = []
        product = 1
        zero_count = 0

        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                product *= num
        for num in nums:
            if zero_count > 1:
                output.append(0)
            elif zero_count == 1:
                output.append(product if num == 0 else 0)
            else:
                output.append(product // num)
        return output"""

        prefix = []
        suffix = []
        product = 1
        output = []

        for p in range(len(nums)):
            prefix.append(product)
            product *= nums[p]
        product = 1
        for s in range(len(nums) - 1, -1, -1):
            suffix.append(product)
            product *= nums[s]
        suffix = suffix[::-1]
        for o in range(len(nums)):
            output.append(prefix[o] * suffix[o])
        return output


