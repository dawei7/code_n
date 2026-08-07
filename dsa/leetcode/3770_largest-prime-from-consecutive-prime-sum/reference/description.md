### 1. Description

You are given an integer `n`.

Return the **largest prime number** less than or equal to `n` that can be expressed as the **sum** of one or more **consecutive prime numbers** starting from 2. If no such number exists, return 0.

### 2. Function Contract

**Inputs**

- `n`: The inclusive upper bound for both the returned prime and its consecutive-prime sum.

Let $N=\texttt{n}$, and list the primes as $p_1=2,p_2=3,p_3=5,\ldots$. The only candidate sums are the prefixes $S_j=\sum_{i=1}^{j}p_i$.

**Return value**

Return the largest $S_j\leq N$ that is prime. Return `0` when no such prefix sum exists; in particular, this occurs when $n = 1$.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** n = 20

**Output:** 17

**Explanation:**

The prime numbers less than or equal to $n = 20$ which are consecutive prime sums are:

- $2 = 2$

- $5 = 2 + 3$

- $17 = 2 + 3 + 5 + 7$

The largest is 17, so it is the answer.

</div>
#### Example 2

<div class="example-block">
**Input:** n = 2

**Output:** 2

**Explanation:**

The only consecutive prime sum less than or equal to 2 is 2 itself.

</div>

### 4. Constraints

- $1 \le n \le 5 * 10^{5}$