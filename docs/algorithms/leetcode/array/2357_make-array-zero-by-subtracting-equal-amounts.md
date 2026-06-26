# Make Array Zero by Subtracting Equal Amounts

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2357 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Greedy, Sorting, Heap (Priority Queue), Simulation |
| Official Link | [make-array-zero-by-subtracting-equal-amounts](https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/) |

## Problem Description & Examples
### Goal
Given an array of non-negative integers, we want to find the minimum number of operations required to make all elements in the array equal to zero. In a single operation, we must:
1. Choose a positive integer `x` that is less than or equal to the smallest non-zero element in the array.
2. Subtract `x` from every positive element in the array.

### Function Contract
**Inputs**

- `nums`: `List[int]` - An array of non-negative integers.

**Return value**

- `int` - The minimum number of operations to reduce all elements in `nums` to zero.

### Examples
**Example 1**

- Input: `nums = [1, 5, 0, 3, 5]`
- Output: `3`
- Explanation:
  1. The smallest positive element is 1. Subtract 1 from all positive elements: `[0, 4, 0, 2, 4]`.
  2. The smallest positive element is 2. Subtract 2 from all positive elements: `[0, 2, 0, 0, 2]`.
  3. The smallest positive element is 2. Subtract 2 from all positive elements: `[0, 0, 0, 0, 0]`.
  Total operations = 3.

**Example 2**

- Input: `nums = [0]`
- Output: `0`
- Explanation: All elements are already zero, so no operations are needed.

**Example 3**

- Input: `nums = [1, 2, 3, 4]`
- Output: `4`
- Explanation: There are 4 unique positive numbers, so it takes 4 operations.

---

## Underlying Base Algorithm(s)
The optimal strategy is to always choose `x` as the minimum positive element in the array at each step. 

When we subtract the minimum positive element from all positive elements:
1. The smallest positive element becomes zero.
2. All other positive elements are reduced but remain positive and distinct from each other.
3. Elements that were already equal remain equal.

This means that each unique positive number in the original array will require exactly one operation to be reduced to zero. Elements that are already zero do not require any operations. Thus, the problem reduces to finding the number of unique strictly positive integers in the input array.

We can solve this efficiently by:
1. Filtering out all zeros from the array.
2. Inserting the remaining positive elements into a hash set to find the unique values.
3. Returning the size of this set.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ where $N$ is the number of elements in `nums`. We iterate through the array once to filter and insert elements into the hash set.
- **Space Complexity**: $\mathcal{O}(N)$ to store the unique positive elements in the hash set.
