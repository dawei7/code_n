# Guided Example: Insert Delete GetRandom O(1)

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"operations": [["insert", 5], ["insert", 5], ["remove", 5]]}`
- **Required output:** `[true, false, true]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Implement the `RandomizedSet` class:

The objective is to compute `[true, false, true]` from `{"operations": [["insert", 5], ["insert", 5], ["remove", 5]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why one ordinary data structure is not enough

The class must support membership-aware insertion, membership-aware removal, and uniform random selection, all in average $O(1)$ time.

A hash set or dictionary makes membership, insertion, and deletion fast, but it does not provide compact integer indices. Choosing a uniformly random element would require first walking through or copying its keys, which is linear. A dynamic array has compact indices, so selecting a uniformly random index is constant time, but deleting an element from the middle normally shifts all later elements and costs linear time.

The exact solution combines the strengths of both structures:

- `q` is a dense list containing every current value exactly once;
- `d` is a dictionary mapping each current value to its index in `q`.

Together they maintain this central invariant:

> For every stored value `v`, `d[v]` is a valid index and `q[d[v]] == v`; conversely, every list entry appears as a key in `d` exactly once.

The list makes random selection efficient, while the dictionary reveals where a value sits so removal can find it without searching.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"operations": [["insert", 5], ["insert", 5], ["remove", 5]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Insertion keeps both views synchronized

The method first tests `if val in d`. The dictionary’s keys are exactly the current set, so existing membership means insertion must fail. The method returns `false` without modifying either structure.

For a new value, its position will be the current list length. If `q` has three elements, for example, the next appended element receives index `3`. The solution records `d[val] = len(q)` and then executes `q.append(val)`. After the append, the stored index points exactly to `val`, so the invariant holds for the new element. Existing elements do not move, so all their mappings remain valid. The method returns `true` because the set changed.

Recording the index immediately before appending is safe: `len(q)` is precisely the index at which `append` places the next element. The code could append first and store `len(q) - 1`; the chosen order simply avoids that subtraction.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why ordinary list deletion is too slow

Suppose `q = [10, 20, 30, 40]` and the caller removes `20`. Deleting index `1` in the usual stable-order manner would shift `30` and `40` left. That shift is linear, and the dictionary indices for both moved values would also need updates.

The class does not promise to preserve insertion order. Therefore, it can fill the removed value’s position with the last list element, then remove the last position. Popping from the end of a dynamic array is constant time because no remaining element needs to shift.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[true, false, true]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"operations": [["insert", 5], ["insert", 5], ["remove", 5]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[true, false, true]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Hash set alone:** Insert and removal are expected $O(1)$, but selecting a uniformly random member requires converting or traversing the set, which costs $O(n)$. It cannot satisfy all three operation bounds simultaneously.
- **List alone:** Random selection and appending are constant time, but checking for an existing value and locating a requested value for removal require a linear search. Stable removal would also shift elements.
- **List with tombstones:** Marking removed positions as empty avoids immediate shifting, but random selection could land on holes. Retrying can become arbitrarily slow when most entries are deleted, while periodic compaction introduces linear work. The dense swap-with-last design avoids holes entirely.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. Let $n$ be the number of values currently stored.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
