# Find Champion II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2924 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-champion-ii/) |

## Problem Description

### Goal

There are $n$ tournament teams numbered from 0 through $n-1$. Each team is a
node in a directed acyclic graph, and every edge `[u, v]` states that team
`u` is stronger than team `v`. The supplied relation is consistent:
opposite strength edges cannot coexist, and transitive strength implications
are present.

A team is a champion when no other team is stronger than it. Return the team
number if exactly one champion exists. If more than one team has no stronger
team, return `-1`.

### Function Contract

**Inputs**

- `n`: The number of teams.
- `edges`: Directed stronger-to-weaker team pairs.

Let $m=\lvert\texttt{edges}\rvert$. The constraints are $1\le n\le100$
and $0\le m\le n(n-1)/2$. Every endpoint is a distinct valid team, the graph
is acyclic, and the strength relation is transitive.

**Return value**

- The unique champion's index, or `-1` if the champion is not unique.

### Examples

#### Example 1

- **Input:** `n = 3, edges = [[0, 1], [1, 2]]`
- **Output:** `0`
- **Explanation:** Teams 1 and 2 each have a stronger team, while team 0 does not.

#### Example 2

- **Input:** `n = 4, edges = [[0, 2], [1, 3], [1, 2]]`
- **Output:** `-1`
- **Explanation:** Neither team 0 nor team 1 has an incoming strength edge, so
  there is no unique champion.
