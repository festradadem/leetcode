# Valid Anagram
# Difficulty: Easy
# Pattern: Hash Map / Frequency Counter
# Time Complexity: O(n)
# Space Complexity: O(n)
# We count the frequency of each character in both strings
# and compare the resulting dictionaries.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        aux={}
        aux2={}
        for x in s:
            if x in aux:
                aux[x]=aux[x]+1
            else:
                aux[x]=1

        for x in t:
            if x in aux2:
                aux2[x]=aux2[x]+1
            else:
                aux2[x]=1
        return aux == aux2