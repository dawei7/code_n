# Formal Mathematical Specification: Modular Multiplicative Inverse

## 1. Definitions and Notation

Let $\mathbb{Z}$ denote the set of integers. Given an integer $a \in \mathbb{Z}$ and a modulus $m \in \mathbb{Z}^+$, we define the **Modular Multiplicative Inverse** as an integer $x$ such that the congruence relation holds:
$$ax \equiv 1 \pmod{m}$$
The domain of the input is $(a, m) \in \mathbb{Z} \times \mathbb{Z}^+$. The output space is $\mathcal{X} = \{x \in \mathbb{Z} \mid 0 \le x < m\} \cup \{-1\}$, where $-1$ denotes the non-existence of an inverse.

The existence of $x$ is governed by the condition $\gcd(a, m) = 1$. If $\gcd(a, m) = d > 1$, then for any $x$, $ax \equiv 0 \pmod{d}$, which implies $ax \not\equiv 1 \pmod{m}$ since $1 \not\equiv 0 \pmod{d}$. Thus, the inverse exists if and only if $a$ and $m$ are coprime.

## 2. Algebraic Characterization

### The Extended Euclidean Approach
The congruence $ax \equiv 1 \pmod{m}$ is equivalent to the existence of an integer $y \in \mathbb{Z}$ such that:
$$ax + my = 1$$
This is a linear Diophantine equation, a specific instance of Bézout's Identity. The Extended Euclidean Algorithm (EEA) computes the greatest common divisor $g = \gcd(a, m)$ and the coefficients $(x, y)$ such that $ax + my = g$. 

The algorithm proceeds by maintaining the invariant:
$$r_i = s_i a + t_i m$$
where $r_i$ is the remainder at step $i$. Given the recurrence $r_{i-2} = q_i r_{i-1} + r_i$, the coefficients are updated as:
$$s_i = s_{i-2} - q_i s_{i-1}$$
$$t_i = t_{i-2} - q_i t_{i-1}$$
Upon termination, $r_k = \gcd(a, m)$. If $r_k = 1$, the modular inverse is $x \equiv s_k \pmod{m}$. To ensure $x \in [0, m-1]$, we compute $x = (s_k \pmod{m} + m) \pmod{m}$.

### Fermat’s Little Theorem (Special Case)
If $m = p$ where $p$ is prime and $p \nmid a$, Fermat's Little Theorem states:
$$a^{p-1} \equiv 1 \pmod{p}$$
Multiplying by $a^{-1}$ yields:
$$a^{p-2} \equiv a^{-1} \pmod{p}$$
This characterizes the inverse as a power function in the multiplicative group $(\mathbb{Z}/p\mathbb{Z})^\times$.

## 3. Complexity Analysis

### Time Complexity
The time complexity is dominated by the Euclidean Algorithm. Let $T(a, m)$ be the number of steps. By Lamé's Theorem, the number of divisions required to compute $\gcd(a, m)$ is at most $5 \cdot \lfloor \log_{10}(\min(a, m)) \rfloor + 1$. 

Since each step involves a constant number of arithmetic operations (division, multiplication, subtraction), the total time complexity is:
$$T(n) = O(\log(\min(a, m)))$$
In the context of the input size $n = \log_2(m)$, this is $O(n)$, which is linear with respect to the number of bits in the modulus.

### Space Complexity
The iterative implementation of the Extended Euclidean Algorithm maintains a constant number of variables ($r, s, q, \text{old\_r}, \text{old\_s}$) regardless of the magnitude of $a$ or $m$. 

- **Auxiliary Space:** $O(1)$, as we only store the current and previous state of the remainder and coefficient sequences.
- **Total Space:** $O(1)$ (excluding the space required to store the input integers themselves). 

If implemented recursively, the space complexity would be $O(\log(\min(a, m)))$ due to the call stack depth, but the iterative formulation achieves the optimal $O(1)$ bound.