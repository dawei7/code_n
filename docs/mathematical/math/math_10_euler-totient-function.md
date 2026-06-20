# Formal Mathematical Specification: Euler's Totient Function

## 1. Definitions and Notation

Let $\mathbb{Z}^+$ denote the set of positive integers. We define Euler's totient function $\phi: \mathbb{Z}^+ \to \mathbb{Z}^+$ as the cardinality of the set of integers $k$ such that $1 \le k \le n$ and $\gcd(k, n) = 1$:
$$\phi(n) = |\{k \in \mathbb{Z} : 1 \le k \le n, \gcd(k, n) = 1\}|$$

**Input:** An integer $n \in \mathbb{Z}^+$.
**Output:** An integer $m \in \mathbb{Z}^+$ such that $m = \phi(n)$.
**State Space:** The algorithm maintains a state tuple $(n_{curr}, \phi_{curr}, p)$, where:
- $n_{curr} \in \mathbb{Z}^+$ represents the remaining factor of the original $n$ yet to be processed.
- $\phi_{curr} \in \mathbb{Z}^+$ represents the partial product calculation of the totient.
- $p \in \mathbb{Z}^+$ represents the current candidate prime factor.

## 2. Algebraic Characterization

The algorithm relies on the property that $\phi(n)$ is a multiplicative function. By the Fundamental Theorem of Arithmetic, any $n > 1$ has a unique prime factorization $n = p_1^{a_1} p_2^{a_2} \cdots p_k^{a_k}$. The totient function is given by:
$$\phi(n) = n \prod_{i=1}^{k} \left(1 - \frac{1}{p_i}\right) = \prod_{i=1}^{k} (p_i^{a_i} - p_i^{a_i-1})$$

**Loop Invariant:**
At the start of each iteration of the loop with candidate $p$, let $n_{orig}$ be the initial input. The state satisfies:
$$\phi_{curr} = n_{orig} \cdot \prod_{p_j < p, p_j | n_{orig}} \left(1 - \frac{1}{p_j}\right)$$
where $n_{curr} = n_{orig} / \prod_{p_j < p, p_j | n_{orig}} p_j^{a_j}$.

**Transition:**
When a prime factor $p$ is identified ($n_{curr} \equiv 0 \pmod p$), the update rule is:
$$\phi_{new} = \phi_{curr} \left(1 - \frac{1}{p}\right) = \phi_{curr} - \frac{\phi_{curr}}{p}$$
This transformation preserves the invariant by incorporating the contribution of the prime factor $p$ into the product. The division $n_{curr} \leftarrow n_{curr} / p^a$ ensures that $p$ is removed from the remaining factorization, satisfying the condition that subsequent iterations only consider prime factors $q > p$.

## 3. Complexity Analysis

### Time Complexity
The algorithm iterates through candidate divisors $p$ starting from $2$ up to $\lfloor \sqrt{n} \rfloor$. 

1. **Case 1: $n$ is prime.** The loop runs for $p = 2, \dots, \lfloor \sqrt{n} \rfloor$. No $p$ divides $n$, so the inner `while` loop never executes. The complexity is $O(\sqrt{n})$.
2. **Case 2: $n$ is composite.** The number of iterations is bounded by $\sqrt{n}$. However, each time a prime factor is found, $n_{curr}$ is reduced by a factor of at least $p$. The total number of divisions performed across all inner `while` loops is bounded by $\Omega(\log n)$. 

The worst-case time complexity is determined by the loop bound:
$$T(n) = \sum_{p=2}^{\sqrt{n}} 1 = O(\sqrt{n})$$
In the average case, for a random integer, the density of prime factors is small, and the reduction of $n_{curr}$ significantly accelerates the loop termination, but the upper bound remains $O(\sqrt{n})$.

### Space Complexity
The algorithm utilizes a fixed number of integer variables ($n_{curr}, \phi_{curr}, p$). No auxiliary data structures (such as arrays or recursion stacks) are allocated that scale with $n$. Thus, the space complexity is:
$$S(n) = O(1)$$
This is optimal, as the algorithm operates in-place on the input value.