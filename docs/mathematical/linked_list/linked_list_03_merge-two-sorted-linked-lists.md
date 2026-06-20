# Formal Mathematical Specification: Merge Two Sorted Linked Lists

## 1. Definitions and Notation

Let $\mathcal{L}$ be the set of all singly linked lists. A linked list $L \in \mathcal{L}$ is defined as an ordered sequence of nodes $N = (v, p)$, where $v \in \mathbb{R}$ is the value and $p \in \mathcal{L} \cup \{\text{null}\}$ is the pointer to the subsequent node.

Formally, a list $L$ of length $n$ is a sequence of nodes $(n_0, n_1, \dots, n_{n-1})$ such that for each $i \in \{0, \dots, n-2\}$, $n_i.next = n_{i+1}$, and $n_{n-1}.next = \text{null}$. 

We define the input as two sorted linked lists:
- $L_1 = (a_0, a_1, \dots, a_{n-1})$ where $a_i.v \le a_{i+1}.v$ for all $0 \le i < n-1$.
- $L_2 = (b_0, b_1, \dots, b_{m-1})$ where $b_j.v \le b_{j+1}.v$ for all $0 \le j < m-1$.

The output is a linked list $L_{merged} = (c_0, c_1, \dots, c_{n+m-1})$ such that:
1. The set of nodes in $L_{merged}$ is exactly the union of the sets of nodes in $L_1$ and $L_2$.
2. $c_k.v \le c_{k+1}.v$ for all $0 \le k < n+m-1$.

## 2. Algebraic Characterization

The algorithm maintains a state defined by the tuple $(p_1, p_2, \text{tail})$, where $p_1$ and $p_2$ are pointers to the current nodes being considered in $L_1$ and $L_2$, and $\text{tail}$ is the last node of the constructed merged list.

### Loop Invariant
At the start of each iteration of the merge process, let $S$ be the set of nodes already appended to the merged list. The following invariant holds:
1. The nodes in $S$ are sorted: $\forall x, y \in S$, if $x$ precedes $y$ in the merged list, then $x.v \le y.v$.
2. For any node $x \in S$ and any node $y \in \{p_1, p_2, \dots, \text{remaining nodes of } L_1, L_2\}$, $x.v \le y.v$.

### Transition Function
The state transition is defined by the mapping $f: (p_1, p_2) \to (p_1', p_2', \text{tail}')$:
$$
\text{tail}'.next = 
\begin{cases} 
p_1 & \text{if } p_1.v \le p_2.v \\
p_2 & \text{otherwise}
\end{cases}
$$
$$
(p_1', p_2') = 
\begin{cases} 
(p_1.next, p_2) & \text{if } p_1.v \le p_2.v \\
(p_1, p_2.next) & \text{otherwise}
\end{cases}
$$

The process terminates when $p_1 = \text{null}$ or $p_2 = \text{null}$. The final step is the concatenation of the non-empty remainder:
$$
\text{tail}_{final}.next = \begin{cases} p_1 & \text{if } p_2 = \text{null} \\ p_2 & \text{if } p_1 = \text{null} \end{cases}
$$

## 3. Complexity Analysis

### Time Complexity
The algorithm performs a single pass over the nodes of $L_1$ and $L_2$. Let $T(n, m)$ be the number of operations. In each iteration of the `while` loop, exactly one node is appended to the merged list, and one pointer ($p_1$ or $p_2$) is advanced. 

The total number of iterations is exactly $n + m$. Since each iteration involves a constant number of pointer assignments and comparisons, the work per iteration is $O(1)$. Thus:
$$T(n, m) = \sum_{k=1}^{n+m} O(1) = O(n + m)$$
The time complexity is $\Theta(n + m)$ as we must visit every node at least once to establish the total ordering.

### Space Complexity
The algorithm utilizes a constant number of auxiliary pointers: `dummy`, `tail`, `p1`, and `p2`. 
- **Auxiliary Space:** The memory required for these pointers is independent of the input size $n$ and $m$. Thus, the auxiliary space complexity is $O(1)$.
- **Total Space:** Since the algorithm performs in-place pointer rewiring (splicing) and does not instantiate new nodes (with the exception of the single dummy node), the total space complexity is $O(1)$ relative to the input lists.