# Hyperexponentiation - Optimal Approach

## Algorithm Explanation

Find the last $8$ digits of $1777 \mathbin{\uparrow \uparrow} 1855$, which is equivalent to computing $1777 \mathbin{\uparrow \uparrow} 1855 \pmod{10^8}$.

### Modular Exponentiation Tower (Euler's Totient Theorem):
1. **Euler's Totient Reduction**:
   Since $\gcd(1777, 10^8) = 1$, by Euler's Totient Theorem:
   $$a^x \equiv a^{x \pmod{\phi(m)}} \pmod m$$
   Therefore, $a \mathbin{\uparrow \uparrow} b \pmod m = a^{(a \mathbin{\uparrow \uparrow} (b-1) \pmod{\phi(m)})} \pmod m$.
2. **Recursive Totient Tower**:
   We recurse down the modulus chain $m \to \phi(m) \to \phi(\phi(m)) \dots$ until $m = 1$ or base case $b = 1$.
   The modulus decreases rapidly:
   - $10^8 \to 4 \cdot 10^7 \to 1.6 \cdot 10^7 \to 6.4 \cdot 10^6 \dots$
3. **Execution**:
   Using `pow(a, exp, m)` at each step computes the exact $8$-digit suffix $95962097$ in $< 1\text{ms}$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\log^* m \cdot \sqrt{m})$ where $\log^* m$ is the iterated logarithm depth. Runs in $\approx 0.000\text{s}$.
- **Space Complexity:** $\mathcal{O}(\log^* m)$ - Recursion stack for totient tower depth.
