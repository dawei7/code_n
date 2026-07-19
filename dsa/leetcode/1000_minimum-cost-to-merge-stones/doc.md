# Minimum Cost to Merge Stones

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1000 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/minimum-cost-to-merge-stones/) |

## Problem Description

### Goal

There are `n` piles of stones arranged in a row, and `stones[i]` gives the number of stones in the $i$th pile. One move must select exactly `k` consecutive piles and replace them with a single pile.

The cost of a move is the total number of stones in the selected piles. Return the minimum total cost required to reduce the entire row to one pile. If the fixed merge size makes that final state impossible, return `-1`.

### Function Contract

**Inputs**

- `stones`: a list of $N$ pile sizes, where $1\le N\le30$ and $1\le\texttt{stones[i]}\le100$.
- `k`: the exact number $K$ of consecutive piles merged per move, where $2\le K\le30$.

**Return value**

- The minimum total merge cost needed to leave one pile, or `-1` when no legal sequence can do so.

### Examples

**Example 1**

- Input: `stones = [3, 2, 4, 1], k = 2`
- Output: `20`
- Explanation: Merge the first pair for $5$, the last pair for $5$, then the two remaining piles for $10$.

**Example 2**

- Input: `stones = [3, 2, 4, 1], k = 3`
- Output: `-1`
- Explanation: One merge leaves two piles, which cannot be merged by an exactly-three operation.

**Example 3**

- Input: `stones = [3, 5, 1, 2, 6], k = 3`
- Output: `25`
- Explanation: Merge `[5, 1, 2]` for $8$, then merge the remaining three piles for $17$.
