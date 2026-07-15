# 3Sum With Multiplicity

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 923 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Two Pointers, Sorting, Counting |
| Official Link | [LeetCode](https://leetcode.com/problems/3sum-with-multiplicity/) |

## Problem Description
### Goal

You are given an integer array `arr` and an integer `target`. Select three distinct positions whose indices occur in the strict order $i<j<k$. A selection contributes to the answer exactly when `arr[i] + arr[j] + arr[k] == target`; the positions themselves, rather than only their three values, identify the selection.

Count every qualifying index triple. Equal values appearing at different positions can therefore produce several distinct triples, and all of that multiplicity must be included. Because the resulting count may be very large, return it modulo $10^9+7$.

### Function Contract
Let $n$ be the length of `arr`, and let $V=101$ be the number of possible values from $0$ through $100$.

**Inputs**

- `arr`: an array of $n$ integers, where $3 \le n \le 3000$ and every value is from $0$ through $100$.
- `target`: an integer from $0$ through $300$.

**Return value**

The number of ordered index choices $i<j<k$ whose three values sum to `target`, reduced modulo $10^9+7$.

### Examples
**Example 1**

- Input: `arr = [1,1,2,2,3,3,4,4,5,5], target = 8`
- Output: `20`
- Explanation: Value triples `(1,2,5)`, `(1,3,4)`, `(2,2,4)`, and `(2,3,3)` contribute with their index multiplicities.

**Example 2**

- Input: `arr = [1,1,2,2,2,2], target = 5`
- Output: `12`

**Example 3**

- Input: `arr = [2,1,3], target = 6`
- Output: `1`

### Required Complexity
- **Time:** $O(n+V^2)$
- **Space:** $O(V)$

<details>
<summary>Approach</summary>

#### General

**Count values before choosing value triples**

Because every array value is in the fixed range from $0$ through $100$, first build a frequency array. Then enumerate value triples $x\le y\le z$ rather than index triples. Once $x$ and $y$ are chosen, `z = target - x - y` is forced; ignore it unless $y\le z\le100$.

**Convert each value pattern into index choices**

The number of index triples depends on which values are equal:

- If $x=y=z$, choose three indices from the same frequency: $\binom{c_x}{3}$.
- If $x=y<z$, choose two occurrences of $x$ and one of $z$: $\binom{c_x}{2}c_z$.
- If $x<y=z$, use $c_x\binom{c_y}{2}$.
- If all three values differ, use $c_xc_yc_z$.

Add these contributions modulo $10^9+7$. Every valid index triple has exactly one nondecreasing value triple, and each combination formula counts precisely the ways to select its distinct indices. Conversely, each selected combination supplies three array positions with the requested sum; sorting their indices gives exactly one order $i<j<k$. Therefore the cases partition the answer without overlap.

#### Complexity detail

Building frequencies takes $O(n)$ time. Enumerating $x$ and $y$ uses $O(V^2)$ pairs, while $z$ is computed directly, giving $O(n+V^2)$ total time. The frequency array uses $O(V)$ space. Here $V=101$ is fixed by the input domain, so both value-range terms are bounded constants.

#### Alternatives and edge cases

- **Index-pair counting:** Maintaining earlier frequencies while enumerating every later pair counts triples in $O(n^2)$ time and $O(V)$ space.
- **Sort plus two pointers:** Fixing one index and scanning the remaining suffix can also handle duplicate runs correctly in $O(n^2)$ time.
- **Naive three loops:** Enumerating every index triple costs $O(n^3)$.
- **Three equal values:** Use a combination, not $c_x^3$, because one array index cannot be selected more than once.
- **Two equal values:** The repeated value may be either the smaller pair or the larger pair; these require different formulas.
- **Missing forced value:** A zero frequency naturally contributes nothing.
- **Modulo arithmetic:** Apply the modulus during accumulation because multiplicities can make the exact count large.

</details>
