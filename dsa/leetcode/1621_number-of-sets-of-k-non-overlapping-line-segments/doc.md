# Number of Sets of K Non-Overlapping Line Segments

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1621 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Dynamic Programming, Combinatorics |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/) |

## Problem Description
### Goal
There are `n` points on a one-dimensional plane at integral coordinates 0 through `n - 1`. Draw exactly `k` line segments whose endpoints are chosen from these points. Every segment must have positive length and therefore cover at least two points.

The interiors of the segments may not overlap, but consecutive segments are allowed to share an endpoint. The segments do not need to cover every point. Count the distinct sets of `k` valid segments and return the result modulo $10^9+7$.

### Function Contract
**Inputs**

- `n`: the number of points, where $2 \le n \le 1000$.
- `k`: the exact number of segments, where $1 \le k \le n-1$.
- Let $M=10^9+7$ be the required prime modulus.

**Return value**

Return the number of sets of exactly `k` non-overlapping positive-length segments, allowing shared endpoints, reduced modulo $M$.

### Examples
**Example 1**

- Input: `n = 4, k = 2`
- Output: `5`

**Example 2**

- Input: `n = 3, k = 1`
- Output: `3`

**Example 3**

- Input: `n = 30, k = 7`
- Output: `796297179`

### Required Complexity
- **Time:** $O(k+\log M)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Write the ordered endpoint constraints.** Sort the segments from left to right and denote segment $i$ by $(\ell_i,r_i)$ for $0 \le i < k$. Positive length gives $\ell_i<r_i$, while non-overlap with shared endpoints allowed gives $r_i\le\ell_{i+1}$. Thus the $2k$ endpoints alternate strict within-segment inequalities and weak between-segment inequalities.

**Turn every inequality strict.** Add the segment index $i$ to both endpoints of segment $i$. The transformed sequence

$$
\ell_0,\ r_0,\ \ell_1+1,\ r_1+1,\ldots,\ell_{k-1}+k-1,\ r_{k-1}+k-1
$$

is strictly increasing. Its values lie from 0 through $n+k-2$, a domain of $n+k-1$ positions. Conversely, choose any $2k$ strictly increasing positions from that domain, pair consecutive positions, and subtract pair index $i$ from both members. Strictness inside each transformed pair restores $\ell_i<r_i$; strictness between pairs restores $r_i\le\ell_{i+1}$. This is a bijection, so the exact count is

$$
\binom{n+k-1}{2k}.
$$

**Evaluate the binomial coefficient modulo a prime.** Multiply the `2k` numerator factors and `2k` denominator factors modulo $M$. Because $2k<M$, the denominator is nonzero modulo $M$. Fermat's little theorem gives its inverse as `pow(denominator, M - 2, M)`. Multiplying the numerator by that inverse yields the requested residue.

#### Complexity detail

The numerator and denominator products contain $2k$ factors, taking $O(k)$ time. Modular exponentiation takes $O(\log M)$ time. Only a constant number of modular integers is stored, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Prefix-sum dynamic programming:** Track how many segment sets end or remain open at each point. This is intuitive and takes $O(nk)$ time with $O(k)$ rolling space.
- **Pascal triangle:** Compute $\binom{n+k-1}{2k}$ by the addition recurrence. It avoids modular inverses but takes $O((n+k)k)$ time and $O(k)$ space.
- **Factorial tables:** Precompute factorials and inverse factorials through $n+k-1$ for $O(n+k+\log M)$ preprocessing and $O(n+k)$ space.
- When `k = 1`, every pair of distinct points defines one segment, giving $\binom{n}{2}$.
- When `k = n - 1`, only the chain of adjacent segments is possible, so the answer is 1.
- Shared endpoints are allowed; replacing $r_i\le\ell_{i+1}$ with a strict original inequality would undercount.
- The modulus is applied to the count, not to endpoint coordinates or segment lengths.

</details>
