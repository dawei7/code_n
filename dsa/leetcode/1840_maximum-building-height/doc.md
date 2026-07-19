# Maximum Building Height

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/maximum-building-height/) |
| Frontend ID | 1840 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Construct $n$ buildings in a line, labeled from 1 through $n$, with non-negative integer heights. Building 1 must have height 0, and the heights of two adjacent buildings may differ by at most 1.

Some unique building IDs have additional upper bounds, supplied as `[id, maxHeight]`; building 1 never appears in that list. Choose heights satisfying every rule and return the greatest possible height of the tallest building anywhere in the line.

### Function Contract

**Inputs**

- `n`: the number of buildings, where $2 \le n \le 10^9$.
- `restrictions`: $r$ distinct pairs `[id, maxHeight]`, where $0 \le r \le \min(n-1,10^5)$.
- Every restricted ID is between 2 and $n$, and every maximum height is between 0 and $10^9$.

**Return value**

- Return the maximum height achievable by any building while all endpoint, adjacency, non-negativity, and explicit upper-bound rules hold.

### Examples

**Example 1**

- Input: `n = 5, restrictions = [[2,1],[4,1]]`
- Output: `2`

Heights `[0,1,2,1,2]` satisfy all rules.

**Example 2**

- Input: `n = 6, restrictions = []`
- Output: `5`

Without explicit caps, heights may rise from 0 by one at every building.

**Example 3**

- Input: `n = 10, restrictions = [[5,3],[2,5],[7,4],[10,3]]`
- Output: `5`

One optimal profile is `[0,1,2,3,3,4,4,5,4,3]`.

### Required Complexity

- **Time:** $O(r\log r)$
- **Space:** $O(r)$

<details>
<summary>Approach</summary>

#### General

**Represent the implicit endpoint constraints**

Add `[1, 0]` for the mandatory first height. Add `[n, n - 1]` as a harmless upper bound at the final building: even without other restrictions, adjacency from building 1 cannot permit a greater height there. Sort all limits by building ID.

**Propagate every cap in both directions**

For consecutive restricted positions $x_{i-1}$ and $x_i$, a left cap $h_{i-1}$ implies

$$
h_i \le h_{i-1} + (x_i-x_{i-1}).
$$

A left-to-right pass tightens each cap by this implication. A right-to-left pass applies the symmetric constraint from the right. After both passes, every stored height is the greatest feasible height at that restricted position under all restrictions, and adjacent stored caps differ by no more than their distance.

**Compute the highest peak inside each interval**

Between feasible endpoints $(x_L,h_L)$ and $(x_R,h_R)$ at distance $d=x_R-x_L$, a height profile can rise by one from the left and by one backward from the right. The two cones meet at a maximum of

$$
\left\lfloor\frac{h_L+h_R+d}{2}\right\rfloor.
$$

This value includes endpoint-dominated cases because feasibility guarantees $\lvert h_L-h_R\rvert\le d$. Evaluate it for every adjacent pair of stored limits and return the largest peak.

**Why the constructed maximum is attainable**

The propagation passes make all endpoint caps mutually consistent. Within one interval, assign each building the smaller of the left-rising and right-rising cones. This profile changes by at most one per step, respects both endpoint caps, and reaches the stated intersection peak. Neighboring intervals share their restricted endpoint height, so their profiles join into one globally feasible construction. No building can exceed both cones, proving the maximum is also an upper bound.

#### Complexity detail

There are $r+2$ stored limits. Sorting them takes $O(r\log r)$ time; the two propagation passes and peak scan are linear. The augmented, sorted limits use $O(r)$ space.

#### Alternatives and edge cases

- **Expand every building:** It is impossible when $n$ is as large as $10^9$ and can take $O(nr)$ time if each position is compared with every restriction.
- **One directional pass:** It misses caps imposed from the opposite side; both left and right propagation are required.
- **Binary-search a candidate height:** Feasibility can be tested, but direct cone intersections compute the exact answer without an extra logarithmic search.
- **No explicit restrictions:** The profile rises from 0 through $n-1$, so the answer is $n-1$.
- **Restriction at building `n`:** Combine it with the implicit endpoint bound by taking the tighter cap.
- **Loose restriction:** Propagation may lower a stated maximum that is unreachable from another cap.
- **Zero-height interior cap:** The profile may rise on both sides of that building but must meet zero there.
- **Odd interval surplus:** Integer division floors the meeting height when the two slopes cannot meet on one integer building.
- **Unsorted input restrictions:** Sort by ID before propagation.
- **Large coordinates and caps:** Use arithmetic wide enough for sums involving values near $10^9$.

</details>
