# Merge Operations to Turn Array Into a Palindrome

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2422 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Merge Operations to Turn Array Into a Palindrome](https://leetcode.com/problems/merge-operations-to-turn-array-into-a-palindrome/) |

## Problem Description

### Goal

You are given an array `nums` containing positive integers. In one operation, choose any two adjacent elements, remove both of them, and insert their sum at the same position. The array becomes one element shorter after every operation.

Find the minimum number of operations needed to make the resulting array a palindrome. The chosen merges may occur anywhere, and an array with one element already satisfies the palindrome condition.

### Function Contract

**Inputs**

- `nums`: A list of positive integers.

The constraints are $1 \le \lvert\texttt{nums}\rvert \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^6$.

**Return value**

- The minimum number of adjacent-pair merge operations required to obtain a palindrome.

### Examples

#### Example 1

- **Input:** `nums = [4,3,2,1,2,3,1]`
- **Output:** `2`

Merging `1 + 2` and then `3 + 1` can produce `[4,3,2,3,4]`.

#### Example 2

- **Input:** `nums = [1,2,3,4]`
- **Output:** `3`

No multi-element palindromic partition is possible, so three merges reduce the array to the singleton `[10]`.

#### Example 3

- **Input:** `nums = [1,2,3,2,1]`
- **Output:** `0`

The original array is already a palindrome.
