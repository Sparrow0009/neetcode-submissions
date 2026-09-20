class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        I think this is pretty easy, we will just set the two pointers;
        Left(L): Start of the array
        Right(R): End of the array
        And then check the sum of the elements at those indices.

        As our array is sorted, this makes it much easier for us.

        If we see that the sum is greater than target that means we need a
        lesser value, hence we will move R inwards.
        If we see that the sum is lesser than target that means we need a 
        bigger value, hence we will move L outwards.
        """
        l = 0
        r = len(numbers) - 1

        while l < r:
            current_sum = numbers[l] + numbers[r]
            if current_sum < target:
                l += 1
            elif current_sum > target:
                r -= 1
            else:
                return [l + 1, r + 1]
            

        