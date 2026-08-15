# Find the Number of Possible Ways for an Event

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3317 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, Dynamic Programming, Combinatorics |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-number-of-possible-ways-for-an-event/) |

## Problem Description

### Goal

An event has $n$ distinct performers and $x$ distinct stages. Every performer is assigned to exactly one stage. Performers assigned to the same stage form one band and perform together, while any number of stages may remain empty.

After the performances, the jury independently gives each nonempty band an integer score from 1 through $y$. Two events are different if at least one performer uses a different stage or if at least one band receives a different score. Count all possible events and return the result modulo $10^9+7$.

### Function Contract

**Inputs**

- `n`: The number of distinct performers, with $1\leq n\leq1000$.
- `x`: The number of distinct available stages, with $1\leq x\leq1000$.
- `y`: The number of possible scores for each nonempty band, with $1\leq y\leq1000$.

**Return value**

Return the number of distinct stage assignments and band-score assignments modulo $1{,}000{,}000{,}007$.

### Examples

#### Example 1

- **Input:** `n = 1, x = 2, y = 3`
- **Output:** `6`

The performer has two stage choices, and the resulting band has three score choices.

#### Example 2

- **Input:** `n = 5, x = 2, y = 1`
- **Output:** `32`

Every performer independently chooses one of two stages, and the only available score adds no extra choice.

#### Example 3

- **Input:** `n = 3, x = 3, y = 4`
- **Output:** `684`
