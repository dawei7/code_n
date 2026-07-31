# Chunk Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2677 |
| Difficulty | Easy |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| LeetCode | [Open problem](https://leetcode.com/problems/chunk-array/) |

## Problem Description

### Goal

Given a JSON-compatible array `arr` and a positive chunk size `size`, divide the array into consecutive subarrays while preserving every element's original order.

Every subarray should contain exactly `size` elements except, when the array length is not divisible by `size`, the final subarray may contain the remaining fewer elements. If `size` is larger than the array length, the entire nonempty array forms one chunk; an empty input produces an empty result. Do not use Lodash's `_.chunk` helper.

### Function Contract

**Inputs**

- `arr`: A valid JSON array. Its serialized representation has length from $2$ through $10^5$.
- `size`: An integer satisfying $1 \leq \texttt{size} \leq \texttt{arr.length} + 1$.

**Return value**

Return a new array of consecutive chunks whose concatenation is `arr` and whose lengths are at most `size`.

### Examples

**Example 1**

- Input: `arr = [1,2,3,4,5], size = 1`
- Output: `[[1],[2],[3],[4],[5]]`

**Example 2**

- Input: `arr = [1,9,6,3,2], size = 3`
- Output: `[[1,9,6],[3,2]]`

**Example 3**

- Input: `arr = [8,5,3,2,6], size = 6`
- Output: `[[8,5,3,2,6]]`

**Example 4**

- Input: `arr = [], size = 1`
- Output: `[]`
