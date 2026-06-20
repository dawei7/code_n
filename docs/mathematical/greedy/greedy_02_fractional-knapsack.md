# Formal Mathematical Specification: Fractional Knapsack Problem

## 1. Definitions and Notation

Let $n \in \mathbb{N}$ be the number of items available. Each item $i \in \{1, 2, \dots, n\}$ is characterized by a pair $(v_i, w_i)$, where $v_i \in \mathbb{R}^+$ is the value and $w_i \in \mathbb{R}^+$ is the weight of the item. Let $W \in \mathbb{R}^+$ denote the total weight capacity of the knapsack.

We define the **density** (or value-to-weight ratio) of item $i$ as:
$$\rho_i = \frac{v_i}{w_i}$$

The objective is to determine a vector of fractions $x = (x_1, x_2, \dots, x_n)$, where $x_i \in [0, 1]$ represents the proportion of item $i$ included in the knapsack. The state space $\mathcal{S}$ is the set of all feasible vectors $x$ satisfying the capacity constraint:
$$\mathcal{S} = \left\{ x \in \mathbb{R}^n : 0 \le x_i \le 1, \forall i \in \{1, \dots, n\} \text{ and } \sum_{i=1}^n x_i w_i \le W \right\}$$

The goal is to maximize the objective function $f(x)$:
$$f(x) = \sum_{i=1}^n x_i v_i$$

## 2. Algebraic Characterization

The Fractional Knapsack Problem is a linear programming problem. By the **Greedy Choice Property**, an optimal solution can be constructed by prioritizing items with the highest density.

Let $\pi$ be a permutation of the set $\{1, \dots, n\}$ such that the densities are ordered non-increasingly:
$$\rho_{\pi(1)} \ge \rho_{\pi(2)} \ge \dots \ge \rho_{\pi(n)}$$

Let $k$ be the critical index such that:
$$\sum_{i=1}^{k-1} w_{\pi(i)} \le W < \sum_{i=1}^{k} w_{\pi(i)}$$

The optimal solution $x^*$ is defined as:
$$x^*_{\pi(i)} = \begin{cases} 1 & \text{if } i < k \\ \frac{W - \sum_{j=1}^{k-1} w_{\pi(j)}}{w_{\pi(k)}} & \text{if } i = k \\ 0 & \text{if } i > k \end{cases}$$

**Correctness (Exchange Argument):**
Suppose there exists an optimal solution $x$ that does not follow the greedy order. If there exist $i, j$ such that $\rho_i > \rho_j$ but $x_i < 1$ and $x_j > 0$, we can construct a new solution $x'$ by increasing $x_i$ by $\epsilon$ and decreasing $x_j$ by $\epsilon \frac{w_i}{w_j}$ such that the total weight remains constant. The change in total value is $\Delta V = \epsilon v_i - (\epsilon \frac{w_i}{w_j}) v_j = \epsilon w_i (\rho_i - \rho_j)$. Since $\rho_i > \rho_j$, $\Delta V > 0$, contradicting the optimality of $x$.

## 3. Complexity Analysis

### Time Complexity
The algorithm consists of two primary phases:
1. **Sorting:** We compute $\rho_i$ for all $n$ items and sort them. Using an efficient comparison-based sort (e.g., Timsort or Quicksort), the time complexity is $T_{sort}(n) = \Theta(n \log n)$.
2. **Linear Scan:** We iterate through the sorted items at most once. This phase performs $n$ constant-time operations, yielding $T_{scan}(n) = \Theta(n)$.

The total time complexity is:
$$T(n) = T_{sort}(n) + T_{scan}(n) = \Theta(n \log n) + \Theta(n) = O(n \log n)$$

### Space Complexity
The space complexity depends on the implementation of the sorting algorithm and the storage of the indices:
1. **Auxiliary Space:** We require an array of indices or pointers of size $n$ to maintain the sorted order without mutating the original input, resulting in $S(n) = O(n)$.
2. **In-place Sorting:** If the input array is mutable and can be sorted in-place, the auxiliary space complexity is $S(n) = O(1)$ (assuming the sorting algorithm uses $O(1)$ or $O(\log n)$ stack space).

Thus, the total space complexity is $O(n)$ in the general case, or $O(1)$ under strict in-place constraints.