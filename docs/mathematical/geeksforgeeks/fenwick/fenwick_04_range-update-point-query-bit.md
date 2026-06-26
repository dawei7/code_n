# Formal Mathematical Specification: Range Update, Point Query (BIT)

## 1. Definitions and Notation

Let $A = [a_0, a_1, \dots, a_{n-1}]$ be an array of $n$ elements, initially $a_i = 0$ for all $i \in \{0, \dots, n-1\}$. We define the **difference array** $D = [d_0, d_1, \dots, d_{n-1}]$ such that:
$$d_i = a_i - a_{i-1} \quad \text{for } i > 0, \quad \text{and } d_0 = a_0$$
By the Fundamental Theorem of Calculus for discrete sequences (the telescoping sum property), any element $a_k$ can be recovered from the prefix sum of $D$:
$$a_k = \sum_{i=0}^{k} d_i$$

The Fenwick Tree (Binary Indexed Tree) is a data structure $\mathcal{B}$ that maintains an array $B$ of size $n+1$ to store partial sums of $D$. The mapping between the index $i$ (0-indexed) and the BIT index $j$ (1-indexed) is given by $j = i + 1$. The BIT supports two primary operations:
1. $\text{update}(i, \delta)$: Modifies $d_i$ by adding $\delta$, which propagates to all $B_j$ covering index $i$.
2. $\text{query}(k)$: Computes the prefix sum $\sum_{i=0}^{k} d_i$.

## 2. Algebraic Characterization

### Range Update
A range update operation $\text{range\_update}(L, R, \Delta)$ modifies the logical array $A$ such that $a_i \leftarrow a_i + \Delta$ for all $i \in [L, R]$. In terms of the difference array $D$, this transformation is:
$$d_L' = d_L + \Delta$$
$$d_{R+1}' = d_{R+1} - \Delta$$
For all $k \notin \{L, R+1\}$, $d_k' = d_k$. 

The correctness follows from the prefix sum property:
- For $k < L$: $\sum_{i=0}^k d_i' = \sum_{i=0}^k d_i = a_k$ (Unchanged).
- For $L \le k \le R$: $\sum_{i=0}^k d_i' = (\sum_{i=0}^k d_i) + \Delta = a_k + \Delta$.
- For $k > R$: $\sum_{i=0}^k d_i' = (\sum_{i=0}^k d_i) + \Delta - \Delta = a_k$ (Unchanged).

### Point Query
The point query $\text{point\_query}(k)$ is defined as the evaluation of the prefix sum of the difference array:
$$\text{point\_query}(k) = \sum_{j=1}^{k+1} B_j$$
where $B_j$ stores the sum of a specific range of $D$ determined by the least significant bit (LSB) of $j$, denoted $\text{lsb}(j) = j \& -j$. Specifically, $B_j = \sum_{i=j-\text{lsb}(j)+1}^{j} d_{i-1}$.

## 3. Complexity Analysis

### Time Complexity
Let $N$ be the number of elements.
- **Update:** The `update` operation traverses the BIT by adding $\text{lsb}(j)$ to the index $j$. Since $j \le N+1$, the number of iterations is bounded by the number of bits in $N$, which is $\lfloor \log_2 N \rfloor + 1$. Thus, each `update` is $O(\log N)$. A `range_update` performs exactly two `update` calls, maintaining $O(2 \log N) = O(\log N)$.
- **Query:** The `query` operation traverses the BIT by subtracting $\text{lsb}(j)$ from $j$. Similarly, this visits at most $\lfloor \log_2 N \rfloor + 1$ nodes. Thus, `point_query` is $O(\log N)$.

The total time complexity for $M$ operations is $O(M \log N)$.

### Space Complexity
The algorithm requires an auxiliary array $B$ of size $N+1$ to store the BIT structure.
- **Auxiliary Space:** $O(N)$ to store the BIT nodes.
- **Total Space:** $O(N)$, as the input array $A$ is implicitly represented by the difference array stored within the BIT. No additional data structures proportional to the number of operations are required.