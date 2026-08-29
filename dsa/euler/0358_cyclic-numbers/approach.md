# Cyclic Numbers - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

A **cyclic number** of $L$ digits is an integer $N$ such that multiplying $N$ by any integer $1, 2, \dots, L$ produces a cyclic permutation (rotation) of the digits of $N$ (preserving leading zeros).
Every base-10 cyclic number of length $L = p - 1$ corresponds to the repetend period of the fraction:
$$\frac{1}{p}$$
where $p$ is a **full reptend prime** in base 10 (i.e. $10$ is a primitive root modulo $p$, meaning the multiplicative order $\operatorname{ord}_p(10) = p - 1$).
The integer value of the cyclic number is given by:
$$N = \frac{10^{p-1} - 1}{p}$$

We are given that there is a unique cyclic number whose:
- Eleven leftmost digits are $00000000137\dots$
- Five rightmost digits are $\dots 56789$

We seek to find the sum of all digits of this cyclic number.

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Direct Digit Generation & Summation
1. Search primes $p$ whose decimal expansions begin with $0.00000000137\dots$
2. Generate all $p - 1$ digits by performing long division of $1/p$.
3. Sum the hundreds of millions of digits one by one.

### Fundamental Bottlenecks:
- **Memory & Storage**: The prime $p \approx 7.3 \times 10^8$ has a repetend length of $p - 1 \approx 730\text{ million digits}$. Storing or iterating over 730 million digits requires gigabytes of RAM and takes substantial runtime.

---

## 3. Core Intuition & Mathematical Structure

### Midy's Theorem for Full Reptend Primes
Let $p$ be a prime with full period $p - 1$, which is an even integer $2k$.
By **Midy's Theorem**, if we split the $2k$-digit period of $1/p$ into two halves $A$ and $B$ each of length $k = \frac{p-1}{2}$:
$$A + B = 10^k - 1 = \underbrace{999\dots9}_{k \text{ nines}}$$
This implies that for every index $i \in \{1, \dots, k\}$, the $i$-th digit $d_i$ and the $(i + k)$-th digit $d_{i+k}$ satisfy:
$$d_i + d_{i+k} = 9$$
Therefore, the sum of all $p - 1$ digits is exactly:
$$\text{Sum of Digits} = 9 \times \frac{p - 1}{2} = \frac{9(p - 1)}{2}$$

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Modular Suffix and Prefix Range Inversion
To identify the unique prime $p$:

1. **Prefix Inversion (Range Bound)**:
   Since $\frac{1}{p} = 0.00000000137\dots$:
   $$0.00000000137 \le \frac{1}{p} < 0.00000000138$$
   $$\left\lfloor \frac{10^{11}}{138} \right\rfloor < p \le \left\lfloor \frac{10^{11}}{137} \right\rfloor \implies 724\,637\,681 \le p \le 729\,927\,007$$
   The search range has a width of only $\approx 5.3 \times 10^6$.

2. **Suffix Inversion (Modular Step Size)**:
   The cyclic number $N$ satisfies $N \cdot p = 10^{p-1} - 1 \equiv -1 \pmod{10^5}$.
   Given that the last 5 digits of $N$ are $56789$:
   $$56789 \cdot p \equiv 99999 \pmod{100\,000}$$
   Multiplying by the modular inverse $(56789)^{-1} \pmod{100\,000}$:
   $$p \equiv 99999 \times (56789)^{-1} \equiv 9891 \pmod{100\,000}$$

3. **Hyper-Fast Stepping**:
   Stepping by $100\,000$ across $[724\,637\,681, 729\,927\,007]$ leaves only **53 candidate integers**!
   Testing primality and checking that $10$ is a primitive root modulo $p$ takes $< 0.001$ seconds and uniquely identifies:
   $$p = 729\,809\,891$$

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example: The Smallest Cyclic Number $N = 142857$ ($p = 7$)
1. $p = 7$ is a full reptend prime with period $p - 1 = 6$.
2. Cyclic number: $N = 142857$.
3. Split into two halves of length 3: $A = 142, B = 857$.
   $A + B = 142 + 857 = 999$.
   Sum of digits: $9 \times \frac{7 - 1}{2} = 9 \times 3 = 27$.
   Direct digit sum: $1 + 4 + 2 + 8 + 5 + 7 = 27$ ($\checkmark$).

### Evaluation for Target $p = 729\,809\,891$
$$\text{Sum of Digits} = \frac{9(729\,809\,891 - 1)}{2} = \frac{9 \times 729\,809\,890}{2} = 9 \times 364\,904\,945 = 3\,284\,144\,505$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

```
[Compute modular inverse: p ≡ 99999 * inv(56789) ≡ 9891 mod 100000]
                             │
                             ▼
[Iterate p in [724637681, 729927007] with step 100000]
   ├─► Check 10^11 // p == 137
   ├─► Check is_prime(p)
   ├─► Check 10 is primitive root mod p (10^((p-1)/q) ≢ 1 mod p)
   └─► Found p = 729809891
                             │
                             ▼
[Apply Midy's Theorem: Digit Sum = 9 * (p - 1) // 2 = 3284144505]
```

---

## 7. Mathematical Complexity & Edge Case Invariants

### Complexity Analysis
- **Modular Step**: Stepping by $10^5$ checks only $53$ integers.
- **Primality & Primitive Root Verification**: Factoring $p-1$ takes $\approx O(\sqrt{p})$, requiring $< 0.001$ seconds.
- **Total Time Complexity**: $O(\sqrt{p}) \approx 0.002\text{ seconds}$ in pure Python.
- **Space Complexity**: $O(1)$ constant auxiliary memory.

### Invariants Handled
- **Leading Zeros**: Handled naturally through the fraction $1/p$ and integer division $10^{11} // p$.
- **Primitive Root Guarantee**: Directly validates that the period has maximal length $p - 1$.
