# Find the Array Concatenation Value

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2562 |
| Difficulty | Easy |
| Topics | Array, Two Pointers, Simulation |
| Official Link | [find-the-array-concatenation-value](https://leetcode.com/problems/find-the-array-concatenation-value/) |

## Problem Description & Examples
### Goal
The objective is to calculate the "concatenation value" of an array by repeatedly pairing the first and last elements. If the array has more than one element, the first and last are concatenated as strings and converted back to an integer. If only one element remains, that element is added to the total as-is. This process continues until the array is empty.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`).

**Return value**

- An integer representing the total sum of all concatenation values calculated during the process.

### Examples
**Example 1**

- Input: `nums = [7,52,2,4]`
- Output: `596`
- Explanation: (7 concatenated with 4 = 74) + (52 concatenated with 2 = 522) = 596.

**Example 2**

- Input: `nums = [5,14,13,8,12]`
- Output: `673`
- Explanation: (5 concatenated with 12 = 512) + (14 concatenated with 8 = 148) + (13) = 673.

**Example 3**

- Input: `nums = [1]`
- Output: `1`

---

## Underlying Base Algorithm(s)
The problem is solved using a **Two Pointers** approach. By maintaining a pointer at the start (`left`) and the end (`right`) of the array, we can simulate the pairing process in a single pass. String conversion is used to perform the concatenation, followed by integer casting.

---

## Complexity Analysis
- **Time Complexity**: `O(N)`, where `N` is the number of elements in the array. We iterate through the array once, processing each element exactly once.
- **Space Complexity**: `O(K)`, where `K` is the number of digits in the integers, as string concatenation and conversion create temporary objects proportional to the number of digits.
