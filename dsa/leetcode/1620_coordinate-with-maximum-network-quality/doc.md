# Coordinate With Maximum Network Quality

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1620 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/coordinate-with-maximum-network-quality/) |

## Problem Description
### Goal
Each entry `[x_i, y_i, q_i]` describes a network tower at an integral coordinate with quality factor $q_i$. Distances on the plane are Euclidean. At an integral coordinate $(x,y)$, tower $i$ is reachable only when its distance $d_i$ is at most `radius`; a reachable tower contributes

$$
\left\lfloor \frac{q_i}{1+d_i} \right\rfloor
$$

to the network quality, while an unreachable tower contributes nothing. The total network quality is the sum of all reachable contributions.

Return the non-negative integral coordinate with maximum network quality. If several coordinates have the same maximum, choose the lexicographically smallest one: minimize the $x$-coordinate first, then the $y$-coordinate.

### Function Contract
**Inputs**

- `towers`: a nonempty list of $T$ entries `[x_i, y_i, q_i]`, where $1 \le T \le 50$ and $0 \le x_i,y_i,q_i \le 50$.
- `radius`: the inclusive reach distance, where $1 \le \texttt{radius} \le 50$.

**Return value**

Return `[c_x, c_y]`, the lexicographically smallest non-negative integral coordinate attaining the greatest total network quality.

### Examples
**Example 1**

- Input: `towers = [[1,2,5],[2,1,7],[3,1,9]], radius = 2`
- Output: `[2,1]`

**Example 2**

- Input: `towers = [[23,11,21]], radius = 9`
- Output: `[23,11]`

**Example 3**

- Input: `towers = [[1,2,13],[2,1,7],[0,1,9]], radius = 2`
- Output: `[1,2]`

### Required Complexity
- **Time:** $O(T)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Restrict the search to the tower bounding box.** Let `maximum_x` and `maximum_y` be the greatest tower coordinates. Consider an integral point beyond either upper bound. Projecting that coordinate back to the corresponding boundary cannot increase its distance to any tower, so no tower contribution decreases. Repeating for both axes gives a point inside `[0, maximum_x] × [0, maximum_y]` with at least as much quality and a lexicographically no-larger coordinate. Thus an optimal answer exists inside this box.

**Evaluate every legal candidate exactly.** Scan `x` from 0 through `maximum_x`, and for each `x`, scan `y` from 0 through `maximum_y`. For every tower, compute the squared distance first. If it exceeds `radius * radius`, skip the tower; otherwise take the square root, apply the floor formula, and add the contribution.

**Let scan order enforce the tie rule.** The nested increasing loops visit coordinates in lexicographic order. Replace the saved coordinate only when the new quality is strictly greater. The first coordinate attaining any quality is therefore retained across ties. Since every coordinate in the sufficient bounding box is evaluated and its quality is exact, the final saved point is the required lexicographically smallest maximizer.

#### Complexity detail

The source contract fixes both coordinates to 0 through 50, so at most $51^2=2601$ candidates exist. Each candidate inspects all $T$ towers, for at most $2601T$ contribution checks, which is $O(T)$ under the fixed legal coordinate domain. Only scalar accumulators and the two-coordinate answer are stored, giving $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Accumulate around each tower:** Visit every grid point within each tower's radius and add its contribution to a table. This is also bounded but uses $O(51^2)$ storage.
- **Scan the full 51×51 grid:** This avoids the bounding-box proof and has the same contract-level asymptotic bound, but performs unnecessary work when towers occupy a small region.
- A tower exactly `radius` units away is reachable because the distance boundary is inclusive.
- A zero-quality tower never increases any coordinate's total, but it still satisfies the input contract.
- When every total is zero, increasing scan order correctly returns `[0,0]`.
- Flooring is applied to each tower contribution before the contributions are summed.
- Multiple towers may share a coordinate; each contributes independently.

</details>
