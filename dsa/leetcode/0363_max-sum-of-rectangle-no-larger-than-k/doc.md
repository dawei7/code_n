# Max Sum of Rectangle No Larger Than K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 363 |
| Difficulty | Hard |
| Topics | Array, Binary Search, Matrix, Prefix Sum, Ordered Set |
| Official Link | [LeetCode](https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/) |

## Problem Description
### Goal
Given a nonempty rectangular integer matrix and an integer limit `k`, choose a nonempty axis-aligned submatrix formed by consecutive rows and consecutive columns. Sum every value inside its rectangular boundaries.

Among rectangles whose sum is at most `k`, return the greatest sum. Sums equal to `k` are allowed and are immediately optimal. Matrix entries may be negative, so enlarging a rectangle does not necessarily increase its sum and the best rectangle need not contain the largest individual values. Return only the optimal sum, not the rectangle coordinates, while meeting the required complexity beyond brute-force enumeration of all cells per rectangle.

### Function Contract
**Inputs**

- `matrix`: a non-empty rectangular matrix of integers
- `k`: the inclusive upper bound for the chosen rectangle's sum

**Return value**

- The greatest rectangular submatrix sum that is at most `k`.

### Examples
**Example 1**

- Input: `matrix = [[1,0,1],[0,-2,3]], k = 2`
- Output: `2`

**Example 2**

- Input: `matrix = [[2,2,-1]], k = 3`
- Output: `3`

**Example 3**

- Input: `matrix = [[-5]], k = -2`
- Output: `-5`

### Required Complexity

- **Time:** $O(s^2 l \log l)$
- **Space:** $O(l)$

<details>
<summary>Approach</summary>

#### General

**Compress between pairs on the smaller dimension**

Let $s = \min(m,n)$ and $l = \max(m,n)$. Treat the smaller dimension as the pair of rectangle boundaries. For each starting boundary, extend an ending boundary one step at a time while maintaining `l` accumulated line sums. Every rectangle between those two boundaries is now a contiguous subarray of this compressed one-dimensional array.

This orientation matters: enumerating boundary pairs costs $O(s^2)$ rather than $O(l^2)$, while the compressed array still contains every possible span along the other dimension.

**Turn the constrained subarray into a prefix-successor query**

For a compressed array with prefix sums $P_0,P_1,\ldots$, a subarray ending at $j$ and starting after an earlier prefix $P_i$ has sum $P_j-P_i$. To keep that sum at most $k$, the earlier prefix must satisfy $P_i \ge P_j-k$. Among eligible earlier prefixes, choosing the smallest one produces the largest legal subarray sum.

Process prefixes from left to right in an ordered multiset. For each current prefix, find the smallest inserted value at least `current - k`, update the answer with their difference, and then insert the current prefix.

**Provide true logarithmic ordering with coordinates and a Fenwick tree**

Python's standard sorted list can locate the successor with binary search, but inserting into its middle is linear. Instead, compute all prefixes for the current compressed array, sort their distinct values once, and use their ranks as coordinates. A Fenwick tree stores how many already-seen prefixes occupy each rank.

A prefix-count query reveals how many inserted values lie below the threshold rank. If fewer than the total inserted prefixes lie below it, a Fenwick order-statistic search finds the next occupied rank in $O(\log l)$. Because only previously inserted prefixes are stored, every candidate represents a non-empty subarray ending at the current position. Repeating this for every boundary pair considers every rectangle exactly once, so the best legal candidate is the required answer.

#### Complexity detail

There are $O(s^2)$ boundary pairs. Updating the compressed values costs $O(l)$ per ending boundary, and each one-dimensional constrained maximum performs coordinate sorting plus `l` Fenwick queries and updates in $O(l \log l)$ time. The total is $O(s^2 l \log l)$. The compressed array, prefix coordinates, and Fenwick tree each use $O(l)$ space.

#### Alternatives and edge cases

- **Enumerate every rectangle with a 2D prefix sum:** evaluates a rectangle in constant time but still examines $O(m^2n^2)$ boundary combinations.
- **Sorted Python list of prefixes:** is concise and often accepted, but middle insertion is $O(l)$, making the one-dimensional phase quadratic in the worst case.
- **Balanced binary-search tree:** gives the same successor and insertion bounds directly in languages with an ordered-set library.
- **Unconstrained Kadane scan:** finds the maximum subarray but cannot enforce the upper bound `k`.
- Negative `k` and all-negative matrices still require choosing a non-empty rectangle.
- A rectangle whose sum equals `k` is optimal, but the algorithm need not depend on encountering one early.
- Repeated prefix sums require multiplicities; the Fenwick counts preserve them.
- Choosing the smaller matrix dimension for boundary pairs prevents avoidable work on highly rectangular inputs.

</details>
