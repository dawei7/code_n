# Merge Similar Items

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2363 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/merge-similar-items/) |

## Problem Description

### Goal

Two arrays, `items1` and `items2`, describe sets of items. Every entry has the
form `[value, weight]`, and each value occurs at most once within either input
array, although it may occur once in both arrays.

Combine entries having the same value by summing their weights. Return one
`[value, total_weight]` pair for every value present in either input, ordered
by value in ascending order.

### Function Contract

**Inputs**

- `items1`: Unique-value item pairs from the first set.
- `items2`: Unique-value item pairs from the second set.

Each array has between 1 and 1000 pairs. Every value and weight is between 1
and 1000. Let $n$ be the combined number of pairs and $V=1000$ be the maximum
legal value.

**Return value**

Return merged `[value, weight]` pairs in ascending value order, with each
weight equal to the sum of all input weights for that value.

### Examples

**Example 1**

- Input: `items1 = [[1,1],[4,5],[3,8]], items2 = [[3,1],[1,5]]`
- Output: `[[1,6],[3,9],[4,5]]`

**Example 2**

- Input: `items1 = [[1,1],[3,2],[2,3]], items2 = [[2,1],[3,2],[1,3]]`
- Output: `[[1,4],[2,4],[3,4]]`

**Example 3**

- Input: `items1 = [[1,3],[2,2]], items2 = [[7,1],[2,2],[1,4]]`
- Output: `[[1,7],[2,4],[7,1]]`
