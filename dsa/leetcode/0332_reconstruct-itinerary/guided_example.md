# Guided Example: Reconstruct Itinerary

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tickets": [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]}`
- **Required output:** `["JFK", "MUC", "LHR", "SFO", "SJC"]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a list of airline `tickets` where $\text{tickets}[i] = [\text{from}_{i}, \text{to}_{i}]$ represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

The objective is to compute `["JFK", "MUC", "LHR", "SFO", "SJC"]` from `{"tickets": [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Model tickets as directed edge occurrences.

Each airport is a vertex, and each ticket `[from, to]` is one directed edge from `from` to `to`. Duplicate tickets are distinct edge occurrences even when their endpoint strings are identical. The required itinerary starts at `JFK`, uses every edge exactly once, and lists the visited vertices in order. In graph terminology, it is a directed Eulerian trail with a fixed starting vertex.

The input guarantee says at least one such trail exists. The remaining tasks are to consume every edge without losing the ability to finish and to choose the lexically smallest valid trail.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tickets": [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Prepare destinations so removing the smallest is cheap.

The source creates a dictionary `g` mapping each departure airport to a list of its unused arrival airports. It iterates through `sorted(tickets, reverse=true)`, which sorts ticket pairs in descending lexicographic order. Because pair comparison examines the departure first and destination second, all destinations stored under one departure are appended in descending order.

For example, outgoing destinations `ATL`, `LAX`, and `SFO` are stored as `[SFO, LAX, ATL]`. Calling `pop()` removes the last element, `ATL`, in constant time. Thus every recursive choice consumes the currently smallest lexical destination without the cost of deleting from the front of a list.

Using a list rather than a set is essential. If two identical tickets exist, both destination entries are appended and both must be popped on separate traversals.

The `defaultdict(list)` also gives an unseen arrival airport an empty outgoing list. Testing `while g[f]` at a dead end therefore works without a separate key check.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why ordinary forward greediness is unsafe.

It is tempting to build the returned itinerary from left to right by always taking the smallest unused destination. That can enter a dead end before all tickets have been used. Consider tickets `JFK -> KUL`, `JFK -> NRT`, and `NRT -> JFK`. The smallest immediate destination is `KUL`, but placing it second would strand the route. The only complete itinerary is `JFK, NRT, JFK, KUL`.

The exact source still explores the smallest edge first, but it does not immediately commit visited airports to the front of the answer. It uses Hierholzer's postorder construction: an airport is appended only after every outgoing ticket reachable from that call has been exhausted. The route is built backward, so a dead-end excursion naturally becomes the end of the final itinerary rather than incorrectly becoming its beginning.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `["JFK", "MUC", "LHR", "SFO", "SJC"]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tickets": [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `["JFK", "MUC", "LHR", "SFO", "SJC"]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Iterative Hierholzer traversal:** Maintain an explicit airport stack, push the smallest unused destination while possible, and move dead ends into the result. This has the same $O(E\log E)$ preprocessing and $O(E)$ space, avoids recursion, and matches the manifest wording.
- **Min-heaps per departure:** Push destinations into a heap and pop the smallest during traversal. This avoids globally sorting tickets but makes edge removal $O(\log d)$ for outdegree $d$; the total remains $O(E\log E)$.
- **Backtracking over tickets:** Try destinations in sorted order and undo choices that cannot finish. It is conceptually direct but may explore exponentially many partial routes. Hierholzer uses the Eulerian structure to avoid that search.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(E\log E)$. Let $E$ be the number of tickets. Sorting all ticket pairs costs $O(E\log E)$ time. Building the graph is $O(E)$. Every ticket is popped and traversed once, every airport occurrence is appended once, and reversing the result is $O(E)$. Total time complexity is $O(E\log E)$.
- **Auxiliary Space Complexity:** $O(E)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
