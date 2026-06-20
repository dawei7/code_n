# 0/1 Knapsack

| | |
|---|---|
| **ID** | `dp_03` |
| **Category** | dynamic |
| **Complexity (required)** | $O(n²)$ |
| **Difficulty** | 5/10 |
| **Interview relevance** | 9/10 |
| **Wikipedia** | [Knapsack problem](https://en.wikipedia.org/wiki/Knapsack_problem) |

## Problem statement

You have `n` items, each with a `weight[i]` and a `value[i]`.
You also have a knapsack that can hold at most `W` units of
weight. Each item can be taken **at most once** (the "0/1"
constraint). Choose a subset that maximizes the total value
without exceeding the weight capacity.

**Input:** `weights = [w1, w2, ..., wn]`,
`values = [v1, v2, ..., vn]`, capacity `W`.
**Output:** the maximum total value achievable.

**Example:**

| Item | Weight | Value |
|---:|---:|---:|
| 0 | 2 | 3 |
| 1 | 3 | 4 |
| 2 | 4 | 5 |
| 3 | 5 | 6 |

`W = 5`. Best subset: items 0 + 1 (weight 5, value 7) or
items 0 + 2 (weight 6 — over) — so the answer is 7. Or take
items 1 + 3 (weight 8 — over). Best: items 0+1 = value 7.

## When to use it

- The most-cited **textbook DP problem** and one of the
  most-asked DP variants in interviews. Recurrence is small
  (two choices per item: take it or skip it) but the state
  space (item × remaining capacity) is 2D.
- Whenever a problem has a **"subset of N items, each with
  two attributes, pick a subset that fits a budget and
  maximizes some metric"** shape, it's knapsack or a
  knapsack variant (subset sum, partition, etc.).

## Approach

Define `dp[i][w]` = the maximum value achievable using only
the first `i` items (items `0..i-1`) with capacity `w`.

**Recurrence** (consider item `i-1`):
- **Skip it:** `dp[i][w] = dp[i-1][w]`.
- **Take it** (only if `weights[i-1] <= w`):
  `dp[i][w] = dp[i-1][w - weights[i-1]] + values[i-1]`.
- Take the max: `dp[i][w] = max(skip, take)`.

**Base case:** `dp[0][w] = 0` for all `w` (no items = no value).
**Answer:** `dp[n][W]`.

**Space optimization:** each row `i` only depends on row
`i-1`, so we can collapse the 2D table into a 1D array
iterated **right-to-left** so we don't overwrite values we
still need:

```
for i in 0..n-1:
    for w in W down to weights[i]:
        dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
```

This is the production implementation and the one cOde(n)'s
engine checks against ($O(n·W)$ time, $O(W)$ space).

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for dp_03: 0/1 Knapsack.

Classic DP table: dp[i][c] = max value using the first i items
with capacity c. O(n * capacity) time, O(n * capacity) space.
"""


def solve(weights, values, capacity, n):
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        w = weights[i - 1]
        v = values[i - 1]
        for c in range(capacity + 1):
            if w <= c:
                dp[i][c] = max(dp[i - 1][c], dp[i - 1][c - w] + v)
            else:
                dp[i][c] = dp[i - 1][c]
    return dp[n][capacity]
```

</details>

## Walk-through

`weights = [2, 3, 4]`, `values = [3, 4, 5]`, `W = 5`.

`dp = [0, 0, 0, 0, 0, 0]` (length 6).

**Item 0 (w=2, v=3):** iterate w from 5 down to 2.

| w | dp[w] before | candidate | dp[w] after |
|---:|---:|---:|---:|
| 5 | 0 | dp[3]+3 = 3 | 3 |
| 4 | 0 | dp[2]+3 = 3 | 3 |
| 3 | 0 | dp[1]+3 = 3 | 3 |
| 2 | 0 | dp[0]+3 = 3 | 3 |

`dp = [0, 0, 3, 3, 3, 3]`.

**Item 1 (w=3, v=4):** iterate w from 5 down to 3.

| w | dp[w] before | candidate | dp[w] after |
|---:|---:|---:|---:|
| 5 | 3 | dp[2]+4 = 7 | **7** |
| 4 | 3 | dp[1]+4 = 4 | 4 |
| 3 | 3 | dp[0]+4 = 4 | 4 |

`dp = [0, 0, 3, 4, 4, 7]`.

**Item 2 (w=4, v=5):** iterate w from 5 down to 4.

| w | dp[w] before | candidate | dp[w] after |
|---:|---:|---:|---:|
| 5 | 7 | dp[1]+5 = 5 | 7 |
| 4 | 4 | dp[0]+5 = 5 | 5 |

`dp = [0, 0, 3, 4, 5, 7]`. Answer: `dp[5] = 7`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(n·W)$ | $O(W)$ |
| **Average** | $O(n·W)$ | $O(W)$ |
| **Worst** | $O(n·W)$ | $O(W)$ |

Note: the complexity is **pseudo-polynomial in W** — it
depends on the *magnitude* of W, not the number of bits.
For `W = 10^9` this is intractable. The 0/1 knapsack is
NP-hard in general; the DP is exact only for small W.

## Variants & optimizations

- **Unbounded knapsack** — items can be taken multiple times.
  Change the inner loop to iterate `w` left-to-right.
  (`dp_05` — Coin Change is a special case.)
- **Fractional knapsack** — items can be split. Solvable by
  greedy: sort by value/weight ratio, take the highest ratio
  first. (Not in cOde(n)'s 0/1 spec.)
- **Subgraph / target-sum** — `dp_06` (Subset Sum) is the
  decision variant (`values = weights` and the target is a
  sum, not a max).
- **Meet-in-the-middle** — for large `W` and small `n` (n ≤ 40),
  split items into two halves, enumerate each half's subsets
  (2^(n/2) each), and combine. Reduces to $O(2^(n/2)$ · n).

## Real-world applications

- **Capital budgeting** — pick a portfolio of projects that
  fits a budget and maximizes expected return.
- **Cargo loading** — pack containers of varying sizes and
  priorities into a ship's hold.
- **Resource allocation in compilers** — picking registers,
  selecting instructions for a delay slot, etc.
- **Subset-sum cryptography** — the Merkle-Hellman knapsack
  cryptosystem is built on the hardness of subset sum.

## Related algorithms in cOde(n)

- **[dp_05 — Coin Change](dp_05_coin-change.md)** — unbounded
  variant: minimize coins, not maximize value. (d=5/10, r=9/10)
- **[dp_06 — Subset Sum](dp_06_subset-sum.md)** — decision
  variant (true/false), 0/1. (d=5/10, r=9/10)
- **[dp_17 — Partition Equal Subset Sum](dp_17_partition-equal-subset-sum.md)** —
  can you split the array into two equal-sum subsets?
  (d=5/10, r=9/10)
- **[dp_30 — Coin Change (Count Ways)](dp_30_coin-change-count-ways.md)** —
  unbounded, counting solutions. (d=3/10, r=9/10)

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-
programming reference sites. For the canonical encyclopedia
entry, follow the Wikipedia link at the top of the page.
Source repository: <https://github.com/dawei7/code_n>.*
