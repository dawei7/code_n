# Formal Mathematical Specification: Longest Common Prefix (Trie Method)

## 1. Definitions and Notation

Let $\Sigma$ be a finite alphabet. Let $S = \{s_1, s_2, \dots, s_n\}$ be a set of $n$ strings where each $s_i \in \Sigma^*$. Let $M = \max_{i} |s_i|$ denote the length of the longest string in $S$.

A **Trie** is defined as a rooted tree $T = (V, E, \text{root}, \text{label}, \text{is\_end})$, where:
*   $V$ is the set of nodes.
*   $E \subseteq V \times V$ is the set of directed edges.
*   $\text{root} \in V$ is the unique starting node.
*   $\text{label}: E \to \Sigma$ is a function mapping each edge to a character in the alphabet.
*   $\text{is\_end}: V \to \{0, 1\}$ is a predicate indicating if a node represents the termination of a string $s_i \in S$.

For any node $u \in V$, let $\text{children}(u) = \{v \in V \mid (u, v) \in E\}$ denote the set of successor nodes. The size of the children set is denoted by $\text{deg}^+(u) = |\text{children}(u)|$.

The **Longest Common Prefix (LCP)** of $S$ is the longest string $p \in \Sigma^*$ such that $p$ is a prefix of every $s_i \in S$.

## 2. Algebraic Characterization

The LCP corresponds to the unique path starting from the root that satisfies specific structural constraints within the Trie. Let $P = (v_0, v_1, \dots, v_k)$ be a path in $T$ such that $v_0 = \text{root}$. The string represented by this path is $\mathcal{L}(P) = \text{label}(v_0, v_1) \cdot \text{label}(v_1, v_2) \dots \text{label}(v_{k-1}, v_k)$.

The LCP is the string $\mathcal{L}(P)$ where $P$ is the maximal path satisfying the following conditions for all $0 \le i < k$:
1.  **Uniqueness:** $\text{deg}^+(v_i) = 1$. This ensures that all strings in $S$ share the same character at this position.
2.  **Continuity:** $\text{is\_end}(v_i) = 0$. This ensures that no string in $S$ has terminated before this point, as a terminated string cannot share a prefix longer than itself.

Formally, the LCP is the sequence of labels along the path $P$ such that:
$$k = \min \{ i \in \mathbb{N} \mid \text{deg}^+(v_i) \neq 1 \lor \text{is\_end}(v_i) = 1 \}$$
The resulting LCP is the concatenation of labels:
$$\text{LCP}(S) = \bigoplus_{i=0}^{k-1} \text{label}(v_i, v_{i+1})$$

## 3. Complexity Analysis

### Time Complexity
The algorithm consists of two distinct phases:
1.  **Construction Phase:** We insert $n$ strings into the Trie. For each string $s_i$, we traverse at most $|s_i|$ nodes. The total time is:
    $$T_{\text{build}} = \sum_{i=1}^{n} O(|s_i|) \le O(n \cdot M)$$
2.  **Traversal Phase:** We traverse the path $P$ defined in Section 2. Since the path length $k$ is bounded by $M$, the traversal takes $O(k) = O(M)$ time.

The total time complexity is $T(n, M) = O(n \cdot M) + O(M) = O(n \cdot M)$.

### Space Complexity
The space complexity is determined by the number of nodes $|V|$ in the Trie. 
*   In the worst case, where all strings are distinct and share no common prefixes, the number of nodes is $\sum_{i=1}^n |s_i| + 1$.
*   Given $|s_i| \le M$, the upper bound on the number of nodes is $O(n \cdot M)$.
*   Each node stores a dictionary (or map) of size at most $|\Sigma|$. Thus, the total space complexity is $O(n \cdot M \cdot |\Sigma|)$. Assuming $|\Sigma|$ is a constant (e.g., 26 for lowercase English letters), the space complexity is $O(n \cdot M)$.