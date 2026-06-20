# Formal Mathematical Specification: Sublist Search

## 1. Definitions and Notation

Let $L$ be a singly linked list defined as an ordered sequence of nodes $N = \{n_0, n_1, \dots, n_{n-1}\}$, where each node $n_i$ contains a value $v_i \in \Sigma$ (where $\Sigma$ is a finite alphabet) and a pointer to the successor node $n_{i+1}$. We denote the length of the main list as $n = |L|$ and the length of the sublist $S$ as $m = |S|$, where $S = \{s_0, s_1, \dots, s_{m-1}\}$.

- **Input Domain:** The set of all pairs $(L, S)$ such that $L$ and $S$ are singly linked lists.
- **Output Codomain:** The boolean set $\mathbb{B} = \{True, False\}$.
- **State Space:** The configuration of the algorithm at any step $k$ is defined by the tuple $\mathcal{S}_k = (p_{first}, p_{main}, p_{sub})$, where $p_{first} \in L \cup \{\text{null}\}$, $p_{main} \in L \cup \{\text{null}\}$, and $p_{sub} \in S \cup \{\text{null}\}$.
- **Matching Predicate:** We define a match of length $m$ starting at index $i$ in $L$ as the condition:
  $$\forall j \in \{0, \dots, m-1\} : \text{val}(n_{i+j}) = \text{val}(s_j)$$

## 2. Algebraic Characterization

The algorithm determines the existence of a contiguous sub-sequence by evaluating the predicate $P(L, S)$:
$$P(L, S) \iff \exists i \in \{0, \dots, n-m\} \text{ s.t. } \bigwedge_{j=0}^{m-1} (\text{val}(n_{i+j}) = \text{val}(s_j))$$

### Loop Invariants
Let $i$ be the index of the node pointed to by $p_{first}$. At the start of each iteration of the outer loop, the following invariant holds:
1. **Progress Invariant:** For all $k < i$, the sublist $S$ is not a prefix of the sublist of $L$ starting at $n_k$.
2. **Termination Condition:** The algorithm terminates when $i > n - m$ (returning $False$) or when the inner loop satisfies $\forall j \in \{0, \dots, m-1\}, \text{val}(n_{i+j}) = \text{val}(s_j)$ (returning $True$).

The transition function for the pointers is defined as:
- **Outer Step:** $p_{first} \leftarrow \text{next}(p_{first})$
- **Inner Step:** If $\text{val}(p_{main}) = \text{val}(p_{sub})$, then $(p_{main}, p_{sub}) \leftarrow (\text{next}(p_{main}), \text{next}(p_{sub}))$.

## 3. Complexity Analysis

### Time Complexity
The time complexity $T(n, m)$ is determined by the nested traversal of the lists. In the worst case, for every starting position $i \in \{0, \dots, n-m\}$, the inner loop performs $m$ comparisons before failing.

The total number of operations $W$ is given by the summation:
$$W = \sum_{i=0}^{n-m} \sum_{j=0}^{m-1} \mathbb{I}(\text{match}) \leq \sum_{i=0}^{n-m} m = (n - m + 1) \cdot m$$

Asymptotically, as $n, m \to \infty$:
$$T(n, m) = O((n-m+1) \cdot m) = O(n \cdot m)$$
The best-case complexity occurs when the first node of $L$ matches the first node of $S$ and the match is either found immediately or fails at the first position, yielding $\Omega(m)$ or $\Omega(1)$ depending on the implementation constraints.

### Space Complexity
The algorithm maintains a constant number of pointers ($p_{first}, p_{main}, p_{sub}$) regardless of the input size $n$ or $m$. 

Let $S_{aux}$ be the auxiliary space:
$$S_{aux} = \mathcal{O}(1)$$
Since no additional data structures (such as hash maps or recursion stacks) are utilized that scale with the input, the space complexity is strictly $O(1)$.