# Maximum OR

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2680 |
| Difficulty | Medium |
| Topics | Array, Greedy, Bit Manipulation, Prefix Sum |
| Official Link | [maximum-or](https://leetcode.com/problems/maximum-or/) |

## Problem Description & Examples
### Goal
Given an array of non-negative integers `nums` and an integer `k`, you are allowed to perform a single operation: choose one element `nums[i]` from the array and multiply it by `2^k`. After this operation (or choosing not to perform it), calculate the bitwise OR of all elements in the resulting array. The objective is to find the maximum possible bitwise OR value that can be achieved.

### Function Contract
**Inputs**

- `nums`: A list of non-negative integers. `1 <= len(nums) <= 10^5`, `0 <= nums[i] <= 10^9`.
- `k`: A non-negative integer representing the exponent for the multiplication factor. `0 <= k <= 30`.

**Return value**

- An integer representing the maximum possible bitwise OR sum of the array after performing at most one multiplication operation.

### Examples
**Example 1**

- Input: `nums = [12, 9], k = 1`
- Output: `26`
- Explanation:
  - Original OR: `12 | 9 = 13`.
  - Option 1: Multiply `12` by `2^1 = 2`. Array becomes `[24, 9]`. OR: `24 | 9 = 25`.
  - Option 2: Multiply `9` by `2^1 = 2`. Array becomes `[12, 18]`. OR: `12 | 18 = 26`.
  - The maximum OR value is `26`.

**Example 2**

- Input: `nums = [8, 1, 2], k = 2`
- Output: `35`
- Explanation:
  - `2^k = 2^2 = 4`.
  - Original OR: `8 | 1 | 2 = 11`.
  - Option 1: Multiply `8` by `4`. Array becomes `[32, 1, 2]`. OR: `32 | 1 | 2 = 35`.
  - Option 2: Multiply `1` by `4`. Array becomes `[8, 4, 2]`. OR: `8 | 4 | 2 = 14`.
  - Option 3: Multiply `2` by `4`. Array becomes `[8, 1, 8]`. OR: `8 | 1 | 8 = 9`.
  - The maximum OR value is `35`.

**Example 3**

- Input: `nums = [1, 2, 4, 8], k = 0`
- Output: `15`
- Explanation:
  - `2^k = 2^0 = 1`. Multiplying any element by 1 does not change its value.
  - The OR sum of the original array is `1 | 2 | 4 | 8 = 15`. This is the maximum possible.

---

## Underlying Base Algorithm(s)
The problem requires us to iterate through each element of the array and consider it as the candidate for multiplication by `2^k`. For each candidate, we need to calculate the bitwise OR of the modified element along with all other elements in the array. To efficiently calculate the OR sum of "all other elements" (i.e., all elements *except* the current candidate), we can use a technique involving **prefix OR sums** and **suffix OR sums**.

1.  **Prefix OR Array**: We compute an array `prefix_or` where `prefix_or[i]` stores the bitwise OR of all elements from `nums[0]` to `nums[i]`.
2.  **Suffix OR Array**: Similarly, we compute an array `suffix_or` where `suffix_or[i]` stores the bitwise OR of all elements from `nums[i]` to `nums[n-1]`.
3.  **Iterate and Calculate**: For each index `i` from `0` to `n-1`:
    *   Calculate the value of `nums[i]` after multiplication: `modified_val = nums[i] * (1 << k)`.
    *   Determine the OR sum of elements *before* `nums[i]`: This is `prefix_or[i-1]` if `i > 0`, otherwise `0`.
    *   Determine the OR sum of elements *after* `nums[i]`: This is `suffix_or[i+1]` if `i < n-1`, otherwise `0`.
    *   The total OR sum for this specific choice of `i` is `modified_val | (OR of elements before i) | (OR of elements after i)`.
    *   Keep track of the maximum OR sum found across all choices of `i`.

This approach allows us to calculate the OR sum of the remaining elements in O(1) time for each `i`, after initial O(N) pre-computation for prefix and suffix arrays.

## Complexity Analysis
- **Time Complexity**: `O(N)`
    - Calculating the `prefix_or` array takes `O(N)` time.
    - Calculating the `suffix_or` array takes `O(N)` time.
    - Iterating through the `nums` array to find the maximum OR sum, performing constant time OR operations for each element, takes `O(N)` time.
    - Overall, the dominant factor is `O(N)`.
- **Space Complexity**: `O(N)`
    - Storing the `prefix_or` array requires `O(N)` space.
    - Storing the `suffix_or` array requires `O(N)` space.
    - Overall, the space complexity is `O(N)`.
