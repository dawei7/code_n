# Guided Example: Design Event Manager

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"operations": ["EventManager", "pollHighest", "updatePriority", "pollHighest", "pollHighest"], "arguments": [[[[5, 7], [2, 7], [9, 4]]], [], [9, 7], [], []]}`
- **Required output:** `[null, 2, null, 5, 9]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an initial list of events, where each event has a unique `eventId` and a `priority`.

The objective is to compute `[null, 2, null, 5, 9]` from `{"operations": ["EventManager", "pollHighest", "updatePriority", "pollHighest", "pollHighest"], "arguments": [[[[5, 7], [2, 7], [9, 4]]], [], [9, 7], [], []]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Maintain both direct lookup and ranking order

The manager needs two different operations:

- find an active event by `eventId` to change its priority;
- find the globally highest-priority event, breaking ties by smallest ID.

A dictionary handles direct lookup but cannot efficiently return the ranked best event. An ordered collection handles ranking but needs the old key to update a particular event. The source keeps both views synchronized.

`d` maps every active `eventId` to its current priority.

`sl` is a `SortedList` containing one tuple

`(-priority, eventId)`

for every active event.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"operations": ["EventManager", "pollHighest", "updatePriority", "pollHighest", "pollHighest"], "arguments": [[[[5, 7], [2, 7], [9, 4]]], [], [9, 7], [], []]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the tuple order matches the requested ranking

`SortedList` orders tuples lexicographically in ascending order.

Negating priority reverses its order: a larger original priority becomes a smaller negative number and appears earlier. For equal priorities, the first tuple fields tie, so the smaller `eventId` appears earlier.

Therefore `sl[0]` is always the active event with:

1. maximum priority;
2. minimum ID among that priority.

This encodes both ranking rules in the data structure's ordinary ascending order.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `SortedList` orders tuples lexicographically in ascending or... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Constructor establishes one synchronized entry per event

For every initial pair `(eventId,priority)`, the constructor inserts `(-priority,eventId)` into the sorted list and records the priority in the dictionary.

Initial IDs are unique, so no key replaces another and every active event receives exactly one representation in each structure.

The key tuple is also unique among active events because event IDs are unique, even when priorities tie.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[null, 2, null, 5, 9]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"operations": ["EventManager", "pollHighest", "updatePriority", "pollHighest", "pollHighest"], "arguments": [[[[5, 7], [2, 7], [9, 4]]], [], [9, 7], [], []]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[null, 2, null, 5, 9]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Lazy heap plus dictionary:** Push every update:** - **Lazy heap plus dictionary:** Push every updated version and discard stale heap tops during polls. This matches the manifest summary and has simple updates, but stale entries can grow storage to `O(E+Q)`.
- **Balanced search tree:** Store `(-priority,id)` keys with direct deletion. This is the abstract structure implemented by the source's ordered collection.
- **Sort all active events on every poll:** Simple but can take `O(A\log A)` per poll.
- **Scan the dictionary on every poll:** Uses no ordered structure but takes `O(A)` per poll.
- **Priority tie:** Negative priorities tie, so ascending tuple order chooses the smaller ID.
- **Update to the same priority:** Eager remove-and-add is logically neutral and preserves one entry.
- **Poll empty manager:** Returns minus one without touching the dictionary.
- **Poll removes activity:** A later update for that ID is excluded by the contract's active-ID guarantee.
- **Large priorities:** Python negation is exact and safely reverses order.
- **Unique IDs:** Required for dictionary identity and tuple uniqueness.
- **No stale keys:** Exact old-key removal is the core difference from a lazy heap.
- **Dependency availability:** Without `sortedcontainers.SortedList`, this exact source cannot run and needs another ordered structure.
- **Output protocol:** Constructor and updates conceptually yield null in the design harness; only polls return integers.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(E\log E)$. Let `E` be the initial event count and `A` the current active count.
- **Auxiliary Space Complexity:** $O(E+Q)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
