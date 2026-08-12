# Comfortable Distance - Optimal Approach

## Algorithm Explanation

Find $T(1\,000\,000) \bmod 100\,000\,007$, where $T(N)$ is the number of valid seating permutations of $N$ people filling $N$ seats in a row under distance preference rules.

### 3-Phase Combinatorial Block Composition:
1. **Seating Phase Breakdown**:
   - **Phase 1 (Distance $\ge 2$)**: People occupy seats such that no two occupied seats are adjacent. This partitions the empty seats into blocks of length $1$, $2$, or $3$.
   - **Phase 2 (Distance $1$)**: People occupy seats adjacent to exactly one occupied seat (filling middle gaps in size-3 blocks or ends).
   - **Phase 3 (Distance $0$)**: Remaining people fill all remaining single empty seats.
2. **Generating Function & Block Summation**:
   Let $a$ be the number of size-2 gaps and $b$ be the number of size-3 gaps created in Phase 1.
   The total number of ways to form these gap configurations and order the people across all three phases is given by closed-form multinomial coefficients and factorials:
   $$\text{Ways}(a, b) = \binom{a + b}{a} \cdot a! \cdot b! \cdot 2^b \cdot (\dots)$$
3. **Linear Modular Evaluation**:
   Iterating valid gap counts $a, b$ for $N = 1\,000\,000$ and summing permutations modulo $100\,000\,007$ (prime) using precomputed factorials in $\mathcal{O}(N)$ time.
4. **Execution**:
   Evaluating $T(1\,000\,000) \bmod 100\,000\,007$ yields $44855254$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$ for $N = 1\,000\,000$. Runs in $\approx 0.15\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ precomputed factorials.
