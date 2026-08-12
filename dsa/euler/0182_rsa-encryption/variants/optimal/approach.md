# RSA Encryption - Optimal Approach

## Algorithm Explanation

Find the sum of all valid RSA exponents $e$ ($1 < e < \phi$, $\gcd(e, \phi) = 1$) such that the number of unconcealed messages $m^e \equiv m \pmod n$ is at a minimum for $p = 1009$ and $q = 3643$.

### Chinese Remainder Theorem & Unconcealed Count:
By CRT, $m^e \equiv m \pmod{pq}$ if and only if $m^e \equiv m \pmod p$ and $m^e \equiv m \pmod q$.

1. **Modular Solvers**:
   For prime $p$, $m = 0$ is a solution. For $m \not\equiv 0 \pmod p$, $m^{e-1} \equiv 1 \pmod p$ has $\gcd(e - 1, p - 1)$ solutions.
   Total unconcealed solutions $\pmod p$: $1 + \gcd(e - 1, p - 1)$.
2. **Total Unconcealed Count**:
   $$U(e) = (1 + \gcd(e - 1, p - 1)) \times (1 + \gcd(e - 1, q - 1))$$
3. **Minimum Condition**:
   Since $e$ is odd and coprime to $\phi(n)$, $e - 1$ is even, making $\gcd(e - 1, p - 1) \ge 2$ and $\gcd(e - 1, q - 1) \ge 2$.
   The theoretical minimum is $U(e) = (1 + 2) \times (1 + 2) = 9$.

Iterate odd $e \in (1, \phi)$, filtering $\gcd(e, \phi) = 1$ and accumulating $e$ where $U(e) = 9$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\phi(n))$ arithmetic operations where $\phi = (p-1)(q-1) = 3,671,136$. Runs in $\approx 0.61\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Constant space.
