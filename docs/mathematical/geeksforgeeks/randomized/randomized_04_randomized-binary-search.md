# Formal Mathematical Specification: Randomized Binary Search

## 1. Definitions and Notation

Let $A = [a_0, a_1, \dots, a_{n-1}]$ be a sequence of $n$ distinct integers such that $a_i < a_{i+1}$ for all $0 \le i < n-1$. Let $x \in \mathbb{Z}$ be the target value.

We define the state of the algorithm at iteration $k$ by the tuple $\mathcal{S}_k = (L_k, R_k)$, representing the inclusive search interval $[L_k, R_k] \subseteq \{0, 1, \dots, n-1\}$.
- **Initial State:** $\mathcal{S}_0 = (0, n-1)$.
- **Random Variable:** Let $P_k$ be a discrete uniform random variable such that $P_k \sim \mathcal{U}\{L_k, R_k\}$.
- **Termination Condition:** The algorithm terminates at step $T$ if $L_T > R_T$ (failure) or $a_{P_T} = x$ (success).

## 2. Algebraic Characterization

The algorithm defines a stochastic process on the search space size $N_k = R_k - L_k + 1$. The transition function $\Phi: \mathcal{S}_k \to \mathcal{S}_{k+1}$ is defined as:

$$
\mathcal{S}_{k+1} = 
\begin{cases} 
(L_k, P_k - 1) & \text{if } a_{P_k} > x \\
(P_k + 1, R_k) & \text{if } a_{P_k} < x \\
\text{terminate} & \text{if } a_{P_k} = x 
\end{cases}
$$

**Loop Invariant:** For all $k \ge 0$, if $x \in A$, then the index $i$ such that $a_i = x$ satisfies $L_k \le i \le R_k$. 
*Proof Sketch:* By induction, the base case holds for $\mathcal{S}_0$. Given $a_{P_k} \neq x$, the sorted property of $A$ ensures that if $a_{P_k} < x$, then for all $j \le P_k$, $a_j < x$, thus $i \notin [L_k, P_k]$. The symmetric argument holds for $a_{P_k} > x$.

## 3. Complexity Analysis

### Time Complexity

Let $T(n)$ be the expected number of comparisons to find $x$ in an array of size $n$. In each step, we choose a pivot $P \in \{0, \dots, n-1\}$ with probability $\frac{1}{n}$. The size of the remaining sub-problem is $P$ (if we search the left) or $n-1-P$ (if we search the right).

The recurrence relation for the expected time is:
$$E[T(n)] = 1 + \frac{1}{n} \sum_{i=0}^{n-1} \max(E[T(i)], E[T(n-1-i)])$$

To simplify, consider the average case where the pivot splits the array into two segments of size $i$ and $n-1-i$. Since the expected size of the remaining segment is approximately $n/2$, we observe:
$$E[T(n)] \approx 1 + E[T(n/2)]$$
By the Master Theorem (or expansion of the recurrence), this yields:
$$E[T(n)] = \Theta(\log n)$$

**Worst-Case:** The worst case occurs when the random pivot is consistently chosen as the boundary element (e.g., $P_k = L_k$ or $P_k = R_k$). In this scenario, the search space reduces by only 1 element per iteration:
$$T(n) = 1 + T(n-1) \implies T(n) = O(n)$$
However, the probability of selecting the boundary element $k$ times consecutively is $2^k / n^k$, which vanishes as $n \to \infty$.

### Space Complexity

The algorithm maintains only a constant number of scalar variables: $L, R, P,$ and $target$. 
- **Auxiliary Space:** $O(1)$, as the state $\mathcal{S}_k$ is updated in-place without recursion or auxiliary data structures.
- **Total Space:** $O(n)$ to store the input array $A$, but $O(1)$ relative to the algorithm's execution logic.