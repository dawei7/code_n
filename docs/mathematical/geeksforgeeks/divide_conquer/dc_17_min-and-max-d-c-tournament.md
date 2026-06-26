# Formal Mathematical Specification: Min and Max in Array (Tournament Method)

## 1. Definitions and Notation

Let $A = [a_0, a_1, \dots, a_{n-1}]$ be an ordered sequence (array) of $n$ elements drawn from a totally ordered set $(\mathcal{X}, \le)$. 

*   **Input:** An array $A$ of size $n \in \mathbb{N}^+$.
*   **Output:** A tuple $(m, M) \in \mathcal{X} \times \mathcal{X}$ such that:
    *   $m = \min \{a_i \mid 0 \le i < n\}$
    *   $M = \max \{a_i \mid 0 \le i < n\}$
*   **State Space:** The algorithm operates on a recursive decomposition of the index set $I = \{0, 1, \dots, n-1\}$. A sub-problem is defined by the interval $[l, r] \subseteq I$, where the state is the pair $(m_{[l,r]}, M_{[l,r]})$ representing the minimum and maximum of the subarray $A[l \dots r]$.

## 2. Algebraic Characterization

The algorithm defines a recursive function $f(l, r)$ that maps an index interval to the set of extrema. The correctness is governed by the following recurrence:

$$
f(l, r) = 
\begin{cases} 
(a_l, a_l) & \text{if } l = r \\
(\min(a_l, a_{l+1}), \max(a_l, a_{l+1})) & \text{if } r = l + 1 \\
(\min(m_L, m_R), \max(M_L, M_R)) & \text{if } r > l + 1
\end{cases}
$$

where $(m_L, M_L) = f(l, \lfloor \frac{l+r}{2} \rfloor)$ and $(m_R, M_R) = f(\lfloor \frac{l+r}{2} \rfloor + 1, r)$.

**Correctness Invariant:**
For any interval $[l, r]$, the returned tuple $(m, M)$ satisfies:
1. $m \in \{a_i\}_{i=l}^r \land M \in \{a_i\}_{i=l}^r$
2. $\forall i \in [l, r], m \le a_i \le M$

The optimality of the comparison count $C(n)$ is defined by the recurrence:
$$C(n) = C(\lceil n/2 \rceil) + C(\lfloor n/2 \rfloor) + 2$$
With base cases $C(1) = 0$ and $C(2) = 1$. Solving this recurrence yields $C(n) = \lceil \frac{3n}{2} \rceil - 2$.

## 3. Complexity Analysis

### Time Complexity
The time complexity is determined by the number of comparisons performed. Let $T(n)$ be the number of comparisons for an input of size $n$. The recurrence relation is:
$$T(n) = 2T\left(\frac{n}{2}\right) + 2$$
Applying the **Master Theorem** for divide-and-conquer recurrences of the form $T(n) = aT(n/b) + f(n)$:
*   Here, $a=2, b=2, f(n)=2$.
*   Since $f(n) = \Theta(n^{\log_b a}) = \Theta(n^{\log_2 2}) = \Theta(n^1)$, we fall into Case 2 of the Master Theorem.
*   Therefore, $T(n) = \Theta(n \log n)$ is incorrect because the work at each level is constant, not linear. Re-evaluating: $T(n) = \Theta(n)$.
*   Specifically, the total number of comparisons is $T(n) = \frac{3n}{2} - 2$ for $n = 2^k$, which is strictly $O(n)$.

### Space Complexity
The space complexity is determined by the maximum depth of the recursion stack.
*   The recursion tree is a binary tree with a branching factor of 2.
*   The depth of the tree $D$ for an input of size $n$ is given by $D = \lceil \log_2 n \rceil$.
*   At each level of the stack, we store a constant amount of metadata (the indices $l, r, mid$ and the returned tuple).
*   Thus, the auxiliary space complexity is $S(n) = O(\text{depth}) = O(\log n)$.