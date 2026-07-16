# Paint House III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1473 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/paint-house-iii/) |

## Problem Description
### Goal

A row contains $m$ houses, and every house must ultimately have one of $n$ colors labeled from $1$ through $n$. A house whose entry in `houses` is nonzero was painted previously and must keep that color. An entry equal to zero is unpainted; assigning it color $c$ costs `cost[i][c - 1]`. The cost matrix still contains rows for previously painted houses, but those values are irrelevant because such houses cannot be repainted.

A neighborhood is a maximal contiguous group of houses sharing one color. For example, `[1,2,2,3,3,2,1,1]` contains the five neighborhoods `[1]`, `[2,2]`, `[3,3]`, `[2]`, and `[1,1]`. Paint every unpainted house so that the finished row contains exactly `target` neighborhoods and the total paid cost is as small as possible. Return `-1` when no legal completion has exactly that neighborhood count.

### Function Contract
**Inputs**

Let $m$ be the house count, $n$ the color count, and $t=\texttt{target}$.

- `houses`: an integer array of length $m$, where `0` denotes an unpainted house and values in $[1,n]$ are immutable colors.
- `cost`: an $m\times n$ matrix; `cost[i][c - 1]` is the price of assigning color $c$ to an unpainted house at index `i`.
- `m`: the row length, where $1 \le m \le 100$.
- `n`: the number of available colors, where $1 \le n \le 20$.
- `target`: the exact required neighborhood count, where $1 \le t \le m$.
- Every painting price lies in $[1,10^4]$.

**Return value**

Return the minimum sum of costs paid for houses that were initially unpainted among all completions with exactly $t$ neighborhoods. Return `-1` if no such completion exists.

### Examples
**Example 1**

- Input: `houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3`
- Output: `9`
- Explanation: Coloring the row `[1,2,2,1,1]` creates three neighborhoods and costs `1 + 1 + 1 + 1 + 5 = 9`.

**Example 2**

- Input: `houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3`
- Output: `11`
- Explanation: Only the first and last houses may change. Choosing `[2,2,1,2,2]` costs `10 + 1 = 11` and forms exactly three neighborhoods.

**Example 3**

- Input: `houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n = 3, target = 3`
- Output: `-1`
- Explanation: The fixed row already has four neighborhoods, and repainting is forbidden.

### Required Complexity
- **Time:** $O(mtn)$
- **Space:** $O(tn)$

<details>
<summary>Approach</summary>

#### General

**Choosing the state that preserves future consequences**

When processing houses from left to right, the effect of a new color depends on two facts about the completed prefix: how many neighborhoods it has and the color of its final house. Define

$$
D_i[g][c]
$$

as the minimum cost for houses from index $0$ through $i$ when that prefix has exactly $g$ neighborhoods and house $i$ has color $c$. Impossible states have value $\infty$.

For the first house, every allowed color creates one neighborhood. If it is already painted, only its fixed color receives cost zero. If it is unpainted, each color $c$ receives `cost[0][c - 1]`.

**How a new house changes the neighborhood count**

Suppose the next house is assigned color $c$. A predecessor ending in the same color keeps the neighborhood count unchanged:

$$
D_i[g][c].
$$

A predecessor ending in any color $p\ne c$ starts a new neighborhood, so it must previously have had $g-1$ neighborhoods:

$$
\min_{p\ne c} D_i[g-1][p].
$$

The better predecessor cost is the minimum of those two quantities. Add zero when the house was already painted, or add its price for color $c$ when it was unpainted. Fixed houses expose only their required color; trying any other color would violate the contract.

**Removing the inner scan over predecessor colors**

Computing $\min_{p\ne c}$ by scanning all $n$ colors for every $c$ would add an unnecessary factor of $n$. For each neighborhood count $g$, inspect the previous row once and record:

- the smallest state value and the color attaining it;
- the second-smallest state value.

When transitioning to color $c$, use the smallest value if its recorded color differs from $c$; otherwise use the second-smallest value. This returns exactly the cheapest predecessor whose color is not $c$ in constant time. Ties are safe: if another color shares the minimum, the second-smallest value is equal to the smallest.

**Rolling the house dimension**

Only states for house $i$ are needed to build states for house $i+1$, so retain two $(t+1)\times n$ tables, `previous` and `next`. Neighborhood counts above the number of processed houses or above $t$ are unreachable and need not influence transitions.

After the final house, the answer is the minimum state `previous[target][c]` over all ending colors. If every such state is infinite, no legal coloring reaches exactly $t$ neighborhoods, so return `-1`.

**Why the dynamic program is complete and optimal**

The initialization enumerates every legal coloring of the one-house prefix with its exact cost. Assume the table correctly represents every legal coloring through house $i$. Any legal coloring through house $i+1$ has some final color $c$ and a uniquely determined previous final color $p$. If $p=c$, it comes from the same-neighborhood transition; otherwise it comes from the new-neighborhood transition. The algorithm considers the permitted $c$, selects the cheapest predecessor of the appropriate kind, and adds exactly the price required at the new house.

Conversely, every transition appends a permitted color to a legal predecessor and updates the neighborhood count according to whether the boundary color changed, so it creates only legal prefixes. Induction proves that each state stores the minimum cost among exactly the colorings it describes. Taking the cheapest final state with $t$ neighborhoods therefore yields the required optimum.

#### Complexity detail

For each of the $m$ houses, preprocessing the smallest two predecessor values for every one of the $t$ neighborhood counts costs $O(tn)$. Evaluating all permitted current colors across those counts also costs at most $O(tn)$. The total time is therefore $O(mtn)$.

Each rolling table contains $(t+1)n$ values, and the smallest/second-smallest summaries use $O(t)$ additional storage. The total space is $O(tn)$.

#### Alternatives and edge cases

- **Scan every different predecessor color:** The direct three-dimensional transition is easier to derive but costs $O(mtn^2)$ time because every state checks all $n$ preceding colors.
- **Top-down memoization:** Recursing on house index, previous color, and neighborhoods formed represents the same state graph. It is correct and often concise, but a naive transition still scans all colors and recursion adds call overhead.
- **Enumerate complete colorings:** Trying every choice for every unpainted house is exponential in their count and becomes infeasible long before the source limits.
- **Full three-dimensional table:** Keeping all $m$ house layers supports reconstruction of an optimal coloring, but the problem asks only for its cost, so $O(mtn)$ storage is unnecessary.
- **Previously painted houses:** Their corresponding `cost` row must never be added. Only the fixed color is a legal transition.
- **Impossible fixed boundaries:** Existing colors may already force more than $t$ neighborhoods; infinite states naturally lead to `-1`.
- **One neighborhood:** Every house must finish with one common color, and any conflicting pair of fixed colors makes the target impossible.
- **Maximum neighborhoods:** Reaching $t=m$ requires every adjacent pair to have different colors.
- **One available color:** Exactly one neighborhood is possible regardless of row length; any target greater than one must return `-1`.
- **Large finite costs:** Use an infinity sentinel safely above the maximum possible total $100\cdot10^4$ so valid expensive colorings are not mistaken for unreachable states.

</details>
