# Guided Example: Course Schedule

We trace the step-by-step directed dependency graph modeling, Kahn's in-degree reduction algorithm, and cycle detection on representative curriculum prerequisite networks:

- **Input:** $\text{numCourses} = 4, \quad \text{prerequisites} = [[1, 0], [2, 0], [3, 1], [3, 2]]$
- **Required output:** `true` (Valid topological orderings exist, e.g. $[0, 1, 2, 3]$)
- **Direct Cycle Instance:** $\text{numCourses} = 2, \quad \text{prerequisites} = [[1, 0], [0, 1]] \implies \text{false}$ (Deadlock cycle $0 \leftrightarrow 1$)
- **Self-Loop Instance:** $\text{numCourses} = 1, \quad \text{prerequisites} = [[0, 0]] \implies \text{false}$ (Course requires itself)
- **Zero Prerequisite Instance:** $\text{numCourses} = 3, \quad \text{prerequisites} = [] \implies \text{true}$

This instance demonstrates modeling course dependency constraints as a Directed Acyclic Graph (DAG), proves why directed cycles produce deadlock states with non-zero in-degrees, executes Kahn's BFS algorithm ($O(V + E)$), and verifies curriculum feasibility.

---

## 1. Instance & Teaching Goal

Given $V = 4$ courses labeled $0, 1, 2, 3$ and prerequisite rules $[a_i, b_i]$ signifying that **course $b_i$ must be taken before course $a_i$**:
$$
\text{prerequisites} = [[1, 0], [2, 0], [3, 1], [3, 2]]
$$
Determine whether it is possible to finish all 4 courses without deadlocks.

Translating prerequisites into directed edges ($b_i \to a_i$):
- $[1, 0] \implies 0 \to 1$ (Taking 0 unlocks 1)
- $[2, 0] \implies 0 \to 2$ (Taking 0 unlocks 2)
- $[3, 1] \implies 1 \to 3$ (Taking 1 helps unlock 3)
- $[3, 2] \implies 2 \to 3$ (Taking 2 helps unlock 3)

Visualizing the dependency graph:
```text
      0
     / \
    v   v
    1   2
     \ /
      v
      3
```
- Course 0 has **no prerequisites** (in-degree 0) $\implies$ Can be taken immediately.
- Taking 0 unlocks courses 1 and 2.
- Completing both 1 and 2 satisfies all prerequisites for course 3.
- All 4 courses can be completed! Return `true`.

Now contrast this with a cycle $[[1, 0], [0, 1]]$ ($0 \to 1$ and $1 \to 0$):
Course 0 requires course 1, while course 1 requires course 0. Neither course can be started, creating a permanent circular deadlock (`false`).

---

## 2. Conceptual Foundation & Invariants

### Graph Formulation & Topological Sort
A sequence of all courses that respects all prerequisites exists if and only if the directed graph $G = (V, E)$ contains **no directed cycles** (i.e. $G$ is a DAG).

### Kahn's Algorithm Protocol (BFS In-Degree Reduction)
1. **Adjacency List and In-Degree Computation:**
   For each course $u \in [0, V - 1]$, maintain:
   - $\text{adj}[u]$: list of courses unlocked by completing $u$.
   - $\text{in\_degree}[u]$: number of outstanding prerequisites required before taking $u$.
   For each pair $[a, b]$, add $a$ to $\text{adj}[b]$ and increment $\text{in\_degree}[a] += 1$.

2. **Initialize Queue with Free Courses:**
   Enqueue all courses with $\text{in\_degree}[u] == 0$:
   $$
   Q = [ u \mid \text{in\_degree}[u] == 0 ]
   $$

3. **Process and Decrement Dependencies:**
   Maintain $\text{processed\_count} = 0$.
   While $Q$ is not empty:
   - Dequeue course $u = Q.\text{popleft}()$.
   - Increment $\text{processed\_count} += 1$.
   - For each neighbor $v \in \text{adj}[u]$:
     $$
     \text{in\_degree}[v] \leftarrow \text{in\_degree}[v] - 1
     $$
     If $\text{in\_degree}[v] == 0$, enqueue $v$:
     $$
     Q.\text{append}(v)
     $$

4. **Feasibility Check:**
   $$
   \text{return } (\text{processed\_count} == V)
   $$

> **Invariant.** A course enters queue $Q$ if and only if all of its incoming prerequisite edges have been removed by previously completed courses. Any node participating in a directed cycle never reaches in-degree 0.

---

## 3. Step-by-Step Worked Execution

We trace Kahn's algorithm on $V = 4$, $\text{prerequisites} = [[1, 0], [2, 0], [3, 1], [3, 2]]$:

### Step 0: Graph Construction & In-Degree Initialization
- Adjacency List:
  - $\text{adj}[0] = [1, 2]$
  - $\text{adj}[1] = [3]$
  - $\text{adj}[2] = [3]$
  - $\text{adj}[3] = []$
- In-Degrees:
  - $\text{in\_degree}[0] = 0$ (No prerequisites)
  - $\text{in\_degree}[1] = 1$ (Needs 0)
  - $\text{in\_degree}[2] = 1$ (Needs 0)
  - $\text{in\_degree}[3] = 2$ (Needs 1 and 2)
- Initial Queue: $Q = [0]$.
- $\text{processed\_count} = 0$.

---

### Step 1: Process Course 0
- Pop $u = 0$.
- Increment $\text{processed\_count} = 0 + 1 = \mathbf{1}$.
- Decrement neighbors:
  - Neighbor 1: $\text{in\_degree}[1] = 1 - 1 = \mathbf{0} \implies$ Enqueue 1!
  - Neighbor 2: $\text{in\_degree}[2] = 1 - 1 = \mathbf{0} \implies$ Enqueue 2!
- Queue state: $Q = [1, 2]$.

---

### Step 2: Process Course 1
- Pop $u = 1$.
- Increment $\text{processed\_count} = 1 + 1 = \mathbf{2}$.
- Decrement neighbors:
  - Neighbor 3: $\text{in\_degree}[3] = 2 - 1 = \mathbf{1} \ne 0$ *(Course 3 still awaits course 2)*.
- Queue state: $Q = [2]$.

---

### Step 3: Process Course 2
- Pop $u = 2$.
- Increment $\text{processed\_count} = 2 + 1 = \mathbf{3}$.
- Decrement neighbors:
  - Neighbor 3: $\text{in\_degree}[3] = 1 - 1 = \mathbf{0} \implies$ Enqueue 3!
- Queue state: $Q = [3]$.

---

### Step 4: Process Course 3
- Pop $u = 3$.
- Increment $\text{processed\_count} = 3 + 1 = \mathbf{4}$.
- Neighbor list $\text{adj}[3] = []$.
- Queue state: $Q = []$ (Empty).

---

### Step 5: Termination & Evaluation
- Loop ends because queue is empty.
- Compare counts:
  $$
  \text{processed\_count} = 4 == \text{numCourses} \implies \mathbf{True!}
  $$

---

## 4. Complete Execution Trace

```text
Graph:
  0 -> 1, 2
  1 -> 3
  2 -> 3

In-degrees: {0: 0, 1: 1, 2: 1, 3: 2}
Initial Q:  [ 0 ]

Step 1: Pop 0 -> Decr 1 (indeg=0, push 1), Decr 2 (indeg=0, push 2) -> Q = [1, 2]
Step 2: Pop 1 -> Decr 3 (indeg=1)                                   -> Q = [2]
Step 3: Pop 2 -> Decr 3 (indeg=0, push 3)                           -> Q = [3]
Step 4: Pop 3 -> No outgoing edges                                  -> Q = []

Total Processed: 4 / 4 -> Return True
```

| Step | Active Course $u$ | In-Degree State $[\text{deg}_0, \text{deg}_1, \text{deg}_2, \text{deg}_3]$ | Unlocked Neighbors | Queue State $Q$ | Processed Count |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Init | - | $[0, 1, 1, 2]$ | - | `[0]` | 0 |
| **1** | **0** | $[0, 0, 0, 2]$ | Courses 1, 2 | `[1, 2]` | 1 |
| **2** | **1** | $[0, 0, 0, 1]$ | Course 3 (deg 1) | `[2]` | 2 |
| **3** | **2** | $[0, 0, 0, 0]$ | Course 3 (deg 0) | `[3]` | 3 |
| **4** | **3** | $[0, 0, 0, 0]$ | - | `[]` | **4 (All cleared)** |

### Contrast: Deadlock in Cycle $[[1, 0], [0, 1]]$
- $0 \to 1, 1 \to 0$.
- In-degrees: $\text{in\_degree}[0] = 1, \text{in\_degree}[1] = 1$.
- No node has in-degree $0 \implies Q = []$.
- $\text{processed\_count} = 0 \ne 2 \implies \mathbf{False}$.

---

## 5. Algorithmic Correctness

**Soundness.** A node is enqueued if and only if all of its incoming directed edges have been traversed and resolved. If all $V$ nodes are popped from the queue, a valid topological ordering has been constructed, proving the graph contains no cycles.

**Completeness.** If the graph contains a directed cycle $C = v_1 \to v_2 \dots \to v_k \to v_1$, each node in $C$ requires another node in $C$ to be processed first. Consequently, no node in $C$ can ever reach in-degree 0. They remain trapped outside the queue, causing $\text{processed\_count} < V$ and returning `false`.

---

## 6. Traps This Instance Exposes

- **Edge Direction Inversion:** Writing directed edge $a \to b$ instead of $b \to a$ reverses dependencies, causing courses to require their advanced successors instead of prerequisites.
- **Disconnected Graphs:** A graph may contain several disconnected components (e.g. some courses with no prerequisites at all). Kahn's algorithm naturally initializes the queue with all in-degree 0 nodes across all components.
- **DFS Recursion Depth on Linear Chains:** Recursive cycle detection using 3-color DFS (`WHITE`, `GRAY`, `BLACK`) on a long chain of $V = 100,000$ courses causes stack overflow. Kahn's BFS queue avoids call-stack limits.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(V + E)$, where $V = \text{numCourses}$ and $E = |\text{prerequisites}|$. Initializing in-degrees takes $O(V + E)$. Each course is enqueued and dequeued at most once ($O(V)$), and each directed edge is decremented exactly once ($O(E)$).
- **Auxiliary Space Complexity:** $O(V + E)$ auxiliary memory for the adjacency list representation and the BFS queue.
