# Factorial Trailing Digits - Optimal Approach

## Algorithm Explanation

Find the last five digits before the trailing zeroes in $N!$ for $N = 10^{12}$.

### Trailing Zero Removal & Modular Chinese Remainder Theorem:
Removing trailing zeroes is equivalent to dividing $N!$ by $10^{v_5(N!)} = 2^{v_5(N!)} \cdot 5^{v_5(N!)}$.
To compute $X = \frac{N!}{10^{v_5(N!)}} \bmod 10^5$, we split $10^5 = 2^5 \times 5^5 = 32 \times 3125$ using the Chinese Remainder Theorem:

1. **Modulo $2^5 = 32$**:
   Since $v_2(N!) - v_5(N!) \ge 5$ for $N \ge 14$, $X \equiv 0 \pmod{32}$.
2. **Modulo $5^5 = 3125$**:
   - $N! / 5^{v_5(N!)} \bmod 3125$ is computed recursively by multiplying full blocks of coprime integers $\le 3125$ mod $3125$.
   - Divide by $2^{v_5(N!)} \pmod{3125}$ via modular inverse $\text{inv}(2) = 1563 \pmod{3125}$:
     $$m_5 = \left( \frac{N!}{5^{v_5(N!)}} \bmod 3125 \right) \times (\text{inv}(2))^{v_5(N!)} \bmod 3125$$
3. **Reconstruction**:
   $$X = m_5 + 3125 \times \left( (0 - m_5) \cdot 3125^{-1} \bmod 32 \right) \pmod{10^5}$$

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\log_5 N \cdot \log 3125)$ where $N = 10^{12}$ ($\approx 18$ recursive steps). Runs in $< 0.001\text{s}$.
- **Space Complexity:** $\mathcal{O}(5^5) = \mathcal{O}(3125)$ - Block product lookup array.
