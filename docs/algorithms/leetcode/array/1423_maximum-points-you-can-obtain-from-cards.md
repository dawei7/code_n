# Maximum Points You Can Obtain from Cards

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1423 |
| Difficulty | Medium |
| Topics | Array, Sliding Window, Prefix Sum |
| Official Link | [maximum-points-you-can-obtain-from-cards](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/) |

## Problem Description & Examples
### Goal
Take exactly `k` cards from either the left end or right end of the row. Maximize the sum of the taken card points.

### Function Contract
**Inputs**

- `cardPoints`: a list of card values.
- `k`: the number of cards that must be taken.

**Return value**

The maximum total points obtainable by taking `k` end cards.

### Examples
**Example 1**

- Input: `cardPoints = [1,2,3,4,5,6,1], k = 3`
- Output: `12`

**Example 2**

- Input: `cardPoints = [2,2,2], k = 2`
- Output: `4`

**Example 3**

- Input: `cardPoints = [9,7,7,9,7,7,9], k = 7`
- Output: `55`

---

## Underlying Base Algorithm(s)
Complement sliding window. Taking `k` cards from the ends is the same as leaving one contiguous middle block of length `n - k`; minimize that block's sum and subtract it from the total.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
