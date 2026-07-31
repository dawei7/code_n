# Distribute Elements Into Two Arrays I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3069 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/distribute-elements-into-two-arrays-i/) |

## Problem Description

### Goal

You are given a conceptually one-indexed array `nums` containing $n$ distinct integers. Distribute every value between two initially empty arrays, `arr1` and `arr2`, in exactly $n$ operations.

Append `nums[1]` to `arr1` in the first operation and `nums[2]` to `arr2` in the second. For every later position $i$, compare the two arrays' last values. If the last value of `arr1` is greater than the last value of `arr2`, append `nums[i]` to `arr1`; otherwise, append it to `arr2`.

Form `result` by concatenating the completed `arr1` followed by the completed `arr2`, and return that array.

### Function Contract

**Inputs**

- `nums`: An array of $n$ distinct integers. The function's language-native list uses zero-based storage even though the operation description numbers positions from $1$.

The constraints are $3 \le n \le 50$, $1 \le \texttt{nums[i]} \le 100$, and all values in `nums` are distinct.

**Return value**

Return the final contents of `arr1` followed immediately by the final contents of `arr2`.

### Examples

**Example 1**

- Input: `nums = [2, 1, 3]`
- Output: `[2, 3, 1]`
- Explanation: The initial arrays are `[2]` and `[1]`. Since `2 > 1`, append `3` to the first array before concatenation.

**Example 2**

- Input: `nums = [5, 4, 3, 8]`
- Output: `[5, 3, 4, 8]`
- Explanation: Append `3` to the first array because `5 > 4`; then append `8` to the second because its last value `4` is greater than the first array's last value `3`.
