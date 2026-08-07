[TOC]

## Solution

--- 

### Overview

Given an array `nums`, we need to find the index that divides the array into two parts and where the difference between the average of the left part of the array and the right part is minimum.        

An index `i` will divide the array into two parts: 
  - the first part will have elements from index `0` to index `i`, and
  - the second part will have elements from index `i + 1` to the last index.       

And the average of both parts of the array will be **rounded down** to the nearest integer.

![example](images/Slide1.png)

Let's look at the brute method first and try to optimize it further.

---

### Approach 1: Brute Force

#### Intuition

The most naive method we can think of is iterating on every index `i` of the array and then finding the averages of the left and right parts of the array broken at index `i` and finding the difference between them.

> **Note:** Firstly, we would need to iterate on every index of the array to consider that index as breaking point and then iterate on all indices again to iterate on both parts of the array to calculate their respective averages. As you can see this method is not optimal, thus this will result in a **Time Limit Exceed**, but it will be a stepping stone to the further approaches.

!?!../Documents/2256/slideshow1.json:960,540!?!

<br />

#### Algorithm

1. Initialize variables:
    - `n`, integer to store the number of elements in the array.
    - `minAvgDiff`, initialized with a large integer value, stores the minimum average difference.
    - `ans`, integer to store the index where we found the minimum average difference.

2. Iterate over each index of the `nums` array:
    - At each index `i`, add all elements of the `nums` array from index `0` to index `i`, and divide the sum by `i + 1` to get the average of the left part of the array.
    - Similarly, add elements from index `i + 1` to `n - 1`, and divide by `n - i - 1` to get the average of the right part of the array. 
    - If the difference between the average of the left and right part of the array is smaller than `minAvgDiff`, then store this difference in `minAvgDiff` and the current index `i` in `ans`. 

3. Return `ans`.

#### Implementation


```python
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -1
        min_avg_diff = math.inf
        
        for index in range(n):
            # Calculate average of left part of array, index 0 to i.
            left_part_average = 0
            for i in range(index + 1):
                left_part_average += nums[i]
            left_part_average //= (index + 1)
            
            # Calculate average of right part of array, index i+1 to n-1.
            right_part_average = 0
            for j in range(index + 1, n):
                right_part_average += nums[j]
        
            # If right part have 0 elements, then we don't divide by 0.
            if index != n - 1:
                right_part_average //= (n - index - 1)
            
            curr_difference = abs(left_part_average - right_part_average)
            
            # If current difference of averages is smaller,
            # then current index can be our answer.
            if curr_difference < min_avg_diff:
                min_avg_diff = curr_difference
                ans = index
                
        return ans
```


#### Complexity Analysis

Here, $n$ is the number of elements in the `nums` array.

* Time complexity: $O(n^{2})$.
  - We iterate over each index of the `nums` array.
  - And at each index, we again iterate on all elements to calculate averages of two parts, which takes $O(n)$ time.
  - Thus, for finding the difference of averages at $n$ indices, it will take $O(n^2)$ time.

* Space complexity: $O(1)$.    
  - We have only used some integer variables. Thus, the space used is constant.


<br />

---


### Approach 2: Prefix Sum

#### Intuition

First of all, if you don't know, prefix sum is the technique where we generate a `prefix` array, and it's each element at `(i + 1)th` index stores the cumulative sum of all array elements from index `0` to index `i`. 

If you carefully notice, when in the previous approach at each index `i`, we needed sum of all elements of `nums` array from index `0` to index `i`, thus we can conclude that we can use a  prefix array instead of iterating again on all elements.

Just like, prefix sums, we can store suffix sum for the `nums` array to get the sum of all elements from index `i + 1` till last index in optimal way. Let's understand this with the following example:     

![prefix_suffix_example](images/Slide18.png)

#### Algorithm

1. Initialize variables:
    - `n`, integer to store the number of elements in the array.
    - `minAvgDiff`, initialized with a large integer value, stores the minimum average difference.
    - `ans`, integer to store the index where we found the minimum average difference.
    - `prefixSum`, `suffixSum`, integer arrays to store prefix and suffix sums for the `nums` array.

2. Precompute prefix and suffix sums for the `nums` array.
    - For prefix sum, iterate from start to end and add the current element to the previous prefix sum.
    - For suffix sum, iterate from end to start and add the current element to the previous suffix sum.

3. Iterate over each index of the `nums` array:
    - At each index `i`, get the sum of all elements of the `nums` array from index `0` to index `i` stored in `prefixSum[i + 1]`, and divide the sum by `i + 1` to get the average of the left part of the array.
    - Similarly, get the sum of elements from index `i +1` to `n - 1` stored in `suffix[i + 1]`, and divide by `n - i - 1` to get the average of the right part of the array. 
    - If the difference between the average of the left and right part of the array is smaller than `minAvgDiff`, then store this difference in `minAvgDiff` and the current index `i` in `ans`. 

4. Return `ans`.

#### Implementation


```python
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -1
        min_avg_diff = math.inf
        
        # Generate prefix and suffix sum arrays.
        prefix_sum = [0] * (n + 1)
        suffix_sum = [0] * (n + 1)
        
        for index in range(n):
            prefix_sum[index + 1] = prefix_sum[index] + nums[index];
        
        for index in range(n - 1, -1, -1):
            suffix_sum[index] = suffix_sum[index + 1] + nums[index];
        
        for index in range(n):
            # Calculate average of left part of array, index 0 to i.
            left_part_average = prefix_sum[index + 1]
            left_part_average //= (index + 1)
            
            # Calculate average of right part of array, index i+1 to n-1.
            right_part_average = suffix_sum[index + 1]
            # If right part have 0 elements, then we don't divide by 0.
            if index != n - 1:
                right_part_average //= (n - index - 1)
            
            curr_difference = abs(left_part_average - right_part_average)
            
            # If current difference of averages is smaller,
            # then current index can be our answer.
            if curr_difference < min_avg_diff:
                min_avg_diff = curr_difference
                ans = index
                
        return ans
```


#### Complexity Analysis

Here, $N$ is the number of elements in the `nums` array.

* Time complexity: $O(n)$.
  - We iterate over `nums` array to precompute `prefixSum` and `suffixSum` arrays.
  - Then, we iterate over each index of the `nums` array and at each index, we calculate averages of two parts in constant time using `prefixSum` and `suffixSum` arrays.
  - Thus, for finding the difference of averages at $n$ indices, it will take $O(n)$ time.

* Space complexity: $O(n)$.    
  - We have used two arrays of size $n$ to store prefix and suffix sums of `nums` array.
  - Thus, overall it will take $O(n)$ space.

<br />

---


### Approach 3: Prefix Sum Optimized

#### Intuition

Our runtime for the previous approach is fairly efficient, but we are using some auxiliary space.        
Let's try optimizing it now.    

We are using two arrays, `prefixSum` to store the sum of all the elements of the array from index `0` to index `i` to get the left part's sum, and `suffixSum` to store the sum of elements from index `i + 1` to the last index to get the right part's sum.            

But if we already had the sum of all elements of the array, then we can subtract the left part's sum from it to get the right part's sum, thus we can discard the `suffixSum` array and use only `prefixSum` array with a `totalSum` variable.

But further we can notice, that while iterating on every index for breaking the `nums` array in two parts at that index, every time we only use the value at the current index `i` from the `prefixSum` array. Thus, instead of storing all prefix sums in an array, we can store the prefix sum till index `i` in a variable. So, we can also discard the `prefixSum` array and only use a `currPrefixSum` variable instead of it.             
Thus, instead of two arrays, we can use only two variables `totalSum` and `currPrefixSum`.       

Let's visualize it better with the following slideshow:

!?!../Documents/2256/slideshow2.json:960,540!?!

#### Algorithm

1. Initialize variables:
    - `n`, integer to store the number of elements in the array.
    - `minAvgDiff`, initialized with a large integer value, stores the minimum average difference.
    - `totalSum`, a variable to store the sum of all elements of the `nums` array.
    - `currPrefixSum`, a variable to store the sum of all elements till the current index of the `nums` array.
    - `ans`, integer to store the index where we found the minimum average difference.

2. Iterate on the `nums` array and calculate `totalSum`.

3. Iterate over each index of the `nums` array:
    - At each index `i`, we add the current element in `currPrefixSum`, to get the sum of all elements of the `nums` array from index `0` to index `i`, and divide the sum by `i + 1` to get the average of the left part of the array.
    - Similarly, we can get the sum of elements from index `i + 1` to `n - 1` after subtracting the left part's sum from the total sum of the array, and then divide it by `n - i - 1` to get the average of the right part of the array. 
    - If the difference between the average of the left and right part of the array is smaller than `minAvgDiff`, then store this difference in `minAvgDiff` and the current index `i` in `ans`. 

4. Return `ans`.

#### Implementation


```python
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -1
        min_avg_diff = math.inf
        curr_prefix_sum = 0
        
        # Get total sum of array.
        total_sum = 0
        for index in range(n):
            total_sum += nums[index]
        
        for index in range(n):
            curr_prefix_sum += nums[index]
            
            # Calculate average of left part of array, index 0 to i.
            left_part_average = curr_prefix_sum
            left_part_average //= (index + 1)
            
            # Calculate average of right part of array, index i+1 to n-1.
            right_part_average = total_sum - curr_prefix_sum
            # If right part have 0 elements, then we don't divide by 0.
            if index != n - 1:
                right_part_average //= (n - index - 1)
            
            curr_difference = abs(left_part_average - right_part_average)
            
            # If current difference of averages is smaller,
            # then current index can be our answer.
            if curr_difference < min_avg_diff:
                min_avg_diff = curr_difference
                ans = index
                
        return ans
```


#### Complexity Analysis

Here, $N$ is the number of elements in the `nums` array.

* Time complexity: $O(n)$.
  - We iterate over each index of the `nums` array and at each index, we calculate averages of two parts in constant time using `currSum` and `totalSum` variables.
  - Thus, for finding the difference of averages at $n$ indices, it will take $O(n)$ time.

* Space complexity: $O(1)$.    
  - We have only used some integer variables. Thus, the space used is constant.