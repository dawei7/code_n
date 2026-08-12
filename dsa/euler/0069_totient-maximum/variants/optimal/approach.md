# Totient Maximum - Optimal Approach

## Algorithm Explanation

Find the value of $n \le 1000000$ that maximizes $\frac{n}{\phi(n)}$.

### Mathematical Derivation
Euler's totient product formula:
$$\phi(n) = n \prod_{p \mid n} \left(1 - \frac{1}{p}\right)$$

Rearranging:
$$\frac{n}{\phi(n)} = \prod_{p \mid n} \frac{p}{p - 1}$$

To maximize this product, $n$ must be the product of as many consecutive smallest prime numbers (the **primorial**) as possible without exceeding $1000000$:
$$n = 2 \times 3 \times 5 \times 7 \times 11 \times 13 \times 17 = 510510$$

Multiplying by the next prime $19$ exceeds $1000000$ ($510510 \times 19 = 9699690$).

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(1)$ - Closed-form primorial product calculation.
- **Space Complexity:** $\mathcal{O}(1)$ - Constant space.
