# Number of Boomerangs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 447 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Math |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-boomerangs/) |

## Problem Description
### Goal
Given unique points in the two-dimensional plane, a boomerang is an ordered triple of distinct indices `(i, j, k)` where the Euclidean distance from pivot point `i` to point `j` equals the distance from `i` to point `k`.

Return the number of boomerangs. Order matters: swapping the two equidistant endpoint indices produces a different triple, while changing the pivot defines another candidate. Compare exact squared distances to avoid floating-point error. Collinearity is not required, and each occurrence of an equal distance around a pivot can pair with every other occurrence at that distance.

### Function Contract
**Inputs**

- `points`: a list of distinct two-dimensional integer coordinates

**Return value**

- Return the number of ordered boomerangs; swapping `j` and `k` creates a different triple.

### Examples
**Example 1**

- Input: `points = [[0, 0], [1, 0], [2, 0]]`
- Output: `2`

**Example 2**

- Input: `points = [[1, 1], [2, 2], [3, 3]]`
- Output: `2`

**Example 3**

- Input: `points = [[0, 0], [1, 0], [0, 1]]`
- Output: `2`

### Required Complexity

- **Time:** $O(n^2)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Fix the pivot before grouping other points**

For each point `i`, compute the squared distance to every other point. Square roots are unnecessary because equal Euclidean distances have equal squared distances, and integer arithmetic stays exact.

**Count points sharing each squared distance**

Maintain a frequency map for the current pivot. If `c` earlier points have the same distance as the next point, that point forms `c` unordered partner pairs. Each pair has two orders, so add `2c` boomerangs before incrementing the frequency.

**Reset distance groups for every pivot**

Distance is measured from the chosen first point. A group formed around one pivot has no meaning for another, so start a fresh map for each outer iteration.

**Why the incremental count is exact**

For a final distance group of size `m`, incremental additions are $2(0 + 1 + \ldots + m - 1) = m(m - 1)$, exactly the number of ordered choices of distinct `j` and `k`. Summing groups for a pivot counts all and only equidistant pairs; summing pivots gives every ordered triple once.

#### Complexity detail

Every pivot compares with all $n - 1$ other points, giving $O(n^2)$ time. One pivot's distance map contains at most $n - 1$ entries, so auxiliary space is $O(n)$.

#### Alternatives and edge cases

- **Count complete groups then use $m(m - 1)$:** is an equivalent $O(n^2)$ formulation.
- **Enumerate every ordered triple:** compares two distances directly but takes $O(n^3)$ time.
- **Use floating-point distances:** adds rounding risk without changing equality information.
- **Collinear points:** symmetric points on opposite sides of a pivot still share a distance.
- **Asymmetric set:** a pivot with all distinct distances contributes zero.
- **Fewer than three points:** no boomerang can be formed.

</details>
