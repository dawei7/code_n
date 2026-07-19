# Minimize the Difference Between Target and Chosen Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1981 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements/) |

## Problem Description
### Goal
You are given an $M \times C$ integer matrix `mat` and an integer `target`.
Form a sum by choosing exactly one element from every row. Choices from
different rows are independent, but no row may be skipped and no row may
contribute more than one value.

Among all sums obtainable in this way, find one whose absolute difference from
`target` is as small as possible. Return that minimum absolute difference. An
exactly achievable target therefore produces `0`; otherwise, sums on either
side of the target must both be considered.

### Function Contract
**Inputs**

- `mat`: an $M \times C$ matrix of positive integers, where
  $1 \le M, C \le 70$ and $1 \le \texttt{mat[i][j]} \le 70$.
- `target`: an integer satisfying $1 \le \texttt{target} \le 800$.
- Let $T$ denote the value of `target`.

**Return value**

- The minimum value of $\lvert s - T \rvert$ over every sum $s$ formed by
  selecting exactly one element from each row.

### Examples
**Example 1**

- Input: `mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], target = 13`
- Output: `0`

Choosing `1`, `5`, and `7` gives the target sum exactly.

**Example 2**

- Input: `mat = [[1], [2], [3]], target = 100`
- Output: `94`

The only possible sum is `6`.

**Example 3**

- Input: `mat = [[1, 2, 9, 8, 7]], target = 6`
- Output: `1`

The closest selectable value is `7`.

### Required Complexity
- **Time:** $O(MCT)$
- **Space:** $O(T)$

<details>
<summary>Approach</summary>

#### General

**Track reachable sums row by row**

Begin with only sum `0` reachable. For each matrix row, combine every currently
retained sum with every distinct value in that row. The resulting set contains
exactly the sums obtainable after choosing one value from each row processed so
far. Deduplicating equal sums prevents different choice histories with the same
total from creating redundant states.

**Why one above-target sum is sufficient**

Retain every new sum at most $T$. Among sums greater than $T$, retain only the
smallest. All unprocessed values are positive, so future choices can only
increase every partial sum. Consequently, if $a$ and $b$ are both above $T$
and $a < b$, then extending $a$ with any fixed future choices remains closer
to $T$ than extending $b$ with those choices. The larger state can never lead
to a better final answer.

This rule leaves at most one state above $T$ and at most $T + 1$ nonnegative
states at or below it. It is important not to discard every above-target sum:
when even the minimum possible total exceeds the target, that smallest excess
is the answer.

**Why the final minimum is optimal**

Before pruning, the transition enumerates every choice from the current row.
The only removed states are dominated above-target totals, as established
above. Thus at least one representative capable of attaining the optimum
survives every row. After the last transition, minimizing
$\lvert s - T \rvert$ over the retained sums returns the globally smallest
difference.

#### Complexity detail

There are $M$ rows and $C$ columns. At most $T + 2$ sums are retained, so
combining a row with the current states takes $O(CT)$ time. Across all rows,
the total time is $O(MCT)$. The current and next reachable-sum sets contain
$O(T)$ values, giving $O(T)$ auxiliary space.

#### Alternatives and edge cases

- **Unpruned reachable-sum set:** Keeping every possible total is correct, but
  the state range can grow to $70M$ even when the small target makes most large
  totals permanently irrelevant.
- **Boolean array or integer bitset:** Shift a reachable-sum representation for
  each distinct row value. This also performs dynamic programming and can be
  efficient, but it must preserve enough above-target information to compare
  the closest excess.
- **Enumerate all row choices:** Trying every combination is straightforward
  but requires up to $C^M$ work.
- Repeated values within a row create the same transition and may be
  deduplicated without changing the set of achievable sums.
- When `target` is below every possible total, the smallest retained
  above-target state determines the answer.
- When `target` exceeds every possible total, the largest achievable sum is
  closest, and all reachable sums remain at or below the target.
- A one-row matrix still requires exactly one choice; the answer is the closest
  value in that row.

</details>
