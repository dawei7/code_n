# Guided Example: Find All People With Secret

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 6, "meetings": [[1, 2, 5], [2, 3, 8], [1, 5, 10]], "firstPerson": 1}`
- **Required output:** `[0, 1, 2, 3, 5]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer `n` indicating there are `n` people numbered from `0` to $n - 1$. You are also given a **0-indexed** 2D integer array `meetings` where $\text{meetings}[i] = [x_{i}, y_{i}, \text{time}_{i}]$ indicates that person $x_{i}$ and person $y_{i}$ have a meeting at $\text{time}_{i}$. A person may attend **multiple meetings** at the same time. Finally, you are given an integer `firstPerson`.

The objective is to compute `[0, 1, 2, 3, 5]` from `{"n": 6, "meetings": [[1, 2, 5], [2, 3, 8], [1, 5, 10]], "firstPerson": 1}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Process meetings in chronological groups

Knowledge can move forward through time, never backward. The source first marks person 0 and `firstPerson` as knowing the secret, then sorts `meetings` by time.

The indices `i` and `j` identify one maximal block whose meetings all have the same timestamp. Grouping equal times is essential because sharing is instantaneous. Someone who learns the secret in one meeting at time $t$ may pass it through another meeting also at time $t$, even if that second row appears earlier or later in the input.

Processing equal-time meetings one by one would incorrectly make the input row order meaningful. Treating the entire group as a graph captures all same-time chains.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 6, "meetings": [[1, 2, 5], [2, 3, 8], [1, 5, 10]], "firstPerson": 1}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Build a temporary graph for one timestamp

For meetings `i` through `j`, the code builds an undirected adjacency list `g` and a participant set `s`. A meeting between `x` and `y` adds both `x -> y` and `y -> x` because either participant can share with the other.

This graph exists only for the current time. A connected component represents people linked by a chain of simultaneous meetings. If any member knew the secret before or at this time, instantaneous sharing spreads it through that entire component. A component with no knowledgeable member learns nothing.

The queue is initialized with every current participant `u` for which `vis[u]` is already true. Those are exactly the components' possible secret sources.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For meetings `i` through `j`, the code builds an undirected ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Use multi-source BFS for instantaneous propagation

The BFS removes a knowledgeable participant `u` and examines every current-time neighbor `v`. If `v` does not yet know, the code sets `vis[v] = true` and enqueues `v`.

Enqueuing newly informed people is what allows a chain such as meetings `1-2` and `2-3` at the same time to inform person 3 immediately when person 1 already knows. BFS continues until every node reachable from a knowledgeable seed in the temporary graph has been marked.

No separate local visited set is necessary. `vis` serves both as permanent knowledge and as the traversal marker. A person who already knew is included among the initial seeds, so skipping them when reached from another neighbor cannot prevent their edges from being processed.

After BFS, the temporary graph is discarded and the scan advances to the next time group. People marked in `vis` remain knowledgeable forever.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[0, 1, 2, 3, 5]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 6, "meetings": [[1, 2, 5], [2, 3, 8], [1, 5, 10]], "firstPerson": 1}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[0, 1, 2, 3, 5]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Process rows individually:** This can miss ins:** - **Process rows individually:** This can miss instantaneous chains when equal-time rows are ordered unfavorably. Equal timestamps must be handled as one connectivity event.
- **Permanent union-find:** Components formed at one time must not persist for people who never learned the secret. A temporary graph avoids leaking same-time connectivity into later times.
- **Timestamp-group union-find with reset:** DSU can union participants within one time, retain only components connected to knowledgeable people, then reset the others. It is valid but more intricate than temporary BFS.
- **Priority traversal by earliest knowledge time:** A time-aware graph search can compute earliest learning times. Sorting and grouping makes the instantaneous equivalence at each timestamp especially explicit.
- **Several known seeds in one component:** They may all enter the queue, but `vis` prevents unknown people from being enqueued repeatedly.
- **No known seed in a component:** BFS never enters it, so nobody there incorrectly learns the secret.
- **Person attends multiple meetings simultaneously:** All incident edges appear in the same temporary graph, allowing immediate receive-and-forward behavior.
- **Repeated participant across different times:** Their permanent `vis` flag seeds every later group they attend after learning.
- **People with no meetings:** Only person 0 or `firstPerson` can know without attending a meeting.
- **Input order:** Sorting deliberately mutates `meetings`; correctness depends on chronological rather than original row order.
- **Answer order:** The final enumeration is increasing, though the contract permits any ordering.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M\log M+n)$. Let $M$ be the number of meetings and $n$ the number of people.
- **Auxiliary Space Complexity:** $O(M+n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
