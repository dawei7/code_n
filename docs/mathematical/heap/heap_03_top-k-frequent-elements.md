# Formal Mathematical Specification: Top K Frequent Elements

## 1. Definitions and Notation

Let $A = [a_1, a_2, \dots, a_N]$ be a sequence of $N$ integers drawn from a domain $\mathcal{D} \subset \mathbb{Z}$. 
Let $U = \{u_1, u_2, \dots, u_M\}$ be the set of unique elements in $A$, where $M = |U| \leq N$.

We define the frequency function $f: U \to \mathbb{Z}^+$ as:
$$f(u) = \sum_{i=1}^{N} \mathbb{I}(a_i = u)$$
where $\mathbb{I}(\cdot)$ is the indicator function.

The objective is to identify a subset $S \subset U$ such that $|S| = k$ (for $1 \leq k \leq M$) satisfying the condition that for all $u \in S$ and $v \in U \setminus S$, $f(u) \geq f(v)$.

The output is a set $S = \{s_1, s_2, \dots, s_k\}$ representing the $k$ elements with the highest frequencies in $A$.

## 2. Algebraic Characterization

### Frequency Mapping
The algorithm first constructs the frequency map $\mathcal{M} = \{(u, f(u)) \mid u \in U\}$. This is a bijective mapping from the set of unique elements to their respective counts.

### Heap-based Selection (Min-Heap Invariant)
For the heap-based approach, we maintain a min-priority queue $\mathcal{H}$ of size $k$. Let $\mathcal{H}_i$ denote the state of the heap after processing $i$ unique elements. The heap stores pairs $(f(u), u)$. The invariant maintained is:
$$\forall (f_a, u_a) \in \mathcal{H}, \forall (f_b, u_b) \in (\mathcal{M} \setminus \mathcal{H}), f_a \geq \min_{(f, u) \in \mathcal{H}} f \implies f_b \leq f_a$$
Upon completion, $\mathcal{H}$ contains the $k$ elements with the largest values of $f(u)$.

### Bucket Sort Formulation
We define a collection of buckets $\mathcal{B} = \{B_0, B_1, \dots, B_N\}$, where each bucket $B_i$ is a set:
$$B_i = \{u \in U \mid f(u) = i\}$$
The algorithm constructs $\mathcal{B}$ such that $\bigcup_{i=0}^N B_i = U$ and $B_i \cap B_j = \emptyset$ for $i \neq j$. The result set $S$ is constructed by concatenating elements from $B_i$ in descending order of index $i$:
$$S = \bigcup_{i=N}^{1} B_i \quad \text{s.t. } |S| = k$$

## 3. Complexity Analysis

### Time Complexity
**Heap Approach:**
1. **Frequency Counting:** Iterating through $A$ takes $O(N)$ time.
2. **Heap Operations:** We perform $M$ insertions into a heap of maximum size $k$. Each insertion/deletion operation takes $O(\log k)$. The total time is:
   $$T(N) = O(N) + \sum_{i=1}^{M} O(\log k) = O(N + M \log k)$$
   Since $M \leq N$, the complexity is $O(N \log k)$.

**Bucket Sort Approach:**
1. **Frequency Counting:** $O(N)$.
2. **Bucket Population:** Iterating over $M$ unique elements to place them into buckets takes $O(M)$.
3. **Bucket Traversal:** Iterating through $N+1$ buckets takes $O(N)$.
   $$T(N) = O(N) + O(M) + O(N) = O(N)$$
   The algorithm is strictly linear, as the number of buckets is bounded by the input size $N$.

### Space Complexity
The space complexity is dominated by the storage of the frequency map and the auxiliary structures (heap or buckets).
1. **Frequency Map:** Stores $M$ unique elements, requiring $O(M)$ space.
2. **Heap/Buckets:** 
   - The heap stores $k$ elements: $O(k)$.
   - The buckets store $M$ elements across $N+1$ lists: $O(N + M)$.
   
Given $M \leq N$ and $k \leq N$, the total auxiliary space complexity is:
$$S(N) = O(N + M) = O(N)$$
Thus, the algorithm operates within linear space relative to the input size.