# Formal Mathematical Specification: Frequency of Elements in Sorted Array

## 1. Definitions and Notation

Let $A = [a_0, a_1, \dots, a_{n-1}]$ be a sequence of integers of length $n \in \mathbb{N}_0$, where the sequence is non-decreasing, such that $a_i \leq a_{i+1}$ for all $0 \leq i < n-1$. Let $x \in \mathbb{Z}$ denote the target value.

We define the set of indices where the target occurs as:
$$I_x = \{i \in \{0, \dots, n-1\} \mid a_i = x\}$$

The objective is to determine the cardinality of $I_x$, denoted $|I_x|$, or return the boundary pair $(\min(I_x), \max(I_x))$ if $I_x \neq \emptyset$, and $(-1, -1)$ otherwise.

- **Domain of indices:** $\mathcal{I} = \{0, 1, \dots, n-1\}$.
- **State space:** The algorithm maintains a state $\mathcal{S} = (l, r, \text{ans})$, where $l, r \in \mathbb{Z}$ represent the search boundaries and $\text{ans} \in \mathcal{I} \cup \{-1\}$ represents the current best candidate index.

## 2. Algebraic Characterization

The algorithm relies on the monotonicity of the predicate $P(i) \equiv (a_i \geq x)$. Because $A$ is sorted, there exists a unique partition point $k$ such that $a_i < x$ for all $i < k$ and $a_i \geq x$ for all $i \geq k$.

### Leftmost Occurrence ($\mathcal{L}$)
To find $\min(I_x)$, we define the search function $f_L(A, x)$ which maintains the invariant:
1. If $a_{mid} < x$, then $\min(I_x) > mid$.
2. If $a_{mid} \geq x$, then $\min(I_x) \leq mid$.

The update rule for the search interval $[l, r]$ is:
$$
\begin{cases} 
l_{t+1} = mid + 1, & \text{if } a_{mid} < x \\
r_{t+1} = mid - 1, \text{ ans} = mid, & \text{if } a_{mid} = x \\
r_{t+1} = mid - 1, & \text{if } a_{mid} > x 
\end{cases}
$$
The search terminates when $l > r$, yielding $\min(I_x) = \text{ans}$ if $a_{\text{ans}} = x$, else $\text{undefined}$.

### Rightmost Occurrence ($\mathcal{R}$)
To find $\max(I_x)$, we define the search function $f_R(A, x)$ which maintains the invariant:
1. If $a_{mid} \leq x$, then $\max(I_x) \geq mid$.
2. If $a_{mid} > x$, then $\max(I_x) < mid$.

The update rule for the search interval $[l, r]$ is:
$$
\begin{cases} 
l_{t+1} = mid + 1, \text{ ans} = mid, & \text{if } a_{mid} = x \\
l_{t+1} = mid + 1, & \text{if } a_{mid} < x \\
r_{t+1} = mid - 1, & \text{if } a_{mid} > x 
\end{cases}
$$
The frequency is given by the mapping $\Phi: A \times \mathbb{Z} \to \mathbb{N}_0$:
$$\Phi(A, x) = \begin{cases} \max(I_x) - \min(I_x) + 1 & \text{if } I_x \neq \emptyset \\ 0 & \text{if } I_x = \emptyset \end{cases}$$

## 3. Complexity Analysis

### Time Complexity
The algorithm performs two independent binary searches. Each binary search operates on a search space of size $N$ that is halved at each iteration $t$. The recurrence relation for the number of operations $T(N)$ is:
$$T(N) = T\left(\frac{N}{2}\right) + c$$
By the Master Theorem, where $a=1, b=2, f(n)=O(1)$, we have $T(N) = O(\log_2 N)$.
Since the algorithm executes two such searches sequentially, the total time complexity is:
$$T_{total}(N) = O(\log N) + O(\log N) = O(\log N)$$

### Space Complexity
The algorithm utilizes a constant number of auxiliary variables ($l, r, mid, \text{first}, \text{last}$) regardless of the input size $N$. 
- **Auxiliary Space:** $O(1)$.
- **Total Space:** $O(N)$ to store the input array, but $O(1)$ additional space beyond the input storage. Thus, the algorithm is strictly in-place.