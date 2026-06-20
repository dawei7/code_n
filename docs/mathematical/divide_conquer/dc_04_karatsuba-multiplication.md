# Formal Mathematical Specification: Karatsuba Multiplication

## 1. Definitions and Notation

Let $\mathbb{N}_0$ denote the set of non-negative integers. We define the input as a pair of integers $(x, y) \in \mathbb{N}_0 \times \mathbb{N}_0$. Let $n$ be the number of digits of the larger integer in a chosen base $B$ (typically $B=10$ or $B=2^k$). 

We represent $x$ and $y$ in base $B$ such that $x, y < B^n$. For a chosen split point $m = \lfloor n/2 \rfloor$, we define the decomposition of $x$ and $y$ as:
$$x = a \cdot B^m + b$$
$$y = c \cdot B^m + d$$
where $a, b, c, d \in \mathbb{N}_0$ such that $0 \le b, d < B^m$. 

The objective is to compute the product $P = x \cdot y$. The state space $\mathcal{S}$ consists of the recursive sub-problems defined by the tuple $(a, b, c, d)$ at each depth of the recursion tree.

## 2. Algebraic Characterization

The product $P$ can be expanded via the distributive property:
$$P = (a \cdot B^m + b)(c \cdot B^m + d) = ac \cdot B^{2m} + (ad + bc) \cdot B^m + bd$$

The naive divide-and-conquer approach requires four multiplications: $ac, ad, bc, bd$. Karatsuba’s insight is to reduce the number of multiplications by exploiting the identity:
$$(a + b)(c + d) = ac + ad + bc + bd$$

Let the three recursive products be defined as:
1. $Z_0 = ac$
2. $Z_1 = bd$
3. $Z_2 = (a + b)(c + d)$

The middle term $(ad + bc)$ is recovered by the linear combination:
$$ad + bc = Z_2 - Z_0 - Z_1$$

Substituting this into the expansion of $P$, we obtain the Karatsuba identity:
$$P = Z_0 \cdot B^{2m} + (Z_2 - Z_0 - Z_1) \cdot B^m + Z_1$$

This formulation is correct for all $x, y \in \mathbb{N}_0$ because the ring of integers $\mathbb{Z}$ is commutative and associative, ensuring the algebraic identity holds regardless of the magnitude of $n$.

## 3. Complexity Analysis

### Time Complexity
The algorithm's execution time $T(n)$ is governed by the number of recursive calls and the overhead of addition/subtraction. Since the algorithm performs three recursive multiplications on inputs of size $n/2$ and performs a constant number of additions and subtractions (which take $O(n)$ time), we establish the recurrence relation:
$$T(n) = 3T(n/2) + O(n)$$

Applying the **Master Theorem** for divide-and-conquer recurrences of the form $T(n) = aT(n/b) + f(n)$:
- Here, $a = 3$, $b = 2$, and $f(n) = O(n^1)$.
- We compare $f(n)$ with $n^{\log_b a} = n^{\log_2 3}$.
- Since $\log_2 3 \approx 1.585 > 1$, the complexity is dominated by the leaves of the recursion tree.
- Thus, $T(n) = \Theta(n^{\log_2 3}) \approx O(n^{1.585})$.

### Space Complexity
The space complexity $S(n)$ is determined by the maximum depth of the recursion stack and the auxiliary storage required for intermediate results at each level.
1. **Recursion Depth:** The depth of the recursion tree is $\log_2 n$.
2. **Auxiliary Space:** At each level of the recursion, we store the intermediate values $Z_0, Z_1, Z_2$ and the decomposed parts $a, b, c, d$. These require $O(n)$ space at the top level, $O(n/2)$ at the next, and so on.
3. **Total Space:** The summation of space across levels is a geometric series:
   $$S(n) = O(n) + O(n/2) + O(n/4) + \dots + O(1) = O(n) \sum_{i=0}^{\log n} \left(\frac{1}{2}\right)^i = O(n)$$
Thus, the total auxiliary space complexity is $O(n)$.