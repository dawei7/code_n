# Count Good Numbers

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/count-good-numbers/) |
| Frontend ID | 1922 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Recursion |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

A digit string is good when its digits obey rules based on their zero-based positions. At every even index, the digit must itself be even, so the choices are `0`, `2`, `4`, `6`, and `8`. At every odd index, the digit must be prime, so the choices are `2`, `3`, `5`, and `7`.

Given the length `n`, count all good digit strings of that length. Leading zeroes are allowed, meaning the objects are strings rather than ordinary decimal representations. Since the count grows rapidly, return it modulo $10^9+7$.

### Function Contract

**Inputs**

- `n`: the required digit-string length, with $1 \le n \le 10^{15}$.

**Return value**

- Return the number of length-$n$ good digit strings modulo $10^9+7$.

### Examples

**Example 1**

- Input: `n = 1`
- Output: `5`

The valid strings are `"0"`, `"2"`, `"4"`, `"6"`, and `"8"`.

**Example 2**

- Input: `n = 4`
- Output: `400`

There are two even-indexed and two odd-indexed positions, giving $5^2 \cdot 4^2=400$ choices.

**Example 3**

- Input: `n = 50`
- Output: `564908303`

### Required Complexity

- **Time:** $O(\log n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Count the two kinds of positions**

Zero-based even indices are `0, 2, 4, ...`. There are

$$
E = \left\lceil \frac{n}{2} \right\rceil
$$

of them, computed as `(n + 1) // 2`. Each independently accepts five digits. The remaining

$$
O = \left\lfloor \frac{n}{2} \right\rfloor
$$

odd-indexed positions each accept four prime digits.

By the product rule, the unrestricted count is $5^E4^O$. This includes leading-zero strings correctly because zero is one of the five choices at index zero.

**Exponentiate under the modulus**

The exponent may be as large as $5\cdot10^{14}$, so multiplying once per position is infeasible. Binary exponentiation repeatedly squares the base and uses the binary digits of the exponent, reducing an exponent with each halving step. Compute both powers modulo $M=10^9+7$, multiply them, and reduce once more.

Every string makes one independent valid choice at each position, and every such choice sequence is a distinct good string. Therefore the product counts every valid string exactly once.

#### Complexity detail

Binary exponentiation uses $O(\log E+\log O)=O(\log n)$ modular multiplications. Only the exponents, bases, modulus, and accumulated products are stored, so iterative exponentiation uses $O(1)$ space.

#### Alternatives and edge cases

- **Multiply once per position:** This computes the same product but takes $O(n)$ time and cannot handle $n$ near $10^{15}$.
- **Enumerate digit strings:** Exploring all combinations is exponential and unnecessary because positions are independent.
- **Use ordinary exponentiation before reducing:** The intermediate integer has an impractical number of digits; reduce during exponentiation.
- **Odd length:** The even-indexed positions receive the extra slot.
- **Leading zero:** It is allowed and must remain one of the five choices at index zero.
- **Length one:** There are five choices and no odd-indexed positions, so the factor $4^0$ is one.

</details>
