# Formal Mathematical Specification: Delete Word from Trie

## 1. Definitions and Notation

Let $\mathcal{T} = (V, E, \Sigma, \text{root}, \text{is\_end}, \text{children})$ be a Trie data structure, where:
*   $V$ is the set of nodes.
*   $\Sigma$ is the finite alphabet of characters.
*   $\text{root} \in V$ is the designated root node.
*   $\text{children}: V \times \Sigma \to V \cup \{\perp\}$ is a partial function mapping a node and a character to a child node.
*   $\text{is\_end}: V \to \{0, 1\}$ is a predicate indicating if a node represents the termination of a valid word.
*   $S = \{s_1, s_2, \dots, s_M\}$ is the target string of length $M$ to be deleted, where $s_i \in \Sigma$.

We define the path corresponding to $S$ as a sequence of nodes $(v_0, v_1, \dots, v_M)$ such that $v_0 = \text{root}$ and $v_i = \text{children}(v_{i-1}, s_i)$ for $1 \le i \le M$. The algorithm assumes the existence of this path such that $\text{is\_end}(v_M) = 1$.

## 2. Algebraic Characterization

The deletion process is defined by a post-order traversal function $f(v, i)$, where $v$ is the current node and $i$ is the index of the character in $S$ being processed. The state transition is governed by the following recursive logic:

**Base Case:**
For $i = M$:
$$\text{is\_end}(v_M) \leftarrow 0$$
Return $\mathbb{1}(\text{degree}(v_M) = 0)$, where $\text{degree}(v) = |\{c \in \Sigma \mid \text{children}(v, c) \neq \perp\}|$.

**Recursive Step:**
For $0 \le i < M$:
Let $v_{i+1} = \text{children}(v_i, s_{i+1})$.
Let $\text{delete\_child} = f(v_{i+1}, i+1)$.
If $\text{delete\_child} = 1$:
1. $\text{children}(v_i, s_{i+1}) \leftarrow \perp$
2. Return $\mathbb{1}(\text{degree}(v_i) = 0 \land \text{is\_end}(v_i) = 0)$
Else:
Return $0$

**Correctness Invariant:**
A node $v$ is removed from $V$ if and only if:
$$\forall v' \in \text{descendants}(v) \cup \{v\}, \text{is\_end}(v') = 0 \land \text{degree}(v') = 0$$
This ensures that the deletion of $v$ does not violate the integrity of any path representing a word $W \in \mathcal{L}(\mathcal{T}) \setminus \{S\}$.

## 3. Complexity Analysis

### Time Complexity
The algorithm performs a depth-first search (DFS) traversal along the path of length $M$. 
Let $T(M)$ be the time complexity. The recurrence relation is:
$$T(M) = T(M-1) + \Theta(1)$$
where $\Theta(1)$ accounts for the dictionary lookup, the update of the `is_end` flag, and the potential deletion of a child pointer. Given the base case $T(0) = \Theta(1)$, the closed form is:
$$T(M) = \sum_{i=1}^{M} \Theta(1) = \Theta(M)$$
Thus, the time complexity is $O(M)$, as we visit each node in the path exactly once and perform constant-time operations at each step.

### Space Complexity
The space complexity is dominated by the auxiliary stack space required for the recursive calls.
*   **Auxiliary Space:** The recursion depth is exactly $M$, corresponding to the length of the string $S$. Each stack frame consumes $O(1)$ space. Thus, the auxiliary space is $O(M)$.
*   **Total Space:** The algorithm modifies the Trie in-place. The total space complexity is $O(M)$ in the worst case (where the entire path is deleted), representing the reduction in the number of nodes $|V|$. Since no additional data structures proportional to the input size are created, the space complexity remains $O(M)$.