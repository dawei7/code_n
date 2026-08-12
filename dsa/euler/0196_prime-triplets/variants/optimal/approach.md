# Prime Triplets - Optimal Approach

## Algorithm Explanation

Find $S(5678027) + S(7208785)$, where $S(n)$ is the sum of primes in row $n$ of the number triangle that belong to some prime triplet.

### 5-Row Window & Segmented Prime Sieve:
1. **Window Localized Primality**:
   To determine if a prime in row $n$ belongs to a prime triplet, we only need to inspect 8-neighbor connections across 5 consecutive rows: $n-2, n-1, n, n+1, n+2$.
2. **Segmented Sieve of Eratosthenes**:
   For row $n$, the 5-row segment contains $\approx 5n$ integers starting at $\frac{(n-3)(n-2)}{2} + 1$.
   Sieve this segment using base primes up to $\sqrt{\text{max\_val}} \approx 6 \times 10^6$.
3. **Triplet Membership Evaluation**:
   A prime at cell $(n, c)$ is part of a prime triplet if:
   - It has $\ge 2$ prime neighbors, OR
   - It is adjacent to a prime neighbor that itself has $\ge 2$ prime neighbors.
4. **Execution**:
   - $S(5678027) = 79,697,256,800,321,526$
   - $S(7208785) = 242,605,983,970,758,409$
   - Sum $= 322,303,240,771,079,935$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(n_1 + n_2)$ where $n_1 = 5678027, n_2 = 7208785$. Runs in $\approx 16\text{s}$.
- **Space Complexity:** $\mathcal{O}(n_1 + n_2)$ - Bytearray arrays for segment primality.
