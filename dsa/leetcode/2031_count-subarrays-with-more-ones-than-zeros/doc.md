# Count Subarrays With More Ones Than Zeros

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2031 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Binary Search, Divide and Conquer, Binary Indexed Tree, Segment Tree, Merge Sort, Ordered Set |
| Official Link | [LeetCode](https://leetcode.com/problems/count-subarrays-with-more-ones-than-zeros/) |

## Problem Description

### Goal

Given a binary array `nums`, count its subarrays that contain strictly more
ones than zeros. A subarray must be contiguous; equal numbers of the two values
do not qualify. Each distinct pair of start and end indices is counted
separately, even when another range contains the same value sequence. Elements
inside a chosen range cannot be skipped or reordered.

Return the count modulo $10^9 + 7$ because the total number of qualifying
subarrays can be large.

### Function Contract

Let $N$ be the length of `nums`.

**Inputs**

- `nums`: a list of $N$ values, each either `0` or `1`, where
  $1 \le N \le 10^5$.

**Return value**

- The number of contiguous subarrays having more ones than zeros, reduced
  modulo $10^9 + 7$.

### Examples

**Example 1**

- Input: `nums = [0, 1, 1, 0, 1]`
- Output: `9`

**Example 2**

- Input: `nums = [0]`
- Output: `0`

**Example 3**

- Input: `nums = [1]`
- Output: `1`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Turn the comparison into a prefix-balance inequality**

Treat each `1` as $+1$ and each `0` as $-1$. Let a prefix balance be the sum
of those transformed values. A subarray beginning after prefix $i$ and ending
at prefix $j$ contains more ones exactly when
$P_j - P_i > 0$, or equivalently $P_i < P_j$.

For each current prefix, the number of qualifying subarrays ending there is
therefore the number of earlier prefix balances strictly smaller than the
current balance.

**Exploit that each balance step is one**

Maintain frequencies of all prior balances and a running count
`smaller_prefixes` for the current balance. When reading a `1`, the balance
moves from `b` to `b + 1`; every prior prefix equal to `b` becomes newly
smaller, so add `frequencies[b]`.

When reading a `0`, the balance moves from `b` to `b - 1`. Prefixes equal to
the new balance were smaller than `b` but are not strictly smaller than
`b - 1`, so subtract `frequencies[b - 1]`.

Add the updated smaller-prefix count to the answer, then record the current
balance for future endpoints. Initially, balance zero has frequency one for
the empty prefix.

The update preserves the exact number of earlier balances below the current
one because an integer step of one crosses only a single balance value. By the
prefix inequality, that count equals all qualifying subarrays ending at this
position. Summing it for every endpoint counts each qualifying subarray once
and no nonqualifying subarray.

#### Complexity detail

Each of the $N$ values causes constant expected-time hash-map operations, so
the total expected time is $O(N)$. Prefix balances range from $-N$ through
$N$, giving at most $O(N)$ distinct frequency entries and $O(N)$ space.
Reducing the accumulated answer modulo $10^9 + 7$ does not change the count
logic.

#### Alternatives and edge cases

- **Fenwick tree:** Coordinate-shift the balances and query how many prior
  values are smaller in $O(\log N)$ per prefix, for $O(N\log N)$ time.
- **Merge-sort counting:** Count ordered increasing prefix pairs during a
  divide-and-conquer merge, also in $O(N\log N)$ time.
- **Enumerate every subarray:** Extending from every starting index is correct
  but takes $O(N^2)$ time.
- A one-element `[1]` qualifies, whereas `[0]` does not.
- A balance difference of zero represents equal counts and must be excluded.
- The empty prefix must be recorded before processing the first element.
- Modulo reduction applies to the final count, not to prefix balances or
  frequencies.

</details>
