# Rod Cutting

| | |
|---|---|
| **ID** | `dp_09` |
| **Category** | dynamic |
| **Complexity (required)** | O(n²) |
| **Difficulty** | 5/10 |
| **Interview relevance** | 9/10 |
| **Wikipedia** | [Cutting stock problem](https://en.wikipedia.org/wiki/Cutting_stock_problem) |

## Problem statement

Given a rod of length `n` and a price table `prices[i]` for a
rod of length `i + 1` (for `i = 0..n-1`), determine the
**maximum revenue** obtainable by cutting the rod into pieces
and selling them.

**Input:** an integer `n` and an array `prices` of length `n`.
**Output:** the maximum revenue.

**Example:**

| Length | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Price  | 1 | 5 | 8 | 9 |10 |17 |17 |20 |

`n = 8`. Best: cut into 2 + 2 + 2 + 2 (revenue 5+5+5+5 = 20)
OR 6 + 2 (17+5 = 22) OR 1+2+5+... — best is **22** (6+2).

## When to use it

- The classic introductory DP for "**partition into pieces
  to maximize something**" — the unbounded-knapsack flavor
  where each cut is between pieces, and pieces can repeat.
- A small variant ("break a stick of length N") is sometimes
  given in phone screens as a warm-up.

## Approach

Let `dp[i]` = the maximum revenue for a rod of length `i`.

**Recurrence:** consider the first cut. If we cut off a piece
of length `j` (for `j = 1..i`), we keep `prices[j-1]` and
have a remaining rod of length `i - j` worth `dp[i - j]`.
Take the max over all first cuts:

```
dp[i] = max(prices[j-1] + dp[i - j])  for j = 1..i
```

**Base case:** `dp[0] = 0` (no rod, no revenue).

**Answer:** `dp[n]`.

This is the unbounded-knapsack shape — we're choosing
"pieces" (lengths) with repetition, maximizing value.

## Algorithm (pseudocode)

```
rod_cut(prices, n):
    dp = [0] * (n + 1)
    for i from 1 to n:
        for j from 1 to i:
            candidate = prices[j-1] + dp[i - j]
            if candidate > dp[i]:
                dp[i] = candidate
    return dp[n]
```

## Walk-through

`prices = [1, 5, 8, 9, 10, 17, 17, 20]`, `n = 8`.

`dp = [0, 0, 0, 0, 0, 0, 0, 0, 0]`.

| i | try j=1 (1+dp[i-1]) | j=2 (5+dp[i-2]) | j=3 (8+dp[i-3]) | j=4 (9+dp[i-4]) | ... | dp[i] |
|---:|---:|---:|---:|---:|---|---:|
| 1 | 1+0=1 | — | — | — | — | 1 |
| 2 | 1+1=2 | 5+0=5 | — | — | — | 5 |
| 3 | 1+5=6 | 5+1=6 | 8+0=8 | — | — | 8 |
| 4 | 1+8=9 | 5+5=10 | 8+1=9 | 9+0=9 | — | 10 |
| 5 | 1+10=11 | 5+8=13 | 8+5=13 | 9+1=10 | 10+0=10 → **13** |
| 6 | 1+13=14 | 5+10=15 | 8+8=16 | 9+5=14 | 10+1=11, 17+0=17 → **17** |
| 7 | 1+17=18 | 5+13=18 | 8+10=18 | 9+8=17 | 10+5=15, 17+1=18, 17+0=17 → **18** |
| 8 | 1+18=19 | 5+17=22 | 8+13=21 | 9+10=19 | 10+8=18, 17+5=22, 17+1=18, 20+0=20 → **22** |

Answer: `dp[8] = 22`. ✓ (cuts: 2 + 6, revenue 5 + 17 = 22.)

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | O(n²) | O(n) |
| **Average** | O(n²) | O(n) |
| **Worst** | O(n²) | O(n) |

Each `dp[i]` is the max over at most `i` candidates, so the
double loop is O(n²). Space is O(n) for the dp array.

## Variants & optimizations

- **Reconstruct the cuts** — keep a parallel `cut_at[i]`
  array recording which `j` was chosen; walk back to print
  the cuts.
- **Cost of cutting** — if each cut costs `c`, subtract `c`
  from the candidate. Some cuts become uneconomical.
- **Minimum cuts for a target revenue** — instead of max
  revenue, find the min number of pieces such that
  revenue ≥ target. Requires a different DP shape (track
  both metrics).
- **Generalized rod cutting** — pieces can have a *width*
  as well as length (e.g. 2D cutting stock). The 1D DP
  generalizes to a 2D DP.

## Real-world applications

- **Cutting stock problem** — cutting raw materials (steel,
  paper, fabric, lumber) into saleable pieces to minimize
  waste. NP-hard in general; the simple version is the
  rod-cutting DP.
- **Logistics** — "how to split a 40-foot container into
  standard pallets to maximize value?"
- **Printing** — best way to cut a roll of paper or fabric
  into print jobs.
- **Compiler register allocation** — "split a long-living
  variable into registers to maximize cache hits."
- **Production planning** — break a long production run into
  batches that match demand.

## Related algorithms in cOde(n)

- **[dp_03 — 0/1 Knapsack](dp_03_knapsack.md)** — bounded
  variant, maximize. (d=5/10, r=9/10)
- **[dp_05 — Coin Change](dp_05_coin-change.md)** — unbounded,
  minimize count. (d=5/10, r=9/10)
- **[dp_07 — LIS](dp_07_longest-increasing-subsequence.md)** —
  another classic 1D DP, also often asked in interviews.
  (d=5/10, r=9/10)

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-
programming reference sites. For the canonical encyclopedia
entry, follow the Wikipedia link at the top of the page.
Source repository: <https://github.com/dawei7/code_n>.*
