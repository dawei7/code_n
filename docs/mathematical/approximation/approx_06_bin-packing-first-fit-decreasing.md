# Formal Mathematical Specification: Bin Packing (First Fit Decreasing)

## 1. Definitions and Notation

Let the Bin Packing Problem (BPP) be defined over a finite set of items and an unlimited supply of homogeneous bins. We formalize the inputs, outputs, and state spaces as follows:

### 1.1 Input Space
*   **Item Set:** Let $I = \{1, 2, \dots, n\}$ be the set of item indices, where $n \in \mathbb{N}$ represents the total number of items.
*   **Capacity:** Let $C \in \mathbb{R}^+$ denote the maximum capacity of each bin. Without loss of generality, the problem can be normalized such that $C = 1$.
*   **Weights:** Let $W = (w_1, w_2, \dots, w_n)$ be a sequence of item weights, where each $w_i \in (0, C]$ for all $i \in I$.

### 1.2 Output Space
The output is a partition of $I$ into $m$ disjoint subsets representing the bins, along with the cardinality $m$.
*   **Bin Partition:** Let $\mathcal{B} = \{B_1, B_2, \dots, B_m\}$ be a family of subsets of $I$ satisfying:
    1.  **Disjointness:** $B_k \cap B_l = \emptyset \quad \forall k \neq l$.
    2.  **Completeness:** $\bigcup_{k=1}^m B_k = I$.
    3.  **Capacity Constraint:** $\sum_{i \in B_k} w_i \le C \quad \forall k \in \{1, \dots, m\}$.
*   **Objective:** Minimize the number of active bins $m = |\mathcal{B}|$.

### 1.3 State Space of the FFD Dynamical System
Let $\mathcal{S}$ denote the state space of the algorithm during execution. At step $j \in \{0, 1, \dots, n\}$, the state is represented by the tuple $S_j = (m_j, R_j)$, where:
*   $m_j \in \{0, \dots, j\}$ is the number of currently open bins.
*   $R_j = (R_{j, 1}, R_{j, 2}, \dots, R_{j, m_j})$ is an ordered sequence of remaining capacities for each open bin, where $R_{j, k} \in [0, C]$ for all $k \in \{1, \dots, m_j\}$.
*   The initial state is defined as $S_0 = (0, \emptyset)$.

---

## 2. Algebraic Characterization

The First Fit Decreasing (FFD) algorithm operates in two distinct phases: a sorting phase and an iterative greedy placement phase governed by a deterministic transition function.

### 2.1 Sorting Phase
Let $\pi: I \to I$ be a permutation of the item indices that sorts the weights in non-increasing order. We define the sorted weight sequence $X = (x_1, x_2, \dots, x_n)$ such that:
$$x_j = w_{\pi(j)} \quad \forall j \in \{1, \dots, n\}$$
where
$$x_1 \ge x_2 \ge \dots \ge x_n$$

### 2.2 Transition Function (First Fit Decision Rule)
For each sorted item $j \in \{1, \dots, n\}$ with weight $x_j$, we define the target bin index $k^*(j)$ using the selection function:
$$k^*(j) = \min \left( \{ k \in \{1, \dots, m_{j-1}\} \mid R_{j-1, k} \ge x_j \} \cup \{ m_{j-1} + 1 \} \right)$$

This selection rule guarantees that the item is placed into the lowest-indexed bin that has sufficient residual capacity. If no such bin exists, a new bin is initialized.

### 2.3 State Update Equations
Given the state $S_{j-1} = (m_{j-1}, R_{j-1})$ and the decision $k^* = k^*(j)$, the state transitions to $S_j = (m_j, R_j)$ according to the following recurrence relations:

#### Case 1: Placement in an existing bin ($k^* \le m_{j-1}$)
$$m_j = m_{j-1}$$
$$R_{j, k} = \begin{cases} 
R_{j-1, k} - x_j & \text{if } k = k^* \\ 
R_{j-1, k} & \text{if } k \neq k^* 
\end{cases} \quad \forall k \in \{1, \dots, m_j\}$$

#### Case 2: Initialization of a new bin ($k^* = m_{j-1} + 1$)
$$m_j = m_{j-1} + 1$$
$$R_{j, k} = \begin{cases} 
R_{j-1, k} & \text{if } k \le m_{j-1} \\ 
C - x_j & \text{if } k = m_j 
\end{cases}$$

### 2.4 Loop Invariants
The correctness and structural properties of the FFD algorithm are preserved by the following invariants, which hold for all steps $j \in \{1, \dots, n\}$:

1.  **Feasibility Invariant:**
    $$\forall k \in \{1, \dots, m_j\}, \quad R_{j, k} \ge 0$$
2.  **Conservation of Mass:**
    $$\sum_{k=1}^{m_j} (C - R_{j, k}) = \sum_{i=1}^j x_i$$
3.  **First-Fit Minimality:**
    $$\forall k < k^*(j), \quad R_{j-1, k} < x_j$$
    *(No bin preceding the chosen bin has enough space to accommodate the current item).*

### 2.5 Approximation Bounds
Let $\text{FFD}(I)$ denote the number of bins produced by the FFD algorithm on instance $I$, and let $\text{OPT}(I)$ denote the optimal number of bins. 

#### Theorem (Dósa, 2007)
For any instance $I$ of the Bin Packing Problem:
$$\text{FFD}(I) \le \frac{11}{9} \text{OPT}(I) + \frac{6}{9}$$

Furthermore, this bound is tight. There exist instances where:
$$\text{FFD}(I) = \left\lfloor \frac{11}{9} \text{OPT}(I) \right\rfloor$$

---

## 3. Complexity Analysis

### 3.1 Time Complexity

The total time complexity of the FFD algorithm is determined by the sum of the work done in the sorting phase and the placement phase:
$$T(n) = T_{\text{sort}}(n) + T_{\text{place}}(n)$$

#### 1. Sorting Phase
Sorting $n$ scalar weights using a comparison-based sorting algorithm (e.g., Mergesort or Heapsort) requires:
$$T_{\text{sort}}(n) = \Theta(n \log n)$$

#### 2. Placement Phase (Naive Linear Scan)
In the standard implementation, finding $k^*(j)$ involves a sequential scan over the existing $m_{j-1}$ bins.
*   **Worst-Case Analysis:** In the worst case, every item requires opening a new bin (e.g., when $w_i > \frac{C}{2}$ for all $i$). The number of active bins at step $j$ is $j-1$. The total number of comparisons is:
    $$T_{\text{place}}(n) = \sum_{j=1}^n O(m_{j-1}) = \sum_{j=1}^n O(j) = O(n^2)$$
*   **Average-Case Analysis:** Under uniform distribution of weights, the expected number of bins scanned per item remains $O(n)$, yielding an average-case complexity of $O(n^2)$.

#### 3. Placement Phase (Optimized Segment Tree)
To achieve the required $O(n \log n)$ complexity, we can represent the bin capacities using a balanced Segment Tree (or Range Maximum Query tree) of size $n$.
*   **Structure:** Let the leaves of the segment tree represent the remaining capacities of the bins $B_1, B_2, \dots, B_n$, initialized to $C$. Each internal node $u$ stores the maximum remaining capacity of its children:
    $$\text{val}(u) = \max(\text{val}(\text{left}(u)), \text{val}(\text{right}(u)))$$
*   **Query and Update:** To place item $x_j$, we traverse the tree to find the leftmost leaf node $k$ such that $\text{val}(k) \ge x_j$.
    *   If $\text{val}(\text{left}(u)) \ge x_j$, we recursively traverse the left child.
    *   Otherwise, we traverse the right child.
    *   Once the leaf $k$ is identified, we update its value: $R_k \leftarrow R_k - x_j$, and propagate the changes back to the root.
*   **Complexity:** Since the height of the segment tree is $\lceil \log_2 n \rceil$, both the search and update operations take $O(\log n)$ time.
    $$T_{\text{place}}(n) = \sum_{j=1}^n O(\log n) = O(n \log n)$$

#### Total Time Complexity
Using the segment tree optimization:
$$T(n) = \Theta(n \log n) + O(n \log n) = \Theta(n \log n)$$

### 3.2 Space Complexity

#### 1. Auxiliary Space
*   **Sorting:** In-place sorting algorithms require $O(\log n)$ auxiliary stack space, while stable mergesort requires $O(n)$ space.
*   **Bin Representation:** 
    *   The naive array representation of bin capacities requires $O(m) \le O(n)$ space.
    *   The segment tree representation requires a tree of size $2^{\lceil \log_2 n \rceil + 1} - 1 \approx 4n$ nodes, which is $O(n)$ space.
*   Therefore, the auxiliary space complexity is:
    $$S_{\text{aux}}(n) = \Theta(n)$$

#### 2. Total Space
Including the input storage for the weights $W$, the total space complexity is:
$$S_{\text{total}}(n) = \Theta(n)$$