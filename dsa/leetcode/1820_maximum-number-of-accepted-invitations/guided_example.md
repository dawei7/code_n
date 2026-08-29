# Guided Example: Maximum Number of Accepted Invitations

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [[1, 1, 1], [1, 0, 1], [0, 0, 1]]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are `m` boys and `n` girls in a class attending an upcoming party.

The objective is to compute `3` from `{"grid": [[1, 1, 1], [1, 0, 1], [0, 0, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Model invitations as bipartite matching

There are two disjoint kinds of vertices: boys and girls. An allowed invitation `grid[i][j] = 1` is an edge from boy $i$ to girl $j$.

A valid accepted-invitation set chooses edges so that no boy and no girl appears more than once. This is exactly a matching in a bipartite graph. The goal is a maximum-cardinality matching.

The protected solution uses the augmenting-path method, often called Kuhn's algorithm.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [[1, 1, 1], [1, 0, 1], [0, 0, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Store the current owner of every girl

Array `match` has one entry per girl:

- `match[j] = -1` means girl $j$ is currently unmatched;
- otherwise `match[j]` is the boy currently matched to her.

The algorithm processes boys one at a time and tries to increase the matching size by one for each.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Search for an augmenting path

Helper `find(i)` tries to obtain some girl for boy $i$.

It scans every girl $j$ that boy $i$ can invite. During one outer attempt, set `vis` records girls already considered anywhere in the recursive search. A visited girl is skipped to prevent cycles and repeated work.

When an allowed unvisited girl is found, two cases exist.

If `match[j] == -1`, the girl is free. Assigning her to boy $i$ immediately increases matching size and returns `true`.

If she is occupied by boy `match[j]`, the algorithm recursively asks whether that boy can move to a different girl. If that recursive call succeeds, his old girl becomes available for boy $i$. The assignment `match[j] = i` completes the chain of reassignments.

If no girl can be obtained, `find(i)` returns `false` and the existing matching remains the same size.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [[1, 1, 1], [1, 0, 1], [0, 0, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Greedy free-girl assignment:** It can miss the optimum because earlier flexible boys may block later constrained boys.
- **Hopcroft-Karp:** It finds batches of shortest augmenting paths in $O(E\sqrt{m+n})$, better for much larger graphs but more complex.
- **Maximum flow:** Source, boy, girl, and sink capacities model the problem correctly, with heavier machinery.
- **Girl with no incoming edges:** She remains unmatched and never affects a DFS.
- **Boy with no allowed invitations:** His row scan returns false immediately.
- **More boys than girls:** The answer cannot exceed $n$.
- **More girls than boys:** The answer cannot exceed $m$.
- **Complete grid:** The answer is $\min(m,n)$.
- **Duplicate path exploration:** `vis` prevents one search from reconsidering a girl.
- **Fresh `vis`:** It allows later boys to use new reassignments through previously examined girls.
- **Recursive reassignment:** Existing matches are changed only after an alternate placement succeeds.
- **Boolean addition:** Each successful augmentation contributes exactly one.
- **Zero-based internal indices:** They represent the problem's ordinal boys and girls without affecting the count.
- **Input preservation:** Only `match` changes; `grid` is read-only.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(m^2n)$. Let $m$ be the number of boys, $n$ the number of girls, and $E$ the number of one-entries.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
