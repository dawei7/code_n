# Formal Mathematical Specification: Reverse String (Recursive)

## 1. Definitions and Notation

Let $\Sigma$ be a finite alphabet. We define the input as a sequence (or array) $S$ of length $n \in \mathbb{N}_0$, where $S = (s_0, s_1, \dots, s_{n-1})$ and each $s_i \in \Sigma$. 

The state space $\mathcal{S}$ of the algorithm is defined by the tuple $(S, \ell, r)$, where:
*   $S \in \Sigma^n$ is the mutable sequence of characters.
*   $\ell \in \{0, 1, \dots, n\}$ is the left pointer index.
*   $r \in \{-1, 0, \dots, n-1\}$ is the right pointer index.

The objective is to define a transformation $f: \Sigma^n \to \Sigma^n$ such that $f(S) = S'$, where $s'_i = s_{n-1-i}$ for all $0 \le i < n$. The recursive function $H(\ell, r)$ acts as a state transformer on the sequence $S$.

## 2. Algebraic Characterization

The algorithm is governed by a recursive transition function $H: \mathbb{N} \times \mathbb{N} \to \text{void}$. Let $\tau(a, b)$ be the transposition operator such that $\tau(S, i, j)$ swaps elements at indices $i$ and $j$.

The behavior of the algorithm is defined by the following recurrence relation:

$$
H(\ell, r) = 
\begin{cases} 
\text{id} & \text{if } \ell \ge r \\
H(\ell + 1, r - 1) \circ \tau(S, \ell, r) & \text{if } \ell < r 
\end{cases}
$$

**Invariant:**
At any depth $k$ of the recursion (where $k=0$ is the initial call), the state of the sequence $S^{(k)}$ satisfies:
1. For all $i < \ell_k$ and $i > r_k$, the elements are already in their target positions: $s_i = s_{n-1-i}$.
2. The sub-segment $S[\ell_k \dots r_k]$ is the original sub-segment $S[\ell_k \dots r_k]$ with its elements permuted such that the remaining reversals are yet to be performed.

The base case $\ell \ge r$ terminates the recursion, ensuring that the sequence $S$ has been transformed into $S'$ where $s'_i = s_{n-1-i}$ for all $i \in \{0, \dots, n-1\}$.

## 3. Complexity Analysis

### Time Complexity
The time complexity $T(n)$ is determined by the number of recursive calls. Each call performs a constant-time transposition $\tau$ and a constant-time comparison. 

The recurrence relation for the number of operations is:
$$T(n) = T(n-2) + \Theta(1)$$
With base cases $T(0) = \Theta(1)$ and $T(1) = \Theta(1)$.

Expanding the recurrence:
$$T(n) = \sum_{i=0}^{\lfloor n/2 \rfloor} \Theta(1) = \Theta\left(\frac{n}{2}\right) = O(n)$$
Thus, the time complexity is linear with respect to the input size $n$.

### Space Complexity
The space complexity $S(n)$ is determined by the maximum depth of the recursion stack. Each recursive call adds a new frame to the call stack, storing the local variables $(\ell, r)$ and the return address.

The depth of the recursion $D(n)$ is defined by the number of steps until the base case $\ell \ge r$ is reached:
$$D(n) = \left\lceil \frac{n}{2} \right\rceil$$

Since each stack frame consumes $\Theta(1)$ auxiliary space, the total auxiliary space complexity is:
$$S(n) = D(n) \cdot \Theta(1) = \Theta(n)$$

In the absence of Tail-Call Optimization (TCO), the space complexity is strictly $O(n)$. If TCO were implemented, the compiler would transform the recursion into an iterative process, reducing the auxiliary space complexity to $O(1)$. However, per the problem constraints and standard execution environments (e.g., CPython), the space complexity remains $O(n)$.