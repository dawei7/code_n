# Formal Mathematical Specification: Trie Insert and Search

## 1. Definitions and Notation

Let $\Sigma$ be a finite alphabet (e.g., $\Sigma = \{a, b, \dots, z\}$). A Trie is a rooted tree $T = (V, E)$ defined over $\Sigma$, where each node $v \in V$ represents a prefix of one or more strings in a dictionary $D \subset \Sigma^*$.

- **Nodes ($V$):** Each node $v \in V$ is a tuple $(C_v, \omega_v)$, where:
    - $C_v: \Sigma \to V \cup \{\bot\}$ is a partial mapping from characters to child nodes.
    - $\omega_v \in \{0, 1\}$ is a boolean indicator where $\omega_v = 1$ if and only if the path from the root to $v$ corresponds to a string $s \in D$.
- **Root ($r$):** The unique node $r \in V$ representing the empty string $\epsilon$.
- **State Space ($\mathcal{S}$):** The set of all possible Tries $T$ that can be constructed from a set of strings $D$.
- **Operations:**
    - $\text{insert}(s)$: A transformation $T \to T'$ such that $D' = D \cup \{s\}$.
    - $\text{search}(s)$: A predicate $P(s, T) \to \{0, 1\}$ defined as $P(s, T) = 1 \iff s \in D$.
    - $\text{startsWith}(p)$: A predicate $Q(p, T) \to \{0, 1\}$ defined as $Q(p, T) = 1 \iff \exists s \in D$ such that $p$ is a prefix of $s$.

## 2. Algebraic Characterization

Let $s = c_1 c_2 \dots c_m$ be a string of length $m$. We define the traversal function $\tau: V \times \Sigma^* \to V \cup \{\bot\}$ recursively:

1. $\tau(v, \epsilon) = v$
2. $\tau(v, c_1 \dots c_m) = \begin{cases} \tau(C_v(c_1), c_2 \dots c_m) & \text{if } C_v(c_1) \neq \bot \\ \bot & \text{if } C_v(c_1) = \bot \end{cases}$

### Correctness Invariants
The operations are governed by the following logical conditions:

- **Insertion:** After $\text{insert}(s)$, the resulting Trie $T'$ satisfies:
  $\forall s' \in D \cup \{s\}, \tau(r, s') = v \implies \omega_v = 1$.
- **Search:** The predicate $\text{search}(s)$ is defined as:
  $$\text{search}(s) = \begin{cases} \omega_{\tau(r, s)} & \text{if } \tau(r, s) \neq \bot \\ 0 & \text{if } \tau(r, s) = \bot \end{cases}$$
- **Prefix Search:** The predicate $\text{startsWith}(p)$ is defined as:
  $$\text{startsWith}(p) = \begin{cases} 1 & \text{if } \tau(r, p) \neq \bot \\ 0 & \text{if } \tau(r, p) = \bot \end{cases}$$

## 3. Complexity Analysis

### Time Complexity
Let $m = |s|$ be the length of the input string. 

For any operation (insert, search, startsWith), the algorithm performs a sequence of transitions $\tau(v, c_i)$. Each transition involves a lookup in the mapping $C_v$. Assuming $C_v$ is implemented as a hash map or a fixed-size array, the lookup time is $O(1)$.
The total time $T(m)$ is the summation of work over the length of the string:
$$T(m) = \sum_{i=1}^{m} O(1) = O(m)$$
Thus, the time complexity is linear with respect to the length of the input string, independent of the total number of strings $N$ stored in the Trie.

### Space Complexity
- **Auxiliary Space:** The algorithm uses $O(1)$ auxiliary space for pointers and loop variables during traversal.
- **Total Space:** In the worst case, where no two strings share a prefix, each character of every inserted string $s_i$ requires the creation of a new node. For a set of strings $D = \{s_1, s_2, \dots, s_n\}$, the total space complexity is:
  $$S = O\left(\sum_{i=1}^{n} |s_i|\right)$$
  For a single insertion of length $m$, the incremental space complexity is $O(m)$. In the context of the Trie structure, this is optimal as it represents the minimum nodes required to represent the set $D$ as a prefix tree.