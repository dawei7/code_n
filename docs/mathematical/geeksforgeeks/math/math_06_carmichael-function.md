# Formal Mathematical Specification: Carmichael Function

## 1. Definitions and Notation

Let $N \in \mathbb{Z}^+$ be a positive integer. The Carmichael function, denoted by $\lambda(N)$, is defined as the exponent of the multiplicative group of integers modulo $N$, denoted $(\mathbb{Z}/N\mathbb{Z})^\times$. Formally, $\lambda(N)$ is the smallest positive integer $M$ such that:
$$a^M \equiv 1 \pmod N \quad \forall a \in \mathbb{Z} \text{ where } \gcd(a, N) = 1$$

The domain of the function is $\mathcal{D} = \{N \in \mathbb{Z} \mid N \ge 1\}$, and the codomain is $\mathcal{C} = \mathbb{Z}^+$. 
Let the prime factorization of $N$ be given by the canonical representation:
$$N = \prod_{i=1}^{m} p_i^{k_i}$$
where $p_i$ are distinct primes and $k_i \in \mathbb{Z}^+$.

## 2. Algebraic Characterization

The Carmichael function is a well-defined arithmetic function that satisfies the property of being the least common multiple of the Carmichael values of its prime power components.

### The Fundamental Theorem of $\lambda(N)$
For $N = p_1^{k_1} p_2^{k_2} \cdots p_m^{k_m}$, the function is defined as:
$$\lambda(N) = \text{lcm}(\lambda(p_1^{k_1}), \lambda(p_2^{k_2}), \dots, \lambda(p_m^{k_m}))$$

### Evaluation on Prime Powers
The value of $\lambda(p^k)$ is determined by the structure of the group $(\mathbb{Z}/p^k\mathbb{Z})^\times$:

1. **For odd primes ($p > 2$):**
   The group is cyclic, and $\lambda(p^k) = \phi(p^k) = p^{k-1}(p-1)$.

2. **For the prime $p = 2$:**
   - If $k=1$, $\lambda(2) = 1$.
   - If $k=2$, $\lambda(4) = 2$.
   - If $k \ge 3$, the group $(\mathbb{Z}/2^k\mathbb{Z})^\times$ is isomorphic to $C_2 \times C_{2^{k-2}}$. Thus, the exponent is:
     $$\lambda(2^k) = 2^{k-2}$$

### Recursive Invariant
Let $f(n, p)$ be a function that extracts the prime power $p^k$ from $n$ and updates the running result $L$. The state transition at each step $i$ is:
$$L_i = \text{lcm}(L_{i-1}, \lambda(p_i^{k_i}))$$
where $L_0 = 1$. The algorithm terminates when $\prod p_i^{k_i} = N$.

## 3. Complexity Analysis

### Time Complexity
The algorithm relies on trial division to determine the prime factorization of $N$. 

1. **Factorization Phase:** We iterate through potential divisors $p$ such that $p \le \sqrt{N}$. In the worst case (where $N$ is prime), the loop executes $\lceil \sqrt{N} \rceil$ iterations. Each iteration performs a constant number of arithmetic operations (modulo and division). Thus, the factorization phase is $O(\sqrt{N})$.
2. **LCM Phase:** Given the prime factorization, there are at most $\omega(N)$ distinct prime factors, where $\omega(N) \le \log_2 N$. The calculation of $\text{lcm}(a, b) = \frac{|a \cdot b|}{\gcd(a, b)}$ involves the Euclidean algorithm, which is $O(\log(\min(a, b)))$. Since $\lambda(N) < N$, this is $O(\log N)$.

Summing these, the total time complexity is dominated by the factorization:
$$T(N) = O(\sqrt{N}) + O(\omega(N) \log N) = O(\sqrt{N})$$

### Space Complexity
The algorithm maintains a constant number of variables: `temp` (the remaining quotient), `p` (the current divisor), `lam` (the running LCM), and `pk_lam` (the local prime power result). 

Since the storage requirements do not scale with the magnitude of $N$ (assuming fixed-width integer arithmetic or logarithmic space for arbitrary-precision integers), the auxiliary space complexity is:
$$S(N) = O(1)$$
If we consider the storage of the prime factors in a dictionary/map, the space complexity is $O(\log N)$ to store the distinct prime factors, but the provided implementation uses an iterative approach that processes factors on-the-fly, maintaining $O(1)$ space.