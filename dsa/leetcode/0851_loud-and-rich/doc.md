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

### Required Complexity
- **Time:** $O(n+m)$
- **Space:** $O(n+m)$

<details>
<summary>Approach</summary>

#### General

**Orient edges toward eligible richer people**

For every observation `[rich, poor]`, add `rich` to an adjacency list for `poor`. Following edges from a person now enumerates people definitely richer than that person. Logical consistency makes this directed graph acyclic.

**Memoize the quietest reachable representative**

Initialize `answer[person]` lazily. A depth-first search begins with the person themself as the best candidate. For every directly richer neighbor, recursively obtain that neighbor's already-complete answer. If its quietness value is smaller, replace the current candidate. Store the final person index before returning it.

Every definitely richer person is reachable along an observation chain. The recursion compares the quietest representative of each outgoing subgraph plus the starting person, so it selects the minimum quietness over exactly the eligible set. Conversely, it never visits an incomparable person. Unique `quiet` values ensure the selected index is unambiguous.

Memoization matters when richer subgraphs overlap: once a person's best representative is computed, all poorer descendants reuse it rather than traversing that subgraph again.

#### Complexity detail

Each of the $n$ people is completed once, and each of the $m$ directed observations is examined once during those searches. The time is $O(n+m)$. Adjacency lists, memoized answers, and a recursion stack of at most $n$ people use $O(n+m)$ space.

#### Alternatives and edge cases

- **Topological propagation:** Start with richest sources and propagate their quietest representative toward poorer neighbors in $O(n+m)$ time without recursion.
- **Fresh search for every person:** Running an independent DFS or BFS from each person is correct but can take $O(n(n+m))$ time.
- **Transitive-closure matrix:** Floyd–Warshall can determine every richer relation, but costs $O(n^3)$ time and $O(n^2)$ space.
- **No observations:** Each person's eligible set contains only themself, so every answer is its own index.
- **Single person:** The only output is `[0]`.
- **Incomplete comparisons:** A globally quieter person is irrelevant when no richer path proves that they have at least as much money.
- **Transitive relation:** A person reached through several richer edges is just as eligible as a direct neighbor.
- **Multiple richer branches:** Compare the memoized representative from every branch; the branches may later merge.
- **Quietness direction:** Smaller `quiet` values mean quieter people.
- **Unique quietness values:** No tie-breaking rule is needed.

</details>
