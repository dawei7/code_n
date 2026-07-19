# Count Number of Pairs With Absolute Difference K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2006 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Counting |
| Official Link | [LeetCode](https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/) |

## Problem Description

### Goal

Given an integer array `nums` and a positive integer `k`, count the index pairs
$(i,j)$ for which $i<j$ and

$$
\lvert \texttt{nums[i]}-\texttt{nums[j]} \rvert=k.
$$

Each pair is distinguished by its indices, so equal values at different
positions can participate in separate pairs. Absolute value ignores the sign
of a difference: $\lvert x\rvert=x$ when $x\ge0$, and
$\lvert x\rvert=-x$ when $x<0$. Consequently, either endpoint may contain the
larger value; only their distance and index order determine whether the pair
qualifies.

### Function Contract

**Inputs**

- `nums`: a list of $N$ integers, where $1\le N\le200$ and
  $1\le\texttt{nums[i]}\le100$.
- `k`: the required absolute difference, where $1\le k\le99$.

**Return value**

Return the number of index pairs satisfying the stated order and absolute
difference.

### Examples

**Example 1**

- Input: `nums = [1, 2, 2, 1], k = 1`
- Output: `4`
- Explanation: Each of the two positions containing `1` pairs with each of the
  two positions containing `2`.

**Example 2**

- Input: `nums = [1, 3], k = 3`
- Output: `0`
- Explanation: The only absolute difference is $2$, not $3$.

**Example 3**

- Input: `nums = [3, 2, 1, 5, 4], k = 2`
- Output: `3`
- Explanation: The value pairs are `3` with `1`, `3` with `5`, and `2` with
  `4`.

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Count only partners that precede the current index.** Scan `nums` from left
to right while a frequency table records the values at earlier indices. When
the current value is `value`, an earlier value forms a valid pair exactly when
it is `value - k` or `value + k`. Add both stored frequencies before recording
the current value.

**Why every pair is counted exactly once.** Consider any valid pair $(i,j)$
with $i<j$. At index $j$, `nums[i]` is already in the frequency table and is
one of the two required partner values, so the pair is counted. It cannot be
counted earlier because its second endpoint has not yet been visited, and it is
never counted later because additions always pair the current index with a
previous one. Since $k$ is positive, `value - k` and `value + k` are distinct,
so the two lookups cannot count the same earlier index.

#### Complexity detail

Here $N$ is the length of `nums`. Each element causes a constant number of
average-case hash-table operations, giving $O(N)$ time. The table can contain
up to $N$ distinct values, so it uses $O(N)$ space.

#### Alternatives and edge cases

- **Examine every index pair:** Testing all $\binom{N}{2}$ pairs is direct but
  takes $O(N^2)$ time.
- **Frequency product after a full pass:** Build all frequencies, then sum
  `count[x] * count[x + k]` once per value. This is also linear in the input
  plus the number of distinct values, but the one-pass method naturally
  enforces $i<j$.
- Duplicate occurrences must be counted by position; two copies on each side
  of the required difference contribute four pairs.
- A one-element array has no index pair and therefore returns zero.
- Values outside the observed range simply have frequency zero; no special
  boundary branch is needed for `value - k` or `value + k`.

</details>
