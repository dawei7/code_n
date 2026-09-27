# Guided Example: Strange Printer II

This guide examines how to determine whether a multicolored target grid can be printed using solid rectangular coats of paint, each color used at most once, by modeling color precedence as a directed graph and executing topological cycle detection.

- **Input Grid:**
  ```text
  [[1, 1, 1, 1],
   [1, 2, 2, 1],
   [1, 2, 2, 1],
   [1, 1, 1, 1]]
  ```
- **Output:** `true` (valid sequence: print color $1$ first, then print color $2$)

---

## 1. Instance & Teaching Goal

The strange printer operates under strict constraints:
1. Each printed area must be a solid axis-aligned rectangle $[r_1, r_2] \times [c_1, c_2]$.
2. Each distinct color may be printed at most once.
3. Later rectangular prints completely overwrite earlier painted cells.

For color $c$, let its minimal bounding box be the smallest rectangle enclosing all final cells of color $c$:
$$[\min r, \max r] \times [\min c, \max c]$$

If any cell $(r, c)$ inside color $a$'s bounding box has final target color $b \ne a$, then color $a$ must have been printed **before** color $b$, so that $b$'s subsequent print covers that cell with its final color. This introduces a directed precedence edge $a \to b$.

```
Color 1 Box: [0, 3] x [0, 3]    Color 2 Box: [1, 2] x [1, 2]
+ - - - - - - - - +             + - - - - - - - - +
| 1   1   1   1   |             | .   .   .   .   |
| 1  [2] [2]  1   |             | .   2   2   .   |
| 1  [2] [2]  1   |             | .   2   2   .   |
| 1   1   1   1   |             | .   .   .   .   |
+ - - - - - - - - +             + - - - - - - - - +
(Contains color 2: 1 -> 2)      (Pure color 2: no edges)
```

Our teaching goal is to trace:
1. Identifying bounding boxes across all distinct colors.
2. Formulating color dependencies as directed edges.
3. Evaluating graph acyclicity via Kahn's topological sort algorithm.

---

## 2. Conceptual Foundation & Invariants

```
+-------------------------------------------------------------------------+
|                 COLOR DEPENDENCY GRAPH CONSTRUCTION                     |
|                                                                         |
|  1. Bounding Box: For each color c:                                     |
|     top = min(r), bottom = max(r), left = min(c), right = max(c)        |
|                                                                         |
|  2. Directed Precedence Edge:                                           |
|     For each cell (r, c) in bounding box of color a:                   |
|     If targetGrid[r][c] = b (b != a):                                   |
|         Add directed edge: a -> b                                       |
|         (Color a must be painted BEFORE color b overwrites it)          |
|                                                                         |
|  3. Solvability Condition:                                              |
|     A print schedule exists <=> Directed graph G is a DAG (no cycles)   |
+-------------------------------------------------------------------------+
```

| Element | Mathematical Definition | Role in Feasibility Test |
|---|---|---|
| Color Set $\mathcal{C}$ | $\{ \text{grid}[r][c] : (r, c) \in R \times C \}$ | Set of active printer operations |
| Bounding Box $B(c)$ | $[r_{\min}(c), r_{\max}(c)] \times [c_{\min}(c), c_{\max}(c)]$ | Minimal unavoidable region painted when applying color $c$ |
| Directed Edge $u \to v$ | $\exists (r, c) \in B(u) \text{ s.t. } \text{grid}[r][c] = v$ | Enforces temporal order: print $u$ strictly before $v$ |
| In-degree $d_{\text{in}}(v)$ | $|\{ u \in \mathcal{C} : u \to v \}|$ | Count of prerequisite colors that must precede $v$ |

> **Acyclicity Equivalence Invariant.** A target grid is printable if and only if the color precedence graph contains zero directed cycles. An edge $u \to v$ mandates that $u$ precedes $v$. A directed cycle $c_1 \to c_2 \to \dots \to c_k \to c_1$ demands that $c_1$ precede itself, which is impossible under single-use printing.

```mermaid
flowchart LR
    accTitle: Strange Printer Color Precedence Graph
    accDescr: Directed dependency graph showing color 1 must be printed before color 2.
    C1["Color 1: Outer Border"] -->|"Box contains Color 2"| C2["Color 2: Inner Square"]
```

---

## 3. Step-by-Step Worked Execution

### Step 1: Compute Bounding Boxes

Scanning the $4 \times 4$ grid reveals two distinct colors: $\mathcal{C} = \{1, 2\}$.
- **Color 1:**
  - Row occurrences: rows $0, 1, 2, 3 \implies [r_{\min}, r_{\max}] = [0, 3]$.
  - Col occurrences: cols $0, 1, 2, 3 \implies [c_{\min}, c_{\max}] = [0, 3]$.
  - Bounding box $B(1) = [0, 3] \times [0, 3]$ (entire grid).
- **Color 2:**
  - Row occurrences: rows $1, 2 \implies [r_{\min}, r_{\max}] = [1, 2]$.
  - Col occurrences: cols $1, 2 \implies [c_{\min}, c_{\max}] = [1, 2]$.
  - Bounding box $B(2) = [1, 2] \times [1, 2]$ (central $2 \times 2$ square).

---

### Step 2: Establish Directed Precedence Edges

- **Inspect Bounding Box $B(1)$:**
  - Cells $(1, 1), (1, 2), (2, 1), (2, 2)$ contain color $2$.
  - Because color $1$'s print covers these cells, color $2$ must be printed after color $1$ to overwrite them.
  - Add edge: $1 \to 2$.
- **Inspect Bounding Box $B(2)$:**
  - Cells $(1, 1), (1, 2), (2, 1), (2, 2)$ contain only color $2$.
  - No foreign colors reside in $B(2)$.
  - Outgoing edges from $2$: $\emptyset$.

Resulting Dependency Graph:
- Vertices: $\{1, 2\}$
- Directed Edges: $\{1 \to 2\}$
- In-degrees: $d_{\text{in}}(1) = 0$, $d_{\text{in}}(2) = 1$.

---

### Step 3: Kahn's Topological Sorting Algorithm

- **Queue Initialization:** Find vertices with in-degree $0$:
  $$\text{Ready Queue} = [1]$$
  $\text{Processed Count} = 0$.

- **Iteration 1:**
  - Pop color $1$. Increment $\text{Processed Count} \leftarrow 1$.
  - Remove outgoing edge $1 \to 2$:
    $$d_{\text{in}}(2) \leftarrow d_{\text{in}}(2) - 1 = 0$$
  - Since $d_{\text{in}}(2) = 0$, push color $2$ into the ready queue.
  - $\text{Ready Queue} = [2]$.

- **Iteration 2:**
  - Pop color $2$. Increment $\text{Processed Count} \leftarrow 2$.
  - Color $2$ has no outgoing edges.
  - Ready queue is now empty.

- **Termination:**
  - $\text{Processed Count} = 2 = |\mathcal{C}|$.
  - All colors successfully ordered without cycle conflict. Return `true`.

---

## 4. Complete Execution Trace

| Step | Active Color / Event | Bounding Box Inspected | Foreign Colors Detected | Dependency Graph Mutation | Ready Queue |
|---|---|---|---|---|---|
| 1 | Box Analysis $c = 1$ | Rows $[0, 3]$, Cols $[0, 3]$ | $2$ at $(1, 1), (1, 2), (2, 1), (2, 2)$ | Add $1 \to 2$; $d_{\text{in}}(2) \mathrel{+}= 1$ | — |
| 2 | Box Analysis $c = 2$ | Rows $[1, 2]$, Cols $[1, 2]$ | None | No new edges | — |
| 3 | Initialize Kahn's | Initial degree scan | $d_{\text{in}}(1) = 0, d_{\text{in}}(2) = 1$ | Vertices with $d_{\text{in}} = 0$ queued | `[1]` |
| 4 | Pop Color $1$ | Print step 1 (Background) | Outgoing edge to $2$ relaxed | $d_{\text{in}}(2) \leftarrow 0$ | `[2]` |
| 5 | Pop Color $2$ | Print step 2 (Foreground) | None | No further edges | `[]` |
| 6 | Evaluate Termination | Verify processed count | $2$ colors processed out of $2$ | Acyclic DAG confirmed | Emits `true` |

---

## 5. Algorithmic Correctness

**Soundness.** Suppose the graph contains no directed cycles. Then there exists a valid topological sort order $c_{\pi_1}, c_{\pi_2}, \dots, c_{\pi_K}$. Printing the bounding rectangles in this exact chronological order guarantees correctness: when printing color $c_{\pi_i}$, it correctly sets all its final cells. Any cell belonging to a different final color $c_{\pi_j}$ within $B(c_{\pi_i})$ generated an edge $c_{\pi_i} \to c_{\pi_j}$, ensuring $c_{\pi_j}$ appears strictly later in the order ($\pi_i < \pi_j$). Thus, $c_{\pi_j}$ will overwrite the intermediate paint, leaving the desired target color intact.

**Completeness.** Any rectangular print of color $u$ unavoidably covers the entire bounding box $B(u)$ because a rectangle is convex and axis-aligned. If a cell inside $B(u)$ has target color $v$, $v$ must be applied after $u$. A circular chain of dependencies $u_1 \to u_2 \to \dots \to u_m \to u_1$ imposes the impossible condition that each color must be printed strictly before the next, while $u_m$ must precede $u_1$. Therefore, cyclic dependency graphs are unprintable.

---

## 6. Traps This Instance Exposes

- **Duplicate Edge Accumulation:** A single foreign color $v$ may appear dozens of times inside $B(u)$. Adding duplicate directed edges will artificially inflate the in-degree $d_{\text{in}}(v)$ above $1$ for that predecessor, preventing $v$ from ever reaching $0$ during topological relaxation. Graph edges must be stored in a set.
- **Unbounded Search Space:** Attempting to brute-force all color permutations leads to $\mathcal{O}(C!)$ complexity, which fails for $C \le 60$. Formulating the problem as graph acyclicity reduces runtime to polynomial time.
- **Disconnected Components:** The dependency graph may consist of multiple disjoint trees or isolated vertices (e.g. non-overlapping color blocks). Kahn's algorithm correctly handles arbitrary DAG topologies by initializing the queue with all zero-degree nodes simultaneously.

---

## 7. Complexity Derivation

- **Time Complexity:** $\mathcal{O}(C \cdot R \cdot K + C^2)$, where $R$ and $K$ are grid rows and columns, and $C \le 60$ is the number of distinct colors. Scanning the grid to compute bounding boxes takes $\mathcal{O}(R \cdot K)$. Checking each color's bounding box to build directed edges takes at most $\mathcal{O}(C \cdot R \cdot K)$. Topological sorting across $C$ vertices and at most $C(C-1)$ edges takes $\mathcal{O}(C + C^2)$.
- **Auxiliary Space Complexity:** $\mathcal{O}(C^2)$ to store the adjacency matrix or adjacency sets and in-degree table for up to $C = 60$ colors.
