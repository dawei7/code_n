# Minimum Difference Between Highest and Lowest of K Scores

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1984 |
| Difficulty | Easy |
| Topics | Array, Sliding Window, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/) |

## Problem Description
### Goal
The 0-indexed integer array `nums` records one score for each student. Select
the scores of exactly `k` different students. For a particular selection, its
spread is the highest selected score minus the lowest selected score; scores
between those extremes do not otherwise affect the measurement.

Choose the `k` scores so that this spread is as small as possible, and return
the minimum achievable difference. Selection is by array position, so equal
scores belonging to different students may all be chosen.

### Function Contract
**Inputs**

- `nums`: a list of $N$ student scores, where $1 \le N \le 1000$ and
  $0 \le \texttt{nums[i]} \le 10^5$.
- `k`: the exact number of students to choose, where $1 \le k \le N$.

**Return value**

- The smallest possible value of
  $\max(\text{chosen scores}) - \min(\text{chosen scores})$ among all
  selections of exactly `k` positions.

### Examples
**Example 1**

- Input: `nums = [90], k = 1`
- Output: `0`

The only selected score is both the minimum and maximum.

**Example 2**

- Input: `nums = [9, 4, 1, 7], k = 2`
- Output: `2`

Choosing scores `7` and `9` gives the smallest spread.

**Example 3**

- Input: `nums = [1, 5, 6, 14, 15], k = 3`
- Output: `5`

Choosing `1`, `5`, and `6` gives spread `5`.

### Required Complexity
- **Time:** $O(N\log N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Sort scores to expose their rank order**

Sort the scores into non-decreasing order. For any selection of `k` students,
only its smallest and largest scores determine its spread. In sorted order,
those two extremes delimit an interval containing every score ranked between
them.

**Why an optimum is a consecutive window**

Suppose a chosen set skips a score lying between its selected minimum and
maximum. Replacing an extreme selected score with such an interior score cannot
increase the spread. Repeating this exchange yields `k` consecutive sorted
positions whose spread is no larger. Therefore at least one optimal selection
appears as a contiguous sorted window of length `k`.

**Scan every fixed-width window**

For each possible starting index `i`, the window ends at `i + k - 1`, and its
spread is computed as
`ordered[i + k - 1] - ordered[i]`. Take the minimum over all such windows.
This examines every form an optimal selection needs to take, so the smallest
recorded spread is globally optimal.

#### Complexity detail

Sorting $N$ scores costs $O(N\log N)$ time. The subsequent scan examines
$N-k+1$ windows in $O(N)$ time, so sorting dominates. Keeping a separate sorted
copy uses $O(N)$ space. An in-place sort may reduce explicit array storage, but
the sorting implementation can still require auxiliary memory.

#### Alternatives and edge cases

- **Enumerate all selections:** Checking every group of `k` positions is
  correct but can require $\binom{N}{k}$ selections.
- **Enumerate all pairs when `k = 2`:** Comparing every score pair takes
  $O(N^2)$ time, while sorting reveals that only adjacent scores matter.
- **Repeatedly extract minima:** Selecting successive ranks without a full sort
  can be made correct, but a naive repeated scan also incurs quadratic work.
- When `k = 1`, every one-score selection has spread `0`.
- When `k = N`, every score is forced, so the answer is the overall maximum
  minus the overall minimum.
- Duplicate scores can produce answer `0` whenever at least `k` equal values
  occur.
- Input order has no effect on the result because students may be selected from
  arbitrary positions.

</details>
