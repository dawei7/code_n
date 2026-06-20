# Formal Mathematical Specification: Word Count with Prefix

## 1. Definitions and Notation

Let $\Sigma$ be a finite alphabet. A dictionary $D$ is a finite set of strings $D = \{s_1, s_2, \dots, s_N\}$, where each $s_i \in \Sigma^*$. 

We define a **Trie** as a rooted tree $T = (V, E)$, where:
*   $V$ is the set of nodes. Each node $v \in V$ represents a prefix $p \in \Sigma^*$.
*   $E \subseteq V \times V$ is the set of directed edges, where an edge $(u, v)$ labeled with $\sigma \in \Sigma$ exists if the prefix represented by $v$ is $p_u \cdot \sigma$.
*   $\text{root} \in V$ represents the empty string $\epsilon$.
*   $\text{count}(v): V \to \mathbb{N}_0$ is an augmentation function mapping each node $v$ to the number of strings in $D$ that have the prefix associated with $v$.

Given a query prefix $q \in \Sigma^*$, the objective is to compute the function $f(q)$:
$$f(q) = |\{s \in D \mid q \text{ is a prefix of } s\}|$$

## 2. Algebraic Characterization

The correctness of the algorithm relies on the inductive definition of the augmentation function $\text{count}(v)$. 

For any node $v$ representing prefix $p$, let $S_v = \{s \in D \mid p \text{ is a prefix of } s\}$. By definition, $\text{count}(v) = |S_v|$. 

**Base Case:**
For the root node $r$ representing $\epsilon$:
$$\text{count}(r) = |D|$$

**Recursive Step:**
For a node $u$ and its child $v$ connected by edge $(u, v)$ labeled $\sigma$:
$$\text{count}(v) = \sum_{s \in S_u} \mathbb{I}(s \text{ starts with } p_u \cdot \sigma)$$
where $\mathbb{I}(\cdot)$ is the indicator function. 

**Insertion Invariant:**
When inserting a word $w = \sigma_1\sigma_2\dots\sigma_m$ into the Trie, we define a path of nodes $v_0, v_1, \dots, v_m$ where $v_0 = \text{root}$ and $v_i$ corresponds to the prefix $w[1 \dots i]$. The update rule for each node $v_i$ on the path is:
$$\text{count}(v_i) \leftarrow \text{count}(v_i) + 1$$
This ensures that for any node $v$ representing prefix $p$, $\text{count}(v)$ is exactly the number of times the insertion path passed through $v$, which is equivalent to the number of words in $D$ having $p$ as a prefix.

**Query Formulation:**
Given a query $q = \sigma_1\sigma_2\dots\sigma_k$, let $v_q$ be the node reached by traversing the Trie from the root following the sequence of characters in $q$. If the path exists, the result is:
$$f(q) = \text{count}(v_q)$$
If the path does not exist, $f(q) = 0$.

## 3. Complexity Analysis

### Time Complexity
Let $M = |q|$ be the length of the query prefix.

1.  **Preprocessing (Insertion):** For each word $s_i \in D$ with length $L_i$, we perform $L_i$ node traversals and updates. The total time complexity for building the Trie is $O(\sum_{i=1}^N L_i)$.
2.  **Querying:** The query algorithm performs a path traversal of length $M$. At each step $j \in \{1, \dots, M\}$, we perform a dictionary lookup in the current node's children, which is $O(1)$ on average (using a hash map) or $O(\log |\Sigma|)$ (using a balanced BST). 
    *   Total Query Time: $O(M)$.

Since $M$ is independent of the dictionary size $N$, the query time is optimal.

### Space Complexity
The space complexity is determined by the number of nodes in the Trie. 
*   In the worst case, where no two words share a prefix, the number of nodes $|V| = 1 + \sum_{i=1}^N L_i$.
*   Each node stores a map of children and an integer `count`. 
*   Total Space: $O(\sum_{i=1}^N L_i)$, which simplifies to $O(M_{total})$ where $M_{total}$ is the sum of the lengths of all strings in the dictionary. 
*   Auxiliary space for a single query is $O(1)$, as we only maintain a pointer to the current node.