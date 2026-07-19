# Create Target Array in the Given Order

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1389 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/create-target-array-in-the-given-order/) |

## Problem Description

### Goal

Two arrays, `nums` and `index`, have the same length. Start with an empty target array and process their entries from left to right. At step `i`, insert `nums[i]` at position `index[i]` in the target as it exists at that moment.

The supplied position is always valid for the current target, so $0 \le \texttt{index[i]} \le i$. Inserting before an existing position shifts that element and every later element one place to the right. Return the target after every insertion has been performed.

### Function Contract

**Inputs**

- `nums`: an integer array of length $n$, with $1 \le n \le 100$.
- `index`: an array of $n$ insertion positions, where `index[i]` is valid after the first `i` operations.

**Return value**

- The final array produced by applying the insertions in input order.

### Examples

**Example 1**

- Input: `nums = [0,1,2,3,4], index = [0,1,2,2,1]`
- Output: `[0,4,1,3,2]`

**Example 2**

- Input: `nums = [1,2,3,4,0], index = [0,1,2,3,0]`
- Output: `[0,1,2,3,4]`

**Example 3**

- Input: `nums = [1], index = [0]`
- Output: `[1]`
