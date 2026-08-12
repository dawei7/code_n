# Pandigital Prime - Optimal Approach

## Algorithm Explanation

Find the largest $n$-digit pandigital prime.

### Divisibility by 3 Proof:
1. **$9$-digit pandigitals**: Digit sum $= \sum_{i=1}^9 i = 45 \equiv 0 \pmod 3$. All $9$-digit pandigitals are divisible by $3$ (composite).
2. **$8$-digit pandigitals**: Digit sum $= \sum_{i=1}^8 i = 36 \equiv 0 \pmod 3$. All $8$-digit pandigitals are divisible by $3$ (composite).
3. **$7$-digit pandigitals**: Digit sum $= \sum_{i=1}^7 i = 28 \equiv 1 \pmod 3$. Can be prime!

### Search Strategy:
- Generate all permutations of digits `"7654321"` in reverse lexicographic order ($7! = 5040$ arrangements).
- Return the first permutation that passes deterministic primality testing.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(7! \cdot \sqrt{P})$ where $7! = 5040$. Runs in $< 0.005\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Constant auxiliary memory.
