# Formal Mathematical Specification: Ternary Search

## 1. Definitions and Notation

Let $A = [a_0, a_1, \dots, a_{n-1}]$ be a sequence of elements from a totally ordered set $(\mathcal{X}, \leq)$, such that for all $i, j \in \{0, \dots, n-1\}$, if $i < j$, then $a_i \leq a_j$. 

We define the search space as a closed interval of indices $\mathcal{I} = [L, R] \subset \mathbb{Z}$, where initially $L = 0$ and $R = n-1$. The objective is to find an index $k \in \{0, \dots, n-1\}$ such that $a_k = \tau$, where $\tau \in \mathcal{X}$ is the target value. If no such $k$ exists, the algorithm returns $-1$.

The state of the algorithm at any iteration $t$ is defined by the tuple $(L_t, R_t)$. The transition function maps the current state to a subsequent state $(L_{t+1}, R_{t+1})$ based on the evaluation of the partition points $m_{1,t}$ and $m_{2,t}$, defined as:
$$m_{1,t} = L_t + \left\lfloor \frac{R_t - L_t}{3} \right\rfloor$$
$$m_{2,t} = R_t - \left\lfloor \frac{R_t - L_t}{3} \right\rfloor$$

## 2. Algebraic Characterization

The correctness of the algorithm relies on the invariant that if $\tau \in \{a_L, \dots, a_R\}$, then $\tau \in \{a_{L_t}, \dots, a_{R_t}\}$. The transition logic is governed by the following partition of the search space:

1. **Base Case (Success):** If $a_{m_{1,t}} = \tau$ or $a_{m_{2,t}} = \tau$, the algorithm terminates and returns the index.
2. **Recursive Step (Reduction):**
   - If $\tau < a_{m_{1,t}}$, then by the monotonicity of $A$, $\tau$ cannot exist in the index range $[m_{1,t}, R_t]$. Thus, $R_{t+1} = m_{1,t} - 1$ and $L_{t+1} = L_t$.
   - If $\tau > a_{m_{2,t}}$, then $\tau$ cannot exist in the index range $[L_t, m_{2,t}]$. Thus, $L_{t+1} = m_{2,t} + 1$ and $R_{t+1} = R_t$.
   - If $a_{m_{1,t}} < \tau < a_{m_{2,t}}$, then $\tau$ cannot exist in $[L_t, m_{1,t}]$ or $[m_{2,t}, R_t]$. Thus, $L_{t+1} = m_{1,t} + 1$ and $R_{t+1} = m_{2,t} - 1$.

The algorithm terminates when $L_t > R_t$, at which point the set of candidate indices is empty, implying $\tau \notin A$.

## 3. Complexity Analysis

### Time Complexity
Let $N_t = R_t - L_t + 1$ be the number of elements in the search space at iteration $t$. In each iteration, the algorithm performs a constant number of comparisons (at most 4) to reduce the search space. The new search space size $N_{t+1}$ satisfies:
$$N_{t+1} \leq \frac{N_t}{3}$$
The recurrence relation for the worst-case number of iterations $T(N)$ is:
$$T(N) = T\left(\frac{N}{3}\right) + c$$
Applying the Master Theorem, where $a=1, b=3, f(N)=O(1)$, we have $N^{\log_b a} = N^0 = 1$. Since $f(N) = \Theta(N^{\log_b a})$, the complexity is:
$$T(N) = \Theta(\log_3 N)$$
Given that each iteration performs two comparisons, the total number of comparisons is approximately $2 \log_3 N$. Using the change-of-base formula $\log_3 N = \frac{\ln N}{\ln 3}$, we observe:
$$2 \frac{\ln N}{\ln 3} \approx 2 \cdot 0.91 \ln N \approx 1.82 \ln N$$
Compared to Binary Search ($\approx \ln N$), Ternary Search is asymptotically equivalent but carries a higher constant factor in the number of comparisons.

### Space Complexity
The algorithm maintains only a fixed number of integer variables ($L, R, m_1, m_2$) regardless of the input size $N$. No auxiliary data structures proportional to the input are allocated. Thus, the auxiliary space complexity is:
$$S(N) = O(1)$$