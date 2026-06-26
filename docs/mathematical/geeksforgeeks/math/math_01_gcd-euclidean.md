# Formal Mathematical Specification: Greatest Common Divisor (Euclidean Algorithm)

## 1. Definitions and Notation

Let $\mathbb{Z}^+$ denote the set of positive integers $\{1, 2, 3, \dots\}$ and $\mathbb{N}_0$ denote the set of non-negative integers $\{0, 1, 2, \dots\}$.

The Greatest Common Divisor (GCD) of two integers $a, b \in \mathbb{Z}^+$ is defined as the unique positive integer $g = \gcd(a, b)$ such that:
1. $g \mid a$ and $g \mid b$ (Common divisor property).
2. For any $d \in \mathbb{Z}^+$, if $d \mid a$ and $d \mid b$, then $d \mid g$ (Maximality property).

The algorithm operates on a state space $\mathcal{S} \subset \mathbb{N}_0 \times \mathbb{N}_0$. Given an initial input $(a_0, b_0) \in \mathbb{Z}^+ \times \mathbb{Z}^+$, the algorithm generates a sequence of states $(a_k, b_k)$ where $k \in \mathbb{N}_0$.

## 2. Algebraic Characterization

The correctness of the Euclidean algorithm is predicated on the Division Theorem and the properties of the GCD function.

**Theorem (Euclidean Reduction):** For any $a, b \in \mathbb{N}_0$ where $b > 0$, let $a = qb + r$, where $q = \lfloor a/b \rfloor$ and $r = a \pmod b$. Then:
$$\gcd(a, b) = \gcd(b, r)$$

**Proof Sketch:**
Let $d_1 = \gcd(a, b)$ and $d_2 = \gcd(b, r)$. 
Since $d_1 \mid a$ and $d_1 \mid b$, then $d_1 \mid (a - qb)$, which implies $d_1 \mid r$. Thus, $d_1$ is a common divisor of $b$ and $r$, so $d_1 \leq d_2$.
Conversely, since $d_2 \mid b$ and $d_2 \mid r$, then $d_2 \mid (qb + r)$, which implies $d_2 \mid a$. Thus, $d_2$ is a common divisor of $a$ and $b$, so $d_2 \leq d_1$.
Therefore, $d_1 = d_2$.

**Loop Invariant:**
Let $(a_k, b_k)$ be the state at iteration $k$. The invariant $\gcd(a_k, b_k) = \gcd(a_0, b_0)$ holds for all $k$ until $b_k = 0$.
The transition function $f: \mathcal{S} \to \mathcal{S}$ is defined as:
$$f(a, b) = (b, a \pmod b)$$
The algorithm terminates at the smallest $k$ such that $b_k = 0$, yielding $\gcd(a_k, 0) = a_k$.

## 3. Complexity Analysis

### Time Complexity
The time complexity is determined by the number of iterations required to reach $b_k = 0$. 

**Theorem (Lamé's Theorem):** Let $a > b \geq 1$. The number of steps $n$ required by the Euclidean algorithm to compute $\gcd(a, b)$ is at most $5 \cdot \log_{10}(b)$.

**Derivation:**
Consider the sequence of remainders $r_0, r_1, \dots, r_n$ where $r_0 = a, r_1 = b$, and $r_{i+1} = r_{i-1} \pmod{r_i}$. 
Since $r_{i-1} = q_i r_i + r_{i+1}$ and $q_i \geq 1$, we have $r_{i-1} \geq r_i + r_{i+1}$. 
If we define the Fibonacci sequence $F_n$ where $F_0=0, F_1=1, F_2=1, \dots$, it can be shown by induction that $r_{n-i+1} \geq F_{i+1}$. 
For the worst case, $b < F_{n+2}$. Using Binet's Formula, $F_n \approx \frac{\phi^n}{\sqrt{5}}$ where $\phi = \frac{1+\sqrt{5}}{2} \approx 1.618$. 
Taking logarithms, $n \approx \log_{\phi}(b) \approx 1.44 \log_2(b)$.
Thus, the time complexity is $O(\log(\min(a, b)))$.

### Space Complexity
The iterative implementation maintains only two integer variables $a$ and $b$ in the state space $\mathcal{S}$. 
The auxiliary space required is independent of the magnitude of the inputs, as the variables are updated in-place.
Therefore, the space complexity is $O(1)$. 

(Note: A recursive implementation would require $O(\log(\min(a, b)))$ stack space to store the activation records of the recursion depth.)