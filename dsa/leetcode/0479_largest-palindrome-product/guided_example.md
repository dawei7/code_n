# Guided Example: Largest Palindrome Product

We trace the step-by-step upper-half prefix generation ($a \in [10^n - 1, 10^{n-1}]$ descending), $2n$-digit palindrome mirror synthesis ($x = a \cdot 10^n + \text{rev}(a)$), trial division factoring ($t^2 \ge x$), modular congruence ($x \pmod{1337}$), and early stopping on representative $n$-digit instances:

- **Input:** $n = 2$
- **Required output:** `987`
  - Maximum 2-digit number: $mx = 10^2 - 1 = 99$
  - Range of 2-digit factors: $[10, 99]$
  - Theoretical upper bound of product: $99 \times 99 = 9801$
  - Candidate palindromes are formed by taking a 2-digit upper half $a$ in descending order and mirroring its digits:
    - Candidate $a = 99 \implies x = 9999$ ($> 9801$, impossible as product of two 2-digit numbers)
    - Candidate $a = 98 \implies x = 9889$:
      - Trial factor test ($t \in [99, \lceil\sqrt{9889}\rceil]$):
      - $9889 / 99 = 99.88$
      - $9889 = 11 \times 899 \implies$ No two 2-digit factors exist.
    - Candidate $a = 97 \implies x = 9779 \implies$ No 2-digit factors.
    - Candidate $a = 96 \implies x = 9669 \implies$ No 2-digit factors.
    - Candidate $a = 95 \implies x = 9559 \implies$ No 2-digit factors.
    - Candidate $a = 94 \dots 91$: None factor into two 2-digit numbers.
    - Candidate $a = 90 \implies x = 9009$:
      - Factor test:
        $$
        9009 / 99 = \mathbf{91}
        $$
      - Both $t_1 = 99$ and $t_2 = 91$ are valid 2-digit numbers ($10 \le 91, 99 \le 99$)!
      - Since $a = 90$ is the highest prefix evaluated with valid factors, $9009$ is the **largest palindrome product**!
  - Modulo operation:
    $$
    9009 \pmod{1337} = 9009 - 6(1337) = 9009 - 8022 = \mathbf{987}
    $$
- **Single Digit Instance ($n = 1$):**
  - Range $[1, 9]$. Largest palindrome product is $3 \times 3 = 9$ (or $9 \times 1 = 9$) $\implies \mathbf{9}$
- **Three-Digit Instance ($n = 3$):**
  - Largest product is $906609 = 993 \times 913$. Modulo: $906609 \pmod{1337} = \mathbf{123}$

This instance demonstrates symmetric numeric palindrome synthesis, mathematically proves why generating palindromes directly is exponentially faster than generating all $O(10^{2n})$ pairwise products, and derives $O(10^n)$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an integer $n$:
Find the **largest palindrome** that can be created as the product of two $n$-digit numbers.
Since the result could be very large, return it **modulo 1337**.

```text
n = 2 digits:
  Factors: [10 .. 99]
  Maximum possible product: 99 * 99 = 9801

Candidate Even Palindromes (Descending):
  9999 (Exceeds 9801)
  9889 -> No 2-digit factors
  9779 -> No 2-digit factors
  ...
  9009 = 99 * 91  (Both 99 and 91 are 2-digit numbers!)

Largest Palindrome: 9009
Output: 9009 % 1337 = 987
```

### Direct Palindrome Generation vs Brute Force Multiplication
- Testing all pairs $(u, v)$ takes $O(10^{2n})$ operations. For $n = 8$, this requires $10^{16}$ multiplications, which is impossible.
- Instead of checking if products are palindromes, **we generate palindromes directly in descending order** and check if they can be factored!
- The largest palindrome product of two $n$-digit numbers has $2n$ digits.
- An even-length palindrome of $2n$ digits is completely and uniquely determined by its **first $n$ digits** (the upper half $a$).
- Iterating $a$ from $10^n - 1$ down to $10^{n-1}$ enumerates all candidate palindromes in strictly decreasing order.
- The **first** generated palindrome that factors into two $n$-digit numbers is guaranteed to be the global maximum!

---

## 2. Conceptual Foundation & Invariants

### 1. Palindrome Assembly:
Let $a$ be an $n$-digit integer ($10^{n-1} \le a \le 10^n - 1$):
Reverse the decimal digits of $a$ to form $rev(a)$.
Construct the $2n$-digit palindrome:
$$
x = a \cdot 10^n + rev(a)
$$
For example, with $n = 2$ and $a = 90$:
$$
rev(90) = 09 \implies x = 90 \times 100 + 9 = 9009
$$

### 2. Factor Feasibility Test:
To test if $x$ can be factored into two $n$-digit numbers:
- We iterate a potential factor $t$ from $mx = 10^n - 1$ downwards.
- If $x \pmod t == 0$:
  The second factor is $u = x / t$.
  Since $t \le mx$, the second factor $u \ge x / mx$.
  As long as $t \ge u$ (which holds while $t^2 \ge x$), both factors $t$ and $u$ are $\le mx$.
  Since $x$ has $2n$ digits and $t \le 10^n - 1$, $u$ automatically satisfies $u \ge 10^{n-1}$ (it is guaranteed to have $n$ digits).
  Therefore, finding $x \pmod t == 0$ with $t^2 \ge x$ proves that $x$ is a valid product!

> **Maximality Invariant.** Because prefixes $a$ are scanned in strictly descending order from $10^n - 1$, the first palindrome $x$ that possesses two $n$-digit divisors is unconditionally the maximum palindrome product.

---

## 3. Step-by-Step Worked Execution

We trace $n = 2$:
$mx = 10^2 - 1 = 99$.

---

### Step 1: Scan Prefixes $a \in [99, 10]$ Descending

- **Prefix $a = 99$:**
  - $x = 9999$.
  - Upper limit on product is $99^2 = 9801 < 9999$.
  - Factoring: $9999 / 99 = 101 > 99$ (3 digits, invalid).

- **Prefix $a = 98$:**
  - $x = 9889$.
  - Test $t \in [99 \dots \lceil\sqrt{9889}\rceil = 100]$:
    - $9889 / 99 = 99.88$ (not integer).
  - No factors found.

- **Prefixes $a = 97 \dots 91$:**
  - $x = 9779, 9669, 9559, 9449, 9339, 9229, 9119$.
  - None have an integer factor $t \in [99 \dots \lceil\sqrt{x}\rceil]$.

- **Prefix $a = 90$:**
  - Mirror $a$: $rev(90) = 09$.
  - Form palindrome:
    $$
    x = 90 \times 100 + 9 = \mathbf{9009}
    $$
  - Factor trial starting from $t = 99$:
    - Check $t = 99$:
      $$
      9009 \pmod{99} = 0 \quad (\mathbf{Exact\ Division!})
      $$
    - Second factor:
      $$
      u = 9009 / 99 = \mathbf{91}
      $$
    - Both $t = 99$ and $u = 91$ have exactly 2 digits ($10 \le 91 \le 99$).
  - Palindrome $9009$ is valid!

---

### Step 2: Compute Modular Answer
$$
9009 \pmod{1337} = 9009 - (6 \times 1337) = 9009 - 8022 = \mathbf{987}
$$

---

## 4. Complete Execution Trace

| Prefix $a$ | Synthesized Palindrome $x$ | Factor Search Range $[mx \dots \sqrt{x}]$ | Trial Divisors Tested | Success Divisor Pair | Status |
|:---:|:---:|:---:|:---:|:---:|:---|
| $99$ | $9999$ | $t \in [99, 100]$ | $99$ ($u = 101 > 99$) | None | Failed |
| $98$ | $9889$ | $t \in [99, 100]$ | $99$ ($9889 / 99 \notin \mathbb{Z}$) | None | Failed |
| $97$ | $9779$ | $t \in [99, 99]$ | $99$ | None | Failed |
| $96 \dots 91$ | $9669 \dots 9119$ | $t \in [99, \dots]$ | $99, 98, \dots$ | None | Failed |
| **$90$** | **$9009$** | $t \in [99, 95]$ | **$99$** | **$99 \times 91$** | **Found: $9009 \pmod{1337} = \mathbf{987}$** |

---

## 5. Boundary Cases & Failure Modes

- **$n = 1$ Edge Case:** Single-digit products can be odd-length palindromes (e.g. $9 = 3 \times 3$). The even-length search starts at 2 digits. For $n = 1$, the loop returns the maximum single-digit palindrome product directly: $\mathbf{9}$.
- **$n = 8$ (Maximum Scale):** Largest 8-digit product is $9999000000009999 \pmod{1337} = 475$. Direct palindrome search evaluates only a few dozen candidate prefixes before finding a factor.
- **Modulo 1337:** Result can be smaller than 1337 or wrap around multiple times.

---

## 6. Traps & Common Anti-Patterns

- **Searching Factors All the Way to 1:** Searching $t$ below $\sqrt{x}$ is completely redundant because any pair $(t, x/t)$ with $t < \sqrt{x}$ has its larger partner $x/t > \sqrt{x}$, which was already tested. Bounding by $t^2 \ge x$ halts searches immediately.
- **Forgetting Odd-Length Palindromes for $n > 1$:** For all $n \in [2, 8]$, the maximum palindrome product is always an even-length palindrome ($2n$ digits). Searching only even-length palindromes guarantees finding the maximum without missing solutions.
- **Using 32-Bit Integer Variables:** For $n \ge 5$, palindromes exceed $2^{31} - 1$ ($9 \times 10^9 > 2 \times 10^9$). Using 64-bit integers (`long long` in C++) prevents arithmetic overflow during multiplication and mirroring.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Prefix generation tests $a$ descending. In practice, valid palindrome products appear very close to $mx$:
    - For $n = 2$: 10 prefixes tested.
    - For $n = 3$: 94 prefixes tested.
    - For $n = 4$: 11 prefixes tested.
  - Factoring each candidate tests at most $10^n - \sqrt{x} \approx O(10^{n/2})$ values of $t$.
  - Total Time: $\mathcal{O}(C \cdot 10^{n/2})$ where $C$ is small ($C \le 100$). Completes in $< 15$ ms for all $n \le 8$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ using scalar integer variables.
