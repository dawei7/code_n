# Corporate Flight Bookings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1109 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/corporate-flight-bookings/) |

## Problem Description

### Goal

There are `n` flights labeled consecutively from `1` through `n`. You receive `bookings`, where each entry `[first, last, seats]` records that `seats` seats were reserved on every flight from `first` through `last`, inclusive.

Several bookings may overlap, so a flight's final reservation count is the sum of every booking range that contains its label. Return an array `answer` of length `n` in flight-label order: `answer[i]` is the total number of seats reserved for flight `i + 1`.

### Function Contract

**Inputs**

- `bookings`: $B$ rows `[first, last, seats]`, with `1 <= first <= last <= n` and a positive `seats` value.
- `n`: the number of flights, labeled from `1` through `n`.

**Return value**

- An integer array of length $n$ whose zero-based position `i` contains the total reserved seats for flight `i + 1`.

### Examples

**Example 1**

- Input: `bookings = [[1,2,10],[2,3,20],[2,5,25]]`, `n = 5`
- Output: `[10,55,45,25,25]`

The first booking adds 10 to flights 1 and 2, the second adds 20 to flights 2 and 3, and the third adds 25 to flights 2 through 5. Adding those contributions by flight gives the output.

**Example 2**

- Input: `bookings = [[1,2,10],[2,2,15]]`, `n = 2`
- Output: `[10,25]`
