## General

**Search cost means the number of record highs**

While scanning an array from left to right, the search algorithm increases its cost whenever the current value is strictly greater than every earlier value. Such a value is a new maximum, also called a record high.

The first array element always creates the first maximum because the conceptual maximum before the array is zero and all allowed values are positive. Later elements increase the cost only when they exceed the current maximum; equal values do not.

To count arrays, a partial construction needs three facts:

- Its current length.
- Its search cost so far.
- Its exact maximum value.

The precise earlier elements no longer matter once those facts are known, because the effect of appending a value depends only on how it compares with the current maximum.

**The three-dimensional state**

The stored solution defines:

$$
\texttt{dp}[i][c][j]
$$

as the number of arrays of length $i$, with search cost exactly $c$, and maximum value exactly $j$.

The table dimensions are `n + 1` by `k + 1` by `m + 1`. Index zero in each dimension is available for convenient boundaries even though a nonempty valid array has positive length, cost, and maximum.

This state distinguishes maxima because the number of legal non-record append choices depends on $j$. If only length and cost were stored, the algorithm would not know whether there are two or ninety values that can be appended without creating a new maximum.

**Base arrays of length one**

For each `i` from 1 through `m`:

```python
dp[1][1][i] = 1
```

There is exactly one length-one array whose maximum is `i`: `[i]`. Its only element is a new maximum, so its cost is one. Every other length-one state remains zero.

The early return for `k == 0` is correct because `n >= 1` and the first positive value always creates cost one. No valid nonempty array can have zero search cost.

**Case one: the appended value is not a new maximum**

Suppose the new length is $i$, cost is $c$, and maximum remains $j$. The first $i-1$ values must already form an array counted by `dp[i - 1][c][j]`.

To keep the maximum equal to $j$ and avoid increasing cost, the appended value may be any integer from 1 through $j$. There are exactly $j$ choices, including $j$ itself because equality is not a new maximum. Therefore:

$$
j \cdot \texttt{dp}[i-1][c][j]
$$

arrays reach the state through a non-record final value. The code installs this as the initial state count:

```python
dp[i][c][j] = dp[i - 1][c][j] * j
```

**Case two: the appended value is a new maximum**

If the last value creates the new maximum $j$, then that last value must be exactly $j$. The preceding array must have cost $c-1$ and some maximum $j_0$ strictly smaller than $j$.

Every $j_0$ from 1 through $j-1$ is possible, so the second contribution is:

$$
\sum_{j_0=1}^{j-1}\texttt{dp}[i-1][c-1][j_0].
$$

The inner loop adds those states one at a time:

```python
for j0 in range(1, j):
    dp[i][c][j] += dp[i - 1][c - 1][j0]
    dp[i][c][j] %= mod
```

Appending $j$ to any counted predecessor creates exactly one new maximum, raises the cost from $c-1$ to $c$, and makes the final maximum exactly $j$.

The two cases are disjoint. A final value cannot both be at most the old maximum and strictly exceed it. Together they cover every possible final value, so adding their counts is safe.

**Loop bounds encode impossible costs**

The outer length loop begins at two because length-one states are initialized. For a length-$i$ array, search cost cannot exceed $i$, and the result only needs costs through $k$. The cost loop:

```python
range(1, min(k + 1, i + 1))
```

therefore visits precisely $1 \le c \le \min(k,i)$. States with a larger cost are impossible and need not be computed.

The maximum loop covers every `j` from 1 through `m`. A small `j` naturally limits how many record highs can occur; impossible combinations simply retain zero counts.

**A small example with `n = 2` and `m = 3`**

Every one-element base state `[1]`, `[2]`, and `[3]` has cost one.

For final maximum 2 and cost one, the previous maximum must already be 2 and the last value may be 1 or 2. This gives `[2,1]` and `[2,2]` through the multiplication term.

For final maximum 2 and cost two, the last value must be the new maximum 2 and the previous maximum must be 1. This gives `[1,2]` through the summation term.

When the requested cost is one, summing final maxima yields six arrays:

```text
[1,1]
[2,1], [2,2]
[3,1], [3,2], [3,3]
```

Any array whose second element exceeds its first has cost two and is excluded.

**Produce the answer across all possible final maxima**

The requested array may finish with any maximum from 1 through `m`. These sets are disjoint, so:

```python
for i in range(1, m + 1):
    ans += dp[n][k][i]
    ans %= mod
```

adds all valid arrays exactly once. Reducing during state transitions and final summation preserves the required remainder modulo $10^9+7$.

**Why the DP is correct**

The base states enumerate every possible one-element array exactly once. Assume all states for length $i-1$ are correct. Any length-$i$ array either ends with a value no greater than its earlier maximum, which is counted by the $j$-choice multiplication, or ends with the strict new maximum $j$, which is counted under its unique earlier maximum $j_0<j$. No array belongs to both cases, and no legal final value lies outside them. Therefore, every length-$i$ state is correct by induction, and summing `dp[n][k][j]` returns exactly the arrays with required cost.

## Complexity detail

The exact stored source has $O(nkm)$ states. For each state with maximum $j$, it explicitly loops over $j-1$ smaller maxima. Summed over all $j$, that is $1+2+\cdots+(m-1)=O(m^2)$ work per length-cost pair. Its true running time is therefore $O(nkm^2)$.

The allocated table contains $(n+1)(k+1)(m+1)$ integers, so the exact source uses $O(nkm)$ space.

The manifest advertises $O(nkm)$ time and $O(km)$ space. Those bounds require two optimizations not present in this stored implementation: prefix sums over the maximum dimension to replace the `j0` loop with an $O(1)$ lookup, and rolling length layers to discard states older than `i-1`. The approach file reports both the protected source's actual cost and the distinction from the advertised optimized form.

## Alternatives and edge cases

- **Prefix sums over previous maxima:** Maintain cumulative sums of `dp[i - 1][c - 1][j0]` so the new-maximum contribution is read in constant time. This reduces time to $O(nkm)$.
- **Rolling length layers:** Only length `i - 1` is needed to compute length `i`. Keeping two $k$ by $m$ layers reduces space to $O(km)$.
- **Top-down memoization:** Cache states by position, current maximum, and remaining cost. It is conceptually direct but its naive transition over larger next maxima still costs an extra factor of $m$.
- **Enumerate all arrays:** There are $m^n$ candidates, which is infeasible even for the moderate parameter limits.
- **`k = 0`:** No nonempty positive array can have zero record highs, so the early return is zero.
- **`k > n`:** An array cannot create more record highs than positions; relevant states remain zero.
- **`k > m`:** Strictly increasing record values must be distinct members of 1 through `m`, so the answer is also zero.
- **`m = 1`:** Every array consists only of ones. Its search cost is one, so exactly one array exists when `k = 1`.
- **Equal to current maximum:** Appending `j` is part of the $j$ non-record choices and does not increase search cost.
- **Modulo timing:** Counts can grow rapidly, so repeated reduction is necessary for bounded representations in fixed-width languages.
