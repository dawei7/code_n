# Formal Mathematical Specification: Tower of Hanoi

## 1. Definitions and Notation

Let $N \in \mathbb{N}^+$ denote the number of disks, where each disk $d \in \{1, 2, \dots, N\}$ is assigned a unique size such that $d_i < d_j$ if $i < j$. 

We define the state space $\mathcal{S}$ as the set of all valid configurations of disks on three rods, denoted by the set $\mathcal{R} = \{S, D, A\}$ (Source, Destination, Auxiliary). A configuration is a mapping $f: \{1, \dots, N\} \to \mathcal{R}$ such that for any rod $r \in \mathcal{R}$, the disks assigned to $r$ are ordered by size, satisfying the constraint that if $d_i, d_j \in r$ and $i < j$, then $d_i$ must be placed above $d_j$.

- **Input:** An integer $N$ and a permutation of rods $(src, dst, aux) \in \mathcal{R}^3$.
- **Output:** A sequence of moves $M = (m_1, m_2, \dots, m_k)$, where each $m_i = (r_{from}, r_{to})$ represents the transfer of the smallest disk on rod $r_{from}$ to rod $r_{to}$.
- **Constraint:** For any move $(r_{from}, r_{to})$, the disk $d_{top}$ moved must satisfy $d_{top} < d_{target}$, where $d_{target}$ is the current top disk on $r_{to}$ (or $d_{target} = \infty$ if $r_{to}$ is empty).

## 2. Algebraic Characterization

The Tower of Hanoi is governed by a recursive functional equation. Let $H(n, src, dst, aux)$ be the sequence of moves required to transfer a stack of $n$ disks from $src$ to $dst$ using $aux$ as an intermediary.

The algorithm is defined by the following recursive decomposition:

$$
H(n, src, dst, aux) = 
\begin{cases} 
\emptyset & \text{if } n = 0 \\
H(n-1, src, aux, dst) \oplus \{(src, dst)\} \oplus H(n-1, aux, dst, src) & \text{if } n > 0 
\end{cases}
$$

where $\oplus$ denotes the concatenation of move sequences. 

**Correctness Invariant:**
For any $n$, the sequence $H(n, src, dst, aux)$ preserves the property that at no point is a larger disk placed upon a smaller disk. By induction, if $H(n-1)$ is valid, then $H(n)$ is valid because:
1. The $n-1$ disks are moved to $aux$, leaving disk $n$ (the largest) free.
2. Disk $n$ is moved to $dst$, which is empty or contains only disks $> n$.
3. The $n-1$ disks are moved from $aux$ to $dst$, where they are placed on top of disk $n$, maintaining the size-ordering invariant.

## 3. Complexity Analysis

### Time Complexity
Let $T(n)$ be the number of moves required to solve the problem for $n$ disks. From the recurrence relation defined in Section 2, we obtain the linear non-homogeneous recurrence:
$$T(n) = 2T(n-1) + 1, \quad T(1) = 1$$

Using the method of iteration or the characteristic equation:
$$T(n) + 1 = 2(T(n-1) + 1)$$
Let $S(n) = T(n) + 1$. Then $S(n) = 2S(n-1)$ with $S(1) = 2$.
This is a geometric progression $S(n) = 2^n$.
Thus, $T(n) = 2^n - 1$.

Since each move requires constant time $O(1)$ to print or store, the total time complexity is:
$$T(n) = \Theta(2^n) = O(2^n)$$

### Space Complexity
The space complexity is determined by the maximum depth of the recursion stack. 
- **Stack Space:** The function $H(n, \dots)$ calls $H(n-1, \dots)$ before returning. The depth of the recursion tree is $N$. Thus, the auxiliary stack space is $O(N)$.
- **Output Space:** If the sequence of moves is stored in memory, the space required is $O(2^N)$ to hold the $2^N - 1$ moves. However, in standard algorithmic analysis, we consider the auxiliary space required for the execution of the algorithm, which is $O(N)$.

Therefore, the auxiliary space complexity is $O(N)$.