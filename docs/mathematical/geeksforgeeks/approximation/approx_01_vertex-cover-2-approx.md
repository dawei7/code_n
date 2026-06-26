# Formal Mathematical Specification: Vertex Cover (2-Approximation)

## 1. Definitions and Notation

Let $G = (V, E)$ be an undirected, simple graph, where:
*   $V = \{v_1, v_2, \dots, v_n\}$ is the finite set of vertices, with $|V| = n$.
*   $E \subseteq \{\{u, v\} \mid u, v \in V, u \neq v\}$ is the set of undirected edges, with $|E| = m$.

### Definition 1.1: Vertex Cover
A subset of vertices $C \subseteq V$ is a **vertex cover** of $G$ if and only if every edge in $E$ is incident to at least one vertex in $C$:
$$\forall \{u, v\} \in E, \quad \{u, v\} \cap C \neq \emptyset$$

### Definition 1.2: Minimum Vertex Cover
A vertex cover $C^* \subseteq V$ is a **minimum vertex cover** of $G$ if it minimizes the cardinality of the cover:
$$C^* \in \arg\min \{ |C| \mid C \subseteq V \text{ is a vertex cover of } G \}$$
We denote the size of the optimal vertex cover as $\tau(G) = |C^*|$. Finding $\tau(G)$ is NP-hard.

### Definition 1.3: Matching
A subset of edges $M \subseteq E$ is a **matching** in $G$ if no two edges in $M$ share a common vertex:
$$\forall e_1, e_2 \in M \text{ with } e_1 \neq e_2, \quad e_1 \cap e_2 = \emptyset$$
A matching $M$ is **maximal** if it cannot be extended by adding any other edge from $E$ without violating the pairwise disjointness property.

### Definition 1.4: State Space of the Approximation Algorithm
The execution of the 2-approximation algorithm can be modeled as a discrete-time transition system. The state space $\mathcal{S}$ is defined as:
$$\mathcal{S} = \{ (C, E') \mid C \subseteq V, \, E' \subseteq E \}$$
where:
*   $C$ represents the set of vertices currently selected for the vertex cover.
*   $E'$ represents the set of active, uncovered edges remaining in the graph.

---

## 2. Algebraic Characterization and Correctness

### 2.1. Algorithmic Transition System
Let $(C_k, E_k) \in \mathcal{S}$ denote the state of the algorithm at step $k \ge 0$.

*   **Initial State ($k = 0$):**
    $$C_0 = \emptyset, \quad E_0 = E$$

*   **State Transition ($k \to k+1$):**
    If $E_k \neq \emptyset$, select an arbitrary edge $e_k = \{u_k, v_k\} \in E_k$. The next state $(C_{k+1}, E_{k+1})$ is defined by the transition relations:
    $$C_{k+1} = C_k \cup \{u_k, v_k\}$$
    $$E_{k+1} = \{ \{x, y\} \in E_k \mid \{x, y\} \cap \{u_k, v_k\} = \emptyset \}$$

*   **Termination Condition:**
    The algorithm terminates at step $T$ when $E_T = \emptyset$. The output is the set $C = C_T$.

> **Remark on Code Discrepancy:** The Python code provided in the context implements a greedy heuristic based on maximum degree, which yields an $O(\log |V|)$-approximation. The mathematical specification below formalizes the *Edge-Picking 2-Approximation* algorithm described in the text, which guarantees a strict factor-2 approximation.

---

### 2.2. Loop Invariants
To prove the correctness and approximation ratio of the algorithm, we define the set of chosen edges at step $k$ as:
$$M_k = \{ e_i \in E \mid 0 \le i < k \}$$

#### Lemma 2.1: Matching Invariant
*For every step $k \ge 0$, the set $M_k$ is a matching in $G$.*

**Proof (By Induction):**
*   **Base Case ($k=0$):** $M_0 = \emptyset$, which is trivially a matching.
*   **Inductive Step:** Assume $M_k$ is a matching. At step $k$, we select $e_k = \{u_k, v_k\} \in E_k$. By definition of the transition relation, $E_k$ only contains edges that do not share any vertices with any previously selected edges in $M_k$ (since all incident edges were removed in prior steps). Thus, $\forall e \in M_k, e \cap e_k = \emptyset$. Consequently, $M_{k+1} = M_k \cup \{e_k\}$ is a matching. $\blacksquare$

#### Lemma 2.2: Covering Invariant
*For every step $k \ge 0$, the set of vertices $C_k$ is exactly the set of endpoints of the edges in $M_k$:*
$$C_k = \bigcup_{e \in M_k} e$$

**Proof:**
This follows directly from the transition rules: $C_0 = \emptyset$, and at each step, we add both endpoints of $e_k$ to $C_k$. Since $M_k$ is a matching, the endpoints of all $e \in M_k$ are pairwise disjoint, implying $|C_k| = 2|M_k|$. $\blacksquare$

---

### 2.3. Proof of Correctness and Approximation Ratio

#### Theorem 2.3: Validity of the Output Cover
*Upon termination at step $T$, the output set $C_T$ is a valid vertex cover of $G$.*

**Proof:**
Suppose for contradiction that $C_T$ is not a vertex cover. Then there exists an edge $e = \{u, v\} \in E$ such that $\{u, v\} \cap C_T = \emptyset$. 
Since $e \in E = E_0$ and $e \notin E_T$ (as $E_T = \emptyset$), there must exist some step $k < T$ where $e$ was removed from $E_k$. 
By the transition rule, an edge $e$ is removed from $E_k$ if and only if $e \cap \{u_k, v_k\} \neq \emptyset$. 
Since $\{u_k, v_k\} \subseteq C_{k+1} \subseteq C_T$, it follows that $e \cap C_T \neq \emptyset$, which contradicts our assumption. Thus, $C_T$ is a valid vertex cover. $\blacksquare$

#### Theorem 2.4: 2-Approximation Ratio
*The size of the vertex cover $C_T$ returned by the algorithm is at most twice the size of the minimum vertex cover $C^*$:*
$$|C_T| \le 2 \cdot |C^*|$$

**Proof:**
1.  Let $M_T$ be the matching constructed by the algorithm upon termination. By Lemma 2.2, $|C_T| = 2|M_T|$.
2.  Let $C^*$ be any optimal vertex cover of $G$. By Definition 1.1, $C^*$ must cover every edge in $G$.
3.  Since $M_T \subseteq E$ is a matching, its constituent edges are pairwise vertex-disjoint. Therefore, to cover the edges in $M_T$, any valid vertex cover (including $C^*$) must select at least one unique vertex for each edge in $M_T$:
    $$\forall e \in M_T, \quad |e \cap C^*| \ge 1$$
4.  Because the edges in $M_T$ share no vertices, we can sum these inequalities:
    $$|C^*| \ge \sum_{e \in M_T} |e \cap C^*| \ge |M_T|$$
5.  Combining $|C_T| = 2|M_T|$ and $|M_T| \le |C^*|$, we obtain:
    $$|C_T| \le 2 \cdot |C^*|$$
This completes the proof that the algorithm guarantees a 2-approximation. $\blacksquare$

---

## 3. Complexity Analysis

### 3.1. Time Complexity

To achieve optimal $O(|V| + |E|)$ time complexity, the algorithm is implemented using an adjacency list representation of $G$ along with an auxiliary boolean array to track covered vertices.

#### Formal Derivation:
Let $G = (V, E)$ be represented as an adjacency list $Adj$. We maintain:
1.  A boolean array $\text{visited}$ of size $|V|$, initialized to $\text{False}$.
2.  An output set $C$, initialized to $\emptyset$.

The algorithm iterates through the edge set $E$. For each edge $e = \{u, v\} \in E$:
$$\text{Work done per edge } e = \{u, v\}: \begin{cases} 
O(1) & \text{if } \text{visited}[u] = \text{True} \text{ or } \text{visited}[v] = \text{True} \\
O(1) \text{ updates} & \text{if } \text{visited}[u] = \text{False} \text{ and } \text{visited}[v] = \text{False}
\end{cases}$$

In the second case, we perform the following constant-time operations:
*   Add $u$ and $v$ to $C$.
*   Set $\text{visited}[u] = \text{True}$ and $\text{visited}[v] = \text{True}$.

The total time complexity $T(|V|, |E|)$ can be expressed as:
$$T(|V|, |E|) = \Theta(|V|) + \sum_{e \in E} O(1) = \Theta(|V| + |E|)$$

Thus, the worst-case, average-case, and best-case time complexity is:
$$\mathcal{O}(|V| + |E|)$$

---

### 3.2. Space Complexity

#### Auxiliary Space:
The auxiliary space consists of the data structures required to execute the approximation logic, excluding the input graph:
1.  The vertex cover set $C$: stores at most $|V|$ vertices, requiring $O(|V|)$ space.
2.  The tracking array $\text{visited}$: requires $O(|V|)$ space.

$$\text{Auxiliary Space} = \Theta(|V|)$$

#### Total Space:
The total space complexity includes the input graph representation. Using an adjacency list, the graph requires $\Theta(|V| + |E|)$ space.

$$\text{Total Space} = \Theta(|V| + |E|)$$