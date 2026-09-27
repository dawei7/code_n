# Guided Example: Maximum Employees to Be Invited to a Meeting

We trace the step-by-step execution of the functional graph cycle decomposition and topological chain propagation approach on a representative problem instance:

- **Favorite Array (`favorite`):** `[2, 2, 1, 2]`
- **Expected Output:** `3`

This instance illustrates the structural divergence in functional graphs between closed cycles of length $L \ge 3$ and mutually reciprocal 2-cycles, demonstrating why 2-cycles can extend via longest incoming branch trees and concatenate around a circular table.

---

## 1. Problem Overview & Representative Instance

A company is seating employees around a single circular table. Each employee $i \in \{0, \dots, n-1\}$ has a single preferred colleague $\text{favorite}[i]$. An arrangement is valid if and only if every seated employee sits directly adjacent to their favorite colleague (either immediately to their left or right).

In our representative instance `favorite = [2, 2, 1, 2]` ($n = 4$):
- Employee $0$ loves Employee $2$ ($0 \to 2$).
- Employee $1$ loves Employee $2$ ($1 \to 2$).
- Employee $2$ loves Employee $1$ ($2 \to 1$).
- Employee $3$ loves Employee $2$ ($3 \to 2$).

Notice the topology:
- Employees $1$ and $2$ form a mutual pair (a 2-cycle: $1 \rightleftharpoons 2$).
- Both Employee $0$ and Employee $3$ direct their preference into Employee $2$.
- We cannot seat all $4$ employees simultaneously because Employee $2$ only possesses two physical neighbor seats, one of which must be occupied by their mutual favorite (Employee $1$).

---

## 2. Mathematical & Algorithmic Principles

### Functional Graph Structure
Because each employee has out-degree exactly $1$, the dependency network is a directed functional graph. Every weakly connected component consists of a set of directed trees rooted at the vertices of a unique directed central cycle.

### Structural Duality of Circular Seating
Depending on cycle length, valid table configurations fall into two mutually exclusive regimes:

1. **Long Cycles ($L \ge 3$):**
   - In a directed cycle $v_1 \to v_2 \to \dots \to v_L \to v_1$ with $L \ge 3$, each employee $v_i$ must sit next to $v_{i+1}$.
   - Because a circular table provides exactly two neighbors per person, employee $v_i$ is bordered by $v_{i-1}$ and $v_{i+1}$.
   - All neighbor slots in the cycle are fully saturated. No tree branches can be attached to the cycle, and no two disjoint long cycles can be combined without breaking adjacency.
   - Hence, the maximum seating from long cycles is:

$$M_{\ge 3} = \max_{|C| \ge 3} |C|$$

2. **Mutual Pairs ($L = 2$) with Incoming Arms:**
   - In a 2-cycle $u \rightleftharpoons v$, each member satisfies the other's preference.
   - Consequently, $u$'s second neighbor seat and $v$'s second neighbor seat remain unconstrained.
   - We can attach the longest directed path entering $u$ (length $d_u$) to $u$'s open side, and the longest directed path entering $v$ (length $d_v$) to $v$'s open side:

$$\text{Chain}(u) - u - v - \text{Chain}(v)$$

   - Furthermore, because the endpoints of these extended lines have open external edges, multiple independent 2-cycle components can be concatenated together into a single circular arrangement!
   - Hence, the maximum seating from 2-cycles is:

$$M_{= 2} = \sum_{(u, v) \in \text{2-cycles}} (2 + d_u + d_v)$$

The global maximum seating capacity is:

$$\text{Max Employees} = \max(M_{\ge 3}, M_{= 2})$$

| Component Topology | Seating Modality | Reusability Across Components | Total Capacity Metric |
|---|---|---|---|
| Cycle of length $L \ge 3$ | Closed loop $v_1 \dots v_L$ | Mutually exclusive (Pick single largest) | $\max |C|$ |
| Mutual pair ($L = 2$) | Extended bidirectional chain | Globally additive (Sum all pairs) | $\sum (2 + d_u + d_v)$ |

---

## 3. Step-by-Step Walkthrough with Intermediate State

### Phase 1: In-Degree Calculation & Topological Stripping
Count incoming edges to identify tree branches:
- $\text{in\_degree}[0] = 0$
- $\text{in\_degree}[1] = 1$ (from $2$)
- $\text{in\_degree}[2] = 3$ (from $0, 1, 3$)
- $\text{in\_degree}[3] = 0$

Initialize chain depth array: $\text{depth} = [1, 1, 1, 1]$.
Enqueue tree leaves (in-degree $0$): `queue = [0, 3]`.

#### Processing Node 0:
- Successor: $\text{favorite}[0] = 2$.
- Update depth: $\text{depth}[2] \leftarrow \max(\text{depth}[2], \text{depth}[0] + 1) = \max(1, 1 + 1) = 2$.
- Decrement in-degree: $\text{in\_degree}[2] = 3 - 1 = 2$.

#### Processing Node 3:
- Successor: $\text{favorite}[3] = 2$.
- Update depth: $\text{depth}[2] \leftarrow \max(\text{depth}[2], \text{depth}[3] + 1) = \max(2, 1 + 1) = 2$.
- Decrement in-degree: $\text{in\_degree}[2] = 2 - 1 = 1$.

Topological sorting completes. Remaining nodes with $\text{in\_degree} > 0$ are cycle nodes: $\{1, 2\}$.

### Phase 2: Cycle Detection and Classification
We trace cycles among nodes with remaining in-degree:
- Starting at Node $1$:
  - $1 \to 2 \to 1$.
  - Cycle length: $2$ (Nodes $\{1, 2\}$).
  - This is a 2-cycle ($L = 2$).
- Evaluate extended 2-cycle capacity:
  - Base pair size: $2$.
  - Longest branch into Node $1$: $\text{depth}[1] - 1 = 1 - 1 = 0$.
  - Longest branch into Node $2$: $\text{depth}[2] - 1 = 2 - 1 = 1$ (achieved by either Node $0$ or Node $3$).
  - Combined extended 2-cycle contribution: $2 + 0 + 1 = 3$.
  - Cumulative 2-cycle sum: $M_{=2} = 3$.

No cycles of length $L \ge 3$ exist in this graph, so $M_{\ge 3} = 0$.

### Phase 3: Global Capacity Resolution
Comparing the two seating modalities:

$$\text{Answer} = \max(M_{\ge 3}, M_{=2}) = \max(0, 3) = 3$$

Valid seating around the table: `[0, 2, 1]`.
- Employee $0$ sits next to Employee $2$ (favorite satisfied).
- Employee $2$ sits between $0$ and $1$ (favorite $1$ satisfied).
- Employee $1$ sits between $2$ and $0$ (favorite $2$ satisfied).
All $3$ seated employees have their preferences fulfilled.

---

## 4. Comprehensive State Trace

The structural classification and metric resolution for all nodes are shown below:

| Node Index | Successor ($\text{favorite}[i]$) | Initial In-Degree | Final In-Degree | Tree Depth | Role in Graph |
|---|---|---|---|---|---|
| $0$ | $2$ | $0$ | $0$ | $1$ | Tree leaf |
| $1$ | $2$ | $1$ | $1$ | $1$ | 2-cycle member |
| $2$ | $1$ | $3$ | $1$ | $2$ | 2-cycle member |
| $3$ | $2$ | $0$ | $0$ | $1$ | Tree leaf |

### Component Evaluation Summary
| Component | Cycle Nodes | Cycle Length $L$ | Modality Category | Extended Arm Depths | Component Contribution |
|---|---|---|---|---|---|
| Component 1 | $\{1, 2\}$ | $2$ | Mutual Pair ($L = 2$) | $d_1 = 0, d_2 = 1$ | $2 + 0 + 1 = 3$ |

Final Result: $\max(M_{\ge 3}, M_{=2}) = \max(0, 3) = 3$.

---

## 5. Algorithmic Correctness & Soundness

**Soundness.** For any cycle $C$ of length $L \ge 3$, arranging $C$ in cyclic order places each person adjacent to their unique favorite, creating a valid circular table of size $L$. For any mutual 2-cycle $u \rightleftharpoons v$, $u$ and $v$ satisfy each other's preference. Any directed path ending at $u$ can be seated linearly before $u$, with each employee positioned next to their successor. Because the two ends of each extended 2-cycle remain open, multiple extended 2-cycles can be joined circularly without introducing conflicts.

**Completeness.** Every node belongs to either a tree arm or a cycle. Kahn's topological peeling isolates all tree branches in linear time, computing the maximal arm depth leading into each cycle node. All remaining cycles are traversed and partitioned into $L = 2$ and $L \ge 3$. Since no arrangement can simultaneously merge a cycle of length $\ge 3$ with external branches or other cycles, taking the maximum of $M_{\ge 3}$ and the sum of all extended 2-cycles exhausts the entire solution space.

---

## 6. Edge Cases & Anti-Patterns

- **Only Long Cycles ($L \ge 3$):** If the graph contains only cycles of length $\ge 3$ without mutual pairs, $M_{=2} = 0$, and the answer is simply the maximum cycle length.
- **Multiple Disjoint 2-Cycles:** If the graph contains multiple distinct mutual pairs, their extended capacities sum together, e.g., $(2 + d_{u_1} + d_{v_1}) + (2 + d_{u_2} + d_{v_2})$.
- **Zero Tree Arms:** If 2-cycles have no incoming branches, each contributes exactly $2$.
- **Anti-Pattern — Summing Long Cycles:** Attempting to sum capacities across multiple cycles of length $\ge 3$ is mathematically impossible because each long cycle saturates all adjacent seating slots.

---

## 7. Complexity Analysis

- **Time Complexity:** $\mathcal{O}(n)$, where $n$ is the number of employees. Kahn's algorithm processes each node and edge once during topological sort in $\mathcal{O}(n)$ time. Cycle tracing visits each remaining cycle node once, and finding maximum arm depths takes linear time across the graph.
- **Auxiliary Space Complexity:** $\mathcal{O}(n)$ to store the in-degree array, the branch depth array, the BFS queue, and cycle visitation markers.
