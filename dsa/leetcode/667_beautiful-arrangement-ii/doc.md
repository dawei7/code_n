# Beautiful Arrangement II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 667 |
| Difficulty | Medium |
| Topics | Array, Math |
| Official Link | [LeetCode](https://leetcode.com/problems/beautiful-arrangement-ii/) |

## Problem Description
### Goal
Given integers `n` and `k`, construct an array `answer` containing `n` different positive integers ranging from `1` through `n`. For every adjacent pair, form the absolute difference `abs(answer[i] - answer[i + 1])`.

The collection of those adjacent differences must contain exactly `k` distinct integers. Return any array satisfying both the permutation and difference requirements. Each value from `1` through `n` must appear exactly once; the goal concerns the number of distinct differences, not the sum or maximum of the differences.

### Function Contract
**Inputs**

- `n`: the permutation length
- `k`: the required number of distinct adjacent absolute differences, with $1 \le k < n$

**Return value**

- Any permutation of `1..n` satisfying the difference requirement

### Examples
**Example 1**

- Input: `n = 3`, `k = 1`
- Output: `[1, 2, 3]`

**Example 2**

- Input: `n = 3`, `k = 2`
- Output: `[1, 3, 2]`

**Example 3**

- Input: `n = 4`, `k = 3`
- Output: `[1, 4, 2, 3]`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Use an increasing prefix for repeated difference one**

Append $1, 2, \ldots, n - k - 1$. Every adjacency inside this prefix has difference one, so the prefix introduces only one distinct difference regardless of its length.

**Zigzag across the remaining interval**

The unused values form the interval `[n - k, n]`, containing $k + 1$ numbers. Repeatedly take its smallest remaining value, then its largest, moving both boundaries inward. The resulting adjacent differences are $k, k - 1, \ldots, 1$ in some order.

The boundary from the increasing prefix into the zigzag, when the prefix exists, also has difference one. Therefore the complete permutation has exactly the distinct differences `{1, 2, ..., k}`.

**Why every value appears exactly once**

The prefix uses precisely the values below $n - k$. The two-pointer zigzag consumes each value from $n - k$ through `n` once as the interval closes. These disjoint ranges cover `1..n`, so the output is a permutation as well as satisfying the difference count.

#### Complexity detail

Every value from `1` through `N` is appended once, giving $O(N)$ time. The returned permutation uses $O(N)$ space; the construction itself needs only constant-sized boundary variables beyond the output.

#### Alternatives and edge cases

- **Zigzag the first $k + 1$ values, then append the rest increasingly:** is another linear construction with the same difference set.
- **Backtracking over permutations:** can find valid outputs for small inputs but grows factorially.
- **Repeated immutable-prefix copying:** preserves the constructive idea but can turn output assembly into $O(N^2)$ work.
- $k = 1$ permits the ordinary increasing permutation.
- $k = n - 1$ uses the entire range as one low-high zigzag.
- Many outputs are valid, so correctness depends on permutation membership and difference count rather than one exact ordering.

</details>
