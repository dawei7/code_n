# Substring XOR Queries

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2564 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String, Bit Manipulation |
| Official Link | [substring-xor-queries](https://leetcode.com/problems/substring-xor-queries/) |

## Problem Description & Examples
### Goal
Given a binary string `s` and a list of integer pairs `queries`, determine the shortest substring of `s` that, when interpreted as a binary number, satisfies the equation `substring_val ^ first_val = second_val`. For each query `[first, second]`, return the starting and ending indices `[left, right]` of the first such occurrence. If no such substring exists, return `[-1, -1]`.

### Function Contract
**Inputs**

- `s`: A string consisting of '0' and '1' characters.
- `queries`: A list of lists, where each inner list contains two integers `[first, second]`.

**Return value**

- A list of lists, where each element is the `[left, right]` index pair for the corresponding query, or `[-1, -1]` if no match is found.

### Examples
**Example 1**

- Input: `s = "101101", queries = [[0,5],[1,2]]`
- Output: `[[0,2],[2,3]]`

**Example 2**

- Input: `s = "0", queries = [[0,0]]`
- Output: `[[0,0]]`

**Example 3**

- Input: `s = "1", queries = [[4,5]]`
- Output: `[[-1,-1]]`

---

## Underlying Base Algorithm(s)
The problem relies on the property that `val ^ first = second` is equivalent to `val = first ^ second`. Since the maximum value of `second` is $10^9$, the binary representation of `val` will not exceed 30 bits. We can pre-process all substrings of `s` that have a length up to 30, store their decimal values in a hash map (mapping value to the first occurrence `[left, right]`), and then answer each query in $O(1)$ time.

## Complexity Analysis
- **Time Complexity**: $O(N \cdot L + Q)$, where $N$ is the length of string `s`, $L$ is the maximum bit length (30), and $Q$ is the number of queries.
- **Space Complexity**: $O(N \cdot L)$ to store the hash map of substring values.
