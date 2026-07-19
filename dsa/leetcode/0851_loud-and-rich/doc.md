# Loud and Rich

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 851 |
| Difficulty | Medium |
| Topics | Array, Depth-First Search, Graph Theory, Topological Sort |
| Official Link | [LeetCode](https://leetcode.com/problems/loud-and-rich/) |

## Problem Description
### Goal
There are $n$ people labeled from $0$ through $n-1$. Their money amounts are all different, and their quietness values are also unique. A pair `[a, b]` in `richer` states that person `a` has more money than person `b`. The observations are logically consistent, so their direct and transitive implications never make two people richer than each other.

For every person `x`, consider `x` plus everyone who is definitely richer than `x` through one or more observations. Set `answer[x]` to the person in that set with the smallest quietness value. Relations not implied by the given pairs must not be assumed. Return the complete `answer` array.

### Function Contract
**Inputs**

- `richer`: an array of $m$ unique pairs `[a, b]`, where $0 \leq m \leq n(n-1)/2$ and each pair means that `a` is richer than `b`.
- `quiet`: an array of $n$ unique integers, where $1 \leq n \leq 500$ and $0 \leq \texttt{quiet[i]} < n$.

**Return value**

Return an array of length $n$ whose entry for each person identifies the quietest person known to have at least as much money, including the person themself.

### Examples
**Example 1**

- Input: `richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet = [3,2,5,4,6,1,7,0]`
- Output: `[5,5,2,5,4,5,6,7]`

For person `0`, person `5` is transitively richer through `3` and `1` and has the smallest quietness value among all definitely eligible people.

**Example 2**

- Input: `richer = [], quiet = [0]`
- Output: `[0]`

**Example 3**

- Input: `richer = [[1,0],[2,1]], quiet = [2,1,0]`
- Output: `[2,2,2]`

Person `2` is richer than everyone through the chain and is also quietest.
