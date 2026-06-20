# Formal Mathematical Specification: Range Sum Query (Point Update)

## 1. Definitions and Notation

Let $A = [a_0, a_1, \dots, a_{n-1}]$ be an array of $n$ elements where $a_i \in \mathbb{R}$. We define a Fenwick Tree (Binary Indexed Tree) as an array $T$ of size $n+1$, where $T[i]$ stores the sum of a specific subset of elements from $A$.

*   **Index Mapping:** We define a bijection between the 0-indexed array $A$ and the 1-indexed tree $T$. The index $i \in \{1, \dots, n\}$ in $T$ corresponds to the range $(i - 2^{k} + 1, i]$, where $k$ is the number of trailing zeros in the binary representation of $i$.
*   **Lowest Set Bit (LSB):** We define the function $\text{lsb}(i) = i \& (-i)$, which extracts the value of the least significant bit of $i$. Mathematically, $\text{lsb}(i) = 2^{\nu_2(i)}$, where $\nu_2(i)$ is the 2-adic valuation of $i$.
*   **State Space:** The state of the system is defined by the tuple $(A, T)$. An update operation $U(i, \Delta)$ transforms $A \to A'$ and $T \to T'$, where $a'_i = a_i + \Delta$.
*   **Query Domain:** A range query is defined as a function $Q(l, r) = \sum_{k=l}^{r} a_k$, where $0 \le l \le r < n$.

## 2. Algebraic Characterization

The Fenwick Tree relies on the property that any integer $i \in [1, n]$ can be uniquely decomposed into a sum of powers of 2, corresponding to the disjoint intervals stored in $T$.

### Prefix Sum Construction
The prefix sum function $P(i) = \sum_{j=0}^{i-1} a_j$ is computed as:
$$P(i) = \sum_{k=0}^{\text{popcount}(i)-1} T[idx_k]$$
where $idx_0 = i$ and $idx_{k+1} = idx_k - \text{lsb}(idx_k)$, terminating when $idx_k = 0$.

### Point Update Transition
When an element $a_i$ is modified by $\Delta = a_{new} - a_{old}$, the update propagates through the tree to all nodes $j$ that cover index $i+1$. The update rule is:
$$T[j] \leftarrow T[j] + \Delta, \quad \text{for } j = (i+1), (i+1) + \text{lsb}(i+1), \dots, \le n$$
This ensures that the invariant $T[j] = \sum_{k=j-\text{lsb}(j)+1}^{j} a_{k-1}$ is maintained for all $j \in \{1, \dots, n\}$.

### Range Query Formulation
By the additive property of the prefix sum, the range sum is:
$$Q(l, r) = P(r+1) - P(l)$$
where $P(i)$ is the prefix sum of the first $i$ elements.

## 3. Complexity Analysis

### Time Complexity
The time complexity is governed by the number of bits in the index $n$.

*   **Query:** The `prefix(i)` operation traverses the tree by stripping the LSB at each step. The number of iterations is equal to the number of set bits in the binary representation of $i+1$, denoted by $\text{popcount}(i+1)$. Since $\text{popcount}(i+1) \le \lfloor \log_2(n) \rfloor + 1$, the query complexity is $O(\log n)$.
*   **Update:** The `update(i, delta)` operation traverses the tree by adding the LSB at each step. The number of nodes visited is bounded by the number of times we can add the LSB before exceeding $n$. This is equivalent to the number of bits that can be flipped from 0 to 1 in the binary representation of $i+1$, which is also bounded by $O(\log n)$.

Thus, both operations are strictly $O(\log n)$.

### Space Complexity
The Fenwick Tree $T$ requires an array of size $n+1$ to store the partial sums.
*   **Auxiliary Space:** $O(1)$ beyond the input storage.
*   **Total Space:** $O(n)$, as we maintain a linear mapping between the original array elements and the tree nodes.