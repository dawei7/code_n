# Find Binomial Coefficients

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BINCOEFF |
| Difficulty Band | Number theory |
| Path | Data Structures and Algorithms |
| Lesson | Modular Arithmetic |
| Official Link | [BINCOEFF](https://www.codechef.com/learn/course/number-theory/LINTDSA07/problems/BINCOEFF) |

---

## Problem Statement

Given two integers $n$, and $k$, find $\binom{n}{k} = \frac{n!}{k!(n-k)!}$. Output the answer modulo $10^9 + 7$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The only line of each test case consists of two integers - $n, k$.

---

## Output Format

For each test case, output on a new line the answer.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq k \leq n \leq 10^6$

---

## Examples

**Example 1**

**Input**

```text
3
5 2
5 3
6 4
```

**Output**

```text
10
10
15
```

**Explanation**

**Test case 1:** $\frac{n!}{k!(n-k)!} = \frac{5!}{2!* 3!} = \frac{5*4}{2} = 10$

**Test case 2:** $\frac{n!}{k!(n-k)!} = \frac{5!}{3! * 2!} = \frac{5*4}{2} = 10$

**Test case 3:** $\frac{n!}{k!(n-k)!} = \frac{6!}{4! * 2!} = \frac{6*5}{2} = 15$

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 2
```

**Output for this case**

```text
10
```



#### Test case 2

**Input for this case**

```text
5 3
```

**Output for this case**

```text
10
```



#### Test case 3

**Input for this case**

```text
6 4
```

**Output for this case**

```text
15
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Element - [Find Binomial Coefficients in Number theory](https://www.codechef.com/learn/course/number-theory/LINTDSA07/problems/BINCOEFF?tab=solution)

### [](#problem-statement-1)Problem Statement:

Given three integers n and k, find \binom{n}{k} = \frac{n!}{k!(n-k)!}. Output the answer modulo 10^9+7

### [](#approach-2)Approach:

- **Precomputation of Factorials and Inverses**:

- We precompute the factorials and their modular inverses up to 10^6.

- **Factorial**: fac[i] stores i! modulo 10^9+7.

- **Inverses**: We use Fermat’s Little Theorem to compute the modular inverses of the factorials: a^{−1} ≡ a^{p−2} mod p (p is prime).

- This allows us to compute k! and (n−k)! inverses efficiently.

- **Binomial Coefficient Calculation**:

- The formula for the binomial coefficient is given by: \binom{n}{k} = \frac{n!}{k!(n-k)!}

- Using the precomputed factorials and inverses, we can compute this in constant time: \binom{n}{k} mod p = fac[n] x inv[k] mod p x inv[n-k] mod p

- **See this for reference**:- [Fermat Binomials in Number theory](https://www.codechef.com/learn/course/number-theory/LINTDSA07/problems/MODAR05)

### [](#complexity-3)Complexity:

- **Time Complexity:** Computing exponentiation will give `O(log n)`, computing factorial will give `O(N)`, computing modular inverse factorial will give `O(N+log N)`. Maximum Time complexity will be `O(N)`.

- **Space Complexity:** `O(N)`. To store the factorials `O(N)` and inverse `O(N)`.

</details>
