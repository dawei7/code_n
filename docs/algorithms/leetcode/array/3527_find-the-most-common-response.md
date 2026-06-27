# Find the Most Common Response

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3527 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String, Counting |
| Official Link | [find-the-most-common-response](https://leetcode.com/problems/find-the-most-common-response/) |

## Problem Description & Examples
### Goal
Given a list of strings representing user responses, identify the string that appears with the highest frequency. If multiple strings share the same maximum frequency, return the one that is lexicographically smallest.

### Function Contract
**Inputs**

- `responses`: A list of strings (`List[str]`) representing the collected responses.

**Return value**

- A string (`str`) representing the most frequent response, or the lexicographically smallest one in case of a tie.

### Examples
**Example 1**

- Input: `["apple", "banana", "apple", "cherry", "banana"]`
- Output: `"apple"`

**Example 2**

- Input: `["cat", "dog", "cat", "dog"]`
- Output: `"cat"`

**Example 3**

- Input: `["a", "b", "c", "a", "b", "c"]`
- Output: `"a"`

---

## Underlying Base Algorithm(s)
The problem is solved using a Hash Map (dictionary in Python) to perform frequency counting. By iterating through the list once, we build a mapping of strings to their respective counts. We then iterate through the map to find the key with the maximum value, applying a tie-breaking condition based on lexicographical order.

---

## Complexity Analysis
- **Time Complexity**: `O(N * K)`, where `N` is the number of responses and `K` is the average length of a string. We iterate through the list once to count and once through the unique keys to find the maximum.
- **Space Complexity**: `O(N * K)` to store the frequency map containing all unique strings.
