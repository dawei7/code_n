# Check if Number is a Sum of Powers of Three

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1780 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/) |

## Problem Description

### Goal

Given a positive integer `n`, determine whether it can be written as a sum of distinct powers of three. A power of three has the form $3^k$ for a nonnegative integer exponent $k$.

Each power may appear at most once in the sum, but any collection of different exponents is allowed. Return `true` when such a representation exists and `false` otherwise.

### Function Contract

**Inputs**

- `n`: an integer satisfying $1 \le n \le 10^7$.
- The input bound means `n` has at most fifteen base-three digits.

**Return value**

Return `true` exactly when there is a set $S$ of distinct nonnegative integers such that

$$
n=\sum_{k\in S}3^k.
$$

### Examples

**Example 1**

- Input: `n = 12`
- Output: `true`
- Explanation: $12=3^1+3^2$.

**Example 2**

- Input: `n = 91`
- Output: `true`
- Explanation: $91=3^0+3^2+3^4$.

**Example 3**

- Input: `n = 21`
- Output: `false`
- Explanation: Its base-three representation requires a digit `2`, which would repeat one power.

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Translate distinct powers into ternary digits**

In a base-three representation, the coefficient of $3^k$ is the digit at position $k$. A sum of distinct powers chooses each coefficient from $\{0,1\}$: zero excludes the power and one includes it. Therefore the requested representation exists exactly when the ordinary ternary expansion of `n` contains no digit `2`.

**Inspect the expansion from least significant digit**

Repeatedly apply `divmod(n, 3)`. The remainder is the next ternary digit, and the quotient contains all higher digits. Return `false` immediately if a remainder is `2`; otherwise continue until the quotient becomes zero. If every digit was zero or one, those one-valued positions give a valid set of distinct powers, proving `true`.

#### Complexity detail

For an unrestricted integer, extracting its ternary digits takes $O(\log_3 n)$ time and $O(1)$ space. The public constraint $n \le 10^7 < 3^{15}$ fixes the loop at no more than fifteen iterations, so both time and auxiliary space are $O(1)$ over the complete legal domain.

#### Alternatives and edge cases

- **Greedy subtraction:** Repeatedly subtract the largest power of three not exceeding the remainder. This can work, but base-three division states the no-repetition condition more directly.
- **Enumerate subsets:** Generate sums of the relevant powers and test membership. With fifteen powers the domain is bounded, but this performs exponential work and obscures the numeral-system structure.
- `n = 1` is representable as $3^0$.
- Any ternary digit `2`, including the least significant one, makes the representation impossible.
- Zero digits are allowed because not every power must be selected.
- A dense valid value can use every power from $3^0$ through $3^{14}$ once.

</details>
