# Formal Mathematical Specification: Find Median from Data Stream

## 1. Definitions and Notation

Let $\mathcal{S} = \{x_1, x_2, \dots, x_n\}$ be a sequence of integers arriving from a stream, where $n$ denotes the number of elements processed at time $t$. Let $\mathcal{S}_{(1)} \le \mathcal{S}_{(2)} \le \dots \le \mathcal{S}_{(n)}$ denote the ordered permutation of the multiset $\mathcal{S}$.

The median $M$ of the multiset $\mathcal{S}$ is defined as:
$$M = \begin{cases} \mathcal{S}_{(\frac{n+1}{2})} & \text{if } n \text{ is odd} \\ \frac{1}{2} \left( \mathcal{S}_{(\frac{n}{2})} + \mathcal{S}_{(\frac{n}{2} + 1)} \right) & \text{if } n \text{ is even} \end{cases}$$

We define two disjoint sets, $L$ (the "lower" half) and $R$ (the "upper" half), such that $L \cup R = \mathcal{S}$ and $L \cap R = \emptyset$. These sets are maintained via two priority queues:
1. $H_{max}$: A max-heap storing elements of $L$, where $\forall l \in L, l \le \max(L)$.
2. $H_{min}$: A min-heap storing elements of $R$, where $\forall r \in R, r \ge \min(R)$.

## 2. Algebraic Characterization

The correctness of the algorithm is governed by the following three invariants maintained after each operation:

**I. Value Integrity:**
$$\forall l \in L, \forall r \in R : l \le r$$
This implies that $\max(L) \le \min(R)$.

**II. Size Balance:**
The cardinality of the sets must satisfy:
$$|L| = |R| \quad \text{or} \quad |L| = |R| + 1$$
This ensures that the median is always accessible via the roots of the heaps.

**III. Median Extraction:**
Given the invariants, the median $M$ is computed as:
$$M = \begin{cases} \text{root}(H_{max}) & \text{if } |L| > |R| \\ \frac{\text{root}(H_{max}) + \text{root}(H_{min})}{2} & \text{if } |L| = |R| \end{cases}$$

**State Transition for `addNum(x)`:**
Let $L_i, R_i$ be the states before insertion. The transition follows:
1. Temporary insertion: $L' \leftarrow L \cup \{x\}$ (if $x \le \max(L)$) else $R \cup \{x\}$.
2. Balancing: If $|L'| > |R'| + 1$, move $\max(L')$ to $R'$. If $|R'| > |L'|$, move $\min(R')$ to $L'$.
This ensures the size balance invariant is restored in $O(\log n)$ time.

## 3. Complexity Analysis

### Time Complexity
Let $T_{push}(k)$ and $T_{pop}(k)$ be the time complexity of heap operations for a heap of size $k$. For a binary heap, $T_{push}, T_{pop} = \Theta(\log k)$.

The `addNum` operation performs a constant number of heap operations (at most 2 pushes and 2 pops). Thus, the total time complexity per insertion is:
$$T_{add} = O(\log |L|) + O(\log |R|) = O(\log n)$$
The `findMedian` operation performs a constant number of root accesses:
$$T_{find} = \Theta(1)$$
The amortized time complexity over $N$ operations is $O(N \log N)$.

### Space Complexity
The algorithm stores each element of the stream exactly once in either $H_{max}$ or $H_{min}$. 
Let $S_{heap}(k)$ be the space required for a heap of $k$ elements, which is $\Theta(k)$.
The total space complexity is:
$$S_{total} = S(H_{max}) + S(H_{min}) = \Theta(|L|) + \Theta(|R|) = \Theta(n)$$
where $n$ is the total number of elements processed. The auxiliary space (excluding the input storage) is also $\Theta(n)$ as the heaps must persist to maintain the median state.