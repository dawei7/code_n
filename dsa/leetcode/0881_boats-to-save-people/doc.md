# Boats to Save People

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 881 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, Greedy, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/boats-to-save-people/) |

## Problem Description
### Goal
Each entry `people[i]` is one person's weight. There is an unlimited supply of boats, every boat has maximum total weight `limit`, and no boat may carry more than two people at once. Two people can share only when their combined weight is at most the limit.

Find the minimum number of boats required to carry every person. Each person must be assigned to exactly one boat, and every individual weight is guaranteed not to exceed `limit`.

### Function Contract
**Inputs**

- `people`: an array of $n$ weights, where $1 \leq n \leq 5\cdot10^4$ and $1 \leq \texttt{people[i]} \leq \texttt{limit}$.
- `limit`: the capacity of each boat, where $1 \leq \texttt{limit} \leq 3\cdot10^4$.

**Return value**

Return the minimum number of capacity-respecting boats needed when each boat carries at most two people.

### Examples
**Example 1**

- Input: `people = [1,2], limit = 3`
- Output: `1`

Both people fit together.

**Example 2**

- Input: `people = [3,2,2,1], limit = 3`
- Output: `3`

One possible assignment is `(1,2)`, `(2)`, and `(3)`.

**Example 3**

- Input: `people = [3,5,3,4], limit = 5`
- Output: `4`

No two weights can share a boat.
