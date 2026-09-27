# Guided Example: Clone Graph

We trace the step-by-step deep copying of an undirected cyclic graph using a hash-mapped DFS/BFS traversal on a representative 4-node cycle:

- **Input:** `adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]` (A 4-node cycle $1 - 2 - 3 - 4 - 1$)
- **Required output:** Deep-cloned copy of the graph with identical topology
- **Base Instances:** $\text{node} = \emptyset \implies \emptyset, \quad \text{adjList} = [[]] \implies \text{Node}(1)$ (isolated node)

This instance demonstrates deep cloning mutable cyclic graph structures, preventing infinite recursion via an `original -> clone` hash map, registering clones *before* neighbor recursion, and verifying structural isomorphism in $O(V + E)$ time and $O(V)$ space.

---

## 1. Instance & Teaching Goal

Given a reference to a node in a connected undirected graph:
$$
\begin{matrix}
1 & \text{---} & 2 \\
\mid & & \mid \\
4 & \text{---} & 3
\end{matrix}
$$
where `adjList` defines each node's neighbors:
- Node 1: `[Node(2), Node(4)]`
- Node 2: `[Node(1), Node(3)]`
- Node 3: `[Node(2), Node(4)]`
- Node 4: `[Node(1), Node(3)]`

Return a **deep copy (clone)** of the graph.
A valid clone satisfies three conditions:
1. **Object Independence:** Every node in the cloned graph must be a newly allocated `Node` instance (e.g. $\text{clone}(u) \ne u$).
2. **Topological Isomorphism:** If an edge $(u, v)$ exists in the original graph, an edge $(\text{clone}(u), \text{clone}(v))$ must exist in the clone.
3. **No Reference Leakage:** No neighbor list in the clone may point to an original node object.

Because undirected graphs contain cycles (e.g. $1 \leftrightarrow 2$), a naive recursive copy without cycle tracking will ping-pong infinitely between neighbors.
Using a hash map `clones: OriginalNode -> ClonedNode` guarantees that each vertex is instantiated exactly once, resolving back-edges to already-instantiated clone references.

---

## 2. Conceptual Foundation & Invariants

### Hash-Mapped DFS Clone Protocol
Maintain a dictionary `clones = {}`.
Define `clone(node)`:

1. **Null Guard:**
   If $\text{node} == \emptyset$: return $\emptyset$.
2. **Cycle & Visited Check:**
   If $\text{node} \in \text{clones}$:
   Return the already created clone:
   $$
   \text{return } \text{clones}[\text{node}]
   $$
3. **Instantiate Clone:**
   Create a new node with identical value:
   $$
   \text{copy} = \text{Node}(\text{node.val})
   $$
4. **Register Immediately in Hash Map (Pre-Recursion):**
   $$
   \text{clones}[\text{node}] \leftarrow \text{copy}
   $$
   *(Registering `copy` BEFORE recursing on neighbors is mandatory to break cyclic back-references)*.
5. **Recursively Populate Neighbors:**
   For each neighbor $v \in \text{node.neighbors}$:
   $$
   \text{copy.neighbors.append}(\text{clone}(v))
   $$
6. **Return Completed Clone:**
   $$
   \text{return } \text{copy}
   $$

> **Invariant.** For every original node $u$ that has been visited, `clones[u]` points to its unique corresponding clone, and `clones[u].val == u.val`.

---

## 3. Step-by-Step Worked Execution

We trace the recursive DFS calls on the 4-cycle graph starting from Node 1:

### Step 1: Call `clone(Node 1)`
- Node 1 not in `clones`.
- Create new node: $C_1 = \text{Node}(1)$.
- Register: $\text{clones}[N_1] \leftarrow C_1$.
- Inspect neighbors of Node 1: $[N_2, N_4]$.
- Recurse on first neighbor: `clone(Node 2)`.

---

### Step 2: Call `clone(Node 2)`
- Node 2 not in `clones`.
- Create new node: $C_2 = \text{Node}(2)$.
- Register: $\text{clones}[N_2] \leftarrow C_2$.
- Inspect neighbors of Node 2: $[N_1, N_3]$.
- **First Neighbor of 2 ($N_1$):**
  - Call `clone(Node 1)`.
  - $N_1 \in \text{clones}$!
  - **Cycle Broken:** Returns existing reference $C_1$.
  - $C_2.\text{neighbors.append}(C_1)$.
- **Second Neighbor of 2 ($N_3$):**
  - Call `clone(Node 3)`.

---

### Step 3: Call `clone(Node 3)`
- Node 3 not in `clones`.
- Create new node: $C_3 = \text{Node}(3)$.
- Register: $\text{clones}[N_3] \leftarrow C_3$.
- Inspect neighbors of Node 3: $[N_2, N_4]$.
- **First Neighbor of 3 ($N_2$):**
  - $N_2 \in \text{clones} \implies$ returns $C_2$.
  - $C_3.\text{neighbors.append}(C_2)$.
- **Second Neighbor of 3 ($N_4$):**
  - Call `clone(Node 4)`.

---

### Step 4: Call `clone(Node 4)`
- Node 4 not in `clones`.
- Create new node: $C_4 = \text{Node}(4)$.
- Register: $\text{clones}[N_4] \leftarrow C_4$.
- Inspect neighbors of Node 4: $[N_1, N_3]$.
- **First Neighbor of 4 ($N_1$):**
  - $N_1 \in \text{clones} \implies$ returns $C_1$.
  - $C_4.\text{neighbors.append}(C_1)$.
- **Second Neighbor of 4 ($N_3$):**
  - $N_3 \in \text{clones} \implies$ returns $C_3$.
  - $C_4.\text{neighbors.append}(C_3)$.
- Node 4 has completed both neighbors! Returns $C_4$ to Node 3.

---

### Step 5: Unwinding the Call Stack
- Node 3 receives $C_4$: $C_3.\text{neighbors.append}(C_4)$. Returns $C_3$ to Node 2.
- Node 2 receives $C_3$. Returns $C_2$ to Node 1.
- Node 1 appends $C_2$: $C_1.\text{neighbors.append}(C_2)$.
- Node 1 inspects second neighbor $N_4$:
  - Call `clone(Node 4)`.
  - $N_4 \in \text{clones} \implies$ returns existing $C_4$.
  - $C_1.\text{neighbors.append}(C_4)$.
- Node 1 completes both neighbors: $C_1.\text{neighbors} = [C_2, C_4]$.
- Return $C_1$.

Deep clone complete! All 4 nodes cloned with preserved cycles.

---

## 4. Complete Execution Trace

```text
Original Graph:                           Cloned Graph:
   N1(1) --- N2(2)                           C1(1) --- C2(2)
    |         |                               |         |
   N4(4) --- N3(3)                           C4(4) --- C3(3)

clones = { N1: C1, N2: C2, N3: C3, N4: C4 }
```

| Recursion Step | Active Node $u$ | In `clones`? | Action Taken | Clone Instantiated | Cloned Neighbors Appended |
|:---:|:---:|:---:|:---|:---:|:---|
| 1 | Node 1 | No | Create $C_1$, register, recurse on 2 | $C_1$ | Awaiting $C_2, C_4$ |
| 2 | Node 2 | No | Create $C_2$, register, recurse on 1 | $C_2$ | Append $C_1$ (cycle link) |
| 2.1 | Node 1 | **Yes** | Return existing $C_1$ | - | - |
| 2.2 | Node 3 | No | Create $C_3$, register, recurse on 2 | $C_3$ | Append $C_2$ (cycle link) |
| 2.2.1 | Node 2 | **Yes** | Return existing $C_2$ | - | - |
| 2.2.2 | Node 4 | No | Create $C_4$, register, recurse on 1 | $C_4$ | Append $C_1$, Append $C_3$ |
| 2.2.2.1 | Node 1 | **Yes** | Return existing $C_1$ | - | - |
| 2.2.2.2 | Node 3 | **Yes** | Return existing $C_3$ | - | - |
| Returns | All unwound | - | Full cycle connected | - | $C_1$ links $[C_2, C_4]$ |

The same eight directed adjacency entries are resolved in this order. No row ever looks up a vertex that is absent from `clones` except the three that instantiate a new clone, and the last four rows are closure work performed while the stack unwinds:

| # | Directed entry $(u, v)$ | `clones` at the lookup | $v$ found? | Role of the entry | Clone neighbor list afterwards |
|:---:|:---|:---|:---:|:---|:---|
| 1 | $(N_2, N_1)$ | `{N1: C1, N2: C2}` | yes, $C_1$ | back edge to the parent while $N_2$ is still open | `C2.neighbors = [C1]` |
| 2 | $(N_3, N_2)$ | `{N1: C1, N2: C2, N3: C3}` | yes, $C_2$ | back edge to the parent while $N_3$ is still open | `C3.neighbors = [C2]` |
| 3 | $(N_4, N_1)$ | `{N1: C1, N2: C2, N3: C3, N4: C4}` | yes, $C_1$ | back edge to the root, three frames deep | `C4.neighbors = [C1]` |
| 4 | $(N_4, N_3)$ | unchanged | yes, $C_3$ | back edge to the parent | `C4.neighbors = [C1, C3]` |
| 5 | $(N_3, N_4)$ | unchanged | yes, $C_4$ | tree edge closed as $N_4$ returns | `C3.neighbors = [C2, C4]` |
| 6 | $(N_2, N_3)$ | unchanged | yes, $C_3$ | tree edge closed as $N_3$ returns | `C2.neighbors = [C1, C3]` |
| 7 | $(N_1, N_2)$ | unchanged | yes, $C_2$ | tree edge closed as $N_2$ returns | `C1.neighbors = [C2]` |
| 8 | $(N_1, N_4)$ | unchanged | yes, $C_4$ | cycle-closing back edge, never a new descent | `C1.neighbors = [C2, C4]` |

Row 3 is the row that proves the protocol. $C_4$ exists in `clones` with an empty neighbor list at that moment, so the lookup succeeds even though $N_4$'s own recursion is still in progress; the entry $(N_4, N_1)$ therefore closes a path back to the root without allocating anything. Had registration been deferred until after the neighbor loop, rows 1 and 3 would both miss and the descent would restart instead of stopping.

---

## 5. Algorithmic Correctness

**Soundness.** A graph is a set of vertices $V$ and edges $E$. Registering each clone in `clones` before recursing guarantees that every original vertex maps to exactly one cloned vertex. When a neighbor $v$ is processed, returning `clones[v]` ensures that edge $(u, v)$ is duplicated as an edge between the exact corresponding cloned instances.

**Completeness.** Since the input graph is connected, DFS/BFS starting from the initial node visits every vertex in $V$ and examines every edge in $E$. No component of the graph is omitted.

---

## 6. Traps This Instance Exposes

- **Registering Clone After Neighbor Loop (The Infinite Loop Bug):** If `clones[node] = copy` is placed *after* the `for neighbor in node.neighbors:` loop, the recursive call `clone(neighbor)` will see that `node` is not yet in `clones`, immediately re-cloning `node` and recursing forever! Registration must happen *before* neighbor iteration.
- **Empty Graph / Null Input:** If `node is None`, the graph is empty. Returning `None` upfront prevents AttributeError on `node.val`.
- **Single Node Without Neighbors:** A graph with one node `adjList = [[]]` has $N_1$ with `neighbors = []`. The algorithm creates $C_1$ with an empty neighbor list and returns it directly.

Every authored case of this package is one of these boundaries, and the counts below are what the protocol must reproduce exactly:

| Authored case | `adjList` | Vertices | Undirected edges | Directed entries | Clone returned |
|:---|:---|:---:|:---:|:---:|:---|
| `sample-null` | `[]` | 0 | 0 | 0 | null reference, with `clones` still empty |
| `sample-single` | `[[]]` | 1 | 0 | 0 | $C_1$ whose neighbor list is empty, not missing |
| `trial-edge` | `[[2], [1]]` | 2 | 1 | 2 | $C_1 \leftrightarrow C_2$ after two registrations and one hit |
| `trial-triangle` | `[[2, 3], [1, 3], [1, 2]]` | 3 | 3 | 6 | $C_1, C_2, C_3$ mutually adjacent after three registrations and three hits |
| `sample-square` | `[[2, 4], [1, 3], [2, 4], [1, 3]]` | 4 | 4 | 8 | $C_1, C_2, C_3, C_4$ on a cycle after four registrations and four hits |

The instantiations equal the vertex count in every row, which is the quantitative form of the invariant: the map is written once per vertex and read once per directed entry. The deferred-registration bug would not merely slow `sample-square` down; it would make even `trial-edge` non-terminating, because the lookup at $(N_2, N_1)$ would miss while $N_1$ is unregistered and restart the descent on a two-vertex cycle forever.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(V + E)$, where $V$ is the number of vertices and $E$ is the number of edges. Each vertex is cloned once, and each edge is traversed twice (once from each endpoint).
- **Auxiliary Space Complexity:** $O(V)$ to store the hash map mapping all $V$ nodes and $O(V)$ recursion stack depth (or BFS queue size).

The $O(V + E)$ bound is shared by every correct variant, so the choice between them is decided by stack depth and by when the map is written:

| Strategy | When `clones[u]` is written | Time | Auxiliary space | Behavior on this 4-cycle |
|:---|:---|:---:|:---:|:---|
| Recursive DFS with pre-registration | Before $u$'s neighbor loop runs | $O(V + E)$ | $O(V)$ map plus $O(V)$ call stack | All four lookups that hit do so while their target frame is still open |
| Iterative BFS with an explicit queue | When $u$ is first enqueued | $O(V + E)$ | $O(V)$ map plus $O(V)$ queue | Same clone; a deep path graph cannot exhaust the interpreter stack |
| Allocate-then-link in two passes | In the allocation pass, before any neighbor is copied | $O(V + E)$ | $O(V)$ map | Still needs one traversal to enumerate the reachable vertices, so the map is required in both passes |
| Recursive copy with no map | Never | unbounded | unbounded | Entry $(N_2, N_1)$ re-enters $N_1$, which has no clone to return, and the cycle never closes |

The first two rows are the practical choices; the third merely reorders the same work, and the fourth is the failure the map exists to prevent.
