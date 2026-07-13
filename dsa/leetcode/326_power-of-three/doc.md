# Power of Three

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 326 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, Recursion |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/power-of-three/) |

## Problem Description
### Goal
Given a signed 32-bit integer `n`, determine whether it can be written exactly as $3^{x}$ for some integer exponent $x \ge 0$. The valid sequence begins with $1 = 3^{0}$, followed by `3`, `9`, `27`, and so on.

Return `True` only for positive exact powers of three. Return `False` for zero, negative integers, and positive numbers containing any factor or remainder outside repeated multiplication by three. The task asks for a boolean classification rather than the exponent. Satisfy the follow-up without using loops or recursion where the platform constraint requests the constant-time divisibility observation.

### Function Contract
**Inputs**

- `n`: the integer to classify

**Return value**

`True` when $n = 3^{x}$ for some integer $x \ge 0$; otherwise `False`.

### Examples
**Example 1**

- Input: `n = 27`
- Output: `True`

**Example 2**

- Input: `n = 0`
- Output: `False`

**Example 3**

- Input: `n = -1`
- Output: `False`

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Use the largest representable power as a divisibility certificate**

Within the positive signed 32-bit range, the largest power of three is $3^{19} = 1,162,261,467$; multiplying by three once more exceeds the maximum integer value allowed by the contract.

Every positive power $3^{x}$ in range divides $3^{19}$. Conversely, the only positive divisors of $3^{19}$ are $3^0,3^1,\ldots,3^{19}$, because its prime factorization contains no prime other than three. Therefore $n$ is a power of three exactly when it is positive and divides $1{,}162{,}261{,}467$ evenly.

**Positivity is a separate requirement**

The remainder operation alone is not enough: zero cannot be a divisor, and negative divisors of the maximum power are not powers $3^{x}$ for nonnegative `x`. Check $n > 0$ before taking the modulus.

The value one is accepted because it is $3^{0}$ and divides every power of three. A value such as 45 is rejected even though three divides it, because its extra factor five prevents it from dividing $3^{19}$.

The prime-factor argument proves both directions: every valid input divides the certificate, and every positive divisor of the certificate has precisely the required form. No logarithm or floating-point equality is involved.

#### Complexity detail

For the fixed signed-32-bit input domain, the method performs one comparison and one integer remainder operation, giving $O(1)$ time and $O(1)$ space.

#### Alternatives and edge cases

- **Repeatedly divide by three:** is simple and exact but takes $O(\log_{3} n)$ divisions.
- **Use a floating-point logarithm:** can misclassify values near an integer exponent because of rounding.
- **Check only $n \bmod 3 = 0$:** accepts composite values such as 45 that contain other prime factors.
- Zero and negative values are false. One is true, and $3^{19}$ is the largest positive power covered by the contract.

</details>
