# Guided Example: Possible Bipartition

We trace the step-by-step conflict graph construction, 2-coloring depth-first search traversal, alternating group assignment ($c \leftrightarrow 3 - c$), odd-cycle detection, and bipartition validation on representative social networks:

- **Input:**
  $$
  n = 4, \quad dislikes = [[1, 2], [1, 3], [2, 4]]
  $$
- **Required output:** `true`
  - Bipartition rules:
    - We want to split $n = 4$ people (labeled $1$ to $4$) into **two distinct groups** such that no two people who dislike each other are placed in the same group.
    - Each pair $[a, b] \in dislikes$ represents a mutual conflict.
    - Graph modeling:
      - Vertices: People $1, 2, 3, 4$.
      - Undirected edges: Dislike pairs $(1, 2), (1, 3), (2, 4)$.
    - Color assignment:
      - Assign person $1$ to Group 1 (Red).
      - Since $1$ dislikes $2$ and $3$, both $2$ and $3$ must be in Group 2 (Blue).
      - Since $2$ dislikes $4$, person $4$ must be in Group 1 (Red).
      - Check conflicts:
        - $(1, 2)$: Red vs Blue (Valid).
        - $(1, 3)$: Red vs Blue (Valid).
        - $(2, 4)$: Blue vs Red (Valid).
      - Valid groups: $\text{Group 1} = \{1, 4\}$, $\text{Group 2} = \{2, 3\}$.
      - Result: **`true`**.
- **The 2-Coloring & Odd-Cycle Invariant:**
  - **Bipartite Equivalence Theorem:**
    - A graph can be partitioned into two independent sets (2-colored) if and only if **it contains no odd-length cycles**.
  - **Alternating DFS State Machine:**
    - We track each node's status in an array $color$ of size $n$, initialized to $0$ (unvisited).
    - Colors are represented as $1$ (Group 1) and $2$ (Group 2).
    - Alternation rule: If current node has color $c$, any uncolored neighbor must receive color $3 - c$ ($3 - 1 = 2$, and $3 - 2 = 1$).
  - **Conflict Trigger:**
    - If a neighbor $v$ is already colored and $color[v] == c$, two people who dislike each other share the exact same group!
    - An odd cycle is detected $\implies$ immediate return `false`.
    - Because the graph may be disconnected, we iterate through all nodes $i \in [0, n - 1]$, initiating DFS from any uncolored node.

---

## 1. Instance & Teaching Goal

Given $n = 4$ and dislikes $[[1, 2], [1, 3], [2, 4]]$, demonstrate how DFS assigns alternating colors without conflict.

```text
Graph Structure:
  (1) [Red]  --- (2) [Blue] --- (4) [Red]
   |
  (3) [Blue]

DFS Propagation:
  Start at 1: Color(1) = Red (1)
  Visit neighbor 2: uncolored -> Color(2) = Blue (2)
  From 2, visit neighbor 4: uncolored -> Color(4) = Red (1)
  From 1, visit neighbor 3: uncolored -> Color(3) = Blue (2)

No neighbor has matching color -> Valid 2-Coloring!
Output: true
```

We also contrast this with the triangle $n = 3$, dislikes $[[1, 2], [1, 3], [2, 3]]$: coloring $1$ Red and $2$ Blue forces $3$ to be both Red (from 2) and Blue (from 1), creating a color collision (odd cycle) that returns `false`.

---

## 2. Conceptual Foundation & Invariants

### 1. Conflict Adjacency:
For each undirected pair $[u, v] \in dislikes$:
$$
u \in \text{Adj}[v] \quad \text{and} \quad v \in \text{Adj}[u]
$$

### 2. 2-Coloring DFS Recurrence:
$$
\text{dfs}(u, c):
$$
1. $color[u] \leftarrow c$
2. For each $v \in \text{Adj}[u]$:
   $$
   \begin{cases}
   \text{return } \mathbf{false} & \text{if } color[v] == c \\
   \text{if } color[v] == 0 \land \neg \text{dfs}(v, 3 - c) \implies \text{return } \mathbf{false}
   \end{cases}
   $$
3. Return $\mathbf{true}$.

---

## 3. Step-by-Step Worked Execution

0-indexed vertices: $0, 1, 2, 3$ (corresponding to people $1, 2, 3, 4$).
Edges: $(0, 1), (0, 2), (1, 3)$.
Initialize: $color = [0, 0, 0, 0]$.

---

### Step 1: Start Component at Node 0
- Assign color $c = 1$ (Red): $color[0] \leftarrow 1$.
- Inspect neighbors of Node $0$: $[1, 2]$.

---

### Step 2: Explore Edge $(0, 1)$
- Target Node $1$ has $color[1] == 0$ (unvisited).
- Recurse with alternate color: $3 - c = 3 - 1 = 2$ (Blue).
- Assign $color[1] \leftarrow 2$.
- Inspect neighbors of Node $1$: $[0, 3]$.
  - Neighbor $0$: $color[0] = 1 \ne 2$ (Valid opposite color).
  - Neighbor $3$: $color[3] == 0$ (unvisited).
- Recurse on Node $3$ with color $3 - 2 = 1$ (Red).
- Assign $color[3] \leftarrow 1$.
- Inspect neighbors of Node $3$: $[1]$.
  - Neighbor $1$: $color[1] = 2 \ne 1$ (Valid opposite color).
- Backtrack from Node $3 \to$ Node $1 \to$ Node $0$.

---

### Step 3: Explore Edge $(0, 2)$
- Target Node $2$ has $color[2] == 0$ (unvisited).
- Recurse with alternate color: $3 - 1 = 2$ (Blue).
- Assign $color[2] \leftarrow 2$.
- Inspect neighbors of Node $2$: $[0]$.
  - Neighbor $0$: $color[0] = 1 \ne 2$ (Valid opposite color).
- Backtrack to Node $0$.

---

### Step 4: Verification Across All Nodes
All nodes colored:
$$
color = [1, 2, 2, 1]
$$
- Red nodes (Color 1): $\{0, 3\} \implies \{1, 4\}$.
- Blue nodes (Color 2): $\{1, 2\} \implies \{2, 3\}$.
- No conflict exists anywhere in the graph!
- **Return: `true`**.

---

## 4. Complete Execution Trace

| DFS Step | Node $u$ | Assigned Color | Neighbor $v$ | Neighbor State ($color[v]$) | Conflict Check | Next Action |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| $1$ | Node $0$ | $1$ (Red) | Node $1$ | $0$ (Uncolored) | Safe | Recurse with color $2$ |
| $2$ | Node $1$ | $2$ (Blue) | Node $0$ | $1$ (Red) | $1 \ne 2$ (Safe) | Skip visited parent |
| $3$ | Node $1$ | $2$ (Blue) | Node $3$ | $0$ (Uncolored) | Safe | Recurse with color $1$ |
| $4$ | Node $3$ | $1$ (Red) | Node $1$ | $2$ (Blue) | $2 \ne 1$ (Safe) | Backtrack |
| $5$ | Node $0$ | $1$ (Red) | Node $2$ | $0$ (Uncolored) | Safe | Recurse with color $2$ |
| $6$ | Node $2$ | $2$ (Blue) | Node $0$ | $1$ (Red) | $1 \ne 2$ (Safe) | Backtrack |
| **End** | **All** | **Valid** | — | — | **No conflict** | **`Return true`** |

---

## 5. Boundary Cases & Failure Modes

- **No Dislikes ($dislikes = []$):** Edges are empty; every node is assigned color 1 independently $\implies$ returns `true`.
- **Odd Cycle / Triangle ($n = 3$, $(1, 2), (2, 3), (3, 1)$):** Node 3 connected to both 1 (Red) and 2 (Blue). Neighbor color equals own color $\implies$ returns `false`.
- **Even Cycle ($n = 4$, square $(1, 2), (2, 3), (3, 4), (4, 1)$):** Can be 2-colored alternately $1 \to 2 \to 1 \to 2 \implies$ returns `true`.
- **Disconnected Components:** Iterating over all uncolored nodes ensures separate components are colored independently.

---

## 6. Traps & Common Anti-Patterns

- **Assuming 1-Indexed Inputs Match 0-Indexed Arrays:** People are numbered $1 \dots n$. Subtracting $1$ prevents off-by-one index out-of-bounds errors.
- **Using Disjoint Set Union (Union-Find) Ineffectively:** DSU can solve bipartition by unioning each node with the "enemies" of its enemies. However, DFS 2-coloring is simpler, linear in time, and avoids path compression overhead.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Graph construction: $\mathcal{O}(|V| + |E|)$ where $|V| = n \le 2000$ and $|E| = |dislikes| \le 10^4$.
  - Depth-first search visits every vertex and edge at most once: $\mathcal{O}(|V| + |E|)$.
  - Total Time: strictly $\mathcal{O}(|V| + |E|)$, completing in $< 10$ ms.
- **Auxiliary Space Complexity:**
  - Adjacency list and color array: $\mathcal{O}(|V| + |E|)$ space.
