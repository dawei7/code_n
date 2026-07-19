# Check if All the Integers in a Range Are Covered

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/) |
| Frontend ID | 1893 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Each element `ranges[i] = [start_i, end_i]` describes an inclusive interval of integers. An integer $x$ is covered when at least one interval satisfies $\textit{start}_i \le x \le \textit{end}_i$.

Given inclusive target bounds `left` and `right`, determine whether every integer from `left` through `right` is covered. Intervals may overlap, touch at endpoints, extend beyond the target, or leave gaps. Return `true` only when no target integer is uncovered.

### Function Contract

**Inputs**

- `ranges`: an array of $N$ inclusive integer intervals.
- `left`, `right`: the inclusive target bounds.
- $1 \le N \le 50$.
- Every interval endpoint and both target bounds lie from $1$ through $50$, with each start no greater than its end and `left <= right`.
- Let $V$ be the greatest coordinate swept, at most $50$.

**Return value**

- Return `true` if every integer in `[left, right]` belongs to at least one interval; otherwise return `false`.

### Examples

**Example 1**

- Input: `ranges = [[1,2],[3,4],[5,6]], left = 2, right = 5`
- Output: `true`

The three intervals collectively cover integers `2`, `3`, `4`, and `5`.

**Example 2**

- Input: `ranges = [[1,10],[10,20]], left = 21, right = 21`
- Output: `false`

Neither interval includes `21`.

**Example 3**

- Input: `ranges = [[1,2],[4,5]], left = 1, right = 5`
- Output: `false`

Integer `3` is the uncovered gap.

### Required Complexity

- **Time:** $O(N+V)$
- **Space:** $O(V)$

<details>
<summary>Approach</summary>

#### General

**Encode inclusive intervals as boundary changes**

Create a difference array over the coordinate domain. For every inclusive interval `[start, end]`, add one at `start` and subtract one at `end + 1`. The subtraction occurs after the covered endpoint, which preserves inclusive semantics.

**Sweep the active coverage**

Take prefix sums from coordinate one through `right`. The running total equals the number of input intervals covering the current integer. Once the sweep reaches `left`, any total of zero proves that the target integer is uncovered and the answer is `false`. If the sweep reaches `right` without finding such a point, return `true`.

Each interval contributes precisely on its inclusive coordinate span: its addition is active starting at `start`, and its subtraction removes that contribution only after `end`. Therefore the prefix total is positive exactly at covered coordinates, making the target check exact.

#### Complexity detail

Writing two boundary changes for each of the $N$ intervals takes $O(N)$ time. Sweeping through at most $V$ coordinates takes $O(V)$, for $O(N+V)$ total time. The difference array contains $O(V)$ entries. Under the stated bound $V\le50$, this storage is also a fixed small constant in absolute terms.

#### Alternatives and edge cases

- **Nested coverage tests:** For every target integer, scan intervals until one covers it. This is straightforward but takes $O(NV)$ time in the worst case.
- **Boolean marking:** Mark every coordinate inside every interval, then inspect the target range; it is correct but can write $O(NV)$ positions.
- **Inclusive endpoint:** Place the negative difference at `end + 1`, not at `end`.
- **Single-point target:** That one integer still must be covered.
- **Adjacent intervals:** `[1,2]` and `[3,4]` jointly cover all integers from one through four without a gap.
- **Overlapping intervals:** Multiple coverage only raises the prefix count; it does not change the boolean result.
- **Irrelevant outside intervals:** Coverage entirely outside `[left, right]` cannot fill a gap inside it.

</details>
