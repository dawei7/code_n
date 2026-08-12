# Prime Power Triples - Optimal Approach

## Algorithm Explanation

Count how many numbers below $50,000,000$ can be expressed as the sum of a prime square, prime cube, and prime fourth power:
$$N = p_1^2 + p_2^3 + p_3^4$$

### Prime Bounds:
- $p_1 < \sqrt{50,000,000} \approx 7071$
- $p_2 < (50,000,000)^{1/3} \approx 368$
- $p_3 < (50,000,000)^{1/4} \approx 84$

### Strategy:
1. Generate all prime numbers up to $7071$ using Sieve of Eratosthenes.
2. Perform a 3-level nested loop over primes $(p_3, p_2, p_1)$.
3. Prune inner loops early as soon as $p_3^4 + p_2^3 + p_1^2 \ge 50,000,000$.
4. Insert valid sum values into a hash set to eliminate duplicate representations.
5. Return the size of the set.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(P_1 \cdot P_2 \cdot P_3)$ where $P_1 = 908, P_2 = 73, P_3 = 23$. Runs in $< 0.45\text{s}$.
- **Space Complexity:** $\mathcal{O}(U)$ where $U \approx 1.1 \times 10^6$ unique expressible numbers in hash set.
