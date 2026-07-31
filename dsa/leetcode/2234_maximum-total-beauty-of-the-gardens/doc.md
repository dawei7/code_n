# Maximum Total Beauty of the Gardens

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2234 |
| Difficulty | Hard |
| Topics | Array, Two Pointers, Binary Search, Greedy, Sorting, Enumeration, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-total-beauty-of-the-gardens/) |

## Problem Description

### Goal

Alice cares for `n` gardens, and `flowers[i]` gives the number already planted in garden `i`. Existing flowers cannot be removed. She may distribute at most `newFlowers` additional flowers among the gardens.

A garden is complete once it contains at least `target` flowers. Every complete garden contributes `full` beauty. If at least one garden remains incomplete, the incomplete group additionally contributes its minimum flower count multiplied by `partial`; this contribution is zero when all gardens are complete. Return the maximum total beauty Alice can obtain. She may leave flowers unused when completing another garden would reduce the more valuable incomplete-garden contribution.

### Function Contract

**Inputs**

- `flowers`: A nonempty list of positive initial flower counts.
- `newFlowers`: The maximum number of additional flowers available.
- `target`: The flower count at which a garden becomes complete.
- `full`: The beauty contributed by each complete garden.
- `partial`: The multiplier applied to the minimum incomplete flower count.

Let $n=\lvert\texttt{flowers}\rvert$. The list length and `target` are at most $10^5$, while `newFlowers` can be as large as $10^{10}$.

**Return value**

Return the greatest possible sum of complete-garden beauty and, when applicable, incomplete-garden minimum beauty.

### Examples

**Example 1**

- Input: `flowers = [1, 3, 1, 1], newFlowers = 7, target = 6, full = 12, partial = 1`
- Output: `14`

**Example 2**

- Input: `flowers = [2, 4, 5, 3], newFlowers = 10, target = 5, full = 2, partial = 6`
- Output: `30`

**Example 3**

- Input: `flowers = [5, 5], newFlowers = 1, target = 5, full = 10, partial = 1`
- Output: `20`
