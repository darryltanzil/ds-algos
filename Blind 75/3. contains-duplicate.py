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

This is a solution from the community, which is better then mine. It utilizes the python "set" function, and determines whether or not the length of nums
is not equal to the length of the set nums, since the set nums does not contain any duplicates.
class Solution(object):
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))