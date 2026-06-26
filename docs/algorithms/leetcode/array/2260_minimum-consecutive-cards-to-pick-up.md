# Minimum Consecutive Cards to Pick Up

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2260 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Sliding Window |
| Official Link | [minimum-consecutive-cards-to-pick-up](https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/) |

## Problem Description & Examples
### Goal
Choose the shortest contiguous group of cards containing at least two cards with the same value.

### Function Contract
**Inputs**

- `cards`: card values in order.

**Return value**

The minimum number of cards in a qualifying segment, or `-1` if no value repeats.

### Examples
**Example 1**

- Input: `cards = [3, 4, 2, 3, 4, 7]`
- Output: `4`

**Example 2**

- Input: `cards = [1, 0, 5, 3]`
- Output: `-1`

**Example 3**

- Input: `cards = [1, 1]`
- Output: `2`

---

## Underlying Base Algorithm(s)
Track the most recent index of each card value. On seeing a repeated value at index `i`, the shortest segment ending there starts at its previous occurrence and has length `i - previous + 1`. Minimize these lengths and update the stored index.

---

## Complexity Analysis
- **Time Complexity**: `O(n)` expected
- **Space Complexity**: `O(n)`
