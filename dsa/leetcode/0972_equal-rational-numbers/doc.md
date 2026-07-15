# Equal Rational Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 972 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [equal-rational-numbers](https://leetcode.com/problems/equal-rational-numbers/) |

## Problem Description

### Goal

Two strings `s` and `t` each represent a non-negative rational number. A representation has an integer part, may have a decimal point followed by a finite non-repeating part, and may finish with a nonempty repeating part enclosed in parentheses. An empty non-repeating part after the decimal point is allowed, as in `"1."` or `"1.(9)"`.

Parentheses mean that their digits repeat forever. Different strings can therefore denote the same value: a repeating block may be shifted or repeated, and an infinite tail of nines can carry into the preceding digits. Return `true` exactly when `s` and `t` denote the same rational number.

### Function Contract

**Inputs**

- `s` and `t`: valid non-negative rational-number representations.
- Each integer part has from $1$ through $4$ digits and no leading zero except the integer `0`.
- Each non-repeating fractional part has from $0$ through $4$ digits.
- When present, each repeating part has from $1$ through $4$ digits.
- Let $L=\lvert s\rvert+\lvert t\rvert$ be the total representation length.

**Return value**

Return `true` if both strings have exactly the same rational value; otherwise return `false`.

### Examples

**Example 1**

- Input: `s = "0.(52)", t = "0.5(25)"`
- Output: `true`

**Example 2**

- Input: `s = "0.1666(6)", t = "0.166(66)"`
- Output: `true`

**Example 3**

- Input: `s = "0.9(9)", t = "1."`
- Output: `true`

### Required Complexity

- **Time:** $O(L)$
- **Space:** $O(L)$

<details>
<summary>Approach</summary>

#### General

**Convert each representation to an exact fraction.** Split off the optional parenthesized digits, then divide the remaining text at the decimal point into an integer part and a possibly empty non-repeating part. Use rational arithmetic throughout; binary floating point cannot reliably distinguish or equate repeating decimals.

**Account for finite decimal digits.** If the non-repeating part has length $m$ and integer value $a$, its contribution is

$$
\frac{a}{10^m}.
$$

Add this to the integer part. Leading zeroes inside the fractional text are preserved by the length $m$, even though integer conversion removes them from $a$.

**Account for the infinite repetition.** If the repeating block has length $r$ and integer value $b$, its repeating decimal value begins after the $m$ finite digits and contributes

$$
\frac{b}{10^m(10^r-1)}.
$$

This geometric-series identity also handles a block of all zeroes and converts a tail of all nines to the exact carried value automatically.

**Compare normalized values.** Python's `Fraction` reduces each numerator and denominator by their greatest common divisor. The two strings are equal exactly when their resulting fractions compare equal, independent of how their repeating blocks were written.

#### Complexity detail

Splitting and converting each representation examines $O(L)$ characters. With the problem's bounded component lengths, exact fraction operations are constant-sized, so total time is $O(L)$. The parsed substrings and exact fractions use $O(L)$ space.

#### Alternatives and edge cases

- **Expand a fixed number of digits:** Repeating each block many times and comparing decimal strings is heuristic unless a sufficient bound is proved, and it obscures the infinite-nines carry.
- **Floating-point conversion:** Numerical rounding may equate different rationals or separate equal representations.
- **Cross-multiply custom fractions:** Construct numerators and denominators with the same formulas, reduce or cross-multiply, and avoid a fraction library. This is exact but more error-prone.
- **Empty non-repeating part:** `"1."` is valid and equals the integer `1`.
- **Repeating zero:** `"0.(0)"` equals `"0"`.
- **Repeating nine:** `"0.9(9)"` equals `"1."` exactly, not merely approximately.

</details>
