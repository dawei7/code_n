# Formal Mathematical Specification: Miller-Rabin Primality Test

## 1. Definitions and Notation

Let $n \in \mathbb{Z}^+$ be an odd integer such that $n > 3$. We define the primality testing problem as the determination of the predicate $\text{is\_prime}(n) : \mathbb{Z}^+ \to \{0, 1\}$.

*   **Decomposition of $n-1$:** Since $n$ is odd, $n-1$ is even. We define the unique factorization $n-1 = 2^s \cdot d$, where $s \in \mathbb{Z}^+$, $d \in \mathbb{Z}^+$, and $d \equiv 1 \pmod 2$.
*   **Witness Set:** Let $a \in \mathbb{Z}$ be a base such that $2 \le a \le n-2$. We define $a$ as a *Miller-Rabin witness* for the compositeness of $n$ if the following conditions hold:
    1. $a^d \not\equiv 1 \pmod n$
    2. $a^{2^r \cdot d} \not\equiv -1 \pmod n$ for all $0 \le r < s$.
*   **State Space:** The algorithm operates within the multiplicative group $(\mathbb{Z}/n\mathbb{Z})^\times$. The state at each iteration $i \in \{1, \dots, k\}$ is defined by the tuple $(a_i, x_{i,r})$, where $x_{i,r} = a_i^{2^r \cdot d} \pmod n$.

## 2. Algebraic Characterization

The correctness of the Miller-Rabin test relies on the contrapositive of the following theorem:

**Theorem:** If $n$ is an odd prime, then for any $a$ such that $\gcd(a, n) = 1$, the sequence $x_r = a^{2^r \cdot d} \pmod n$ for $0 \le r < s$ satisfies:
1. $x_0 \equiv 1 \pmod n$, OR
2. There exists some $r \in \{0, 1, \dots, s-1\}$ such that $x_r \equiv -1 \pmod n$.

**Proof Sketch:** By Fermat’s Little Theorem, $a^{n-1} \equiv 1 \pmod n$. Since $n$ is prime, the field $\mathbb{Z}/n\mathbb{Z}$ has only two square roots of $1$, namely $1$ and $-1$. The sequence $x_r$ is formed by repeated squaring. If $x_0 \not\equiv 1$, then the first $r$ for which $x_r \equiv 1$ must have been preceded by $x_{r-1}$ such that $x_{r-1}^2 \equiv 1$. By the property of fields, $x_{r-1}$ must be $-1 \equiv n-1$.

**Decision Rule:**
For a chosen base $a$, $n$ is declared composite if:
$$a^d \not\equiv 1 \pmod n \land \forall r \in \{0, \dots, s-1\} : a^{2^r \cdot d} \not\equiv -1 \pmod n$$
Otherwise, $n$ is declared a *strong probable prime* to base $a$. The probability of a composite $n$ passing a single round is bounded by $\frac{1}{4}$ (Monier-Rabin Theorem). For $k$ independent trials, the error probability is bounded by:
$$P(\text{false positive}) \le 4^{-k}$$

## 3. Complexity Analysis

### Time Complexity
The algorithm performs $k$ independent rounds. Each round consists of:
1. **Modular Exponentiation:** Computing $a^d \pmod n$ using the binary exponentiation (square-and-multiply) algorithm. This requires $O(\log d)$ modular multiplications. Since $d < n$, this is $O(\log n)$ multiplications.
2. **Squaring Sequence:** At most $s-1$ squarings, where $s < \log_2 n$. This is $O(\log n)$ modular multiplications.

Given that each modular multiplication of two $m$-bit integers (where $m = \log_2 n$) takes $O(m^2)$ time using standard multiplication (or $O(m \log m \log \log m)$ using Schönhage-Strassen), the complexity per round is $O(\log^3 n)$.
Summing over $k$ rounds, the total time complexity is:
$$T(n, k) = O(k \cdot \log^3 n)$$

### Space Complexity
The algorithm maintains a constant number of variables ($s, d, a, x, r$) regardless of the magnitude of $n$. Each variable requires $O(\log n)$ bits of storage. Thus, the auxiliary space complexity is:
$$S(n) = O(\log n)$$
In terms of word-RAM model complexity where a word holds $\log n$ bits, the space complexity is:
$$S(n) = O(1)$$