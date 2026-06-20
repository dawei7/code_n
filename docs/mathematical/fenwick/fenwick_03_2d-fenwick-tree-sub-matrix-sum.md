# Formal Mathematical Specification: 2D Fenwick Tree (Sub-matrix Sum)

## 1. Definitions and Notation

Let $A$ be a matrix of dimensions $N \times M$ over a field $\mathbb{F}$ (typically $\mathbb{R}$ or $\mathbb{Z}$), where $A_{i,j}$ denotes the element at row $i$ and column $j$, for $1 \le i \le N$ and $1 \le j \le M$.

We define the **2D Fenwick Tree** (or Binary Indexed Tree) as a data structure represented by a matrix $T$ of dimensions $(N+1) \times (M+1)$, where $T_{i,j} \in \mathbb{F}$. The structure is governed by the function $L(k) = k \& -k$, which returns the value of the least significant bit of $k$.

- **Point Update:** An operation $\text{update}(r, c, \delta)$ modifies $A_{r,c} \leftarrow A_{r,c} + \delta$ and propagates the change to $T$.
- **Prefix Sum:** A function $S(r, c) = \sum_{i=1}^r \sum_{j=1}^c A_{i,j}$ representing the sum of the rectangular region $[1, r] \times [1, c]$.
- **Range Query:** A function $Q(r_1, c_1, r_2, c_2)$ returning the sum of the sub-matrix defined by the top-left corner $(r_1, c_1)$ and bottom-right corner $(r_2, c_2)$.

## 2. Algebraic Characterization

The 2D Fenwick Tree $T$ stores partial sums such that each entry $T_{i,j}$ maintains the sum of a sub-rectangle of $A$ with dimensions $L(i) \times L(j)$. Specifically:
$$T_{i,j} = \sum_{x=i-L(i)+1}^{i} \sum_{y=j-L(j)+1}^{j} A_{x,y}$$

### Prefix Sum Invariant
The prefix sum $S(r, c)$ is computed by aggregating non-overlapping sub-rectangles stored in $T$:
$$S(r, c) = \sum_{i \in \text{path}(r)} \sum_{j \in \text{path}(c)} T_{i,j}$$
where the path is defined by the sequence $p_0 = k, p_{m+1} = p_m - L(p_m)$ until $p_m = 0$.

### Range Query via Inclusion-Exclusion
The sum of the sub-matrix $A[r_1 \dots r_2][c_1 \dots c_2]$ is derived from the Principle of Inclusion-Exclusion:
$$Q(r_1, c_1, r_2, c_2) = S(r_2, c_2) - S(r_1-1, c_2) - S(r_2, c_1-1) + S(r_1-1, c_1-1)$$

### Update Transition
For an update $\delta$ at $(r, c)$, the structure maintains the invariant by updating all $T_{i,j}$ such that the range covered by $T_{i,j}$ includes $(r, c)$:
$$T_{i,j} \leftarrow T_{i,j} + \delta, \quad \text{for } i \in \{r, r+L(r), \dots \le N\}, j \in \{c, c+L(c), \dots \le M\}$$

## 3. Complexity Analysis

### Time Complexity
- **Update Operation:** The update traverses indices $i$ and $j$ by adding the least significant bit. The number of iterations for a single dimension $N$ is bounded by the number of set bits, which is $\lfloor \log_2 N \rfloor + 1$. Given the nested structure, the total number of operations is:
  $$T_{\text{update}} = O(\log N \cdot \log M)$$
- **Query Operation:** Similarly, the prefix sum $S(r, c)$ traverses indices by subtracting the least significant bit. The number of steps is bounded by the bit-length of the indices:
  $$T_{\text{query}} = O(\log N \cdot \log M)$$
- **Range Query:** Since a range query consists of four constant-time calls to the prefix sum function, the complexity remains $O(\log N \cdot \log M)$.

### Space Complexity
The structure requires a 2D array $T$ of size $(N+1) \times (M+1)$ to store the partial sums.
- **Total Space:** $S(N, M) = (N+1)(M+1) \in \Theta(NM)$.
- **Auxiliary Space:** The algorithm operates in-place on the structure $T$, requiring $O(1)$ additional space beyond the storage of the tree itself.