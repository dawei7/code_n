# Daily Temperatures

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_53` |
| Frontend ID | 739 |
| Difficulty | Medium |
| Topics | Array, Stack, Monotonic Stack |
| Official Link | [daily-temperatures](https://leetcode.com/problems/daily-temperatures/) |

## Problem Description & Examples
### Goal
Koko has `piles` of bananas and `h` hours to eat them all. She eats at speed `k` bananas/hour. Find the minimum integer `k` such that she can finish in `h` hours.

### Function Contract
**Inputs**

- `piles`: List[int] - banana pile sizes
- `h`: int - hours available

**Return value**

int - minimum eating speed k

### Examples
**Example 1**

- Input: `piles = [3, 6, 7, 11], h = 8`
- Output: `4`

**Example 2**

- Input: `piles = [50, 98], h = 15`
- Output: `10`

**Example 3**

- Input: `piles = [18, 73], h = 4`
- Output: `25`

---

## Underlying Base Algorithm(s)
- [Balanced parentheses / stack invariant](stack_01_balanced-parentheses.md)
- [Monotonic stack histogram](stack_04_largest-rectangle-in-histogram.md)
- [Trapping rain water](stack_06_trapping-rain-water.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(1)` auxiliary space, excluding the output object unless the output itself is the constructed result.
