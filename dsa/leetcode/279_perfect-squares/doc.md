# Perfect Squares

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 279 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Dynamic Programming, Breadth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/perfect-squares/) |

## Problem Description
### Goal
Given a positive integer `n`, express it as a sum of perfect-square integers such as `1`, `4`, `9`, or `16`. The same square may be used more than once, and every term must be the square of an integer.

Return the minimum number of terms among all sums equaling `n` exactly. A perfect-square input requires one term, while other values may have several decompositions with different lengths. The function returns only the smallest count, not the chosen squares or their order, and may not use zero-valued terms to pad a representation.

### Function Contract
**Inputs**

- `n`: a positive integer

**Return value**

The smallest count of square terms summing to `n`.

### Examples
**Example 1**

- Input: `n = 12`
- Output: `3`

**Example 2**

- Input: `n = 13`
- Output: `2`

**Example 3**

- Input: `n = 1`
- Output: `1`

### Required Complexity

- **Time:** $O(\sqrt{n})$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Number theory reduces the answer to four classified cases**

Lagrange guarantees that every positive integer needs at most four squares. First test whether `n` is one square. Remove factors of four, then Legendre's theorem says a remainder congruent to seven modulo eight requires exactly four squares.

Removing factors of four does not change whether the minimum is four: a representation of $n / 4$ scales by two, and squares modulo four force the reverse implication. The reduced $n \bmod 8 = 7$ test therefore identifies precisely the four-square case.

**Exhaustively test the two-square case**

Try each square $a^{2} \le n$ and check whether $n - a^{2}$ is also a square. A match gives two; if no match and the four-square condition did not apply, the answer is three.

**Exhausting cases in minimality order determines the answer**

The direct square test identifies exactly answer one. The loop considers every possible first square $a^{2}$, so a perfect-square remainder exists exactly when answer two is possible. Legendre's necessary-and-sufficient form identifies answer four. If none of those classifications applies, Lagrange still guarantees an answer no larger than four; excluding one, two, and four leaves exactly three.

#### Complexity detail

At most $\lfloor \sqrt{n} \rfloor$ candidates are tested with constant-time integer-square checks, giving $O(\sqrt{n})$ time and $O(1)$ space.

#### Alternatives and edge cases

- **Dynamic programming over every value through n:** takes $O(n \sqrt{n})$ time and $O(n)$ space.
- Integer square roots avoid floating-point rounding; one is itself a square.

</details>
