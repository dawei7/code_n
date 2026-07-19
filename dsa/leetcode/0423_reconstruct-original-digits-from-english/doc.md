# Reconstruct Original Digits from English

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 423 |
| Difficulty | Medium |
| Topics | Hash Table, Math, String |
| Official Link | [LeetCode](https://leetcode.com/problems/reconstruct-original-digits-from-english/) |

## Problem Description
### Goal
The English names of one or more decimal digits—`zero` through `nine`—were concatenated and all their lowercase letters shuffled. Given the resulting string, recover which digit occurrences supplied exactly that multiset of letters.

Return the reconstructed digits as one string sorted in ascending numerical order. Preserve multiplicity, so repeated digit names produce repeated output characters. The input guarantee ensures a valid reconstruction, and no letters may remain unused or be borrowed across incompatible names. The original name order is lost and does not affect the sorted result.

### Function Contract
**Inputs**

- `s`: a string containing exactly the shuffled letters of one or more English digit names from `zero` through `nine`

**Return value**

- Return a string containing every reconstructed digit with multiplicity, sorted from `0` to `9`.

### Examples
**Example 1**

- Input: `s = "owoztneoer"`
- Output: `"012"`

**Example 2**

- Input: `s = "fviefuro"`
- Output: `"45"`

**Example 3**

- Input: `s = "zerozero"`
- Output: `"00"`
