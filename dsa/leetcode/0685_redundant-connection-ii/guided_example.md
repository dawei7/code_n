# Guided Example: Redundant Connection II

We trace the step-by-step directed in-degree accounting ($ind[v]$), dual-parent conflict detection ($\exists v: ind[v] == 2$), candidate parent edge pair collection ($dup = [e_1, e_2]$), trial edge exclusion simulation via Disjoint Set Union (testing if omitting $e_2$ eliminates cycles), pure directed cycle resolution (when all in-degrees equal $1$), and rooted tree topology restoration on representative directed graphs:

- **Input:** $edges = [[1, 2], [1, 3], [2, 3]]$
- **Required output:** `[2, 3]`
  - Directed rooted tree definition:
    - Exactly one root node has **in-degree 0**.
    - Every other node has **in-degree 1** (exactly one parent).
    - The graph is weakly connected and has **zero directed cycles**.
    - Adding one extra directed edge creates one of three possible structural defects:
      1. **Two Parents, No Cycle:** A node has in-degree 2; removing the later parent leaves a valid tree.
      2. **Two Parents, With a Cycle:** A node has in-degree 2, and exactly one of its incoming edges lies on a directed cycle. Removing that specific cycle-forming edge is mandatory.
      3. **Pure Cycle, No Node with Two Parents:** The extra edge points to the root (every node has in-degree 1). Removing the edge that closes the cycle restores the tree.
- **Structural Taxonomy & Disjoint Set Union Invariant:**
  - **Phase 1: In-Degree Accounting:**
    - Compute the in-degree of every node:
      $$
      ind[v] = \sum_{(u, v) \in edges} 1
      $$
    - If there exists a node $V$ with $ind[V] == 2$:
      - Record the two incoming edges $dup = [e_1, \; e_2]$ in order of appearance in the input.
  - **Phase 2: Decision Branching:**
    - **Branch A: A Node Has Two Parents ($dup$ is non-empty):**
      - One of $e_1$ or $e_2$ must be deleted.
      - We test a trial graph omitting $e_2$ (the later edge):
        - Process all other edges in forward order using Disjoint Set Union (DSU).
        - If DSU discovers a cycle while omitting $e_2$:
          - Then the cycle is caused by $e_1$!
          - Therefore, **$e_1$ must be removed** $\implies$ return $edges[dup[0]]$.
        - If DSU completes without finding any cycle:
          - Then omitting $e_2$ successfully leaves an acyclic valid tree!
          - Therefore, **$e_2$ is the redundant edge** $\implies$ return $edges[dup[1]]$.
    - **Branch B: No Node Has Two Parents ($dup$ is empty, all $ind \le 1$):**
      - The graph contains a pure directed cycle.
      - Run standard DSU across all edges: the first edge $(u, v)$ where $find(u) == find(v)$ closes the cycle.
      - Return that edge immediately.
- **Step-by-Step Worked Execution Trace on $edges = [[1, 2], [1, 3], [2, 3]]$ ($n = 3$):**
  - **Step 1: Calculate In-Degrees:**
    - Edge $[1, 2] \implies ind[2] = 1$.
    - Edge $[1, 3] \implies ind[3] = 1$.
    - Edge $[2, 3] \implies ind[3] = 1 + 1 = \mathbf{2}$.
    - Node 3 has **in-degree 2**!
  - **Step 2: Collect Candidate Edges for Node 3:**
    - Incoming edge 1: $edges[1] = [1, 3]$ (index $dup[0] = 1$).
    - Incoming edge 2: $edges[2] = [2, 3]$ (index $dup[1] = 2$).
    - Candidate pair: $dup = [1, 2]$.
  - **Step 3: Trial Simulation (Omit $e_2 = [2, 3]$):**
    - Initialize DSU parent array: $p = [0, 1, 2]$ for nodes $1, 2, 3$.
    - Iterate through edges, skipping index $dup[1] = 2$:
    - **Process Edge $0: [1, 2]$:**
      - $find(1) = 0, \; find(2) = 1$.
      - Roots differ ($0 \ne 1$) $\implies$ Union: $p[0] \leftarrow 1$.
      - Component: $\{1, 2\}$.
    - **Process Edge $1: [1, 3]$:**
      - $find(1) = 1, \; find(3) = 2$.
      - Roots differ ($1 \ne 2$) $\implies$ Union: $p[1] \leftarrow 2$.
      - Component: $\{1, 2, 3\}$.
    - **Edge 2: $[2, 3]$ is Skipped.**
    - All non-skipped edges processed with **zero cycles** detected!
  - **Step 4: Conclude Redundant Edge:**
    - Because omitting $e_2 = [2, 3]$ yields a connected acyclic tree, edge $[2, 3]$ is the redundant edge!
    - Return **`[2, 3]`**.
- **Two Parents with Cycle Trace ($edges = [[2, 1], [3, 1], [4, 2], [1, 4]]$):**
  - Node 1 has two parents: $e_1 = [2, 1]$ and $e_2 = [3, 1]$.
  - Omit $e_2 = [3, 1]$ and test remaining edges $[2, 1], [4, 2], [1, 4]$:
    - Path: $2 \to 1 \to 4 \to 2$ forms a cycle!
    - Because omitting $e_2$ still leaves a cycle, $e_1 = [2, 1]$ is part of the cycle and must be removed!
    - Output: `[2, 1]`.
- **Pure Directed Cycle Trace ($edges = [[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]]$):**
  - All nodes have in-degree 1. $dup = []$.
  - DSU unions $1-2, 2-3, 3-4$.
  - Edge $[4, 1]$ finds both endpoints already in root $4 \implies$ Cycle detected!
  - Output: `[4, 1]`.

This instance demonstrates directed graph degree constraint decomposition and counterfactual edge removal simulation, mathematically proves why trial verification of the second in-degree edge partitions cycle-forming and multi-parent anomalies, and derives $O(N \cdot \alpha(N))$ runtime and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a directed graph of $n$ nodes and $n$ edges:
Find the edge that can be removed to restore a **directed rooted tree**.
If multiple answers exist, return the one that appears **last in the input**.

```text
edges = [ [1, 2], [1, 3], [2, 3] ]

Directed edges:
  1 -> 2
  1 -> 3
  2 -> 3

Node 3 has in-degree 2 (incoming from 1 and 2)!
Candidates to remove: [1, 3] or [2, 3].

Test: omit [2, 3].
Remaining graph: 1 -> 2 and 1 -> 3.
Tree is valid and acyclic!
Result: [2, 3]
```

### The Invariant of the Three Anomaly Classes
1. **Node with in-degree 2, no cycle:** remove the later incoming edge ($dup[1]$).
2. **Node with in-degree 2, with cycle:** remove the incoming edge that lies on the cycle ($dup[0]$).
3. **No node with in-degree 2 (all in-degrees 1):** remove the edge that closes the directed cycle (standard DSU).

---

## 2. Conceptual Foundation & Invariants

### 1. In-Degree Classification:
$$
ind[v] = |\{u \mid (u, v) \in E\}|
$$
$$
dup = [i \mid edges[i] = (u, v) \land ind[v] == 2]
$$

### 2. The Trial Verification Rule:
If $dup$ is non-empty:
- Temporarily omit $edges[dup[1]]$.
- Run DSU over the remaining $n - 1$ edges.
- If a cycle occurs $\implies \text{return } edges[dup[0]]$.
- Else $\implies \text{return } edges[dup[1]]$.

> **Directed Arborescence Elimination Invariant.** A directed graph with $|V| = |E|$ is a directed rooted tree if and only if $\max_{v} ind(v) \le 1$ and the underlying undirected skeleton contains zero cycles; trial omission of the second multi-parent edge uniquely distinguishes cycle-entangled predecessors.

---

## 3. Step-by-Step Worked Execution

We trace $edges = [[1, 2], [1, 3], [2, 3]]$:

---

### Step 1: In-Degrees
- $ind[2] = 1$.
- $ind[3] = 2 \implies dup = [1, 2]$ (edges $[1, 3]$ and $[2, 3]$).

---

### Step 2: Omit $edges[2] = [2, 3]$
- Process $[1, 2]$: $Union(1, 2)$.
- Process $[1, 3]$: $Union(2, 3)$.
- Skip $[2, 3]$.

---

### Step 3: Check Cycle
- No cycle found in remaining edges.
- Return omitted edge: **`[2, 3]`**.

---

## 4. Complete Execution Trace

| Edge Stream $edges$ | In-Degree State | Node with $ind = 2$ | Candidates $dup$ | Trial Result Omission | Final Identified Edge |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `[[1, 2], [1, 3], [2, 3]]` | $ind[3] = 2$ | Node 3 | `[ [1, 3], [2, 3] ]` | Omitting `[2, 3]` is Acyclic | **`[2, 3]`** |
| `[[2, 1], [3, 1], [4, 2], [1, 4]]` | $ind[1] = 2$ | Node 1 | `[ [2, 1], [3, 1] ]` | Omitting `[3, 1]` leaves Cycle | **`[2, 1]`** |
| `[[1, 2], [2, 3], [3, 1]]` | All $ind = 1$ | None | $\emptyset$ | DSU detects cycle at `[3, 1]` | **`[3, 1]`** |

---

## 5. Boundary Cases & Failure Modes

- **Pure Directed Cycle:** Extra edge connects leaf to root $\implies$ handled by standard DSU without $dup$.
- **Two Parents Without Cycle:** Root splits into two paths that converge at a leaf $\implies$ trial omission cleanly succeeds.
- **Two Parents With Cycle:** Directed cycle passes through one parent $\implies$ DSU detects cycle during trial, selecting first parent.

---

## 6. Traps & Common Anti-Patterns

- **Using Plain Undirected DSU Without In-Degree Check:** Undirected DSU can delete the wrong edge on directed graphs with 2 parents (e.g., removing a valid tree edge instead of the dual parent).
- **Always Removing the Second Parent:** If the *first* parent is part of a cycle, removing the second parent leaves the cycle intact! The trial simulation is required to verify which parent is guilty.
- **Forgetting Tie-Breaking Rule:** When two edges are equally valid, the one appearing later in the input must be returned.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Counting in-degrees: $\mathcal{O}(N)$.
  - Single pass DSU trial run: $\mathcal{O}(N \cdot \alpha(N))$.
  - Total Time: $\mathcal{O}(N \cdot \alpha(N)) \approx \mathcal{O}(N)$. Completes in $< 1$ ms for $N = 1000$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space for in-degree and DSU parent arrays.
