# Formal Mathematical Specification: Extended Euclidean Algorithm

## 1. Definitions and Notation

Let $\mathbb{Z}$ denote the set of integers. We define the input domain as a pair $(a, b) \in \mathbb{Z}_{\ge 0} \times \mathbb{Z}_{\ge 0}$, where $(a, b) \neq (0, 0)$. 

The algorithm computes a triplet $(g, x, y) \in \mathbb{Z} \times \mathbb{Z} \times \mathbb{Z}$ such that:
1. $g = \gcd(a, b)$, where $\gcd(a, b)$ is the unique non-negative integer satisfying:
   - $g \mid a$ and $g \mid b$.
   - For any $d \in \mathbb{Z}$, if $d \mid a$ and $d \mid b$, then $d \mid g$.
2. The triplet satisfies Bézout's identity: $ax + by = g$.

The state space $\mathcal{S}$ of the iterative implementation is defined by the tuple $(r_i, s_i, t_i)$, representing the remainder and the coefficients at step $i$, such that $r_i = a s_i + b t_i$.

## 2. Algebraic Characterization

The algorithm relies on the Euclidean division theorem. For any $a, b \in \mathbb{Z}$ with $b > 0$, there exist unique $q, r \in \mathbb{Z}$ such that $a = bq + r$ and $0 \le r < b$.

### Recurrence Relation
The GCD satisfies the recurrence:
$\gcd(a, b) = \gcd(b, a \pmod b)$
With the base case $\gcd(a, 0) = a$.

To maintain the coefficients $(x, y)$ such that $ax + by = \gcd(a, b)$, we observe the transition from the recursive step. Let $(g, x_1, y_1)$ be the solution for $(b, a \pmod b)$, such that:
$b x_1 + (a \pmod b) y_1 = g$

Substituting $a \pmod b = a - \lfloor \frac{a}{b} \rfloor b$:
$b x_1 + (a - \lfloor \frac{a}{b} \rfloor b) y_1 = g$
$a(y_1) + b(x_1 - \lfloor \frac{a}{b} \rfloor y_1) = g$

Thus, the update rule for the coefficients is:
$x = y_1$
$y = x_1 - \lfloor \frac{a}{b} \rfloor y_1$

### Loop Invariant
For the iterative implementation, let $(r_0, r_1) = (a, b)$, $(s_0, s_1) = (1, 0)$, and $(t_0, t_1) = (0, 1)$. At each iteration $i$, the following invariants hold:
1. $r_i = a s_i + b t_i$
2. $\gcd(r_i, r_{i+1}) = \gcd(a, b)$

The algorithm terminates at index $k$ where $r_{k+1} = 0$, yielding $r_k = \gcd(a, b)$.

## 3. Complexity Analysis

### Time Complexity
The time complexity is governed by the number of divisions performed, which is identical to the standard Euclidean algorithm. By Lamé's Theorem, the number of steps $n$ required to compute $\gcd(a, b)$ is bounded by the number of digits in the smaller input. Specifically, if $a > b \ge 1$, the number of iterations is $O(\log b)$. 

Since each iteration involves a constant number of arithmetic operations (division, multiplication, subtraction), the total time complexity is:
$T(a, b) = O(\log(\min(a, b)))$

### Space Complexity
- **Recursive Implementation:** The algorithm requires a call stack of depth equal to the number of recursive steps. Since the number of steps is $O(\log(\min(a, b)))$, the auxiliary space complexity is $O(\log(\min(a, b)))$.
- **Iterative Implementation:** The algorithm maintains a constant number of variables $(r, s, t, q)$ regardless of the input size. Thus, the auxiliary space complexity is $O(1)$. 

The provided implementation is iterative, occupying $O(1)$ auxiliary space, though the problem statement notes the recursive logic is often used for its mathematical elegance.