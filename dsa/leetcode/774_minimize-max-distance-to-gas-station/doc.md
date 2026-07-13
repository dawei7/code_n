# Minimize Max Distance to Gas Station

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 774 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimize-max-distance-to-gas-station/) |

## Problem Description

### Goal

Given strictly increasing positions of existing gas stations along a number line, add exactly `k` new stations at arbitrary real-valued positions between or around the existing coordinates.

After insertion, consider the distances between every pair of consecutive stations in sorted order. Place the new stations to minimize the maximum of those adjacent distances, and return that minimum possible value within the accepted floating-point tolerance. Multiple new stations may divide the same original gap when beneficial.

### Function Contract

**Inputs**

- `stations`: a strictly increasing list of existing integer positions.
- `k`: the number of additional stations available.

**Return value**

- The smallest achievable maximum adjacent-station distance as a floating-point value.

### Examples

**Example 1**

- Input: `stations = [1,2,3,4,5,6,7,8,9,10]`, `k = 9`
- Output: `0.5`
- Explanation: Placing one new station in every unit gap halves all nine gaps.

**Example 2**

- Input: `stations = [23,24,36,39,46,56,57,65,84,98]`, `k = 1`
- Output: `14.0`
- Explanation: Splitting the length-19 gap leaves the existing length-14 gap as the maximum.

**Example 3**

- Input: `stations = [0,10]`, `k = 3`
- Output: `2.5`
- Explanation: Four equal segments are optimal.

### Required Complexity

- **Time:** $O(n \log(R/epsilon))$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Test whether a maximum gap is feasible**

For an original interval of length $g$, keeping every new segment at most $D$ requires $\lceil g/D\rceil$ pieces and therefore $\lceil g/D\rceil-1$ new stations. Sum this requirement over all original gaps; $D$ is feasible exactly when the total is at most $k$.

**Binary-search the answer value**

The feasibility predicate is monotone: increasing `D` never requires more stations. Start with lower bound zero and upper bound equal to the largest original gap. At each iteration, test their midpoint. A feasible midpoint becomes the new upper bound; an infeasible one becomes the lower bound. A fixed number of iterations shrinks the interval far below the accepted tolerance.

Every value below the true optimum is infeasible and every value at or above it is feasible. The binary-search invariant keeps the optimum between the two bounds, with the upper bound feasible. Once the bounds are sufficiently close, returning the upper bound approximates the minimum feasible distance to the required precision.

#### Complexity detail

Let `n` be the station count, `R` the largest original gap, and `epsilon` the target precision. Each feasibility check scans $n - 1$ gaps, and binary search performs $O(\log(R / \varepsilon))$ checks, for $O(n \log(R / \varepsilon))$ time and $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Maximum heap of current segment lengths:** Add stations one at a time to the interval with the largest current segment; it is exact but costs $O((n + k) \log n)$ time.
- **Enumerate station allocations among gaps:** This can prove tiny cases but grows combinatorially with `k` and the number of intervals.
- **Integer-only binary search:** It cannot represent arbitrary real station positions or fractional answers.
- **One original gap:** The answer is its length divided by $k + 1$.
- **Exact divisibility:** A gap already split into exact length-`D` pieces needs one fewer station than the piece count.
- **Unused capacity:** If a candidate needs fewer than `k` stations, extra stations can be placed without increasing its maximum gap.
- **Floating-point comparison:** Results within the accepted tolerance represent the same optimum.

</details>
