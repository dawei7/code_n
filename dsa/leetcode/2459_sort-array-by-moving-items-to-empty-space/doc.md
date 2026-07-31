# Sort Array by Moving Items to Empty Space

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2459 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sort-array-by-moving-items-to-empty-space/) |

## Problem Description

### Goal

You are given an integer array `nums` of length $n$ containing every value from $0$ through $n-1$ exactly once. Values $1$ through $n-1$ represent numbered items, while `0` represents one empty space.

In one operation, choose any item and move it into the empty position; the item's previous position becomes the new empty space. The array is sorted when all item numbers appear in ascending order and the empty space is at either end. Thus the two valid final layouts are `[0, 1, ..., n - 1]` and `[1, 2, ..., n - 1, 0]`.

Return the minimum number of operations required to reach either valid layout.

### Function Contract

**Inputs**

- `nums`: A permutation of every integer from $0$ through $n-1$.

The array length satisfies $2\le n\le10^5$.

**Return value**

- The minimum number of moves into the empty space needed to produce either sorted layout.

### Examples

**Example 1**

- Input: `nums = [4, 2, 0, 3, 1]`
- Output: `3`
- Explanation: Moving items `2`, `1`, and `4` into the successive empty positions produces `[0, 1, 2, 3, 4]`.

**Example 2**

- Input: `nums = [1, 2, 3, 4, 0]`
- Output: `0`
- Explanation: The items are already ascending with the empty space at the end.

**Example 3**

- Input: `nums = [1, 0, 2, 4, 3]`
- Output: `2`
- Explanation: Two moves can produce `[1, 2, 3, 4, 0]`.
