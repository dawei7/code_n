# Ugly Number III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1201 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Binary Search, Combinatorics, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/ugly-number-iii/) |

## Problem Description

### Goal

For this problem, an ugly number is any positive integer divisible by at least one of the three given integers `a`, `b`, or `c`. Divisibility by more than one of them still identifies a single number in the ordered sequence.

Given `n` and the three divisors, return the $n$th ugly number in increasing order. The result is guaranteed to exist between 1 and $2\times10^9$, inclusive.

### Function Contract

**Inputs**

- `n`: The 1-indexed position, where $1\le n\le10^9$.
- `a`, `b`, and `c`: Positive divisors, each at most $10^9$, with $1\le abc\le10^{18}$.
- Let $U=2\times10^9$, the guaranteed upper bound on the answer.

**Return value**

- The $n$th positive integer divisible by `a`, `b`, or `c`.

### Examples

**Example 1**

- Input: `n = 3`, `a = 2`, `b = 3`, `c = 5`
- Output: `4`

The sequence begins `2,3,4,5,6,8,...`.

**Example 2**

- Input: `n = 4`, `a = 2`, `b = 3`, `c = 4`
- Output: `6`

**Example 3**

- Input: `n = 5`, `a = 2`, `b = 11`, `c = 13`
- Output: `10`

### Required Complexity

- **Time:** $O(\log U)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Count the union without enumerating it.** For a candidate bound $x$, ordinary division counts multiples of one divisor. Multiples shared by two divisors are counted twice and must be subtracted using least common multiples; numbers shared by all three are then added back. Define $L_{ab}=\operatorname{lcm}(a,b)$, $L_{ac}=\operatorname{lcm}(a,c)$, $L_{bc}=\operatorname{lcm}(b,c)$, and $L_{abc}=\operatorname{lcm}(a,b,c)$. Then

$$
C(x)=\left\lfloor\frac{x}{a}\right\rfloor+\left\lfloor\frac{x}{b}\right\rfloor+\left\lfloor\frac{x}{c}\right\rfloor-\left\lfloor\frac{x}{L_{ab}}\right\rfloor-\left\lfloor\frac{x}{L_{ac}}\right\rfloor-\left\lfloor\frac{x}{L_{bc}}\right\rfloor+\left\lfloor\frac{x}{L_{abc}}\right\rfloor.
$$

This is exactly the number of ugly numbers at most $x$.

**Binary-search the first sufficient bound.** The function $C(x)$ is monotone. Search the inclusive answer domain from 1 through $U$ for the smallest `x` satisfying $C(x)\ge n`. That first sufficient value must itself be ugly: otherwise its count would equal the preceding count, contradicting minimality. It is therefore exactly the $n$th ugly number.

**Compute least common multiples safely.** Use `left // gcd(left, right) * right`, dividing before multiplying. This reduces overflow risk in fixed-width languages while preserving the exact least common multiple needed by inclusion-exclusion.

#### Complexity detail

The four least common multiples take a constant number of greatest-common-divisor operations on bounded machine integers. Binary search performs $O(\log U)$ iterations, and each evaluates seven constant-time integer divisions, giving $O(\log U)$ time. Only fixed scalar bounds and least common multiples are stored, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Three-pointer sequence merge:** Advancing the next multiple of each divisor is correct and avoids duplicates, but takes $O(n)$ time and cannot handle $n$ up to $10^9$.
- **Test every integer:** Checking divisibility one value at a time may examine nearly the entire answer range.
- **Redundant divisors:** If one divisor is a multiple of another, inclusion-exclusion cancels the duplicate contribution correctly.
- **Equal divisors:** The union still contains each multiple once despite three identical input streams.
- **First position:** The answer is `min(a, b, c)`.
- **Shared multiples:** A number divisible by two or all three divisors occupies only one sequence position.
- **Large products:** Least common multiples and midpoint counts require sufficiently wide integer arithmetic in bounded-integer languages.
- **Lower-bound search:** Returning an arbitrary value with $C(x)\ge n$ is insufficient; the smallest such value is required.

</details>
