# Formal Mathematical Specification: Sqrt(x) (Floor Square Root)

## 1. Definitions and Notation

Let $x \in \mathbb{N}_0$ be the input non-negative integer. We define the objective function $f: \mathbb{N}_0 \to \mathbb{N}_0$ such that:
$$f(x) = \lfloor \sqrt{x} \rfloor$$
where $\lfloor \cdot \rfloor$ denotes the floor function, mapping a real number to the greatest integer less than or equal to it.

The algorithm operates over a discrete search space $\mathcal{S} = \{0, 1, 2, \dots, x\}$. We define the state of the algorithm at iteration $k$ by the tuple $(L_k, R_k, \text{res}_k)$, where:
*   $L_k \in \mathbb{N}_0$ is the lower bound of the search interval.
*   $R_k \in \mathbb{N}_0$ is the upper bound of the search interval.
*   $\text{res}_k \in \mathbb{N}_0$ is the current best approximation (the "candidate" floor) such that $\text{res}_k^2 \le x$.

## 2. Algebraic Characterization

The algorithm is a search for the unique integer $y \in \mathcal{S}$ satisfying the condition:
$$y^2 \le x < (y+1)^2$$

### Loop Invariant
At the start of each iteration $k$, the following invariant holds:
1.  The true value $f(x)$ is contained within the interval $[L_k, R_k]$ if we consider the candidate $\text{res}_k$. More formally, for all $z \in \mathbb{N}_0$ such that $z^2 \le x$, $z \le R_k$ is not necessarily true, but $\text{res}_k = \max \{ z \in \{0, \dots, L_k-1\} \mid z^2 \le x \}$.
2.  The search space is monotonically decreasing: $|R_{k+1} - L_{k+1}| \approx \frac{1}{2} |R_k - L_k|$.

### State Transitions
Given $m_k = \lfloor L_k + \frac{R_k - L_k}{2} \rfloor$, the transition function $\delta: (L_k, R_k, \text{res}_k) \to (L_{k+1}, R_{k+1}, \text{res}_{k+1})$ is defined as:
$$
(L_{k+1}, R_{k+1}, \text{res}_{k+1}) = 
\begin{cases} 
(m_k + 1, R_k, m_k) & \text{if } m_k^2 \le x \\
(L_k, m_k - 1, \text{res}_k) & \text{if } m_k^2 > x 
\end{cases}
$$
The algorithm terminates at iteration $K$ when $L_K > R_K$, returning $\text{res}_K$.

## 3. Complexity Analysis

### Time Complexity
The algorithm performs a binary search over the domain $\mathcal{D} = [0, x]$. Let $N = x$. In each iteration, the size of the search interval $I_k = R_k - L_k + 1$ is reduced by approximately half:
$$I_{k+1} \le \frac{I_k}{2}$$
The recurrence relation for the number of operations $T(N)$ is:
$$T(N) = T\left(\frac{N}{2}\right) + c$$
where $c$ represents the constant time required for arithmetic operations (multiplication, comparison, and addition). By the Master Theorem (Case 2), where $a=1, b=2, d=0$:
$$T(N) = \Theta(\log_2 N)$$
Thus, the time complexity is $O(\log x)$.

### Space Complexity
The algorithm maintains a fixed number of scalar variables: $L, R, \text{res}, \text{mid}, \text{sq}$. 
Let $S(N)$ be the auxiliary space required. Since the memory consumption is independent of the input size $x$ (assuming fixed-width integer representation for $x$), we have:
$$S(N) = O(1)$$
The algorithm operates in-place, requiring no additional data structures that scale with the input.