# Array Transformation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1243 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/array-transformation/) |

## Problem Description

### Goal

You are given an integer array `arr`. Repeatedly transform all interior elements simultaneously. If an element is strictly smaller than both immediate neighbors, increase it by one; if it is strictly larger than both neighbors, decrease it by one. Every other element remains unchanged.

The first and last elements never change. Each round must use the values from the beginning of that round, so an update cannot influence another update until the next round. Continue until an entire round makes no change, then return the resulting stable array.

### Function Contract

**Inputs**

- `arr`: A list of $n$ integers, where $3\le n\le100$ and $1\le\texttt{arr[i]}\le100$.

Let $C$ be the total number of individual element updates made before the array stabilizes.

**Return value**

- The stable array obtained after applying the simultaneous transformation until no element changes.

### Examples

**Example 1**

- Input: `arr = [6,2,3,4]`
- Output: `[6,3,3,4]`

The value `2` is a strict valley and rises once; the next round makes no change.

**Example 2**

- Input: `arr = [1,6,3,4,3,5]`
- Output: `[1,4,4,4,4,5]`

Several peaks and valleys change across multiple simultaneous rounds.

**Example 3**

- Input: `arr = [1,2,3,4]`
- Output: `[1,2,3,4]`

A monotone array has no strict interior extremum and is already stable.
