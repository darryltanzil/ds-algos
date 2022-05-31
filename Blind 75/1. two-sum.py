# hash table solution
# remember to explain initial brute force solution

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
            