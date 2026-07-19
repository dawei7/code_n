# Count Number of Special Subsequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1955 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/count-number-of-special-subsequences/) |

## Problem Description
### Goal
A sequence is special when it contains a positive number of `0` values,
followed by a positive number of `1` values, followed by a positive number of
`2` values. No other ordering or value is allowed within that sequence.

Given an array containing only `0`, `1`, and `2`, count its special
subsequences. A subsequence keeps the original relative order while possibly
discarding elements. Two subsequences count separately when they select
different sets of source indices, even if their resulting value sequences are
identical. Return the count modulo $10^9+7$.

### Function Contract
**Inputs**

- `nums`: a list of $N$ integers, where $1\le N\le 10^5$ and every element is
  `0`, `1`, or `2`.

**Return value**

- The number of index-distinct special subsequences, reduced modulo
  $10^9+7$.

### Examples
**Example 1**

- Input: `nums = [0, 1, 2, 2]`
- Output: `3`

**Example 2**

- Input: `nums = [2, 2, 0, 0]`
- Output: `0`

**Example 3**

- Input: `nums = [0, 1, 2, 0, 1, 2]`
- Output: `7`

### Required Complexity
- **Time:** $O(N)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Represent the three valid stages**

Maintain three counts while scanning from left to right. Let `zero` count
nonempty subsequences consisting only of `0` values, `one` count subsequences
of the form `0+1+`, and `two` count complete `0+1+2+` subsequences. These
states retain exactly the prefixes that may still become special; values
chosen out of stage order never enter a state.

**Update with the current value**

When the current value is `0`, every existing `zero` subsequence may either
skip it or append it, and the current index can begin a new subsequence. Thus
the update is `zero = 2 * zero + 1`.

For a `1`, every existing `one` subsequence may skip or append the new index,
while every `zero` subsequence may append it to enter the second stage. This
gives `one = 2 * one + zero`. Similarly, a `2` produces
`two = 2 * two + one`. Unmentioned states remain unchanged, and every update
is reduced modulo $10^9+7$.

Each index-distinct subsequence has one unique history of skip, extend, or
stage-transition choices, so it is counted once. Conversely, every transition
preserves the required block order and positivity of all stages. The final
`two` count is therefore exactly the number requested.

#### Complexity detail

The scan performs constant work for each of the $N$ elements, taking $O(N)$
time. Only the three counts and the modulus are retained, so the auxiliary
space is $O(1)$.

#### Alternatives and edge cases

- **Prefix dynamic-programming table:** Store all three counts after every
  array position. It uses the same transitions and $O(N)$ time, but consumes
  $O(N)$ space that the next update does not need.
- **Enumerate all subsequences:** Testing every chosen index set is direct but
  takes exponential time and is infeasible for $N=10^5$.
- Values that appear before their required stage, such as an initial `1` or
  `2`, cannot begin a valid partial subsequence and are ignored.
- At least one value from each stage is mandatory; arrays missing any of
  `0`, `1`, or `2` have answer zero.
- Equal value sequences selected from different source indices are distinct
  and must all contribute to the count.
- Apply the modulus during every transition so intermediate counts remain
  bounded.

</details>
