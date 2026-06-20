# Formal Mathematical Specification: Minimum Coins (Greedy Variant)

## 1. Definitions and Notation

Let $\mathcal{D} = \{d_1, d_2, \dots, d_n\}$ be a set of coin denominations such that $d_i \in \mathbb{Z}^+$ and $d_1 > d_2 > \dots > d_n$. Without loss of generality, we assume $d_n = 1$ to ensure the existence of a solution for any target value $V \in \mathbb{Z}_{\ge 0}$.

*   **Target Value:** $V \in \mathbb{Z}_{\ge 0}$, the total amount to be represented.
*   **Denomination Set:** $\mathcal{D} \subset \mathbb{Z}^+$, ordered such that $d_1 > d_2 > \dots > d_n$.
*   **Solution Vector:** Let $\mathbf{x} = (x_1, x_2, \dots, x_n)$ be a vector where $x_i \in \mathbb{Z}_{\ge 0}$ represents the count of coins of denomination $d_i$ used.
*   **Objective Function:** We seek to minimize the total number of coins $f(\mathbf{x}) = \sum_{i=1}^n x_i$, subject to the constraint:
    $$\sum_{i=1}^n x_i \cdot d_i = V$$

## 2. Algebraic Characterization

The greedy approach constructs the solution vector $\mathbf{x}$ by iteratively applying the division algorithm. For each denomination $d_i$, we determine the maximum number of coins $x_i$ such that the remaining value is non-negative.

### The Greedy Transition
For each $i \in \{1, \dots, n\}$, let $R_i$ be the remaining value before considering denomination $d_i$, where $R_1 = V$. The greedy choice is defined by the recurrence:
$$x_i = \left\lfloor \frac{R_i}{d_i} \right\rfloor$$
$$R_{i+1} = R_i \pmod{d_i} = R_i - x_i \cdot d_i$$

The algorithm terminates when $R_{n+1} = 0$. The total number of coins is given by:
$$N = \sum_{i=1}^n \left\lfloor \frac{R_i}{d_i} \right\rfloor$$

### The Canonical Condition
The greedy strategy is optimal if and only if the set $\mathcal{D}$ is **canonical**. A set $\mathcal{D}$ is canonical if the greedy algorithm produces the optimal solution for all $V \in \mathbb{Z}^+$. Mathematically, this requires that for any $V$, the greedy solution $\mathbf{x}^G$ satisfies:
$$f(\mathbf{x}^G) = \min \left\{ \sum x_i \mid \sum x_i d_i = V, x_i \in \mathbb{Z}_{\ge 0} \right\}$$
If $\mathcal{D}$ is non-canonical, there exists at least one $V$ such that the greedy choice at some step $i$ prevents the global optimum, necessitating a dynamic programming approach where the state space is defined by the Bellman equation:
$$OPT(v) = 1 + \min_{d \in \mathcal{D}, d \le v} \{ OPT(v - d) \}$$

## 3. Complexity Analysis

### Time Complexity
The algorithm iterates through the set of denominations $\mathcal{D}$ exactly once. For each denomination $d_i$, the operations performed are:
1.  **Integer Division:** $\lfloor R_i / d_i \rfloor$
2.  **Modulo Operation:** $R_i \pmod{d_i}$

Assuming standard arithmetic operations on fixed-width integers take $O(1)$ time, the total time complexity is:
$$T(n) = \sum_{i=1}^n \Theta(1) = \Theta(n)$$
Where $n = |\mathcal{D}|$. Since the denominations are processed in a single pass, the complexity is linear with respect to the number of available denominations, $O(n)$. In practical currency systems where $n$ is a small constant, this is effectively $O(1)$.

### Space Complexity
*   **Auxiliary Space:** The algorithm maintains only a few scalar variables ($count$, $amount$, $R_i$), which occupy $O(1)$ space.
*   **Total Space:** If the algorithm returns only the integer count of coins, the space complexity is $O(1)$. If the algorithm is required to return the solution vector $\mathbf{x}$ (the list of coins used), the space complexity is $O(k)$, where $k = \sum x_i$ is the total number of coins dispensed. Given the greedy constraint, $k$ is bounded by $V/d_n = V$, thus the space complexity is $O(V)$ in the worst case for output storage.