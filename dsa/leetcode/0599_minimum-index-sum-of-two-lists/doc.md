# Minimum Index Sum of Two Lists

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 599 |
| Difficulty | Easy |
| Topics | Array, Hash Table, String |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-index-sum-of-two-lists/) |

## Problem Description
### Goal
Given two arrays of distinct strings, `list1` and `list2`, find their common strings. For a string appearing at `list1[i]` and `list2[j]`, define its index sum as $i + j$, using the string's position in each list.

Return every common string with the least index sum, in any order. More than one string may share that least sum, and all such ties must be included; common strings with a larger sum are excluded even when they rank highly in one list.

### Function Contract
**Inputs**

- `list1: list[str]`: the first preference list with distinct strings
- `list2: list[str]`: the second preference list with distinct strings

**Return value**

- Every common string minimizing `index_in_list1 + index_in_list2`
- Results may be returned in any order

### Examples
**Example 1**

- Input: `["Shogun","Tapioca Express","Burger King","KFC"]` and `["KFC","Shogun","Burger King"]`
- Output: `["Shogun"]`

**Example 2**

- Input: the same first list and `["KFC","Burger King","Tapioca Express","Shogun"]`
- Output: all four restaurant names in any order because every index sum is three

**Example 3**

- Input: `["happy","sad","good"]` and `["sad","happy","good"]`
- Output: `["happy","sad"]` in any order
