# Formal Mathematical Specification: Reverse Nodes in k-Group

## 1. Definitions and Notation

Let $L$ be a singly linked list defined as a sequence of nodes $N = \{n_1, n_2, \dots, n_m\}$. Each node $n_i$ is a tuple $(v_i, p_i)$, where $v_i$ is the data value and $p_i \in N \cup \{\text{null}\}$ is the pointer to the successor node. The list is represented by the ordered sequence of nodes $(n_1, n_2, \dots, n_m)$ such that $p(n_i) = n_{i+1}$ for $1 \le i < m$ and $p(n_m) = \text{null}$.

Let $k \in \mathbb{Z}^+$ be the grouping parameter. We define the partition of $L$ into contiguous segments $S_j$ of length $k$:
$S_j = (n_{(j-1)k+1}, \dots, n_{jk})$ for $1 \le j \le \lfloor m/k \rfloor$.
Let $R$ be the remainder segment $R = (n_{\lfloor m/k \rfloor \cdot k + 1}, \dots, n_m)$, where $R = \emptyset$ if $m \equiv 0 \pmod k$.

The transformation function $f: L \to L'$ maps the original list to a modified list $L'$ where each segment $S_j$ is reversed, denoted as $S_j^R = (n_{jk}, n_{jk-1}, \dots, n_{(j-1)k+1})$, while $R$ remains invariant. The resulting list $L'$ is the concatenation:
$L' = S_1^R \oplus S_2^R \oplus \dots \oplus S_{\lfloor m/k \rfloor}^R \oplus R$.

## 2. Algebraic Characterization

The algorithm maintains a state defined by the tuple $\sigma = (\text{prev\_tail}, \text{curr\_head}, \text{next\_group\_start})$. 

**Loop Invariant:**
At the start of each iteration $j \in \{1, \dots, \lfloor m/k \rfloor\}$, the list is partitioned into three segments:
1. A processed prefix $P_{j-1} = \bigoplus_{i=1}^{j-1} S_i^R$.
2. An unprocessed segment $U_j = S_j \oplus \dots \oplus S_{\lfloor m/k \rfloor} \oplus R$.
3. The invariant $\text{prev\_tail}$ points to the terminal node of $S_{j-1}^R$.

**Transition Function:**
For a segment $S_j = (a_1, a_2, \dots, a_k)$, the reversal operation $\rho(S_j)$ is defined by the update of successor pointers $p$:
$$\forall i \in \{2, \dots, k\}: p(a_i) = a_{i-1}$$
The stitching operation at step $j$ is defined as:
$$p(\text{prev\_tail}) = a_k$$
$$p(a_1) = \text{head}(S_{j+1})$$
where $\text{head}(S_{j+1})$ is the first node of the subsequent segment. This ensures the global connectivity of the list is preserved under the local reversal of $S_j$.

## 3. Complexity Analysis

### Time Complexity
Let $T(m)$ be the time required to process a list of length $m$. The algorithm performs two distinct operations per node:
1. **Traversal:** Finding the $k$-th node requires $k$ steps. This is performed $\lfloor m/k \rfloor$ times. Total cost: $\sum_{j=1}^{\lfloor m/k \rfloor} k = O(m)$.
2. **Reversal:** Reversing $k$ pointers is performed $\lfloor m/k \rfloor$ times. Total cost: $\sum_{j=1}^{\lfloor m/k \rfloor} k = O(m)$.

The total time complexity is:
$$T(m) = \sum_{j=1}^{\lfloor m/k \rfloor} (k + k) + |R| = 2 \cdot \lfloor m/k \rfloor \cdot k + (m \pmod k) = \Theta(m)$$
Since $m = N$, the time complexity is $O(N)$.

### Space Complexity
The algorithm utilizes a fixed set of pointers: $\{\text{dummy}, \text{prev\_group\_tail}, \text{kth}, \text{prev}, \text{curr}, \text{next\_node}\}$. 
Let $S_{aux}$ be the auxiliary space. Since the number of pointers is independent of $N$ and $k$:
$$S_{aux} = \sum_{i=1}^{c} \text{sizeof}(\text{pointer}) = O(1)$$
The algorithm operates in-place, modifying only the existing pointer fields $p_i$ of the nodes $n_i$. Thus, the total auxiliary space complexity is $O(1)$.