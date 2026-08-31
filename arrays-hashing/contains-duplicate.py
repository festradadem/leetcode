# Contains Duplicate
# Difficulty: Easy
# Pattern: Hash Set
# Time Complexity: O(n)
# Space Complexity: O(n)
# We used set() instead of a regular list because a set() allows O(1) instead of O(n)

class Solution:

    def containsDuplicate(self, nums: List[int]) -> bool:
        aux = set()

        for x in nums:
            if x in aux:
                return True

            aux.add(x)

        return False