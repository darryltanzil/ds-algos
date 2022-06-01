# time to complete: 2 minutes 30 seconds

My solution was a one pass hash solution. Originally, I thought of brute forcing it like in the two-sum problem, but then quickly realized
that I could just use a hash table in order to solve it. Quickly wrote up a varation of two-sum, and it worked, in O(n) time complexity.
In a real world situation I would walk through the brute force solution before moving onto the hash table solution.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for i, v in enumerate(nums):
            if v in seen:
                return True
            seen[v] = i
        return False