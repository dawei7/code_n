# Number of Pairs of Interchangeable Rectangles

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2001 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Math, Counting, Number Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/) |

## Problem Description

### Goal

An array `rectangles` describes $N$ rectangles. Entry `rectangles[i] = [width_i, height_i]` gives the positive width and height of rectangle $i$.

Two distinct rectangles at indices $i<j$ are interchangeable when their width-to-height ratios are equal:

$$
\frac{\textit{width}_i}{\textit{height}_i}
=
\frac{\textit{width}_j}{\textit{height}_j}.
$$

Count all index pairs that satisfy this equality. Equal dimensions at different indices still represent different rectangles and therefore form distinct pairs.

### Function Contract

**Inputs**

- `rectangles`: an array of $N$ pairs, where $1 \le N \le 10^5$.
- Every width and height lies between $1$ and $10^5$ inclusive.
- Let $M$ be the largest supplied dimension.

**Return value**

Return the number of index pairs $(i,j)$ with $i<j$ whose rectangles have the same width-to-height ratio.

### Examples

**Example 1**

- Input: `rectangles = [[4, 8], [3, 6], [10, 20], [15, 30]]`
- Output: `6`
- Explanation: All four ratios reduce to $1/2$, so every pair is interchangeable.

**Example 2**

- Input: `rectangles = [[4, 5], [7, 8]]`
- Output: `0`
- Explanation: The two ratios differ.

**Example 3**

- Input: `rectangles = [[1, 2], [2, 4], [3, 6], [4, 7]]`
- Output: `3`
- Explanation: The first three rectangles share ratio $1/2$ and create three pairs; the last rectangle has a different ratio.

### Required Complexity

- **Time:** $O(N\log M)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Represent each ratio exactly.** For dimensions `(width, height)`, compute $g=\gcd(\textit{width},\textit{height})$ and use `(width // g, height // g)` as its canonical key. Two positive fractions have the same reduced numerator and denominator exactly when their ratios are equal, avoiding floating-point rounding and integer-division mistakes.

**Count partners as each rectangle arrives.** Maintain a frequency map from reduced ratio keys to the number of earlier rectangles with that key. If the current key has appeared $c$ times, the current index forms exactly $c$ new pairs—one with each earlier matching index. Add $c$ to the answer, then increment the frequency.

Every valid pair is counted once, when its larger index is processed. No invalid pair is counted because different exact reduced ratios receive different keys. This incremental count is equivalent to summing $\binom{c}{2}$ for each final ratio-group size $c$ without requiring a second pass.

#### Complexity detail

Euclid's algorithm computes each greatest common divisor in $O(\log M)$ time, so processing all rectangles takes $O(N\log M)$ time. At most $N$ distinct reduced ratios are stored, giving $O(N)$ space.

#### Alternatives and edge cases

- **Compare every pair:** Cross multiplication gives an exact equality test but examines $O(N^2)$ pairs.
- **Use floating-point division as the key:** This is concise but makes correctness depend on binary rounding; reduced integer pairs are exact.
- **Use integer division only:** Ratios such as $3/2$ and $4/3$ have the same truncated quotient but are not interchangeable.
- A single rectangle creates no pair.
- Duplicate rectangles at different indices each contribute independently.
- Large groups can produce more than 32-bit many pairs, so languages with fixed-width integers need a 64-bit accumulator.

</details>
