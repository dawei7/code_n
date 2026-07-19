# Search in a Sorted Array of Unknown Size

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 702 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Interactive |
| Official Link | [LeetCode](https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/) |

## Problem Description
### Goal
An integer array is sorted in strictly increasing order, but its length is not available. You may read a position only through `ArrayReader.get(index)`, which returns the stored value for a valid non-negative index and a sentinel greater than every legal array value when the index is outside the array.

Given `target`, return its zero-based index if it occurs and `-1` otherwise. The search must discover a sufficient index range through the reader rather than relying on a supplied length, and it must treat the out-of-bounds sentinel as unavailable data rather than as a possible match.

### Function Contract
**Inputs**

- `reader`: the sorted values behind the unknown-size reader; app-local cases provide them as a list, while the native LeetCode method receives an `ArrayReader`
- `target`: the value to locate

**Return value**

- The zero-based index of `target`, or `-1` when it is absent

### Examples
**Example 1**

- Input: `reader = [-1,0,3,5,9,12], target = 9`
- Output: `4`

**Example 2**

- Input: `reader = [-1,0,3,5,9,12], target = 2`
- Output: `-1`

**Example 3**

- Input: `reader = [1,2,4,8,16], target = 16`
- Output: `4`
