# Minimum Total Space Wasted With K Resizing Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1959 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-total-space-wasted-with-k-resizing-operations/) |

## Problem Description
### Goal
The value `nums[t]` is the number of elements stored in a dynamic array at
time `t`. Its allocated size at that time must be at least `nums[t]`, and the
difference between the allocated size and `nums[t]` is wasted space.

Choose any valid initial allocation without counting it as a resize. During
the remaining timeline, the allocation may be changed at most `k` times, to
any sizes that continue to fit the corresponding element counts. Return the
minimum sum of wasted space over every time index.

### Function Contract
**Inputs**

- `nums`: a list of $N$ required element counts, where $1\le N\le200$ and
  $1\le\texttt{nums[i]}\le10^6$.
- `k`: the maximum number of resizing operations, where $0\le k<N$. Define
  $K=k+1$, the maximum number of constant-capacity intervals.

**Return value**

- The minimum total wasted space obtainable with at most `k` resizes.

### Examples
**Example 1**

- Input: `nums = [10, 20], k = 0`
- Output: `10`

**Example 2**

- Input: `nums = [10, 20, 30], k = 1`
- Output: `10`

**Example 3**

- Input: `nums = [10, 20, 15, 30, 20], k = 2`
- Output: `15`

### Required Complexity
- **Time:** $O(KN^2)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Measure one constant-capacity interval**

Between two resizes, the allocated size is constant. For a segment
`nums[start:end]`, the smallest feasible capacity is its maximum value; any
larger capacity only adds waste. If the segment maximum is $M$ and its sum is
$S$, its minimum waste is

$$
M(\texttt{end}-\texttt{start})-S.
$$

Thus a schedule with at most `k` resizes is a partition of the timeline into
at most $K=k+1$ contiguous segments.

**Choose optimal segment boundaries**

Let the previous DP row store the minimum waste for each prefix using one
fewer segment. For every possible segment end, scan its start backward while
maintaining the segment maximum and sum. Combining the previous prefix cost
with the resulting segment cost considers every possible final boundary.

The recurrence chooses the least cost among all such boundaries, so by
induction each DP entry is optimal for its prefix and segment count. Splitting
a segment cannot increase its minimum waste, so an optimum using at most $K$
segments can be represented with exactly $K$ nonempty segments when
$K\le N$. The final entry after $K$ rows is therefore the requested minimum.

#### Complexity detail

For each of the $K$ segment counts, all $N$ endpoints scan up to $N$ starting
positions, giving $O(KN^2)$ time. Segment maxima and sums are updated in
constant time during the backward scan. Two DP rows of $N+1$ values are
retained, so the auxiliary space is $O(N)$.

#### Alternatives and edge cases

- **Precompute every segment cost:** A quadratic table makes each transition
  lookup constant-time but uses $O(N^2)$ additional space without improving
  the $O(KN^2)$ time bound.
- **Memoized recursive partitioning:** The same states and boundaries can be
  explored top-down, but recursion and a full memo table add overhead and
  generally use $O(KN)$ space.
- With `k = 0`, one capacity equal to the maximum of all `nums` values must
  cover the entire timeline.
- With `k = N - 1`, every time index may form its own segment, giving zero
  waste.
- Equal requirements in a segment cause no waste when its capacity equals
  that common value.

</details>
