# Maximum Number of Accepted Invitations

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/maximum-number-of-accepted-invitations/) |
| Frontend ID | 1820 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Depth-First Search, Graph Theory, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

A party has $m$ boys and $n$ girls. The binary matrix `grid` describes which invitations can be accepted: `grid[i][j] = 1` means boy `i` may invite girl `j` and she would accept, while zero means that pairing is unavailable.

Each boy may send an invitation to at most one girl, and each girl may accept an invitation from at most one boy. Choose compatible boy-girl pairs subject to both exclusivity rules and return the greatest number of invitations that can be accepted simultaneously.

### Function Contract

**Inputs**

- `grid`: an $m\times n$ binary matrix, where $1 \le m,n \le 200$.
- `grid[i][j]` is 1 exactly when the edge from boy `i` to girl `j` is available.

**Return value**

- Return the maximum number of pairwise non-conflicting available boy-girl matches.

### Examples

**Example 1**

- Input: `grid = [[1,1,1],[1,0,1],[0,0,1]]`
- Output: `3`

All three boys can be paired with different acceptable girls.

**Example 2**

- Input: `grid = [[1,0,1,0],[1,0,0,0],[0,0,1,0],[1,1,1,0]]`
- Output: `3`

The fourth girl has no incident edge, but three non-conflicting invitations can still be accepted.

### Required Complexity

- **Time:** $O(m^2n)$
- **Space:** $O(m+n)$

<details>
<summary>Approach</summary>

#### General

**View accepted invitations as a bipartite matching**

Boys form one vertex partition and girls the other; every 1 in `grid` is an edge. An accepted set cannot reuse a vertex, so it is exactly a matching. Store, for each girl, the boy currently matched to her, or `-1` when she is free.

**Search for an augmenting path from every boy**

For one boy, run depth-first search across acceptable girls not yet visited during this attempt. A free girl can be matched immediately. If a girl is occupied, recursively try to move her current boy to another acceptable girl. When that succeeds, assign the newly freed girl to the requesting boy. Use a fresh visited-girl array for each outer attempt so later boys may reconsider paths while cycles within one attempt are avoided.

**Why every successful search increases an optimal matching**

A successful recursion traces an alternating path whose edges switch between unmatched and matched. Reversing their status adds the starting boy and ends at a previously free girl, increasing matching size by one without duplicating any endpoint. If no augmenting path exists from any remaining unmatched boy, the augmenting-path characterization of bipartite matching says the current matching is maximum. Processing every boy therefore returns the largest feasible invitation count.

#### Complexity detail

Let $E\le mn$ be the number of 1-cells. One augmenting search visits each girl at most once and scans adjacency rows reached through matched boys, costing $O(E)$ in the worst case. Running it for all $m$ boys costs $O(mE)\subseteq O(m^2n)$. The girl-match array, one visited array, and recursive boy path use $O(m+n)$ space.

#### Alternatives and edge cases

- **Choose the first free girl greedily:** It can strand a later boy whose only option was taken; augmenting paths repair exactly this failure.
- **Bitmask dynamic programming:** It is exact for a small number of girls, but its $O(m2^n)$ state space is infeasible when $n$ reaches 200.
- **Maximum-flow network:** Source/boy/girl/sink capacities produce the same answer, but a dedicated bipartite matcher is simpler here.
- **All-zero matrix:** No augmenting search succeeds, so return zero.
- **Rectangular matrix:** The answer is at most $\min(m,n)$; the algorithm does not require equal partition sizes.
- **One girl acceptable to many boys:** At most one of those incident edges can belong to the matching.
- **Reassignment required:** Recursion may move several earlier boys before a free girl is reached.

</details>
