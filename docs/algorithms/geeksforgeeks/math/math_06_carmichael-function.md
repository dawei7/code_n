# Carmichael Function

| | |
|---|---|
| **ID** | `math_06` |
| **Category** | math |
| **Complexity (required)** | $O(\sqrt{N})$ Time, $O(1)$ Space |
| **Difficulty** | 9/10 |
| **Interview relevance** | 1/10 |
| **Wikipedia** | [Carmichael function](https://en.wikipedia.org/wiki/Carmichael_function) |

## Problem statement

Given a positive integer `N`. Calculate the Carmichael function \lambda(N).
The Carmichael function \lambda(N) returns the smallest positive integer M such that A^M \equiv 1 \pmod N for every integer A that is coprime to N.
(It is closely related to Euler's Totient function \phi(N), but yields the *absolute minimum* exponent rather than a universally guaranteed larger exponent).

**Input:** An integer `N`.
**Output:** An integer representing \lambda(N).

## When to use it

- In extremely advanced Number Theory and Cryptography optimization.
- When you need the absolute tightest bound on the periodicity of modular exponentiation. (In RSA cryptography, using \lambda(N) instead of \phi(N) generates much smaller, more efficient private keys!)

## Approach

**1. The Relationship with Euler's Totient (\phi):**
Euler's Totient function \phi(N) counts the number of integers coprime to N.
Euler's Theorem guarantees that A^{\phi(N)} \equiv 1 \pmod N.
However, \phi(N) is sometimes an overkill exponent.
For example, N = 8. \phi(8) = 4. So A^4 \equiv 1 \pmod 8.
But the Carmichael function reveals that \lambda(8) = 2! A smaller exponent works perfectly: 3^2 \equiv 1 \pmod 8, 5^2 \equiv 1 \pmod 8, 7^2 \equiv 1 \pmod 8.

**2. The Rules for Computing \lambda(N):**
Like the Totient function, \lambda(N) is calculated by looking at the Prime Factorization of N.
Let N = p_1^{k_1} \cdot p_2^{k_2} \cdots p_m^{k_m}.
The Carmichael function for the composite number is the **Least Common Multiple (LCM)** of the Carmichael functions of its prime components!
\lambda(N) = \text{LCM}(\lambda(p_1^{k_1}), \lambda(p_2^{k_2}), \dots, \lambda(p_m^{k_m}))

**3. Evaluating Prime Powers:**
For any prime power p^k, the Carmichael function is usually identical to the Totient function:
\lambda(p^k) = \phi(p^k) = p^{k-1} \cdot (p - 1).

There is exactly ONE exception in all of mathematics: when p = 2 and k \ge 3.
\lambda(2^k) = \frac{1}{2} \cdot \phi(2^k) = 2^{k-2}.
(This is exactly why N=8=2^3 resulted in \lambda(8) = 2, not 4).

**4. The Algorithm:**
1. Maintain a running `lcm_result = 1`.
2. Extract the factors of 2 from N. If there are any, compute \lambda(2^k) using the special exception rules, and update `lcm_result`.
3. Loop through all odd numbers P from 3 up to \sqrt{N}. If P divides N, extract all powers of P to find P^k. Compute \lambda(P^k) = P^{k-1} \cdot (P - 1).
4. Update `lcm_result = LCM(lcm_result, \lambda(P^k))`.
5. If N > 1 after the loop, it means the remaining N is a prime number itself! \lambda(N) = N - 1. Update the LCM.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for math_06: Carmichael Function.

Factor n. lambda per prime power: p^(k-1) * (p-1) for odd
primes, 2^(k-2) for n=2^k (k>=3). Combine via lcm.
"""


def solve(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n == 4:
        return 2
    temp = n
    factors = {}
    p = 2
    while p * p <= temp:
        while temp % p == 0:
            factors[p] = factors.get(p, 0) + 1
            temp //= p
        p += 1
    if temp > 1:
        factors[temp] = factors.get(temp, 0) + 1
    from math import gcd
    lam = 1
    for p, k in factors.items():
        if p == 2:
            if k == 1:
                pk_lam = 1
            elif k == 2:
                pk_lam = 2
            else:
                pk_lam = 2 ** (k - 2)
        else:
            pk_lam = (p ** (k - 1)) * (p - 1)
        lam = lam * pk_lam // gcd(lam, pk_lam)
    return lam
```

</details>

## Walk-through

Calculate \lambda(15). (N=15). `result = 1`.

1. `15 % 2 != 0`. Skip factor 2.
2. `p = 3`: 3 x 3 \le 15.
   - `15 % 3 == 0`.
   - `k = 1`, `n = 15 // 3 = 5`.
   - `lambda_val = (3^0) * (3-1) = 2`.
   - `result = lcm(1, 2) = 2`.
3. `p = 5`: 5 x 5 \not\le 5. Loop terminates!
4. Check remaining N: `5 > 1`. `5` is prime!
   - `lambda_val = 5 - 1 = 4`.
   - `result = lcm(2, 4) = 4`.

Result: \lambda(15) = 4. ✓
*(Verify: \phi(15) = \phi(3) \cdot \phi(5) = 2 \cdot 4 = 8. So A^8 \equiv 1 \pmod{15}. But Carmichael says an exponent of 4 is enough! 2^4 = 16 \equiv 1 \pmod{15}. Correct!)*

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(\log N)$ | $O(1)$ |
| **Average** | $O(\sqrt{N})$ | $O(1)$ |
| **Worst** | $O(\sqrt{N})$ | $O(1)$ |

The time complexity is identical to standard Prime Factorization. The `while` loop checks all odd numbers up to \sqrt{N}. If N is prime, it takes exactly \sqrt{N} checks. If N is highly composite (e.g. 2^{30}), it instantly reduces N down to 1 in $O(\log N)$ time.
Thus, worst-case time is $O(\sqrt{N})$.
Space complexity is $O(1)$ constant.

## Variants & optimizations

- **Pollard's rho algorithm:** If N is astronomically large (e.g., a 100-digit number), checking up to \sqrt{N} (10^{50} iterations) takes trillions of years. Advanced probabilistic factorization algorithms like Pollard's rho or the General Number Field Sieve are required to factorize N before calculating the Carmichael function.

## Real-world applications

- **RSA Key Generation (PKCS#1):** Modern implementations of RSA cryptography (like OpenSSL) explicitly use \lambda(N) instead of \phi(N) to calculate the private decryption key d. Because \lambda(N) is often much smaller than \phi(N), it results in a strictly smaller private key, making decryption significantly faster on low-power devices without sacrificing any mathematical security!

## Related algorithms in cOde(n)

- **[math_10 - Euler Totient Function](math_10_euler-totient-function.md)** — The simpler, more universally taught predecessor to this function.
- **[math_01 - GCD](math_01_gcd-euclidean.md)** — Required to calculate the LCM when merging the results of the prime components.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
