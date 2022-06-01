# hash table solution
# remember to explain initial brute force solution

So, my first approach to this problem would be to think of a brute force way of doing it.
Given an array of integers nuts, and an integer target, we have to find the two numbers that add up to the target, that are not the same. Well the first thing I would think of Is to loop through every item in the array, and then for every item, loop through it again, add the two numbers together, and see if it equals to target. If it does, return the indices of the two. If not, then it would fail.

This initial solution would have a time complexity of n^2, since it loops through it twice. In order to fix this, we have to think of an alternative solution. 
One way of doing so is to find a number, when added to the current indice, equals the target- we then have to find that target in the array. We can do so by creating a hash map, with the array value as the key, and the index as the hash value.


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i, v in enumerate(nums):
            hash[v] = i
            
        for i, v in enumerate(nums):
            answer_value = target - v
            if answer_value in hash and i != hash[answer_value]:
                return [i, hash[answer_value]]
        return [-1, -1]

# same runtime, in less lines of code
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, v in enumerate(nums):
            remaining = target - v 
            if remaining in seen:
                return [seen[remaining], i]
            seen[v] = i 
        return []
