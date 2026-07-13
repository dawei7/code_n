# Maximum Total Beauty of the Gardens

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2234 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Two Pointers, Binary Search, Greedy, Sorting, Enumeration, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-total-beauty-of-the-gardens](https://leetcode.com/problems/maximum-total-beauty-of-the-gardens/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-total-beauty-of-the-gardens/).

### Goal
Distribute at most `newFlowers` among gardens. A garden reaching `target` flowers is complete and contributes `full` beauty. If any gardens remain incomplete, they collectively add `partial` times the minimum flower count among them. Maximize total beauty.

### Function Contract
**Inputs**

- `flowers`: current flower counts.
- `newFlowers`: the available additional flowers.
- `target`: the completion threshold.
- `full`: beauty per complete garden.
- `partial`: multiplier for the minimum incomplete count.

**Return value**

The maximum total beauty obtainable.

### Examples
**Example 1**

- Input: `flowers = [1, 3, 1, 1]`, `newFlowers = 7`, `target = 6`, `full = 12`, `partial = 1`
- Output: `14`

**Example 2**

- Input: `flowers = [2, 4, 5, 3]`, `newFlowers = 10`, `target = 5`, `full = 2`, `partial = 6`
- Output: `30`

**Example 3**

- Input: `flowers = [5, 5]`, `newFlowers = 0`, `target = 5`, `full = 10`, `partial = 1`
- Output: `20`

---

## Solution
### Approach
Cap flower counts at `target` and sort them. Consider each possible number of gardens made complete, paying from the largest incomplete counts downward. For the remaining incomplete prefix, use prefix sums and binary search to find the greatest common minimum below `target` affordable with the leftover flowers. Combine that partial beauty with the complete-garden contribution and maximize over all choices.

### Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)` for sorted values and prefix sums

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
