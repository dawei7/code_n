# Formal Mathematical Specification: Permutations

## 1. Definitions and Notation

Let $\mathcal{U}$ be a totally ordered universe of elements. We define the input to the algorithm as a sequence (or array) $A$ of length $n \in \mathbb{N}_0$, represented as an $n$-tuple:

$$A = (a_1, a_2, \dots, a_n) \in \mathcal{U}^n$$

where the elements are pairwise distinct, i.e., 

$$\forall i, j \in \{1, \dots, n\}, \quad i \neq j \implies a_i \neq a_j$$

Let $S_A = \{a_1, a_2, \dots, a_n\}$ denote the underlying set of elements in $A$, where $|S_A| = n$.

### 1.1 Permutations
A **permutation** of the sequence $A$ is a bijection $\sigma: \{1, \dots, n\} \to S_A$. Equivalently, we represent a permutation as an $n$-tuple $P = (p_1, p_2, \dots, p_n) \in S_A^n$ such that:

$$\forall i, j \in \{1, \dots, n\}, \quad i \neq j \implies p_i \neq p_j$$

The set of all possible permutations of $A$ is denoted by $\mathcal{P}(A)$. The cardinality of this set is given by the factorial of the sequence length:

$$|\mathcal{P}(A)| = n!$$

### 1.2 State Space of the Backtracking Search
The backtracking algorithm systematically explores the space of partial permutations. We define the **state space** $\mathcal{X}$ as the set of all prefixes of permutations of $A$:

$$\mathcal{X} = \bigcup_{k=0}^{n} \left\{ (p_1, \dots, p_k) \in S_A^k \;\middle|\; \forall i, j \in \{1, \dots, k\}, \, i \neq j \implies p_i \neq p_j \right\}$$

For any state $x = (p_1, \dots, p_k) \in \mathcal{X}$, we define:
*   The **length** of the state: $|x| = k$.
*   The **empty state** (root of the search space): $\epsilon = ()$ where $|\epsilon| = 0$.
*   The **terminal states** (leaves of the search space): $\mathcal{T} = \{ x \in \mathcal{X} \mid |x| = n \}$. Note that $\mathcal{T} = \mathcal{P}(A)$.

---

## 2. Algebraic Characterization

The backtracking algorithm can be formally modeled as a Depth-First Search (DFS) over a directed state-transition tree $T = (\mathcal{X}, E)$.

### 2.1 Transition Relation and Search Tree
The set of directed edges $E \subset \mathcal{X} \times \mathcal{X}$ defines the valid transitions from a partial permutation of length $k$ to a partial permutation of length $k+1$:

$$E = \left\{ (u, v) \;\middle|\; u = (p_1, \dots, p_k), \, v = (p_1, \dots, p_k, a_i) \text{ for some } a_i \in S_A \setminus \{p_1, \dots, p_k\} \right\}$$

For any state $u \in \mathcal{X} \setminus \mathcal{T}$, the set of its children (immediate successors) is defined by:

$$\text{children}(u) = \left\{ u \cdot a_i \;\middle|\; a_i \in S_A \setminus \text{set}(u) \right\}$$

where $\cdot$ denotes the concatenation operator, and $\text{set}(u)$ is the set of elements appearing in the tuple $u$.

### 2.2 State Representation and Invariants
At any step of the recursion, the algorithm maintains a global state tuple $(P, U)$, where:
1.  $P \in \mathcal{X}$ is the active path sequence representing the current partial permutation.
2.  $U \in \{0, 1\}^n$ is a boolean tracking vector (the `used` array) of size $n$.

The algorithm preserves the following **Representation Invariants** at the entry and exit of every recursive call:

$$\forall i \in \{1, \dots, n\}, \quad U_i = 1 \iff a_i \in \text{set}(P)$$

$$\forall i, j \in \{1, \dots, |P|\}, \quad i \neq j \implies P_i \neq P_j$$

### 2.3 Recursive Formulation of the Generator
Let $f: \mathcal{X} \to \mathcal{P}(\mathcal{P}(A))$ be a set-valued function that maps a partial state $P$ to the set of all complete permutations reachable from $P$. We define $f$ inductively:

$$f(P) = \begin{cases} 
\{ P \} & \text{if } |P| = n \\
\bigcup_{i \in \{1, \dots, n\}: U_i = 0} f(P \cdot a_i) & \text{if } |P| < n
\end{cases}$$

The primary objective of the algorithm is to compute $f(\epsilon)$, which yields the complete set of permutations:

$$f(\epsilon) = \mathcal{P}(A)$$

The correctness of the backtracking algorithm follows directly from this inductive definition, as the search tree is finite, acyclic, and every terminal node is visited exactly once.

---

## 3. Complexity Analysis

### 3.1 Time Complexity

To derive the time complexity, we analyze the total number of nodes visited in the state-transition tree $T$ and the computational work performed at each node.

#### 3.1.1 Node Count of the Search Tree
The search tree $T$ is structured into levels $k \in \{0, 1, \dots, n\}$, where level $k$ contains all partial permutations of length $k$. The number of nodes at level $k$, denoted by $N_k$, is the number of $k$-permutations of $n$ elements:

$$N_k = P(n, k) = \frac{n!}{(n-k)!}$$

The total number of nodes in the tree, $N_{\text{total}}$, is the sum over all levels:

$$N_{\text{total}} = \sum_{k=0}^{n} N_k = \sum_{k=0}^{n} \frac{n!}{(n-k)!} = n! \sum_{j=0}^{n} \frac{1}{j!}$$

Using the Taylor series expansion of the exponential function $e^x = \sum_{j=0}^{\infty} \frac{x^j}{j!}$, we bound the summation:

$$e - 1 < \sum_{j=0}^{n} \frac{1}{j!} < e \quad (\text{for } n \ge 1)$$

Thus, the total number of nodes in the search tree is strictly bounded:

$$n! \le N_{\text{total}} < e \cdot n!$$

This establishes that the total number of states visited is $\Theta(n!)$.

#### 3.1.2 Work Performed Per Node
We partition the work done by the algorithm into two categories:
1.  **Internal Nodes ($|P| < n$):** At each internal node of level $k$, the algorithm executes a loop of size $n$. Within each iteration, it performs $O(1)$ operations: checking the boolean array $U$, updating $U$, appending to $P$, recursing, and backtracking (popping from $P$ and resetting $U$). Thus, the local work at each internal node is $\Theta(n)$.
2.  **Leaf Nodes ($|P| = n$):** At each leaf node, the base case is triggered. The algorithm deep-copies the current path $P$ of length $n$ into the global result list. This copy operation requires $\Theta(n)$ operations.

#### 3.1.3 Total Time Complexity Derivation
Let $W(n)$ represent the total computational work:

$$W(n) = \sum_{k=0}^{n-1} \left( N_k \cdot \Theta(n) \right) + N_n \cdot \Theta(n)$$

$$W(n) = \Theta(n) \sum_{k=0}^{n} \frac{n!}{(n-k)!} = \Theta(n) \cdot \Theta(n!) = \Theta(n \cdot n!)$$

Thus, the overall time complexity is:

$$T(n) = \Theta(n \cdot n!)$$

---

### 3.2 Space Complexity

We analyze the space complexity by partitioning it into auxiliary space (working memory) and total space (including output storage).

#### 3.2.1 Auxiliary Space
The auxiliary space consists of the memory allocated on the call stack and the state variables:
1.  **Recursion Stack Depth:** The maximum depth of the recursion tree is $n + 1$ (corresponding to the path from the root $\epsilon$ to a leaf of length $n$). Each stack frame stores a constant number of references and primitive variables. Thus, the call stack space is $O(n)$.
2.  **State Variables:** 
    *   The path array $P$ stores at most $n$ elements: $O(n)$ space.
    *   The boolean tracking array $U$ stores exactly $n$ elements: $O(n)$ space.

Combining these components, the auxiliary space complexity is:

$$S_{\text{aux}}(n) = O(n)$$

#### 3.2.2 Total Space
If the space required to store the final output is included, the algorithm must store $n!$ permutations, where each permutation is an array of size $n$. The space required for the output is:

$$S_{\text{out}}(n) = \Theta(n \cdot n!)$$

Therefore, the total space complexity, including the output representation, is:

$$S_{\text{total}}(n) = \Theta(n \cdot n!)$$