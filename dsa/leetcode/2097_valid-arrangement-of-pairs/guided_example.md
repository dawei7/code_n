# Guided Example: Valid Arrangement of Pairs

We trace the directed multigraph reduction, Eulerian trail start-node identification, and Hierholzer's post-order traversal on a representative collection of pairs:

- **Input Pairs:** `[[5, 1], [4, 5], [11, 9], [9, 4]]`
- **Number of Directed Edges $|E|$:** `4`
- **Expected Valid Arrangement:** `[[11, 9], [9, 4], [4, 5], [5, 1]]`

---

## 1. Problem Overview & Representative Instance

We are given a 2D integer array `pairs` where each element $\text{pairs}[i] = [u_i, v_i]$ represents a directed pair.
An arrangement of `pairs` is defined as **valid** if for every adjacent pair in the sequence, the second element of the previous pair equals the first element of the current pair:
$$\text{end}_{i-1} == \text{start}_i \quad \forall i \in \{1, \dots, |E|-1\}$$

### Graph-Theoretic Equivalence: Directed Eulerian Trail
Each pair $[u, v]$ can be modeled as a directed edge $u \to v$ in a directed multigraph $G = (V, E)$.
Arranging the pairs such that every pair is used exactly once and consecutive pairs connect end-to-start is mathematically equivalent to finding an **Eulerian trail** (or **Eulerian path**) in $G$.
- In an arbitrary directed graph, a naive depth-first search or greedy traversal easily enters a dead end before traversing all edges.
- Hierholzer's algorithm guarantees that by traversing edges iteratively and recording vertices in **post-order** (when all outgoing edges from a vertex are exhausted), sub-cycles are automatically spliced into the main path without getting trapped.

```mermaid
flowchart LR
    accTitle: Directed Multigraph for Eulerian Trail
    accDescr: Directed graph showing vertices 11, 9, 4, 5, 1 connected linearly by directed edges representing the input pairs.
    N11["Vertex 11 (out:1, in:0)"] -->|"[11, 9]"| N9["Vertex 9 (out:1, in:1)"]
    N9 -->|"[9, 4]"| N4["Vertex 4 (out:1, in:1)"]
    N4 -->|"[4, 5]"| N5["Vertex 5 (out:1, in:1)"]
    N5 -->|"[5, 1]"| N1["Vertex 1 (out:0, in:1)"]

    classDef startNode fill:#fef3c7,stroke:#b45309,stroke-width:2px;
    classDef endNode fill:#fee2e2,stroke:#b91c1c,stroke-width:2px;
    classDef intermediate fill:#dbeafe,stroke:#1d4ed8,stroke-width:1px;

    class N11 startNode;
    class N1 endNode;
    class N9,N4,N5 intermediate;
```

---

## 2. Invariants & Eulerian Trail Graph Theory

Let $G = (V, E)$ be a directed multigraph. For each vertex $v \in V$, let $\text{out}(v)$ denote the number of directed edges leaving $v$, and $\text{in}(v)$ denote the number of directed edges entering $v$.
Define the net degree imbalance:
$$\Delta(v) = \text{out}(v) - \text{in}(v)$$

### Invariant 1: Degree Balance Classification
Because the problem statement guarantees that a valid arrangement always exists, the multigraph must satisfy exactly one of two topological structures:
1. **Eulerian Circuit:** For every vertex $v \in V$, $\Delta(v) = 0$ ($\text{out}(v) = \text{in}(v)$). The trail starts and ends at the same vertex, and any vertex $v$ with $\text{out}(v) > 0$ can serve as the starting node.
2. **Open Eulerian Trail:** Exactly one vertex $s$ has $\Delta(s) = 1$ (the unique start node), exactly one vertex $t$ has $\Delta(t) = -1$ (the unique end node), and all other vertices $v \notin \{s, t\}$ have $\Delta(v) = 0$. The trail must strictly begin at $s$.

### Invariant 2: Hierholzer's Post-Order Splicing Invariant
During traversal, if a vertex $u$ has no remaining outgoing edges, any path departing $u$ has already been fully explored.
Appending $u$ to the trail history at the moment its outgoing edges are exhausted produces the **reverse** Eulerian trail.
Reversing this sequence reconstructs the canonical chronological traversal.

| Vertex $v$ | $\text{out}(v)$ | $\text{in}(v)$ | Imbalance $\Delta(v)$ | Topological Role |
|---|---|---|---|---|
| $11$ | $1$ | $0$ | $+1$ | Unique Trail Start ($\text{out} - \text{in} = 1$) |
| $9$ | $1$ | $1$ | $0$ | Balanced Intermediate Vertex |
| $4$ | $1$ | $1$ | $0$ | Balanced Intermediate Vertex |
| $5$ | $1$ | $1$ | $0$ | Balanced Intermediate Vertex |
| $1$ | $0$ | $1$ | $-1$ | Unique Trail End ($\text{out} - \text{in} = -1$) |

---

## 3. Step-by-Step Worked Execution

We trace `pairs = [[5, 1], [4, 5], [11, 9], [9, 4]]`.

### Step 1: Multigraph Construction & Degree Imbalance
Construct the adjacency lists and compute $\Delta(v)$:
- Edge $5 \to 1$: $\text{adj}[5] = [1]$, $\Delta(5) = +1$, $\Delta(1) = -1$.
- Edge $4 \to 5$: $\text{adj}[4] = [5]$, $\Delta(4) = +1$, $\Delta(5) = 0$.
- Edge $11 \to 9$: $\text{adj}[11] = [9]$, $\Delta(11) = +1$, $\Delta(9) = -1$.
- Edge $9 \to 4$: $\text{adj}[9] = [4]$, $\Delta(9) = 0$, $\Delta(4) = 0$.

Final degree states:
- $\Delta(11) = +1$
- $\Delta(1) = -1$
- $\Delta(9) = \Delta(4) = \Delta(5) = 0$

### Step 2: Determine Trail Start Vertex
We scan all vertices for $\Delta(v) == 1$:
- Vertex $11$ has $\Delta(11) = 1$.
- Thus, $s = 11$ is uniquely chosen as the start vertex.
- Initialize the traversal stack: $\text{stack} = [11]$.
- Initialize the post-order sequence: $\text{route} = []$.

### Step 3: Iterative Hierholzer Traversal
1. Top of stack is $11$.
   - $\text{adj}[11] = [9]$ is non-empty.
   - Pop edge to $9$: $\text{stack}$ becomes $[11, 9]$.
2. Top of stack is $9$.
   - $\text{adj}[9] = [4]$ is non-empty.
   - Pop edge to $4$: $\text{stack}$ becomes $[11, 9, 4]$.
3. Top of stack is $4$.
   - $\text{adj}[4] = [5]$ is non-empty.
   - Pop edge to $5$: $\text{stack}$ becomes $[11, 9, 4, 5]$.
4. Top of stack is $5$.
   - $\text{adj}[5] = [1]$ is non-empty.
   - Pop edge to $1$: $\text{stack}$ becomes $[11, 9, 4, 5, 1]$.
5. Top of stack is $1$.
   - $\text{adj}[1] = []$ (empty!). Dead end reached.
   - Pop $1$ from stack and append to $\text{route}$: $\text{route} = [1]$.
   - $\text{stack} = [11, 9, 4, 5]$.
6. Top of stack is $5$.
   - $\text{adj}[5] = []$ (empty).
   - Pop $5$ from stack and append to $\text{route}$: $\text{route} = [1, 5]$.
   - $\text{stack} = [11, 9, 4]$.
7. Top of stack is $4$.
   - $\text{adj}[4] = []$ (empty).
   - Pop $4$ and append: $\text{route} = [1, 5, 4]$.
   - $\text{stack} = [11, 9]$.
8. Top of stack is $9$.
   - $\text{adj}[9] = []$ (empty).
   - Pop $9$ and append: $\text{route} = [1, 5, 4, 9]$.
   - $\text{stack} = [11]$.
9. Top of stack is $11$.
   - $\text{adj}[11] = []$ (empty).
   - Pop $11$ and append: $\text{route} = [1, 5, 4, 9, 11]$.
   - $\text{stack} = []$ (traversal completed).

### Step 4: Reversal & Edge Pair Reconstruction
Reversing $\text{route}$ yields the forward path of vertices:
$$\text{path} = [11, 9, 4, 5, 1]$$
Reconstructing consecutive pairs $[\text{path}[i], \text{path}[i+1]]$:
$$[[11, 9], [9, 4], [4, 5], [5, 1]]$$
Every input pair is used exactly once, and consecutive endpoints match identically.

---

## 4. Complete Execution Trace & Stack Progression

| Iteration | Stack Top $u$ | Remaining $\text{adj}[u]$ | Action Taken | Current Stack | Accumulated $\text{route}$ |
|---|---|---|---|---|---|
| $0$ | $11$ | $[9]$ | Consume edge $11 \to 9$, push $9$ | $[11, 9]$ | $[]$ |
| $1$ | $9$ | $[4]$ | Consume edge $9 \to 4$, push $4$ | $[11, 9, 4]$ | $[]$ |
| $2$ | $4$ | $[5]$ | Consume edge $4 \to 5$, push $5$ | $[11, 9, 4, 5]$ | $[]$ |
| $3$ | $5$ | $[1]$ | Consume edge $5 \to 1$, push $1$ | $[11, 9, 4, 5, 1]$ | $[]$ |
| $4$ | $1$ | $[]$ | No outgoing edges: pop $1$ | $[11, 9, 4, 5]$ | $[1]$ |
| $5$ | $5$ | $[]$ | No outgoing edges: pop $5$ | $[11, 9, 4]$ | $[1, 5]$ |
| $6$ | $4$ | $[]$ | No outgoing edges: pop $4$ | $[11, 9]$ | $[1, 5, 4]$ |
| $7$ | $9$ | $[]$ | No outgoing edges: pop $9$ | $[11]$ | $[1, 5, 4, 9]$ |
| $8$ | $11$ | $[]$ | No outgoing edges: pop $11$ | $[]$ | $[1, 5, 4, 9, 11]$ |

---

## 5. Algorithmic Correctness & Soundness

### Proof of Hierholzer's Algorithm Correctness
1. **Eulerian Condition Sufficiency:**
   By Euler's Theorem for directed graphs, a weakly connected multigraph where all vertices have $\text{in}(v) = \text{out}(v)$, except possibly one start node with $\text{out}(s) - \text{in}(s) = 1$ and one end node with $\text{in}(t) - \text{out}(t) = 1$, contains an Eulerian trail.
2. **Cycle Splicing Guarantee:**
   When a forward walk from $u$ reaches a dead end, it must be at the trail's end node $t$ (or the start node $s$ in a circuit). Any vertex with exhausted edges has all its incident edges already placed in sub-trails.
3. **Post-Order Invariance:**
   Because a node is added to the result sequence only after its entire forward subgraph has been completely consumed, sub-cycles originating from any intermediate vertex $w$ are explored and returned before $w$ is added to the post-order sequence. Upon reversing the list, the sub-cycles appear seamlessly nested within the main walk.
4. **Edge Multiset Conservation:**
   Every pair $[u, v]$ corresponds to one element in $\text{adj}[u]$. Popping from $\text{adj}[u]$ exactly once ensures every edge is consumed with its exact multiplicity.

---

## 6. Structural Configurations & Boundary Behaviors

| Configuration | Structural Signature | Start Vertex Selection Rule | Traversal Outcome |
|---|---|---|---|
| Single Pair | One edge $u \to v$ | $\Delta(u) = 1$, choose $u$ | Trivial trail $[u, v]$ |
| Closed Cycle (Circuit) | $\Delta(v) = 0 \quad \forall v \in V$ | Any vertex with $\text{out}(v) > 0$ (e.g. $\text{pairs}[0][0]$) | Closed Eulerian circuit |
| Multiple Parallel Edges | Multi-edges between same $u, v$ | Imbalances accumulate correctly | Each copy of edge popped individually |
| Detached Sub-Cycle | Main path + loop attached to a node | Start at $\Delta = 1$; loop spliced via postorder | Complete trail traversing loop then continuing |

---

## 7. Complexity Analysis

- **Time Complexity:** $\mathcal{O}(|V| + |E|)$.
  - Constructing adjacency lists and computing degree imbalances takes $\mathcal{O}(|E|)$ time, where $|E| = \text{len}(\text{pairs})$.
  - Finding the starting vertex takes $\mathcal{O}(|V|)$ time.
  - Hierholzer's traversal visits each edge exactly once. Popping from an adjacency list takes $\mathcal{O}(1)$ time amortized.
  - Reversing the path and constructing the final pair list takes $\mathcal{O}(|E|)$ time.
  - Overall time complexity is strictly linear in the number of pairs: $\mathcal{O}(|E|)$.
- **Auxiliary Space Complexity:** $\mathcal{O}(|V| + |E|)$.
  - Adjacency hash maps store $|E|$ edges across $|V|$ vertices.
  - The traversal stack and post-order vertex buffer each store at most $|E| + 1$ elements.
  - Space complexity is optimal and linear in the input size.
