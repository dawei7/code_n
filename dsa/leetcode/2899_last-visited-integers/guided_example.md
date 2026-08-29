# Guided Example: Last Visited Integers

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, -1, -1, -1]}`
- **Required output:** `[2, 1, -1]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums` where $\text{nums}[i]$ is either a positive integer or `-1`. We need to find for each `-1` the respective positive integer, which we call the last visited integer.

The objective is to compute `[2, 1, -1]` from `{"nums": [1, 2, -1, -1, -1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

**Store positives in arrival order instead of physically prepending.** The problem describes putting each positive value at the front of `seen`. Repeated insertion at the front of a Python list would shift all existing elements and could make the algorithm quadratic.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, -1, -1, -1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The source instead appends positives to the end. The most recently seen positive is then the last list element, the second most recent is the second-to-last, and so on. Python negative indexing retrieves exactly that order:

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

- `seen[-1]` is the first element of the conceptual front-prepended list;
- `seen[-2]` is the second;
- `seen[-k]` is the $k$-th.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[2, 1, -1]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, -1, -1, -1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[2, 1, -1]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Prepend literally:** `seen.insert(0, x)` matches the prose but shifts a growing list and can take $O(n^2)$ total time.
- **Deque front insertion:** It makes prepending efficient, but indexed access to the $k$-th item is not the deque's strongest operation.
- **Queries before any positive:** Every one returns `-1` because `seen` is empty.
- **Positive resets `k`:** The next query always asks for the newest positive, not the next rank from an older query run.
- **History is retained:** Reset the query count, not the `seen` list.
- **No queries:** Return an empty answer list.
- **Long query run:** Once `k` exceeds history length, all later queries in that same run also return `-1`.
- **Duplicate positives:** Each occurrence is a separate visit and occupies its own historical position.
- **Why negative indexing is safe:** The source evaluates `seen[-k]` only when `k <= len(seen)`. That guard prevents an out-of-range access while mapping query number one to the newest appended value, query number two to the second newest, and so on.
- **Queries are numbered within a run:** Only consecutive `-1` operations increase `k`. Encountering a positive integer ends that run before the next query begins again at rank one.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. The loop processes each of $n$ inputs once. List append, length checking, negative indexing, and answer append are amortized or worst-case constant time, so total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
