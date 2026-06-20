# Formal Mathematical Specification: Longest Consecutive Sequence

## 1. Definitions and Notation

Let $A = \{a_1, a_2, \dots, a_n\}$ be a multiset of integers, where $n = |A|$. We define the universe of discourse as $\mathbb{Z}$. 

*   **Input:** An unordered sequence (or multiset) $A \subset \mathbb{Z}$.
*   **Hash Set:** Let $S = \{x \mid x \in A\}$ be the set of unique elements in $A$. The construction of $S$ maps $A$ to its characteristic set representation.
*   **Consecutive Sequence:** A subset $C \subseteq S$ is a consecutive sequence if there exists $k \in \mathbb{Z}$ and $m \in \mathbb{N}$ such that $C = \{k, k+1, \dots, k+m-1\}$.
*   **Objective:** Find the maximum cardinality of any such subset $C$ that is a subset of $S$. Formally, we seek:
    $$\mathcal{L} = \max \{ |C| : C \subseteq S \land \exists k \in \mathbb{Z}, \forall i \in \{0, \dots, |C|-1\}, (k+i) \in S \}$$

## 2. Algebraic Characterization

To ensure $O(N)$ efficiency, we define a predicate $\text{is\_starter}(x)$ for any $x \in S$:
$$\text{is\_starter}(x) \iff (x - 1) \notin S$$

This predicate partitions $S$ into disjoint sets of sequences. For every $x \in S$, if $\text{is\_starter}(x)$ is true, $x$ is the unique minimal element of a maximal consecutive sequence $C_x \subseteq S$. We define the sequence starting at $x$ as:
$$C_x = \{x + i \mid i \in \mathbb{N}_0, x+i \in S, \forall j < i, x+j \in S\}$$

The length of the sequence starting at $x$ is given by the function $f(x) = |C_x|$. The global maximum is:
$$\mathcal{L} = \max_{x \in S, \text{is\_starter}(x)} f(x)$$

**Loop Invariant:**
Let $S_i$ be the set of elements processed after $i$ iterations of the outer loop. Let $L_i$ be the maximum length found among all sequences starting with $x \in S_i$. At each step $i$, the algorithm maintains:
$$L_i = \max \{ f(x) : x \in S_i \land \text{is\_starter}(x) \}$$
The algorithm terminates when $S_i = S$, yielding $L_n = \mathcal{L}$.

## 3. Complexity Analysis

### Time Complexity
The algorithm consists of two phases:
1.  **Set Construction:** Mapping $A$ to $S$ requires $n$ insertions into a hash table. Assuming a uniform hash function, each insertion is $O(1)$ on average. Total time: $O(n)$.
2.  **Sequence Traversal:** We iterate through each $x \in S$. The inner `while` loop executes only if $\text{is\_starter}(x)$ is true. 
    Let $T$ be the total number of operations. We can express $T$ as:
    $$T = \sum_{x \in S} \mathbb{I}(\text{is\_starter}(x)) \cdot |C_x| + O(n)$$
    where $\mathbb{I}$ is the indicator function. Since every element $y \in S$ belongs to exactly one maximal consecutive sequence $C_x$, the sum of the lengths of all disjoint sequences is exactly $|S| \leq n$:
    $$\sum_{x \in S, \text{is\_starter}(x)} |C_x| = |S| \leq n$$
    Thus, the total time complexity is $O(n) + O(n) = O(n)$.

### Space Complexity
The algorithm requires the storage of the set $S$. In the worst case, where all elements in $A$ are distinct, $|S| = n$.
*   **Auxiliary Space:** The hash set $S$ stores $n$ integers.
*   **Total Space:** $O(n)$ to maintain the set $S$ and $O(1)$ for auxiliary variables (`best`, `cur`).
The space complexity is strictly $O(n)$.