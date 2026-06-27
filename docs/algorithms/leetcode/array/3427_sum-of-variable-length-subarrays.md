# Sum of Variable Length Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3427 |
| Difficulty | Easy |
| Topics | Array, Prefix Sum |
| Official Link | [sum-of-variable-length-subarrays](https://leetcode.com/problems/sum-of-variable-length-subarrays/) |

## Problem Description & Examples
### Goal
Given an integer array `nums`, calculate the total sum of all subarrays defined by the constraint `start_i = max(0, i - nums[i])` to `end_i = i`. For every index `i` in the array, identify the subarray starting at `start_i` and ending at `i`, sum its elements, and return the grand total of these sums across all indices.

### Function Contract
**Inputs**

- `nums`: A list of integers where each element determines the start index of its corresponding subarray.

**Return value**

- An integer representing the sum of all elements contained within the specified variable-length subarrays.

### Examples
**Example 1**

- Input: `nums = [2, 3, 1]`
- Output: `11`
- Explanation: 
  - i=0: start=max(0, 0-2)=0, subarray=[2], sum=2
  - i=1: start=max(0, 1-3)=0, subarray=[2, 3], sum=5
  - i=2: start=max(0, 2-1)=1, subarray=[3, 1], sum=4
  - Total: 2 + 5 + 4 = 11

**Example 2**

- Input: `nums = [3, 1, 1, 2]`
- Output: `13`
- Explanation:
  - i=0: [3], sum=3
  - i=1: [3, 1], sum=4
  - i=2: [1, 1], sum=2
  - i=3: [1, 1, 2], sum=4
  - Total: 3 + 4 + 2 + 4 = 13

**Example 3**

- Input: `nums = [1, 2, 3]`
- Output: `10`

---

## Underlying Base Algorithm(s)
The problem utilizes a **Prefix Sum** approach to optimize subarray sum calculations. By precomputing the cumulative sums of the array, the sum of any subarray `[start, end]` can be computed in $O(1)$ time using the formula `prefix_sum[end + 1] - prefix_sum[start]`.

---

## Complexity Analysis
- **Time Complexity**: $O(n)$, where $n$ is the length of the input array. We iterate through the array once to build the prefix sum array and once more to calculate the total sum.
- **Space Complexity**: $O(n)$ to store the prefix sum array. This can be optimized to $O(1)$ if we calculate the subarray sums iteratively without an explicit prefix array, though $O(n)$ is standard for clarity.
