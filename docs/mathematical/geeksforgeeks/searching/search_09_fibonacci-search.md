# Formal Mathematical Specification: Fibonacci Search

## 1. Definitions and Notation

Let $A = [a_0, a_1, \dots, a_{n-1}]$ be a sequence of elements from a totally ordered set $(\mathcal{X}, \le)$, such that $a_i \le a_{i+1}$ for all $0 \le i < n-1$. Let $x \in \mathcal{X}$ be the target value.

We define the Fibonacci sequence $\{F_k\}_{k \in \mathbb{N}_0}$ by the recurrence:
$F_0 = 0, F_1 = 1, F_k = F_{k-1} + F_{k-2}$ for $k \ge 2$.

The algorithm operates on a state space $\mathcal{S} \subseteq \mathbb{N}_0^3 \times \mathbb{Z} \times \mathbb{Z}$, where a state is defined by the tuple $(F_k, F_{k-1}, F_{k-2}, \text{offset}, n)$.
- $n \in \mathbb{N}$ is the length of the array.
- $k$ is the index such that $F_k$ is the smallest Fibonacci number satisfying $F_k \ge n$.
- $\text{offset} \in \{-1, 0, \dots, n-2\}$ represents the index immediately preceding the current search sub-interval.

The output is a function $f: \mathcal{X}^n \times \mathcal{X} \to \{-1, 0, \dots, n-1\}$ defined as:
$f(A, x) = \begin{cases} i & \text{if } a_i = x \\ -1 & \text{if } \forall i, a_i \neq x \end{cases}$

## 2. Algebraic Characterization

The algorithm maintains the invariant that the target $x$, if present, lies within the index range $(\text{offset}, \text{offset} + F_k]$. The search proceeds by partitioning the current range of length $F_k$ into two sub-intervals of lengths $F_{k-1}$ and $F_{k-2}$, where $F_k = F_{k-1} + F_{k-2}$.

Let $i = \min(\text{offset} + F_{k-2}, n-1)$. The transition logic is governed by the trichotomy property of the ordered set $\mathcal{X}$:

1. **Case $a_i < x$:** The target must reside in the interval $(\text{offset} + F_{k-2}, \text{offset} + F_k]$. We update:
   $\text{offset}' = i$
   $F_k' = F_{k-1}, \quad F_{k-1}' = F_{k-2}, \quad F_{k-2}' = F_{k-1} - F_{k-2} = F_{k-3}$
   
2. **Case $a_i > x$:** The target must reside in the interval $(\text{offset}, \text{offset} + F_{k-2}]$. We update:
   $\text{offset}' = \text{offset}$
   $F_k' = F_{k-2}, \quad F_{k-1}' = F_{k-3}, \quad F_{k-2}' = F_{k-2} - F_{k-3} = F_{k-4}$

3. **Case $a_i = x$:** The search terminates with index $i$.

The loop terminates when $F_k \le 1$. The correctness relies on the property that the search space is reduced by a factor related to the golden ratio $\phi = \frac{1+\sqrt{5}}{2}$, specifically $F_{k-2} \approx \frac{F_k}{\phi^2}$, ensuring the interval size strictly decreases.

## 3. Complexity Analysis

### Time Complexity
The algorithm performs a constant number of additions and subtractions per iteration. The number of iterations $T(n)$ is determined by the number of steps required to reduce $F_k$ to 1. 

Given Binet's Formula, $F_k = \frac{\phi^k - \psi^k}{\sqrt{5}}$, where $\phi = \frac{1+\sqrt{5}}{2}$ and $\psi = \frac{1-\sqrt{5}}{2}$. Since $|\psi| < 1$, we have $F_k \approx \frac{\phi^k}{\sqrt{5}}$.
Setting $F_k \ge n$, we find $k \approx \log_\phi(n\sqrt{5})$. 
Since each iteration reduces the index $k$ by at least 1, the number of iterations is $O(\log_\phi n)$. By the change of base formula, $\log_\phi n = \frac{\ln n}{\ln \phi}$, thus:
$T(n) = O(\log n)$.

### Space Complexity
The algorithm maintains a fixed set of variables: $\{F_k, F_{k-1}, F_{k-2}, \text{offset}, i\}$. None of these variables scale with the input size $n$ in terms of memory allocation (they are stored in fixed-width registers). 
Therefore, the auxiliary space complexity is:
$S(n) = O(1)$.