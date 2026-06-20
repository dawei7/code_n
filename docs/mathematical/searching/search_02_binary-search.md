# Formal Mathematical Specification: Binary Search

## 1. Definitions and Notation

Let $A = (a_0, a_1, \dots, a_{n-1})$ be a sequence of elements drawn from a totally ordered set $(\mathcal{X}, \le)$. The sequence is sorted such that $a_i \le a_{i+1}$ for all $0 \le i < n-1$. Given a target value $t \in \mathcal{X}$, the objective is to determine an index $k \in \{0, 1, \dots, n-1\}$ such that $a_k = t$, or return a sentinel value $\bot \notin \{0, \dots, n-1\}$ if no such $k$ exists.

We define the state of the algorithm at iteration $m$ by the tuple $(L_m, R_m)$, where $L_m, R_m \in \mathbb{Z}$ represent the inclusive boundaries of the search interval $[L_m, R_m]$. The initial state is $(L_0, R_0) = (0, n-1)$.

## 2. Algebraic Characterization

The algorithm is governed by a loop invariant $\mathcal{I}(L, R)$ which asserts that if $t$ exists in $A$, then its index must reside within the closed interval $[L, R]$.

**Invariant:**
$$\mathcal{I}(L, R) \equiv \forall k \in \{0, \dots, n-1\} : (a_k = t) \implies (L \le k \le R)$$

**Transition Function:**
Let $M_m = \lfloor \frac{L_m + R_m}{2} \rfloor$. The state transition $(L_m, R_m) \to (L_{m+1}, R_{m+1})$ is defined by the trichotomy of the ordered set $\mathcal{X}$:

1. If $a_{M_m} = t$, the algorithm terminates and returns $M_m$.
2. If $a_{M_m} < t$, then for all $k \le M_m$, $a_k \le a_{M_m} < t$. Thus, $a_k \neq t$. The new state is $(L_{m+1}, R_{m+1}) = (M_m + 1, R_m)$.
3. If $a_{M_m} > t$, then for all $k \ge M_m$, $a_k \ge a_{M_m} > t$. Thus, $a_k \neq t$. The new state is $(L_{m+1}, R_{m+1}) = (L_m, M_m - 1)$.

**Termination:**
The algorithm terminates when $L_m > R_m$. At this point, the invariant $\mathcal{I}(L_m, R_m)$ implies that the set of indices $\{k \mid L_m \le k \le R_m\}$ is empty. Consequently, there exists no $k$ such that $a_k = t$, and the algorithm returns $\bot$.

## 3. Complexity Analysis

### Time Complexity
Let $N_m = R_m - L_m + 1$ be the size of the search space at iteration $m$. In each iteration, the algorithm performs a constant number of operations $c$ to compute $M_m$ and compare $a_{M_m}$ with $t$. The size of the search space evolves as:
$$N_{m+1} \le \left\lfloor \frac{N_m}{2} \right\rfloor$$
This recurrence relation $T(n) = T(n/2) + O(1)$ describes the halving of the search space. By the Master Theorem (Case 2), where $a=1, b=2, f(n)=O(1)$, we have:
$$T(n) = \Theta(n^{\log_b a}) = \Theta(n^0 \log n) = O(\log n)$$
The worst-case number of iterations $m$ is the smallest integer such that $N_m < 1$, which satisfies $n/2^m < 1$, yielding $m = \lceil \log_2(n+1) \rceil$.

### Space Complexity
The algorithm maintains a fixed number of scalar variables $(L, R, M, \text{value})$ regardless of the input size $n$. 
- **Auxiliary Space:** The iterative implementation requires $O(1)$ auxiliary space to store the pointers and the mid-point index.
- **Total Space:** The space complexity is $O(n)$ to store the input array $A$, but the algorithm's memory footprint is $O(1)$ relative to the input.