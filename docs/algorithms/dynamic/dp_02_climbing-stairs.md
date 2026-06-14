# Climbing Stairs

| | |
|---|---|
| **ID** | `dp_02` |
| **Category** | dynamic |
| **Complexity (required)** | O(n) |
| **Difficulty** | 5/10 |
| **Interview relevance** | 9/10 |
| **Wikipedia** | [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_sequence) (same recurrence) |

## Problem statement

You are at the bottom of a staircase with `n` steps. You can
climb **1 or 2 steps at a time**. How many distinct ways can
you reach the top?

**Input:** an integer `n >= 0` (the number of steps).
**Output:** the count of distinct ways to reach the top,
modulo nothing (or modulo `10^9 + 7` in the harder variant).

**Example:**

| n | Ways | Explanation |
|---:|---:|---|
| 0 | 1 | One way: stay put. (Edge case convention.) |
| 1 | 1 | One 1-step. |
| 2 | 2 | `1+1`, or `2`. |
| 3 | 3 | `1+1+1`, `1+2`, `2+1`. |
| 4 | 5 | `1+1+1+1`, `1+1+2`, `1+2+1`, `2+1+1`, `2+2`. |
| 5 | 8 | (Fibonacci again.) |

The sequence `1, 1, 2, 3, 5, 8, 13, ...` is exactly Fibonacci.

## When to use it

- The canonical **first DP problem** in most interview-prep
  books. The state and recurrence are obvious, and the only
  trick is recognizing the rolling-variable space optimization.
- As a **fibonacci-recognition warm-up**: many "you can do
  thing A or thing B in k steps" problems reduce to a Fibonacci
  recurrence.
- The "k steps at a time" generalization (1, 2, ..., or k
  steps) generalizes to the k-bonacci sequence and is a
  natural follow-up.

## Approach

Let `f(n)` be the number of ways to climb `n` steps. The last
move you make is either a 1-step (leaving `n-1` steps to go) or
a 2-step (leaving `n-2` steps to go). These choices don't
overlap, so:

```
f(n) = f(n-1) + f(n-2)
```

with `f(0) = 1` (the empty sequence is "one way" to stay) and
`f(1) = 1`. This is the Fibonacci recurrence, shifted by one
index — `f(n) = F(n+1)`.

The dynamic-programming insight: the naive recursive
formulation re-evaluates `f(k)` exponentially many times; the
top-down memoized or bottom-up tabulated version touches each
`f(k)` exactly once. And the rolling version only needs the
last two values.

## Algorithm (pseudocode)

```
climb_stairs(n):
    if n < 2:
        return 1
    prev = 1        # f(0)
    curr = 1        # f(1)
    for i from 2 to n:
        next = prev + curr
        prev = curr
        curr = next
    return curr
```

For the modulo variant, replace `next = prev + curr` with
`next = (prev + curr) mod M`.

## Walk-through

`n = 5`:

| Iteration | i | prev (f(i-2)) | curr (f(i-1)) | next (f(i)) |
|---|---:|---:|---:|---:|
| init | — | 1 | 1 | — |
| 1 | 2 | 1 | 1 | 2 |
| 2 | 3 | 1 | 2 | 3 |
| 3 | 4 | 2 | 3 | 5 |
| 4 | 5 | 3 | 5 | 8 |

Returns 8. ✓ (8 distinct ways to climb 5 stairs.)

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | O(1) | O(1) — `n < 2` |
| **Average** | O(n) | O(1) |
| **Worst** | O(n) | O(1) |

The required complexity is O(n); the rolling implementation
matches it exactly. The memoized recursive version is also
O(n) but uses O(n) stack space (or O(n) extra heap if you
use a dict).

## Variants & optimizations

- **k steps at a time** — replace the 1-or-2 with 1-or-2-or-…-or-k.
  Recurrence becomes `f(n) = f(n-1) + f(n-2) + … + f(n-k)`,
  the k-bonacci sequence. Space stays O(1) but the constant
  is now `O(k)` per iteration; switch to a sliding window of
  size `k` to keep it tight.
- **Distinct step costs** — instead of "1 or 2 steps", you
  pay a `cost[i]` for taking `i` steps. Recurrence:
  `f(n) = max(f(n-1) + cost[1], f(n-2) + cost[2])`. This is
  the **Min Cost Climbing Stairs** problem (`dp_23`).
- **Memoized recursion** — clean code but uses O(n) space for
  the call stack. The cOde(n) engine will accept it as long
  as total operations are O(n) (they are, because each `f(k)`
  is computed once).
- **Matrix exponentiation** — for very large `n` (say `n > 10^9`)
  and many queries, raise the 2×2 transition matrix to the
  nth power in O(log n).

## Real-world applications

- **Counting paths in a DAG** — any DAG where the in-degree of
  each node is bounded and the edge labels are 1 and 2 reduces
  to this recurrence. Used in compilers (counting paths in a
  control-flow graph) and in network routing.
- **Tiling a 1×n board with 1×1 and 1×2 tiles** — exactly the
  same recurrence, different framing. (The 1×1 tile is a "1
  step", the 1×2 tile is a "2 steps".)
- **Combinatorial identities** — proves the Cassini identity
  `F(n-1)·F(n+1) − F(n)^2 = (−1)^n` and several others by
  the matrix-exponentiation form.

## Related algorithms in cOde(n)

- **[dp_01 — Fibonacci](dp_01_fibonacci.md)** — the same
  recurrence, framed for computing Fibonacci numbers directly.
  (d=5/10, r=9/10)
- **[dp_23 — Min Cost Climbing Stairs](dp_23_min-cost-climbing-stairs.md)** —
  generalization with per-step costs. (d=3/10, r=9/10)
- **[dp_11 — House Robber](dp_11_house-robber.md)** — also
  uses a 2-variable rolling DP, but the recurrence is
  `f(n) = max(f(n-1), f(n-2) + a[n])` (decision, not count).
  (d=5/10, r=9/10)

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-
programming reference sites. For the canonical encyclopedia
entry, follow the Wikipedia link at the top of the page.
Source repository: <https://github.com/dawei7/code_n>.*
