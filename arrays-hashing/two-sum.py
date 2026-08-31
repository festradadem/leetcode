# Two Sum
# Difficulty: Easy
# Pattern: Hash Map
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# We store each number we have already seen together
# with its index. For each new number, we check whether
# its complement (target - num) has already been seen.

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        aux = {}
        for i, num in enumerate(nums):
            if target - num in aux:
                return [i, aux[target - num]]
            aux[num] = i