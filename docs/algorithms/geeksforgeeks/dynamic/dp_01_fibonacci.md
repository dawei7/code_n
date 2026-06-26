# Fibonacci

| | |
|---|---|
| **ID** | `dp_01` |
| **Category** | dynamic |
| **Complexity (required)** | $O(n)$ |
| **Difficulty** | 5/10 |
| **Interview relevance** | 9/10 |
| **Wikipedia** | [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_sequence) |

## Problem statement

Compute the *n*-th Fibonacci number. The Fibonacci sequence is
defined by:

```
F(0) = 0,  F(1) = 1
F(n) = F(n-1) + F(n-2)   for n >= 2
```

The first few values are `0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...`.

**Input:** a non-negative integer `n`.
**Output:** `F(n)`.

**Example:**

| Input | Output |
|---|---|
| 0 | 0 |
| 1 | 1 |
| 2 | 1 |
| 10 | 55 |
| 30 | 832040 |

## When to use it

- As a **pedagogical introduction to dynamic programming**: it
  has the smallest possible state (`prev`, `curr`) and the most
  recognizable recurrence. Interviewers use it to test whether
  you can identify the right DP shape (top-down memoization
  vs. bottom-up tabulation vs. $O(1)$-space rolling).
- To introduce the **naive-vs-cached contrast**: the literal
  recursive formulation is $O(2^n)$ and exhausts the call stack
  around `n=50`; the same code with memoization is $O(n)$.
- As a **producer of large numbers for testing**: at `n=1000`
  `F(n)` is a 209-digit integer, so it's a natural fit for
  big-int or modular-arithmetic follow-ups.

Don't use it in production code — the naive recursion is
catastrophically slow, and the closed-form (Binet's formula)
loses precision for `n > 70`.

## Approach

The naive recursive definition `F(n) = F(n-1) + F(n-2)`
recomputes the same sub-problem exponentially many times:
`F(2)` is recomputed once for every leaf in the recursion tree.

**Memoization** (top-down DP) stores each computed value in a
table indexed by `n`. The first call to `F(k)` computes it; all
subsequent calls are $O(1)$ lookups. This turns the recursion
from $O(2^n)$ into $O(n)$ time and $O(n)$ space.

**Tabulation** (bottom-up DP) starts from the smallest
sub-problems (`F(0)`, `F(1)`) and works up to `F(n)`, filling
a table. Same $O(n)$ time, $O(n)$ space.

**Rolling / $O(1)$-space** observes that `F(n)` only depends on
the previous two values, so the entire table collapses into
two variables `prev` and `curr`. Each iteration:
`prev, curr = curr, prev + curr`. This is the production
implementation and the one cOde(n)'s engine checks against
(the required complexity is $O(n)$).

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for dp_01: Fibonacci.

Compute the n-th Fibonacci number bottom-up. O(n) time, O(1)
space.
"""


def solve(n):
    if n <= 1:
        return n
    previous, current = 0, 1
    for _ in range(2, n + 1):
        previous, current = current, previous + current
    return current
```

</details>

## Walk-through

Compute `F(6)`:

| Iteration | i | prev | curr | next = prev + curr |
|---|---:|---:|---:|---:|
| init | — | 0 | 1 | — |
| 1 | 2 | 0 | 1 | 1 |
| 2 | 3 | 1 | 1 | 2 |
| 3 | 4 | 1 | 2 | 3 |
| 4 | 5 | 2 | 3 | 5 |
| 5 | 6 | 3 | 5 | 8 |

After `i = 6`, `curr = 8`, which is `F(6)`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(1)$ | $O(1)$ — `n < 2` short-circuit |
| **Average** | $O(n)$ | $O(1)$ |
| **Worst** | $O(n)$ | $O(1)$ |

The recurrence is `T(n) = T(n-1) + O(1)`, which solves to
$O(n)$. Space is $O(1)$ in the rolling implementation; $O(n)$ in
the memoized/tabulated variants.

## Variants & optimizations

- **Naive recursion** — `def f(n): return f(n-1) + f(n-2) if n > 1 else n`.
  $O(2^n)$ time, $O(n)$ stack space. **Don't submit this in
  interviews**, but DO mention it as a foil to show you
  understand the optimization.
- **Memoized recursion** — top-down with a dict. $O(n)$ time, $O(n)$
  space. Useful when not all sub-problems are needed.
- **Matrix exponentiation** — `[[1,1],[1,0]]^n` gives
  `F(n+1)` in $O(log n)$ time. The right answer if the problem
  asks for many queries and `n` is large.
- **Doubling identities** — `F(2k) = F(k) * (2*F(k+1) - F(k))`,
  `F(2k+1) = F(k+1)^2 + F(k)^2`. Combined with fast exponentiation
  this gives $O(log n)$ time and is the standard for huge `n`
  (e.g. `n = 10^18`).

## Real-world applications

- **Fibonacci search** — a search algorithm on sorted arrays
  that uses Fibonacci numbers instead of binary-search halving.
  Marginally faster than binary search on some hardware because
  it avoids the `(low+high)//2` overflow.
- **Fibonacci heap** — a priority queue with $O(1)$ amortized
  insert and $O(log n)$ extract-min. Used in some shortest-path
  and minimum-spanning-tree implementations.
- **Financial ratios** — Fibonacci retracement levels (23.6 %,
  38.2 %, 61.8 %) are used in technical stock analysis. (Worth
  knowing exists; not scientifically robust.)
- **Modular arithmetic puzzles** — `F(n) mod m` is a standard
  programming-contest warmup that requires careful handling
  of large `n` and periodicity (Pisano period).

## Related algorithms in cOde(n)

- **[dp_02 — Climbing Stairs](dp_02_climbing-stairs.md)** — same
  recurrence shape (`F(n) = F(n-1) + F(n-2)`), different
  framing. (d=5/10, r=9/10)
- **[dp_11 — House Robber](dp_11_house-robber.md)** — adjacent
  element exclusion, also a 2-state rolling DP. (d=5/10, r=9/10)
- **[dp_23 — Min Cost Climbing Stairs](dp_23_min-cost-climbing-stairs.md)** —
  same Fibonacci-shaped recurrence with a cost dimension.
  (d=3/10, r=9/10)

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-
programming reference sites. For the canonical encyclopedia
entry, follow the Wikipedia link at the top of the page.
Source repository: <https://github.com/dawei7/code_n>.*
