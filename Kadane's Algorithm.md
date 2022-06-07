## Kadane's Algorithm

The following notes are taken from this website link. While trying to solve the "maximum sub-array" problem in leetcode's blind 75,
I saw that most submissions used Kadane's algorithm.

https://favtutor.com/blogs/kadanes-algorithm-python

## Definition

* Famous approach to solving the maximum sub-array using **dynamic programming**. 

Question:
```
Given an integer array nums, find the contiguous subarray
(containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.
```
* Upon first glance, one may think that the result is just all the elements of the array summed.
* However, one needs to take into consideration negative numbers.
* One could always just create a brute-force approach, but that would have a `O(n)^2` time complexity.
* This is why the algorithm is needed.

## Process
*  Two variables: The sum so far, and the maximum total
*  Will traverse the array, updating these variables
*  Must look at the conditions in which we update variables.

1. Initalize variables
2. For every element in the array, complete the following:
```python

sum_so_far = sum_so_far + a[i] # adds max ending with value of current element in index

if sum_so_far < 0:
  sum_so_far = 0
elif current_max < sum_so_far:
  current_max = sum_so_far
  
return max_till_now
```

Time complexity is `O(n)` since it only traverse through the array once.
Space complexity of the algorithm is `O(1)`.

## Visual Representation

![image](https://user-images.githubusercontent.com/5387769/172429962-901f4b91-a45f-44fe-ac7b-414c2562342b.png)
![image](https://user-images.githubusercontent.com/5387769/172430052-023f98e3-741a-4910-85a3-d61c7cfafbf0.png)


