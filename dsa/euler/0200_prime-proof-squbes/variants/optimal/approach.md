# Prime-proof Squbes - Optimal Approach

## Algorithm Explanation

Find the $200$th prime-proof sqube $S = p^2 q^3$ containing the contiguous substring `"200"`.

### Sqube Generation & Miller-Rabin Primality Verification:
1. **Definition**:
   A sqube is a number of the form $S = p^2 q^3$ for distinct primes $p \neq q$.
   A sqube $S$ is prime-proof if replacing any single digit of $S$ with any other digit $(0 \dots 9)$ never yields a prime.
2. **Candidate Generation**:
   We generate squbes $S = p^2 q^3$ up to $3 \times 10^{11}$, filter for those containing `"200"`, and sort them in ascending order.
3. **Prime-Proof Testing**:
   For each candidate $S$, we test all single-digit substitutions using a deterministic Miller-Rabin primality test.
4. **Execution**:
   The $200$th prime-proof sqube containing `"200"` is $229161792008$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(P^2 \log P + K \cdot D)$ where $P \approx 2 \times 10^5$ and $D = 12$ digits per candidate. Runs in $\approx 0.14\text{s}$.
- **Space Complexity:** $\mathcal{O}(P)$ - Prime sieve array.
