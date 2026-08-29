# Guided Example: Minimum Score of a Path Between Two Cities

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 4, "roads": [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]]}`
- **Required output:** `5`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a positive integer `n` representing `n` cities numbered from `1` to `n`. You are also given a **2D** array `roads` where $\text{roads}[i] = [a_{i}, b_{i}, \text{distance}_{i}]$ indicates that there is a **bidirectional **road between cities $a_{i}$ and $b_{i}$ with a distance equal to $\text{distance}_{i}$. The cities graph is not necessarily connected.

The objective is to compute `5` from `{"n": 4, "roads": [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]]}` while avoiding redundant calculations and unnecessary overhead.

A naive or brute-force exploration risks evaluating infeasible states or repeating subproblem computations. The optimal method establishes a clear invariant that advances deterministically toward the goal.

---

## 2. Conceptual Foundation & Invariants

We maintain the core conceptual parameters and state variables:

| State Parameter | Role & Purpose | Initial State |
|---|---|---|
| Primary State | Tracks active elements, frontier indices, or DP table cells | Initialized at boundary |
| Accumulator | Preserves confirmed optimal sub-answers or counts | Empty / Neutral |

> **Invariant.** At every processing step, all previously evaluated subproblems strictly satisfy the problem constraints, and no viable candidate solution has been omitted.

---

## 3. Step-by-Step Worked Execution

### Step 1: The objective is unusual: make the minimum edge as small as possible

The score of a path is its smallest road distance. Unlike a shortest-path problem, a large total distance is irrelevant, and taking detours can improve the answer by introducing one very small road.

Paths may revisit cities and even traverse the same road multiple times. That permission changes the problem fundamentally. If cities 1 and `n` lie in the same connected component, a walk can leave the direct route, travel to any road in that component, cross that road, and then travel onward to city `n`. Repeated vertices and edges make such a detour legal.

The test guarantee says at least one path connects 1 to `n`, so city `n` belongs to city 1's connected component.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 4, "roads": [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the answer is the lightest road in that component

Let $w_{\min}$ be the minimum distance among all roads in the connected component containing city 1.

Every path from 1 to `n` uses only roads from that component. No road on any such path can have distance below $w_{\min}$, so the path's minimum road distance cannot be smaller than $w_{\min}$. This gives a lower bound on the best possible score.

Now choose a road $(u,v)$ whose distance is $w_{\min}$. Since `u` is in city 1's component, there is a route from 1 to `u`. Cross the chosen road to `v`. Because `v` and `n` are in the same component, there is also a route from `v` to `n`. Concatenating these routes creates a legal walk from 1 to `n` that contains the lightest road. Its score is exactly $w_{\min}$, since no component road is lighter.

The lower bound is achievable, so $w_{\min}$ is the required answer.

This proof also explains the second example: the path can travel from city 1 to city 2 along the distance-two road, return along that road, and then continue toward city `n`. A simple path restriction would prevent that detour, but this problem explicitly allows it.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Build the undirected graph

The adjacency list `g` has `n+1` entries so city numbers can be used directly as indices. For every input `[a,b,w]`, the code appends `(b,w)` to `g[a]` and `(a,w)` to `g[b]`.

Both insertions are necessary because roads are bidirectional. Omitting either direction could make depth-first search miss cities or roads that are reachable only by traversing the input edge opposite its listed order.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `5` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 4, "roads": [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `5` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Iterative DFS:** Use an explicit stack to avoid Python recursion-depth failure while preserving the same $O(n+m)$ bounds.
- **Breadth-first search:** A queue visits the same component and can update the same minimum.
- **Union-find:** Unite road endpoints and then inspect roads whose endpoint belongs to city 1's component. It works but is more machinery than a traversal.
- **Shortest-path algorithms:** Dijkstra minimizes total distance, which is not this path score and can produce the wrong objective.
- **Disconnected graph:** Only the component containing city 1 matters; city `n` is guaranteed to be inside it.
- **Tiny road on a detour:** It still determines the answer because repeated cities and roads are legal.
- **Visited neighbor:** Its connecting edge must still update `ans` even though recursion is skipped.
- **Parallel direction storage:** Each bidirectional road must be inserted for both endpoints.
- **Single connecting route:** The minimum road on that component's edges is attainable even if reaching it requires backtracking.
- **Recursion limit:** Prefer an iterative queue or stack in production Python for $n=10^5$.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n+m)$. Let $m$ be the number of roads. Building the adjacency list costs $O(n+m)$ initialization and insertion time. DFS visits each city in city 1's component once and examines each of its undirected road entries, for $O(n+m)$ worst-case time. Total time is $O(n+m)$.
- **Auxiliary Space Complexity:** $O(n+m)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
