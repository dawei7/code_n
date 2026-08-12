# Semiprimes - Optimal Approach

## Algorithm Explanation

Count the number of semiprimes $n < 10^8$ (composite integers with exactly two prime factors $n = p_1 \cdot p_2$ with $p_1 \le p_2$).

### Prime Sieve & Binary Search:
1. **Sieve of Eratosthenes**:
   Generate all primes up to $N/2 = 50,000,000$ using a bytearray sieve.
2. **Two-Pointer / Binary Search Counting**:
   For each prime $p_1 \le \sqrt{N} = 10000$:
   We require $p_2 \ge p_1$ such that $p_1 \cdot p_2 < 10^8 \implies p_2 \le \lfloor (10^8 - 1)/p_1 \rfloor$.
   Using `bisect_right(primes, max_p2)` finds the index `idx` of the largest valid $p_2$.
   The number of valid pairs for $p_1$ is `idx - i`.
3. **Total Count**:
   Summing over all $p_1 \le 10000$ yields $17,427,258$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(M \log \log M + \pi(\sqrt{N}) \log \pi(M))$ where $M = N/2 = 5 \times 10^7$. Runs in $\approx 3.1\text{s}$.
- **Space Complexity:** $\mathcal{O}(M)$ - Bytearray for prime sieve and prime array.
