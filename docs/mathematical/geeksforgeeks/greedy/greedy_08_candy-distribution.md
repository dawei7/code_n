# Formal Mathematical Specification: Candy Distribution Problem

## 1. Definitions and Notation

Let $R = \langle r_0, r_1, \dots, r_{n-1} \rangle$ be a sequence of ratings, where $r_i \in \mathbb{Z}^+$ represents the rating of the $i$-th child. The set of children is indexed by $I = \{0, 1, \dots, n-1\}$.

We define a distribution function $C: I \to \mathbb{Z}^+$, where $C(i)$ denotes the number of candies assigned to child $i$. The objective is to find a function $C$ that minimizes the total sum $S = \sum_{i=0}^{n-1} C(i)$, subject to the following constraints:

1. **Positivity Constraint:** $\forall i \in I, C(i) \geq 1$.
2. **Local Monotonicity Constraint:** 
   - If $r_i > r_{i-1}$, then $C(i) > C(i-1)$ for $i \in \{1, \dots, n-1\}$.
   - If $r_i > r_{i+1}$, then $C(i) > C(i+1)$ for $i \in \{0, \dots, n-2\}$.

The state space $\mathcal{S}$ is the set of all vectors $\mathbf{c} \in (\mathbb{Z}^+)^n$ satisfying the above constraints. We seek $\mathbf{c}^* = \arg \min_{\mathbf{c} \in \mathcal{S}} \sum_{i=0}^{n-1} c_i$.

## 2. Algebraic Characterization

To solve for $\mathbf{c}^*$, we decompose the constraints into two independent directional passes. Let $L_i$ be the minimum candies required to satisfy the left-neighbor constraint, and $R_i$ be the minimum candies required to satisfy the right-neighbor constraint.

### Pass 1: Left-to-Right Sweep
We define the sequence $L = \langle L_0, L_1, \dots, L_{n-1} \rangle$ via the recurrence:
$$L_0 = 1$$
$$L_i = \begin{cases} L_{i-1} + 1 & \text{if } r_i > r_{i-1} \\ 1 & \text{otherwise} \end{cases} \quad \text{for } i = 1, \dots, n-1$$

### Pass 2: Right-to-Left Sweep
We define the sequence $R = \langle R_0, R_1, \dots, R_{n-1} \rangle$ via the recurrence:
$$R_{n-1} = 1$$
$$R_i = \begin{cases} R_{i+1} + 1 & \text{if } r_i > r_{i+1} \\ 1 & \text{otherwise} \end{cases} \quad \text{for } i = n-2, \dots, 0$$

### Optimal Solution
The minimal candy distribution $C^*(i)$ is given by the pointwise maximum of the two directional constraints:
$$C^*(i) = \max(L_i, R_i)$$
The total minimum candies $S^*$ is:
$$S^* = \sum_{i=0}^{n-1} \max(L_i, R_i)$$

**Correctness Invariant:** For any $i$, $C^*(i)$ is the smallest integer satisfying both $C^*(i) > C^*(i-1)$ (if $r_i > r_{i-1}$) and $C^*(i) > C^*(i+1)$ (if $r_i > r_{i+1}$). Since $L_i$ and $R_i$ are the tightest lower bounds for their respective directions, their maximum is the tightest lower bound for the intersection of both constraints.

## 3. Complexity Analysis

### Time Complexity
The algorithm performs three distinct linear passes over the input array of size $n$:
1. The forward pass computes $L_i$ in $O(n)$ time, as each step $i$ involves a constant number of operations: $T_1 = \sum_{i=1}^{n-1} \Theta(1) = \Theta(n)$.
2. The backward pass computes $R_i$ and the running sum $S^*$ in $O(n)$ time: $T_2 = \sum_{i=n-2}^{0} \Theta(1) = \Theta(n)$.
3. The total time complexity is $T(n) = T_1 + T_2 = \Theta(n)$.

### Space Complexity
The algorithm requires the allocation of an auxiliary array `candies` of size $n$ to store the values of $L_i$ and subsequently update them to $C^*(i)$.
- The space required is $S(n) = \text{sizeof}(\text{int}) \times n$.
- Thus, the auxiliary space complexity is $O(n)$. 
- Total space complexity, including input storage, is $O(n)$.