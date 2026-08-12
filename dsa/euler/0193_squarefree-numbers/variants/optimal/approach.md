# Squarefree Numbers - Optimal Approach

## Algorithm Explanation

Count the number of positive squarefree integers $n < 2^{50} = 1,125,899,906,842,624$.

### Inclusion-Exclusion Principle & Möbius Function:
1. **Inclusion-Exclusion Formula**:
   A number $n$ is squarefree if no prime square $p^2$ divides $n$. By inclusion-exclusion using the Möbius function $\mu(d)$:
   $$\text{Squarefree}(N) = \sum_{d=1}^{\lfloor\sqrt{N}\rfloor} \mu(d) \left\lfloor \frac{N}{d^2} \right\rfloor$$
   where $N = 2^{50} - 1$ and $\lfloor\sqrt{N}\rfloor = 33,554,431$.
2. **Linear Sieve for Möbius Function**:
   Compute $\mu(d)$ for all $d \le 2^{25} = 33,554,432$ using a bytearray linear sieve.
3. **Summation**:
   Accumulating $\mu(d) \lfloor N/d^2 \rfloor$ yields $679,284,789,597,219$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\sqrt{N})$ where $\sqrt{N} = 2^{25} \approx 3.35 \times 10^7$. Runs in $\approx 26\text{s}$.
- **Space Complexity:** $\mathcal{O}(\sqrt{N})$ - Bytearray arrays for prime sieve and Möbius values.
