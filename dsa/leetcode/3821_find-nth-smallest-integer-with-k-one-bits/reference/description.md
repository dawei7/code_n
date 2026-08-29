### 1. Description

You are given two positive integers `n` and `k`.

Return an integer denoting the $n^{\text{th}}$ smallest positive integer that has **exactly** `k` ones in its binary representation. It is guaranteed that the answer is **strictly less** than $2^{50}$.

### 2. Function Contract

**Inputs**

- `n`: The positive, one-based rank of the requested integer.
- `k`: The exact number of one bits required in its binary representation.

Let $B=50$. Because the answer is less than $2^B$, every candidate can be viewed as a $B$-bit string with leading zeros. A candidate qualifies when exactly `k` of those positions contain `1`. Leading zeros do not change the represented positive integer or its one-bit count.

The source guarantee ensures that `n` does not exceed the number of qualifying values below $2^B$ for the supplied `k`.

**Return value**

Return the `n`th smallest positive integer whose binary representation contains exactly `k` ones.

### 3. Examples

#### Example 1

- **Input:** n = 4, k = 2

- **Output:** 9

- **Explanation:** The 4 smallest positive integers that have exactly $k = 2$ ones in their binary representations are:

- $3 = \text{11}_{2}$

- $5 = \text{101}_{2}$

- $6 = \text{110}_{2}$

- $9 = \text{1001}_{2}$

#### Example 2

- **Input:** n = 3, k = 1

- **Output:** 4

- **Explanation:** The 3 smallest positive integers that have exactly $k = 1$ one in their binary representations are:

- $1 = 1_{2}$

- $2 = \text{10}_{2}$

- $4 = \text{100}_{2}$

### 4. Constraints

- $1 \le n \le 2^{50}$

- $1 \le k \le 50$

- The answer is strictly less than $2^{50}$.
