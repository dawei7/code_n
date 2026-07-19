# Maximize Number of Nice Divisors

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/maximize-number-of-nice-divisors/) |
| Frontend ID | 1808 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, Recursion, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Given a positive integer `primeFactors`, construct some positive integer $n$ whose prime factorization contains at most `primeFactors` factors when multiplicity is counted. For example, $12 = 2^2 \cdot 3$ has the factor list `[2,2,3]`, so it uses three prime factors.

A divisor of $n$ is nice when it is divisible by every distinct prime factor of $n$. For $n=12$, the divisors $6$ and $12$ are nice because both contain factors $2$ and $3$, while $3$ and $4$ each omit one of them. Choose $n$ so that its number of nice divisors is as large as possible under the prime-factor limit. Return that maximum count modulo $10^9+7$; the value of $n$ itself is not required.

### Function Contract

**Inputs**

- `primeFactors`: an integer $P$ satisfying $1 \le P \le 10^9$. It is the maximum number of prime factors of $n$, counted with multiplicity.

**Return value**

- Return the greatest achievable number of nice divisors modulo $10^9+7$.

### Examples

**Example 1**

- Input: `primeFactors = 5`
- Output: `6`

One valid construction has prime exponents $3$ and $2$, whose product gives $3 \cdot 2=6$ nice divisors.

**Example 2**

- Input: `primeFactors = 8`
- Output: `18`

Splitting the exponent budget as $3+3+2$ gives $3 \cdot 3 \cdot 2=18$.

**Example 3**

- Input: `primeFactors = 1`
- Output: `1`

A prime $n$ has only itself as a divisor containing its sole prime factor.

### Required Complexity

- **Time:** $O(\log P)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Translate divisors into an exponent product**

Write a candidate integer as

$$
n = p_1^{a_1}p_2^{a_2}\cdots p_t^{a_t},
$$

where the $p_i$ are distinct primes and the positive exponents satisfy $\sum_i a_i \le P$. A nice divisor must contain every $p_i$, but its exponent for that prime may be any integer from $1$ through $a_i$. These choices are independent, so the number of nice divisors is

$$
a_1a_2\cdots a_t.
$$

The actual prime values do not affect the count. The task is therefore to partition the available exponent budget into positive integers whose product is maximum.

**Use the full budget and prefer parts of three**

Except at the smallest boundary, leaving budget unused cannot improve the product: it can enlarge an existing part or create another useful part. Any part $x \ge 5$ should be split into $3$ and $x-3$, because $3(x-3)>x$. Parts equal to $1$ are harmful beside a part of $3$, since replacing $3+1$ by $2+2$ changes the product from $3$ to $4$. Consequently an optimal partition uses as many threes as possible, with only these remainder repairs:

- remainder $0$: use only threes;
- remainder $1$: replace one `3 + 1` by `2 + 2`, contributing a factor of $4$;
- remainder $2$: append one factor of $2$.

For $P \le 3$, no split improves the single part, so the answer is $P$.

**Compute the enormous power without constructing it**

Use modular exponentiation for the power of three and multiply by the remainder factor modulo $10^9+7$. Binary exponentiation evaluates the power with logarithmically many modular multiplications even when $P$ is one billion.

#### Complexity detail

The arithmetic that chooses the remainder case is constant time. Modular exponentiation uses $O(\log P)$ multiplications and $O(1)$ iterative storage. All other operations are constant-space modular arithmetic.

#### Alternatives and edge cases

- **Dynamic programming over every budget:** The integer-break recurrence is correct but needs $O(P^2)$ time in its direct form, which is impossible for $P$ up to $10^9$.
- **Repeated multiplication:** Multiplying one factor of three at a time uses $O(P)$ time; binary modular exponentiation obtains the same residue in $O(\log P)$.
- **Floating-point exponentiation:** It cannot represent the enormous exact product and may corrupt the modular result through rounding or overflow.
- **Budgets from one through three:** Return `primeFactors` directly; forcing the general remainder-one rewrite would otherwise request a negative exponent when $P=1$.
- **Remainder one:** Use one fewer factor of three and multiply by four, rather than multiplying by one.
- **Modulo timing:** Apply the modulus during exponentiation and after the final factor, not after attempting to construct the unbounded integer.
- **Prime identities:** Distinct prime choices do not matter; only their positive exponents determine the number of nice divisors.

</details>
