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

        n = len(nums)
        output = [1] * n

        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]
        return output


