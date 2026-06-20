# Formal Mathematical Specification: Combination Sum

## 1. Definitions and Notation

To establish a rigorous foundation for the **Combination Sum** algorithm, we define the input parameters, the output space, and the state space of the backtracking search using formal set theory and algebraic structures.

### 1.1 Input Space
Let $C$ be a finite set of $N$ distinct positive integers representing the candidates:
$$C = \{c_1, c_2, \dots, c_N\} \subset \mathbb{Z}^+$$
Without loss of generality, we assume the elements of $C$ are sorted in strictly increasing order:
$$c_1 < c_2 < \dots < c_N$$
Let $T \in \mathbb{Z}^+$ denote the target sum.

### 1.2 Output Space (The Solution Set)
A valid combination is a multiset of elements from $C$ that sums to $T$. To avoid duplicate representations and enforce uniqueness, we represent each combination uniquely as a non-decreasing sequence (or tuple) $P$.

Let $P = (p_1, p_2, \dots, p_k)$ be a sequence of length $k \ge 1$. We define the set of all valid combinations $\mathcal{P}(C, T)$ as:
$$\mathcal{P}(C, T) = \left\{ (p_1, p_2, \dots, p_k) \in C^k \;\middle|\; k \in \mathbb{Z}^+, \ \sum_{j=1}^k p_j = T, \text{ and } p_j \le p_{j+1} \ \forall j \in \{1, \dots, k-1\} \right\}$$

Alternatively, we can characterize the solution set using a multiplicity vector $x = (x_1, x_2, \dots, x_N) \in \mathbb{N}_0^N$, where $x_i$ represents the frequency of candidate $c_i$ in the combination:
$$\mathcal{S}(C, T) = \left\{ (x_1, x_2, \dots, x_N) \in \mathbb{N}_0^N \;\middle|\; \sum_{i=1}^N x_i c_i = T \right\}$$
There exists a bijection $\phi: \mathcal{P}(C, T) \to \mathcal{S}(C, T)$ mapping each sorted sequence to its corresponding multiplicity vector.

### 1.3 Backtracking State Space
The backtracking algorithm systematically explores a state space tree. A search state $u$ is defined as a triple:
$$u = (i, R, P) \in \mathcal{X}$$
where:
*   $i \in \{1, \dots, N\}$ is the **start index**, restricting choices to the suffix $\{c_i, \dots, c_N\}$ to prevent duplicate permutations (e.g., generating both $(2, 3)$ and $(3, 2)$).
*   $R \in \mathbb{Z}_{\ge 0}$ is the **remaining target** sum.
*   $P = (p_1, \dots, p_d)$ is the **current path** (sequence of choices made so far) of depth $d \ge 0$.

The formal state space $\mathcal{X}$ is defined as:
$$\mathcal{X} = \left\{ (i, R, P) \;\middle|\; 1 \le i \le N, \ 0 \le R \le T, \ P \in C^d, \ \sum_{y \in P} y = T - R \right\}$$

---

## 2. Algebraic Characterization

The backtracking algorithm can be modeled as a directed state-transition graph $G = (\mathcal{X}, E)$, where the set of directed edges $E$ represents valid single-step decisions.

### 2.1 State Transition Relation
For any state $u = (i, R, P) \in \mathcal{X}$ where $R > 0$, a transition to a child state $u'$ exists for each candidate $c_j$ that does not violate the ordering or exceed the remaining target:
$$(i, R, P) \xrightarrow{c_j} (j, R - c_j, P \parallel c_j)$$
where:
*   $j \in \{i, \dots, N\}$ (enforces non-decreasing order of elements in $P$).
*   $c_j \le R$ (pruning condition).
*   $P \parallel c_j$ denotes the concatenation of the sequence $P$ with the element $c_j$.

### 2.2 Recurrence Relation
Let $f(i, R)$ be a set-valued function returning all valid suffix-restricted sequences of elements from $\{c_i, \dots, c_N\}$ that sum to $R$. We define $f(i, R)$ recursively as:

$$f(i, R) = \begin{cases} 
\{ () \} & \text{if } R = 0 \\
\emptyset & \text{if } R < 0 \text{ or } i > N \\
\bigcup_{j=i}^{N} \left\{ (c_j) \parallel p \;\middle|\; p \in f(j, R - c_j) \right\} & \text{otherwise}
\end{cases}$$

#### Sorting Optimization and Early Pruning
Because the candidate array $C$ is sorted ($c_1 < c_2 < \dots < c_N$), if $c_j > R$ for some $j \ge i$, then for all $k \ge j$, $c_k > R$. This allows us to truncate the union:
$$f(i, R) = \bigcup_{\substack{j=i \\ c_j \le R}}^{N} \left\{ (c_j) \parallel p \;\middle|\; p \in f(j, R - c_j) \right\}$$
This algebraic formulation guarantees that the search space is pruned immediately when a candidate exceeds the remaining target, preventing the exploration of redundant subtrees.

### 2.3 Correctness Proof Sketch
The correctness of the algorithm is established by induction on the remaining target $R$.
*   **Base Case ($R = 0$):** The empty sequence $()$ is the unique sequence summing to $0$. $f(i, 0) = \{()\}$, which is correct.
*   **Inductive Step:** Assume $f(j, R - c_j)$ correctly computes all valid non-decreasing sequences summing to $R - c_j$ using elements from $\{c_j, \dots, c_N\}$. By prepending $c_j$ to each sequence in $f(j, R - c_j)$, we obtain sequences summing to $c_j + (R - c_j) = R$. Since $j \ge i$, the prepended element $c_j$ is less than or equal to all elements in the sequences of $f(j, R - c_j)$, preserving the non-decreasing order. Taking the union over all valid $j \ge i$ yields exactly the set of all non-decreasing sequences summing to $R$ starting with an element index $\ge i$.

---

## 3. Complexity Analysis

### 3.1 Time Complexity

Let $M = \min(C) = c_1$ be the smallest candidate in $C$. 

#### 3.1.1 Maximum Depth of the Search Tree
The maximum depth $D$ of the recursion tree occurs when we repeatedly choose the smallest element $c_1$:
$$D = \left\lfloor \frac{T}{M} \right\rfloor$$

#### 3.1.2 Upper Bound on the Number of States
At each node in the search tree, we can branch up to $N$ times. A loose upper bound on the total number of nodes in the search tree is given by the sum of a geometric series:
$$\sum_{d=0}^{D} N^d = \frac{N^{D+1} - 1}{N - 1} = O\left(N^D\right) = O\left(N^{T/M}\right)$$

#### 3.1.3 Tight Combinatorial Bound
Because we enforce a non-decreasing order on the paths ($j \ge i$), we do not explore all permutations of a combination. The number of unique non-decreasing sequences of length at most $D$ using $N$ elements is equivalent to the number of combinations with repetition (multicombinations):
$$\left(\!\left( \begin{matrix} N \\ D \end{matrix} \right)\!\right) = \binom{N + D - 1}{D}$$

Summing over all possible depths $d \le D$:
$$\sum_{d=0}^{D} \binom{N + d - 1}{d} = \binom{N + D}{D} = \binom{N + \lfloor T/M \rfloor}{\lfloor T/M \rfloor}$$

At each leaf node representing a valid solution, copying the path of length at most $D$ to the output list takes $O(D) = O(T/M)$ time. Thus, the tight asymptotic time complexity is bounded by:
$$\mathcal{O}\left( \frac{T}{M} \cdot \binom{N + T/M}{T/M} \right)$$
In the worst-case scenario where $N \gg T/M$, this is loosely bounded by $O\left( N^{T/M} \right)$.

---

### 3.2 Space Complexity

The space complexity is analyzed in terms of auxiliary space (memory used by the algorithm during execution, excluding the output storage).

#### 3.2.1 Recursion Stack Space
The maximum depth of the call stack corresponds to the maximum height of the state-space tree. The deepest branch is explored when the algorithm repeatedly selects the minimum element $M = c_1$. The maximum stack depth is:
$$\text{Depth}_{\max} = \left\lfloor \frac{T}{M} \right\rfloor$$
Each stack frame stores a constant number of variables ($start$, $remaining$, and loop indices), requiring $O(1)$ space per frame.

#### 3.2.2 Path Storage Space
The algorithm maintains a dynamic array `path` to store the current combination sequence. The maximum size of this array is bounded by the maximum depth of the tree:
$$\text{Size}_{\max}(\text{path}) = \left\lfloor \frac{T}{M} \right\rfloor$$

#### 3.2.3 Total Auxiliary Space
Combining the recursion stack and the path storage, the auxiliary space complexity is:
$$\mathcal{O}\left(\text{Depth}_{\max} + \text{Size}_{\max}(\text{path})\right) = \mathcal{O}\left(\frac{T}{M}\right)$$

If the space required to store the final output list is included, the total space complexity is:
$$\mathcal{O}\left( \frac{T}{M} \cdot \left| \mathcal{P}(C, T) \right| + \frac{T}{M} \right)$$
where $\left| \mathcal{P}(C, T) \right|$ is the total number of valid combinations.