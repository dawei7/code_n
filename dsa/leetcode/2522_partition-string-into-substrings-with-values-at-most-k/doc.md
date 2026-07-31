# Partition String Into Substrings With Values at Most K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2522 |
| Difficulty | Medium |
| Topics | String, Dynamic Programming, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/partition-string-into-substrings-with-values-at-most-k/) |

## Problem Description
### Goal
You are given a string `s` containing decimal digits from `1` through `9` and a positive integer `k`. Partition `s` into one or more contiguous, nonempty substrings. Every digit must belong to exactly one substring, so the substrings retain their original order and concatenate back to `s`.

A partition is good when the decimal value represented by every substring is at most `k`. Return the minimum possible number of substrings in a good partition. If even one digit is greater than `k`, no valid partition can contain it, so return `-1`.

### Function Contract
**Inputs**

- `s`: A string of $n$ characters, each from `1` through `9`, where $1 \le n \le 10^5$.
- `k`: The maximum permitted substring value, where $1 \le k \le 10^9$.

**Return value**

Return the minimum number of substrings in a good partition, or `-1` if no good partition exists.

### Examples
**Example 1**

- Input: `s = "165462", k = 60`
- Output: `4`
- Explanation: One minimum partition is `"16"`, `"54"`, `"6"`, `"2"`.

**Example 2**

- Input: `s = "238182", k = 5`
- Output: `-1`
- Explanation: The digit `8` is already greater than `k`, so no good partition exists.
