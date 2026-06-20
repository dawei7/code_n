# Formal Mathematical Specification: Subsets (Power Set)

## 1. Definitions and Notation

Let $S$ be a finite set of $N$ distinct elements, where $N = |S| \in \mathbb{N}_0$. To facilitate algorithmic indexing, we impose an arbitrary total order on $S$ to represent it as an indexed sequence:

$$\mathbf{s} = (s_0, s_1, \dots, s_{N-1}) \in \mathcal{X}^N$$

where $\mathcal{X}$ is the underlying domain of the elements.

### The Power Set
The power set of $S$, denoted by $\mathcal{P}(S)$ or $2^S$, is the set of all subsets of $S$:

$$\mathcal{P}(S) = \{ A \mid A \subseteq S \}$$

The cardinality of the power set is given by $|\mathcal{P}(S)| = 2^N$.

### State Space Representation
The backtracking algorithm systematically explores the decision space of subset constructions. We model this decision space as a directed, rooted, complete binary tree $T = (V, E)$ of height $N$:

*   **Vertices ($V$):** Each vertex $v \in V$ corresponds to a partial decision sequence $\mathbf{b} = (b_0, b_1, \dots, b_{i-1}) \in \{0, 1\}^i$ of length $i \in \{0, \dots, N\}$, representing the choices made for the first $i$ elements of $\mathbf{s}$. 
    *   The root node $r \in V$ corresponds to the empty sequence $\epsilon$ (where $i = 0$).
    *   The leaf nodes $L \subset V$ correspond to complete decision sequences of length $N$, i.e., $L = \{0, 1\}^N$.
*   **Edges ($E$):** For any internal vertex $v$ representing $\mathbf{b} \in \{0, 1\}^i$ with $i < N$, there exist exactly two outgoing directed edges:
    1.  An edge to $v_{\text{include}}$ representing $(\mathbf{b}, 1)$, indicating the inclusion of $s_i$.
    2.  An edge to $v_{\text{exclude}}$ representing $(\mathbf{b}, 0)$, indicating the exclusion of $s_i$.

### The Output Mapping
We define a bijection $\phi: \{0, 1\}^N \to \mathcal{P}(S)$ that maps each leaf node (complete decision path) to its corresponding subset:

$$\phi(\mathbf{b}) = \{ s_i \in S \mid b_i = 1 \}$$

The objective of the algorithm is to construct the family of sets:

$$\mathcal{R} = \{ \phi(\mathbf{b}) \mid \mathbf{b} \in \{0, 1\}^N \}$$

---

## 2. Algebraic Characterization

### Recursive Formulation
Let $f: \{0, \dots, N\} \times \mathcal{P}(S) \to \mathcal{P}(\mathcal{P}(S))$ be a set-valued function defined recursively as:

$$f(i, A) = \begin{cases}
\{ A \} & \text{if } i = N \\
f(i+1, A \cup \{s_i\}) \cup f(i+1, A) & \text{if } 0 \le i < N
\end{cases}$$

where $i$ represents the current decision index, and $A \subseteq \{s_0, \dots, s_{i-1}\}$ represents the accumulated subset.

### Proof of Correctness
We prove by induction on the remaining depth $d = N - i$ that for any $i \in \{0, \dots, N\}$ and any $A \subseteq \{s_0, \dots, s_{i-1}\}$:

$$f(i, A) = \{ A \cup B \mid B \subseteq \{s_i, \dots, s_{N-1}\} \}$$

#### Base Case ($d = 0 \implies i = N$):
By definition:

$$f(N, A) = \{ A \}$$

Since the only subset of the empty set $\emptyset$ is $\emptyset$ itself, we have:

$$\{ A \cup B \mid B \subseteq \emptyset \} = \{ A \cup \emptyset \} = \{ A \}$$

Thus, the base case holds.

#### Inductive Step:
Assume the induction hypothesis holds for $d = k$, which corresponds to index $i+1$ (where $0 \le i < N$). That is, for any $A' \subseteq \{s_0, \dots, s_i\}$:

$$f(i+1, A') = \{ A' \cup B' \mid B' \subseteq \{s_{i+1}, \dots, s_{N-1}\} \}$$

We evaluate $f(i, A)$ for $A \subseteq \{s_0, \dots, s_{i-1}\}$:

$$f(i, A) = f(i+1, A \cup \{s_i\}) \cup f(i+1, A)$$

Applying the induction hypothesis to both terms on the right-hand side:

1.  For $A' = A \cup \{s_i\}$:
    $$f(i+1, A \cup \{s_i\}) = \{ A \cup \{s_i\} \cup B' \mid B' \subseteq \{s_{i+1}, \dots, s_{N-1}\} \}$$
2.  For $A' = A$:
    $$f(i+1, A) = \{ A \cup B' \mid B' \subseteq \{s_{i+1}, \dots, s_{N-1}\} \}$$

Combining these two families of sets yields:

$$f(i, A) = \{ A \cup C \mid C \in \mathcal{C} \}$$

where $\mathcal{C} = \{ \{s_i\} \cup B' \mid B' \subseteq \{s_{i+1}, \dots, s_{N-1}\} \} \cup \{ B' \mid B' \subseteq \{s_{i+1}, \dots, s_{N-1}\} \}$. 

By the fundamental properties of power sets, any subset $B \subseteq \{s_i, \dots, s_{N-1}\}$ either contains $s_i$ (in which case $B = \{s_i\} \cup B'$ for some $B' \subseteq \{s_{i+1}, \dots, s_{N-1}\}$) or does not contain $s_i$ (in which case $B = B'$). Thus, $\mathcal{C} = \mathcal{P}(\{s_i, \dots, s_{N-1}\})$.

Therefore:

$$f(i, A) = \{ A \cup B \mid B \subseteq \{s_i, \dots, s_{N-1}\} \}$$

This completes the induction.

#### Corollary:
For the initial call where $i = 0$ and $A = \emptyset$:

$$f(0, \emptyset) = \{ \emptyset \cup B \mid B \subseteq \{s_0, \dots, s_{N-1}\} \} = \{ B \mid B \subseteq S \} = \mathcal{P}(S)$$

This formally proves that the recursive formulation computes the exact power set of $S$.

### State Transition and Backtracking Mutation
To optimize space complexity, the algorithm avoids copying the subset $A$ at each recursive step. Instead, it maintains a single mutable stack $\mathbf{a}$ representing the current state. 

Let $\mathbf{a}^{(t)}$ denote the state of the stack at step $t$. The transition from state $(i, \mathbf{a}^{(t)})$ to its subproblems is characterized by the following sequence of operations:

1.  **Inclusion Branch:**
    $$\mathbf{a}^{(t+1)} \leftarrow \mathbf{a}^{(t)} \mathbin{\Vert} s_i$$
    where $\Vert$ denotes the append operation. The algorithm then recurses to state $(i+1, \mathbf{a}^{(t+1)})$.
2.  **Backtracking (State Restoration):**
    $$\mathbf{a}^{(t+2)} \leftarrow \text{pop}(\mathbf{a}^{(t+1)}) = \mathbf{a}^{(t)}$$
3.  **Exclusion Branch:**
    The algorithm recurses to state $(i+1, \mathbf{a}^{(t+2)})$ without modifying the stack.

---

## 3. Complexity Analysis

### Time Complexity
Let $W(N)$ represent the total computational work (time complexity) required to generate the power set of a set of size $N$. 

The execution of the backtracking algorithm corresponds to a depth-first traversal of the complete binary tree $T$. The total number of nodes in a complete binary tree of height $N$ is:

$$\sum_{i=0}^{N} 2^i = 2^{N+1} - 1$$

We partition the work done at these nodes into two categories:

1.  **Internal Nodes ($i < N$):** At each of the $2^N - 1$ internal nodes, the algorithm performs $O(1)$ operations (index incrementing, stack push/pop operations, and recursive call overhead).
2.  **Leaf Nodes ($i = N$):** There are exactly $2^N$ leaf nodes. At each leaf node, the algorithm must copy the current state of the stack $\mathbf{a}$ to the output collection. Since the size of the subset at a leaf node can be up to $N$, copying the subset takes $\Theta(|\mathbf{a}|) = O(N)$ time.

Thus, the total work $W(N)$ is bounded by:

$$W(N) = \sum_{i=0}^{N-1} 2^i \cdot \Theta(1) + 2^N \cdot \Theta(N)$$

$$W(N) = \Theta(2^N) + \Theta(N \cdot 2^N) = \Theta(N \cdot 2^N)$$

Therefore, the time complexity of the algorithm is strictly $\Theta(N \cdot 2^N)$ in the best, average, and worst cases.

### Space Complexity

#### Auxiliary Space
Auxiliary space is the extra space used by the algorithm, excluding the memory allocated for the final output.

1.  **Recursion Stack:** The maximum depth of the recursion tree is $N$. Consequently, the system call stack will contain at most $N + 1$ active stack frames at any given instant. Each frame requires $O(1)$ space to store local variables (such as the index $i$). This contributes $O(N)$ space.
2.  **State Representation:** The mutable stack $\mathbf{a}$ used to store the current subset contains at most $N$ elements of $\mathcal{X}$. This contributes $O(N)$ space.

Thus, the auxiliary space complexity is:

$$\text{Space}_{\text{aux}}(N) = O(N)$$

#### Total Space
Total space includes the memory required to store the final output $\mathcal{R}$. 

The output consists of $2^N$ subsets. The average size of a subset in the power set is given by the expected value of the binomial distribution for $p = 0.5$:

$$\mathbb{E}[|A|] = \frac{1}{2^N} \sum_{k=0}^{N} \binom{N}{k} k = \frac{1}{2^N} \left( N 2^{N-1} \right) = \frac{N}{2}$$

The total memory required to store all generated subsets is:

$$\text{Space}_{\text{total}}(N) = 2^N \cdot \Theta(N) = \Theta(N \cdot 2^N)$$