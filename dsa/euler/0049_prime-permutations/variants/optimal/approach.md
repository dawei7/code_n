# Prime Permutations - Optimal Approach

## Algorithm Explanation

Find the $12$-digit number formed by concatenating an arithmetic sequence of three $4$-digit primes $(a, b, c)$ that are digit permutations of each other (other than $1487, 4817, 8147$).

1. Generate all $4$-digit primes $p \in [1000, 9999]$ using Sieve of Eratosthenes.
2. Group primes by their sorted digit canonical key `"".join(sorted(str(p)))`.
3. For groups containing $\ge 3$ primes:
   - Test prime pairs $(p_1, p_2)$ and check if $p_3 = 2p_2 - p_1$ is also in the group.
   - Skip the known example $p_1 = 1487$.
4. Return concatenated string `f"{p1}{p2}{p3}"` as an integer.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(P^2)$ where $P = 1061$ ($4$-digit prime count). Runs in $< 0.01\text{s}$.
- **Space Complexity:** $\mathcal{O}(P)$ - Hash map bucket storage.
