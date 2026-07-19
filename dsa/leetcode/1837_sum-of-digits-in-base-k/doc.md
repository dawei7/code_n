# Sum of Digits in Base K

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/sum-of-digits-in-base-k/) |
| Frontend ID | 1837 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

You are given a positive integer `n` written as an ordinary base-10 value and a target base `k`. Convert the value of `n` to its base-$k$ digit representation.

The standard base-$k$ representation uses digits from 0 through $k-1$ and has no leading zeros. Interpret each resulting digit as a base-10 integer, add those digits, and return the sum as a base-10 integer. The representation itself does not need to be returned or stored.

### Function Contract

**Inputs**

- `n`: a positive base-10 integer, where $1 \le n \le 100$.
- `k`: the target base, where $2 \le k \le 10$.

**Return value**

- Return the sum of the digits in the standard base-$k$ representation of `n`.

### Examples

**Example 1**

- Input: `n = 34, k = 6`
- Output: `9`

The base-6 representation is `54`, and $5+4=9$.

**Example 2**

- Input: `n = 10, k = 10`
- Output: `1`

The representation remains `10`, whose digits sum to 1.

**Example 3**

- Input: `n = 8, k = 2`
- Output: `1`

The binary representation is `1000`.

### Required Complexity

- **Time:** $O(\log_k n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Extract the least significant base-\(k\) digit**

For a positive current value $x$, Euclidean division gives

$$
x = kq + r,
\qquad 0 \le r < k.
$$

The remainder $r$ is the least significant digit of $x$ in base $k$, and the quotient $q$ contains every more significant digit. Add `x % k` to the answer, replace `x` with `x // k`, and repeat until the quotient is zero.

**Why the accumulated remainders are exactly the digits**

The first division separates the units digit from a multiple of $k$. Dividing the quotient repeats the same decomposition for the next power of $k$. After $t$ iterations,

$$
n = d_0 + d_1k + \cdots + d_{t-1}k^{t-1},
$$

where every extracted remainder $d_i$ lies between 0 and $k-1$. This is precisely the unique base-$k$ representation, so summing the remainders returns the required digit sum.

The digits emerge from least significant to most significant, but addition is order-independent. No string conversion or reversal is needed.

#### Complexity detail

Each iteration divides the remaining value by $k$, so there are $\lfloor\log_k n\rfloor+1$ iterations and time is $O(\log_k n)$. The current quotient, remainder, and sum use $O(1)$ space.

#### Alternatives and edge cases

- **Build a representation string:** It is correct but stores $O(\log_k n)$ characters that are unnecessary when only the sum is requested.
- **Repeated subtraction for division:** It can recover each quotient and remainder without division, but may perform $O(n)$ total subtractions.
- **Recursive digit extraction:** It mirrors the positional definition but uses $O(\log_k n)$ call-stack space.
- **`n < k`:** The representation has one digit and the answer is `n`.
- **Base 10:** Repeated quotient and remainder operations sum the familiar decimal digits.
- **Base 2:** Every digit is 0 or 1, so the result equals the number of set bits.
- **Power of `k`:** Its representation is 1 followed by zeros and the answer is 1.
- **Maximum input:** `n = 100` still follows the same loop for every allowed base.
- **Zero remainders:** Interior or trailing zero digits contribute nothing but division must continue while the quotient is positive.

</details>
