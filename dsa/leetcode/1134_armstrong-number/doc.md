# Armstrong Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1134 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/armstrong-number/) |

## Problem Description

### Goal

You are given a positive integer `n` containing $d$ decimal digits. The number is an Armstrong number when the sum obtained by raising each of its digits to the $d$th power is exactly equal to `n` itself.

Determine whether `n` is an Armstrong number and return the corresponding boolean value. Repeated digits contribute separately, and a digit `0` contributes $0^d=0$. The exponent is the digit count of the complete input, not a fixed value such as three.

### Function Contract

**Inputs**

- `n`: an integer satisfying $1 \le n \le 10^8$.

Let $d=\lfloor \log_{10} n \rfloor+1$ be the number of decimal digits in `n`; the input bound guarantees $1 \le d \le 9$.

**Return value**

`true` exactly when the sum of the $d$th powers of all decimal digits equals `n`; otherwise `false`.

### Examples

**Example 1**

- Input: `n = 153`
- Output: `true`
- Explanation: $1^3+5^3+3^3=153$.

**Example 2**

- Input: `n = 123`
- Output: `false`
- Explanation: $1^3+2^3+3^3=36$, which is not `123`.

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Determine the shared exponent.** Copy `n` and repeatedly apply integer division by `10`, incrementing `digits` once per extracted decimal position. This obtains the number of digits without changing the original value needed for the final comparison.

**Accumulate each digit's contribution.** Reset the working copy to `n`. Repeatedly compute `digit = remaining % 10`, add `digit ** digits` to `total`, and update `remaining //= 10`. Each decimal digit is extracted exactly once and raised to the same exponent.

When no digits remain, `total` is precisely the sum in the Armstrong definition, so `total == n` is necessary and sufficient. The computation uses the original number only for comparison and never mistakes a partial sum or truncated working copy for the target.

#### Complexity detail

The arithmetic method performs two passes over the $d$ digits and uses constant scalar storage. Abstractly this is $O(d)$ time and $O(1)$ space, but the public domain fixes $d \le 9$, so runtime and space are both $O(1)$ over every valid input.

#### Alternatives and edge cases

- **Decimal string:** Convert `n` to a string, use its length as $d$, and sum converted character powers; this is concise but allocates $O(d)$ string space.
- **Precomputed Armstrong set:** Membership in the finite set of Armstrong numbers under $10^8$ is constant time, but it hides the defining calculation and is less adaptable.
- **Single-digit number:** Every value from `1` through `9` is Armstrong because $x^1=x$.
- **Internal zero digits:** Zero positions contribute nothing but still count toward the exponent $d$.
- **Power exponent:** The exponent must be recomputed from the complete number; using a hard-coded cube handles only three-digit inputs.

</details>
