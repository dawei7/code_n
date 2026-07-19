# Cutting Ribbons

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/cutting-ribbons/) |
| Frontend ID | 1891 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Each value in `ribbons` is the positive integer length of one ribbon. A ribbon may remain whole or be cut into any number of pieces whose lengths are positive integers. Material left after producing useful pieces may be discarded.

Choose one positive integer length $x$ and produce at least `k` pieces that all have exactly that length. Extra pieces are allowed and need not be used. Return the greatest feasible $x$, or return `0` when even `k` pieces of length one cannot be obtained.

### Function Contract

**Inputs**

- `ribbons`: an array of $N$ positive integer ribbon lengths.
- `k`: the required number of equal-length pieces.
- $1 \le N \le 10^5$, $1 \le \texttt{ribbons[i]} \le 10^5$, and $1 \le k \le 10^9$.
- Let

$$
M=\min\left(\max(\texttt{ribbons}),\left\lfloor\frac{\sum_i \texttt{ribbons[i]}}{k}\right\rfloor\right).
$$

**Return value**

- Return the maximum positive integer piece length that can be produced at least `k` times, or `0` if none exists.

### Examples

**Example 1**

- Input: `ribbons = [9,7,5], k = 3`
- Output: `5`

Each ribbon can provide one length-`5` piece.

**Example 2**

- Input: `ribbons = [7,5,9], k = 4`
- Output: `4`

The ribbons yield one, one, and two length-`4` pieces.

**Example 3**

- Input: `ribbons = [5,7,9], k = 22`
- Output: `0`

Their total length is only `21`, so 22 positive-length pieces are impossible.

### Required Complexity

- **Time:** $O(N\log M)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Turn a length into a feasibility test**

For a proposed positive length $x$, a ribbon of length $r$ contributes $\left\lfloor r/x\right\rfloor$ complete pieces. Summing this quantity over all ribbons determines whether at least `k` pieces can be produced. Remainders require no special handling because unused material may be discarded.

Feasibility is monotone: if length $x$ works, every smaller positive integer length also works; if $x$ fails, every larger length fails. The answer is therefore the last feasible value in an ordered integer range.

**Binary-search the last feasible value**

Use `0` as a feasible sentinel and $M$ as the greatest possible answer: no piece can exceed the longest ribbon or the average material available per required piece. At each step choose the upper midpoint so a two-value interval makes progress. If the piece count reaches `k`, retain the midpoint as the lower boundary; otherwise move the upper boundary below it.

The maintained interval always contains the largest feasible length. When its endpoints meet, every larger value has been rejected and the remaining value is feasible. A result of zero means the positive range was empty, exactly matching the impossible case.

#### Complexity detail

Each feasibility check scans at most $N$ ribbons and may stop once the count reaches `k`. Binary search makes $O(\log M)$ checks, for $O(N\log M)$ worst-case time. The boundaries, midpoint, and running piece count use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Test every length:** Evaluating all candidates from one through $M$ is correct but takes $O(NM)$ time.
- **Binary search with lower midpoint:** It also works, but the boundary updates must be chosen carefully to avoid an infinite two-value interval.
- **Insufficient total material:** If the total ribbon length is less than `k`, the upper bound is zero and the answer is immediately `0`.
- **Discarded remainder:** A ribbon need not be divided evenly; leftover length has no cost.
- **More than `k` pieces:** Feasibility requires at least `k`, not exactly `k`.
- **One required piece:** The longest original ribbon is optimal.
- **Large piece count:** Stop accumulating once `k` is reached to avoid unnecessary work and fixed-width overflow.

</details>
