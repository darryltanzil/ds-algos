# Big O Notation

![Untitled](Big%20O%20Notation%20ca12154c0aca49bfa69f950c634803bf/Untitled.png)

# Constant Time = O(1)

- independent of input, constant time to execute

```python

given_array = [1, 4, 3, 2, ..., 10]

def foo(given_array):
	total = 0 -> O(1)
	return total -> O(1)

# O(1) + O(1) = O(1)
```

# Linear time = O(n)

- proportional to input size
- traversing array, linked list, linear search, comparison of two strings, palindrome check, bucket sort, etc.

```python
def find_sum(given_array):
	total = 0 -> O(1)
	for each i in given_array: (1)
		tital += i -> O(1) # which is executed n times
	return total -> O(1)

O(1) + n * O(1) + O(n) = O(n)
```

# Quadratic = O(n^2)

- proportional to input size
- nested loop, bubble sort, insertion sort, selection sort, etc.

```python
array_2d = [[1, 4, 3], [3, 1, 9], [0, 5, 2]]
# number of columns is the same as rows.

def find_sum_2d(array_2d):
	total = 0 -> O(1)
	for each row in array_2d: # repeated n where n is num of columns
		for each i in row: 
			total += i -> O(1) # repeated n where n is num of rows
	return total -> O(1)

T = O(1) + n^2 * O(1) + O(1)

If there was two arrays, then it would be O(2n^2),
which is equivalent to O(n^2)
```

# Logarithmic Time = O(logn)

- proportional to input size
- binary search, skip list, etc.

```python
def binarySearch(arr, 1, r, x):
	low = 0
	high = len(arr) - 1
	mid = 0

	while low <= high:
		mid = (high + low) // 2
		
	# x greater, ignore left half
	if arr[mid] < x:
		low = mid + 1
	
	# x smaller, ignore right half
	elif arr[mid] > x:
		high = mid - 1
		
	# means x is present at mid
		else:
			return mid

	return -1 # element not here
```

# Formula

`T = an + b = O(n)`

1. Find the fastest growing term
2. Take out the Coefficient
- `T` - Average time to run function for array item
- `a` - coefficient
- `n` - current item in array
- `b` - time irrelevant to current item

### Example

`T = cn^2 + dn + e` = O(n^2), is co-efficient

![https://user-images.githubusercontent.com/5387769/171221200-8a481bcc-afd5-42aa-9e9f-e4a80c074baa.png](https://user-images.githubusercontent.com/5387769/171221200-8a481bcc-afd5-42aa-9e9f-e4a80c074baa.png)

![Untitled](Big%20O%20Notation%20ca12154c0aca49bfa69f950c634803bf/Untitled%201.png)

# Space Complexity
* Primitives (Booleans, Numbers) take up constant space. `var x = 100` same memory as `var x = 200`
* Arrays, Strings, Objects take up linear space. Array with 4 elements take twice the memory of array with two elements.

![image](https://user-images.githubusercontent.com/5387769/171231449-83334933-ea81-4589-9548-2fd7fd91966d.png)


