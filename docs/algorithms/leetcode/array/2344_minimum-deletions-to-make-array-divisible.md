# Minimum Deletions to Make Array Divisible

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2344 |
| Difficulty | Hard |
| Topics | Array, Math, Sorting, Heap (Priority Queue), Number Theory |
| Official Link | [minimum-deletions-to-make-array-divisible](https://leetcode.com/problems/minimum-deletions-to-make-array-divisible/) |

## Problem Description & Examples
### Goal
You are given two arrays of positive integers, `nums` and `numsDivide`. Your objective is to determine the minimum number of elements you must delete from the beginning of `nums` such that the smallest remaining element in `nums` can perfectly divide every single element in `numsDivide`. If no such element exists in `nums` that satisfies this condition, return -1.

### Function Contract
**Inputs**

- `nums`: A list of integers, representing the array from which elements can be deleted. `1 <= nums.length <= 10^5`, `1 <= nums[i] <= 10^9`.
- `numsDivide`: A list of integers, representing the array whose elements must be divisible by a chosen number from `nums`. `1 <= numsDivide.length <= 10^5`, `1 <= numsDivide[i] <= 10^9`.

**Return value**

An integer representing the minimum number of deletions required from `nums`, or -1 if no solution is possible.

### Examples
**Example 1**

- Input: `nums = [2,3,2,4,3]`, `numsDivide = [9,6,9,3,15]`
- Output: `2`
- Explanation:
  1. Calculate the GCD of `numsDivide`: `gcd(9,6,9,3,15) = 3`.
  2. Sort `nums`: `[2,2,3,3,4]`.
  3. Iterate through sorted `nums`:
     - `2` does not divide `3`.
     - `2` does not divide `3`.
     - `3` divides `3`. This is the first element that satisfies the condition. It is at index 2 in the sorted array, meaning 2 deletions (the two '2's) are needed.

**Example 2**

- Input: `nums = [4,3,6]`, `numsDivide = [8,2,6]`
- Output: `-1`
- Explanation:
  1. Calculate the GCD of `numsDivide`: `gcd(8,2,6) = 2`.
  2. Sort `nums`: `[3,4,6]`.
  3. Iterate through sorted `nums`:
     - `3` does not divide `2`.
     - `4` does not divide `2`.
     - `6` does not divide `2`.
  4. No element in `nums` divides `2`. Return -1.

**Example 3**

- Input: `nums = [10,20,30]`, `numsDivide = [100,200]`
- Output: `0`
- Explanation:
  1. Calculate the GCD of `numsDivide`: `gcd(100,200) = 100`.
  2. Sort `nums`: `[10,20,30]`.
  3. Iterate through sorted `nums`:
     - `10` divides `100`. This is the first element that satisfies the condition. It is at index 0, meaning 0 deletions are needed.

---

## Underlying Base Algorithm(s)
1.  **Greatest Common Divisor (GCD):** A number `x` divides all elements in `numsDivide` if and only if `x` divides the greatest common divisor (GCD) of all elements in `numsDivide`. This property simplifies the problem significantly, as we only need to check divisibility against a single value (the GCD of `numsDivide`) instead of every element in `numsDivide`.
2.  **Sorting:** To find the *minimum* number of deletions, we need to find the *smallest* element in `nums` that satisfies the divisibility condition. By sorting `nums` in ascending order, we can iterate through it and the first element we encounter that satisfies the condition will correspond to the minimum number of deletions (its index in the sorted array).

---

## Complexity Analysis
- **Time Complexity**: `O(N_divide * log(max(numsDivide)) + N_nums * log(N_nums))`
    - Calculating the GCD of `numsDivide`: This involves iterating through `numsDivide` and repeatedly applying the `gcd` function. For `N_divide` elements, where each `gcd(a, b)` operation takes `O(log(min(a, b)))` time, the total time is `O(N_divide * log(max(numsDivide)))`.
    - Sorting `nums`: Using an efficient sorting algorithm like Timsort (Python's default) takes `O(N_nums * log(N_nums))` time, where `N_nums` is the length of `nums`.
    - Iterating through sorted `nums`: In the worst case, we iterate through all `N_nums` elements. Each check (`g % num == 0`) is `O(1)`. This takes `O(N_nums)` time.
    - Combining these, the dominant terms are the GCD calculation and sorting.
- **Space Complexity**: `O(N_nums)`
    - Sorting `nums`: Python's `list.sort()` (Timsort) typically uses `O(N_nums)` auxiliary space in the worst case.
    - Storing the GCD value: `O(1)`.
    - Overall, the space complexity is dominated by the sorting process.
