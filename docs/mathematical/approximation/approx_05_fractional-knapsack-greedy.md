# Formal Mathematical Specification: Fractional Knapsack (Greedy Bound)

## 1. Definitions and Notation

The Fractional Knapsack Problem is a continuous optimization problem. We model the problem instance, the feasible region, and the objective function using the following mathematical formalisms.

### 1.1 Problem Instance
A problem instance is defined by a 4-tuple $\mathcal{P} = (I, \mathbf{v}, \mathbf{w}, W)$ where:
*   $I = \{1, 2, \dots, n\}$ is a finite set of $n \in \mathbb{N}^+$ items.
*   $\mathbf{v} = (v_1, v_2, \dots, v_n) \in (\mathbb{R}^+)^n$ is the vector of item values, where $v_i > 0$ represents the utility or value of item $i$.
*   $\mathbf{w} = (w_1, w_2, \dots, w_n) \in (\mathbb{R}^+)^n$ is the vector of item weights, where $w_i > 0$ represents the physical weight of item $i$.
*   $W \in \mathbb{R}_{\ge 0}$ is the maximum weight capacity of the knapsack.

### 1.2 Decision Variables and State Space
Unlike the 0-1 Knapsack problem where selection is binary, the fractional variant allows continuous partitioning of items. 
*   Let $\mathbf{x} = (x_1, x_2, \dots, x_n) \in [0, 1]^n$ be the allocation vector, where $x_i$ denotes the fraction of item $i$ placed in the knapsack.
*   The feasible region (or state space) $\mathcal{S}(W)$ is defined as the convex polytope:
    $$\mathcal{S}(W) = \left\{ \mathbf{x} \in [0, 1]^n \;\middle|\; \sum_{i=1}^n w_i x_i \le W \right\}$$

### 1.3 Objective Function
The objective is to maximize the total value of the selected fractions. We define the objective function $f: [0, 1]^n \to \mathbb{R}_{\ge 0}$ as:
$$f(\mathbf{x}) = \sum_{i=1}^n v_i x_i$$

The optimization problem is formulated as:
$$\text{Maximize } f(\mathbf{x}) \quad \text{subject to } \mathbf{x} \in \mathcal{S}(W)$$

### 1.4 Value Density (Efficiency)
For each item $i \in I$, we define its value density (or efficiency ratio) $r_i$ as:
$$r_i = \frac{v_i}{w_i}$$
The density $r_i \in \mathbb{R}^+$ represents the utility per unit weight of item $i$.

---

## 2. Algebraic Characterization and Correctness

The greedy algorithm solves this continuous optimization problem by sorting items in non-increasing order of their value densities.

### 2.1 Permutation and Sorting
Let $\pi: I \to I$ be a bijective mapping (permutation) that sorts the items by value density in non-increasing order:
$$r_{\pi(1)} \ge r_{\pi(2)} \ge \dots \ge r_{\pi(n)}$$

To simplify notation without loss of generality, we assume the items are pre-sorted such that:
$$\frac{v_1}{w_1} \ge \frac{v_2}{w_2} \ge \dots \ge \frac{v_n}{w_n}$$

### 2.2 The Greedy Allocation Rule
Let $k \in I \cup \{n+1\}$ be the critical index (often called the *split item* index) defined as:
$$k = \min \left\{ j \in I \;\middle|\; \sum_{i=1}^j w_i > W \right\}$$
If $\sum_{i=1}^n w_i \le W$, we define $k = n + 1$.

The greedy allocation vector $\mathbf{x}^g = (x_1^g, x_2^g, \dots, x_n^g)$ is defined algebraically as:
$$x_i^g = \begin{cases} 
1 & \text{if } i < k \\
\frac{W - \sum_{j=1}^{k-1} w_j}{w_k} & \text{if } i = k \\
0 & \text{if } i > k 
\end{cases}$$
If $k = n+1$, then $x_i^g = 1$ for all $i \in I$.

### 2.3 Proof of Optimality (Variational/Exchange Argument)
We prove that the greedy allocation $\mathbf{x}^g$ is globally optimal: $f(\mathbf{x}^g) \ge f(\mathbf{y})$ for any feasible $\mathbf{y} \in \mathcal{S}(W)$.

**Proof:**
Let $\mathbf{y} = (y_1, y_2, \dots, y_n) \in \mathcal{S}(W)$ be an arbitrary feasible solution. Consider the difference in their objective values:
$$f(\mathbf{x}^g) - f(\mathbf{y}) = \sum_{i=1}^n v_i (x_i^g - y_i) = \sum_{i=1}^n r_i w_i (x_i^g - y_i)$$

We analyze the terms of this sum relative to the critical index $k$:
1.  For $i < k$, we have $x_i^g = 1$. Since $y_i \in [0, 1]$, it follows that $x_i^g - y_i \ge 0$. By the sorted order, $r_i \ge r_k$. Thus:
    $$(r_i - r_k)(x_i^g - y_i) \ge 0$$
2.  For $i > k$, we have $x_i^g = 0$. Since $y_i \in [0, 1]$, it follows that $x_i^g - y_i \le 0$. By the sorted order, $r_i \le r_k$. Thus:
    $$(r_i - r_k)(x_i^g - y_i) \ge 0$$
3.  For $i = k$, the term $r_i - r_k = 0$, so trivially:
    $$(r_i - r_k)(x_i^g - y_i) = 0$$

Therefore, for all $i \in I$, we have the inequality:
$$(r_i - r_k) w_i (x_i^g - y_i) \ge 0$$

Now, we rewrite the objective difference by adding and subtracting $r_k \sum_{i=1}^n w_i (x_i^g - y_i)$:
$$\sum_{i=1}^n r_i w_i (x_i^g - y_i) = \sum_{i=1}^n (r_i - r_k) w_i (x_i^g - y_i) + r_k \sum_{i=1}^n w_i (x_i^g - y_i)$$

*   The first summation is non-negative because each term is non-negative:
    $$\sum_{i=1}^n (r_i - r_k) w_i (x_i^g - y_i) \ge 0$$
*   For the second term, if $k \le n$, the greedy solution completely fills the knapsack, meaning $\sum_{i=1}^n w_i x_i^g = W$. Since $\mathbf{y}$ is feasible, $\sum_{i=1}^n w_i y_i \le W$. Thus:
    $$\sum_{i=1}^n w_i (x_i^g - y_i) = W - \sum_{i=1}^n w_i y_i \ge 0$$
    Since $r_k > 0$, the second term is also non-negative. (If $k = n+1$, then $x_i^g = 1 \ge y_i$ for all $i$, making the inequality hold trivially).

Combining these results:
$$f(\mathbf{x}^g) - f(\mathbf{y}) \ge 0 \implies f(\mathbf{x}^g) \ge f(\mathbf{y})$$
Thus, the greedy allocation $\mathbf{x}^g$ is optimal. $\blacksquare$

### 2.4 State Transition and Loop Invariants
Let $j \in \{0, 1, \dots, n\}$ denote the loop iteration index. We define the state variables at step $j$:
*   $R^{(j)}$: Remaining capacity of the knapsack.
*   $T^{(j)}$: Accumulated value.

The recurrence relations governing the state transitions are:
$$R^{(0)} = W, \quad T^{(0)} = 0$$

For $j \ge 1$:
$$R^{(j)} = \max\left(0, R^{(j-1)} - w_{\pi(j)}\right)$$
$$T^{(j)} = T^{(j-1)} + v_{\pi(j)} \cdot \min\left(1, \frac{R^{(j-1)}}{w_{\pi(j)}}\right)$$

#### Loop Invariant
At the start of iteration $j$ (where $1 \le j \le n+1$):
1.  The remaining capacity is $R^{(j-1)} = W - \sum_{i=1}^{j-1} w_{\pi(i)} x_{\pi(i)}^g$.
2.  The accumulated value is $T^{(j-1)} = \sum_{i=1}^{j-1} v_{\pi(i)} x_{\pi(i)}^g$.
3.  The partial allocation $(x_{\pi(1)}^g, \dots, x_{\pi(j-1)}^g)$ is optimal for the subproblem containing only the first $j-1$ sorted items with capacity $W - R^{(j-1)}$.

---

## 3. Complexity Analysis

### 3.1 Time Complexity
The execution of the algorithm consists of two distinct phases: sorting and greedy selection.

#### Phase 1: Sorting
Computing the density ratios $r_i = \frac{v_i}{w_i}$ for all $i \in I$ requires $n$ divisions:
$$T_{\text{ratio}}(n) = \Theta(n)$$

Sorting the items based on these ratios using a comparison-based sorting algorithm (e.g., Mergesort or Heapsort) requires:
$$T_{\text{sort}}(n) = \Theta(n \log n)$$

#### Phase 2: Greedy Selection
The algorithm iterates through the sorted items. In each iteration $j$, it performs $O(1)$ operations:
*   A comparison: $w_{\pi(j)} \le R^{(j-1)}$
*   Arithmetic updates for $R^{(j)}$ and $T^{(j)}$.

In the worst case (where $\sum_{i=1}^n w_i \le W$), the loop runs $n$ times. Thus, the selection phase complexity is:
$$T_{\text{select}}(n) = O(n)$$

#### Total Time Complexity
Combining the phases, the total time complexity $T(n)$ is dominated by the sorting step:
$$T(n) = T_{\text{ratio}}(n) + T_{\text{sort}}(n) + T_{\text{select}}(n) = \Theta(n) + \Theta(n \log n) + O(n) = \Theta(n \log n)$$

#### Note on $O(n)$ Optimization
Using a selection algorithm (such as QuickSelect / Median-of-Medians) to find the split item $k$ without fully sorting the array allows the problem to be solved in:
$$T_{\text{opt}}(n) = \Theta(n) \text{ worst-case time.}$$

---

### 3.2 Space Complexity

#### Auxiliary Space
*   **Sorting:** If an in-place sorting algorithm (e.g., Heapsort) is used to sort the indices of the items, the auxiliary space is $O(1)$. If Mergesort is used, the auxiliary space is $O(n)$.
*   **State Variables:** The variables tracking the remaining capacity $R^{(j)}$, the accumulated value $T^{(j)}$, and the loop index $j$ require $O(1)$ auxiliary space.
*   **Ratio Storage:** Storing the computed ratios or sorted index mappings requires $O(n)$ auxiliary space.

Thus, the auxiliary space complexity is:
$$S_{\text{aux}}(n) = O(n)$$
(or $O(1)$ if we are permitted to modify the input arrays in-place and use an in-place sort).

#### Total Space Complexity
The input representation requires storing the vectors $\mathbf{v}$ and $\mathbf{w}$ of size $n$. Therefore, the total space complexity is:
$$S_{\text{total}}(n) = \Theta(n)$$