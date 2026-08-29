# Guided Example: Design Task Manager

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"operations": ["TaskManager", "add", "edit", "execTop", "rmv", "add", "execTop"], "arguments": [[[[1, 101, 10], [2, 102, 20], [3, 103, 15]]], [4, 104, 5], [102, 8], [], [101], [5, 105, 15], []]}`
- **Required output:** `[null, null, null, 3, null, null, 5]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is a task management system that allows users to manage their tasks, each associated with a priority. The system should efficiently handle adding, modifying, executing, and removing tasks.

The objective is to compute `[null, null, null, 3, null, null, 5]` from `{"operations": ["TaskManager", "add", "edit", "execTop", "rmv", "add", "execTop"], "arguments": [[[[1, 101, 10], [2, 102, 20], [3, 103, 15]]], [4, 104, 5], [102, 8], [], [101], [5, 105, 15], []]}` while avoiding redundant calculations and unnecessary overhead.

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

**Each operation needs two different views of the same tasks.** Looking up a task by `taskId` is necessary for `edit` and `rmv`. Executing the globally best task requires ordering all live tasks by priority and, for equal priorities, by task ID. One data structure does not provide both views efficiently, so the source keeps them synchronized:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"operations": ["TaskManager", "add", "edit", "execTop", "rmv", "add", "execTop"], "arguments": [[[[1, 101, 10], [2, 102, 20], [3, 103, 15]]], [4, 104, 5], [102, 8], [], [101], [5, 105, 15], []]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

- `d` is a dictionary from `taskId` to `(userId, priority)`;
- `st` is a `SortedList` of `(-priority, -taskId)` pairs.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

The dictionary is the direct identity view. It answers “who owns this task?” and “what is its current priority?” in expected constant time. The sorted list is the ranking view. It keeps every live task in the exact order needed by `execTop`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[null, null, null, 3, null, null, 5]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"operations": ["TaskManager", "add", "edit", "execTop", "rmv", "add", "execTop"], "arguments": [[[[1, 101, 10], [2, 102, 20], [3, 103, 15]]], [4, 104, 5], [102, 8], [], [101], [5, 105, 15], []]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[null, null, null, 3, null, null, 5]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Heap with lazy deletion:** Keep current metadata in a dictionary, push a new heap item on each add or edit, and skip stale entries during execution. This is the editorial method, but it can retain $O(q)$ obsolete entries and is not the protected source.
- **Scan the dictionary on every execution:** Add, edit, and remove remain simple, but finding the best live task costs $O(N)$ per `execTop`, which is too slow for the operation limit.
- **Priority buckets:** Priorities reach $10^9$, so allocating a bucket for every possible priority is impractical; task-ID tie-breaking would still need an ordered structure.
- **Equal priorities:** The negative task ID in the second tuple field guarantees that the numerically largest `taskId` is executed first.
- **Priority zero:** Negation leaves zero unchanged, and tuple ordering still works. Zero-priority tasks remain executable if no higher priority exists.
- **Empty manager:** `execTop` checks `not st` and returns `-1` without touching the dictionary.
- **Multiple tasks for one user:** Tasks are keyed by `taskId`, not `userId`. A user can own any number of tasks without collisions.
- **Editing the owner:** `edit` changes only priority. The source reads and preserves the existing `userId`, matching the contract.
- **Uniqueness guarantees:** `add` assumes a new task ID, while `edit` and `rmv` assume an existing one. The implementation intentionally relies on those input guarantees rather than defining overwrite or missing-task behavior.
- **Synchronization failures:** Every change must update both structures. Forgetting to remove an old ranking tuple could make `execTop` access a missing dictionary task or execute an obsolete priority.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log N)$. Let $N$ be the number of live tasks immediately before an operation. Expected dictionary lookup, insertion, and deletion cost $O(1)$. A `SortedList` lookup/removal/insertion or indexed pop has $O(\log N)$ target-search cost and the library's block-based update cost is logarithmic or amortized sublinear; the standard problem-level bound treats each such ordered-set operation as $O(\log N)$.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
