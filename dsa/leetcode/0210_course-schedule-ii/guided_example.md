# Guided Example: Course Schedule II

We trace the step-by-step Kahn topological sort ordering reconstruction, queue-driven dependency unlocking, and deadlock cycle detection on representative curriculum prerequisite networks:

- **Input:** $\text{numCourses} = 4, \quad \text{prerequisites} = [[1, 0], [2, 0], [3, 1], [3, 2]]$
- **Required output:** $[0, 1, 2, 3]$ (or $[0, 2, 1, 3]$)
- **Deadlock Cycle Instance:** $\text{numCourses} = 2, \quad \text{prerequisites} = [[1, 0], [0, 1]] \implies []$ (Cycle prevents full topological traversal)
- **Unconstrained Instance:** $\text{numCourses} = 3, \quad \text{prerequisites} = [] \implies [0, 1, 2]$ (Any permutation of courses is valid)
- **Single Course Instance:** $\text{numCourses} = 1, \quad \text{prerequisites} = [] \implies [0]$

This instance demonstrates generating an explicit valid linear ordering of vertices in a Directed Acyclic Graph (DAG), proves why the existence of a cycle requires returning an empty array (`[]`), tracks evolving in-degrees ($u \to v$), and runs in strictly $O(V + E)$ time.

---

## 1. Instance & Teaching Goal

Given $V = 4$ courses ($0, 1, 2, 3$) and prerequisite rules $[a_i, b_i]$ where **course $b_i$ must precede course $a_i$**:
$$
\text{prerequisites} = [[1, 0], [2, 0], [3, 1], [3, 2]]
$$
Construct and return a **complete sequence of all 4 courses** satisfying all prerequisite constraints. If no valid sequence exists (due to a circular dependency), return the empty list `[]`.

Graph structure ($b_i \to a_i$):
- $0 \to 1$
- $0 \to 2$
- $1 \to 3$
- $2 \to 3$

```text
      0
     / \
    v   v
    1   2
     \ /
      v
      3
```

Topological analysis:
- Course $0$ has no prerequisites $\implies$ Must be taken first.
- Once $0$ is completed, both courses $1$ and $2$ become available.
- Either $1$ or $2$ can be taken next.
- Course $3$ requires both $1$ and $2$, so it must be taken last.
Valid output schedules: $[0, 1, 2, 3]$ or $[0, 2, 1, 3]$.

---

## 2. Conceptual Foundation & Invariants

### Kahn's Algorithm for Topological Ordering
1. **Graph Representation:**
   Build adjacency list $\text{adj}$ and in-degree array $\text{in\_degree}$:
   For each $[a, b] \in \text{prerequisites}$:
   $$
   \text{adj}[b].\text{append}(a), \quad \text{in\_degree}[a] \leftarrow \text{in\_degree}[a] + 1
   $$
2. **Seed Initial Frontier:**
   Find all courses that currently have zero unsatisfied prerequisites:
   $$
   Q = \text{deque}([u \mid \text{in\_degree}[u] == 0])
   $$
3. **Queue-Driven Order Assembly:**
   Maintain output array $\text{order} = []$.
   While $Q$ is not empty:
   - Pop available course $u = Q.\text{popleft}()$.
   - Append to schedule: $\text{order.append}(u)$.
   - For each dependent course $v \in \text{adj}[u]$:
     $$
     \text{in\_degree}[v] \leftarrow \text{in\_degree}[v] - 1
     $$
     If $\text{in\_degree}[v] == 0$:
       $$
       Q.\text{append}(v)
       $$
4. **Cycle Verification:**
   If $\text{len}(\text{order}) == V$, return $\text{order}$.
   Otherwise, a directed cycle exists preventing some courses from reaching in-degree 0 $\implies$ return `[]`.

> **Invariant.** At every step, every course appended to `order` has all of its prerequisites already present at earlier positions in `order`.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on $V = 4$, $\text{prerequisites} = [[1, 0], [2, 0], [3, 1], [3, 2]]$:

### Step 0: Initial State
- Adjacency Map:
  - $0 \to [1, 2]$
  - $1 \to [3]$
  - $2 \to [3]$
  - $3 \to []$
- In-Degrees:
  - $\text{in\_degree} = [0, 1, 1, 2]$
- Initial Queue: $Q = [0]$ (Only course 0 has in-degree 0).
- $\text{order} = []$.

---

### Step 1: Process Course 0
- Pop $u = 0$.
- Append to schedule: $\text{order} = [0]$.
- Decrement outgoing edges from 0:
  - Edge $0 \to 1$: $\text{in\_degree}[1] = 1 - 1 = \mathbf{0} \implies$ Enqueue 1!
  - Edge $0 \to 2$: $\text{in\_degree}[2] = 1 - 1 = \mathbf{0} \implies$ Enqueue 2!
- Queue state: $Q = [1, 2]$.

---

### Step 2: Process Course 1
- Pop $u = 1$.
- Append to schedule: $\text{order} = [0, 1]$.
- Decrement outgoing edges from 1:
  - Edge $1 \to 3$: $\text{in\_degree}[3] = 2 - 1 = \mathbf{1} \ne 0$ *(Course 3 still awaits course 2)*.
- Queue state: $Q = [2]$.

---

### Step 3: Process Course 2
- Pop $u = 2$.
- Append to schedule: $\text{order} = [0, 1, 2]$.
- Decrement outgoing edges from 2:
  - Edge $2 \to 3$: $\text{in\_degree}[3] = 1 - 1 = \mathbf{0} \implies$ Enqueue 3!
- Queue state: $Q = [3]$.

---

### Step 4: Process Course 3
- Pop $u = 3$.
- Append to schedule: $\text{order} = [0, 1, 2, 3]$.
- No outgoing edges from 3.
- Queue state: $Q = []$ (Empty).

---

### Step 5: Feasibility Validation
- Loop terminates.
- Check length:
  $$
  \text{len}(\text{order}) = 4 == \text{numCourses}
  $$
- Complete schedule successfully generated: $\mathbf{[0, 1, 2, 3]}$.

---

## 4. Complete Execution Trace

```text
Prerequisites: [[1,0], [2,0], [3,1], [3,2]], numCourses = 4

In-degrees: {0: 0, 1: 1, 2: 1, 3: 2}
Queue: [ 0 ]

Step 1: Pop 0 -> order = [0]
        Edge 0->1: indeg[1] = 0 -> Q.push(1)
        Edge 0->2: indeg[2] = 0 -> Q.push(2)
        Q = [1, 2]

Step 2: Pop 1 -> order = [0, 1]
        Edge 1->3: indeg[3] = 1 -> Q = [2]

Step 3: Pop 2 -> order = [0, 1, 2]
        Edge 2->3: indeg[3] = 0 -> Q.push(3)
        Q = [3]

Step 4: Pop 3 -> order = [0, 1, 2, 3] -> Q = []

Length matches numCourses (4 == 4) -> Return [0, 1, 2, 3]
```

| Step | Popped Course $u$ | In-Degree State $[\text{deg}_0, \text{deg}_1, \text{deg}_2, \text{deg}_3]$ | Decremented Edges | Newly Enqueued | Cumulative `order` |
|:---:|:---:|:---:|:---|:---:|:---|
| Init | - | $[0, 1, 1, 2]$ | - | Course 0 | `[]` |
| **1** | **0** | $[0, 0, 0, 2]$ | $0 \to 1, \, 0 \to 2$ | Courses 1, 2 | `[0]` |
| **2** | **1** | $[0, 0, 0, 1]$ | $1 \to 3$ | None | `[0, 1]` |
| **3** | **2** | $[0, 0, 0, 0]$ | $2 \to 3$ | Course 3 | `[0, 1, 2]` |
| **4** | **3** | $[0, 0, 0, 0]$ | None | None | **`[0, 1, 2, 3]` (Final)** |

### Contrast: Deadlock in Cycle $[[1, 0], [0, 1]]$
- In-degrees: $\{0: 1, 1: 1\}$.
- $Q = []$.
- Loop terminates immediately.
- $\text{len}(\text{order}) = 0 \ne 2 \implies$ Returns `[]`.

---

## 5. Algorithmic Correctness

**Soundness.** A course $u$ is appended to `order` only after being popped from the zero in-degree queue, which requires that all incoming edges from prerequisites have already been decremented to zero by earlier courses. Thus, every prerequisite appears before its dependent courses.

**Completeness.** If the graph is a DAG, at least one node has in-degree zero at every step until all vertices are consumed. If a cycle exists, the vertices within the cycle never reach in-degree zero, causing $\text{len}(\text{order}) < V$, which correctly triggers the return of `[]`.

---

## 6. Traps This Instance Exposes

- **Returning Partial Array on Cycle:** If the graph has 4 courses but 2 are in a cycle (e.g. $0 \to 1$ and $2 \leftrightarrow 3$), the queue will process courses 0 and 1 and then stall. Returning `[0, 1]` is wrong because the contract requires an ordering of *all* courses. The method must verify $\text{len}(\text{order}) == V$ and return `[]`.
- **Multiple Valid Orders:** Topological sorts are generally non-unique ($[0, 1, 2, 3]$ and $[0, 2, 1, 3]$ are both valid). Any valid topological order is accepted by the judge.
- **Disconnected Components:** Courses with zero prerequisites across separate subcomponents are all enqueued initially. Their relative ordering is unconstrained.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(V + E)$, where $V = \text{numCourses}$ and $E = |\text{prerequisites}|$. Graph construction takes $O(V + E)$. Each course is enqueued and dequeued once, and each edge is examined once.
- **Auxiliary Space Complexity:** $O(V + E)$ auxiliary memory for the adjacency list, in-degree array, and BFS queue.
