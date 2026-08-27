# Guided Example: Design Memory Allocator

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"commands": ["Allocator", "freeMemory", "allocate"], "inputs": [[3], [9], [1, 9]]}`
- **Required output:** `[null, 0, 0]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer `n` representing the size of a **0-indexed** memory array. All memory units are initially free.

The objective is to compute `[null, 0, 0]` from `{"commands": ["Allocator", "freeMemory", "allocate"], "inputs": [[3], [9], [1, 9]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Represent every memory unit by its current owner

The allocator stores `m`, an array of length `n`. Entry zero means the unit is free, while a positive entry is the `mID` that owns it.

This encoding is unambiguous because the constraints require `mID>=1`. It also naturally supports the same identifier owning several separated blocks: every owned unit independently stores that identifier.

At construction, `[0]*n` marks all units free.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"commands": ["Allocator", "freeMemory", "allocate"], "inputs": [[3], [9], [1, 9]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Find the leftmost free run during allocation

`allocate(size,mID)` scans the memory array from index zero upward. Variable `cnt` is the length of the consecutive free run ending at the current index.

- If `v` is nonzero, the current unit is occupied and no free run can cross it, so `cnt` resets to zero.
- If `v` is zero, the current free run extends by one and `cnt` increments.

When `cnt==size` at index `i`, the run begins at

`i-size+1`

and ends at `i`.

The slice

`m[i-size+1:i+1] = [mID]*size`

assigns every unit in that block to the requested identifier. The method immediately returns the start index.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `allocate(size,mID)` scans the memory array from index zero ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the first found run is the leftmost

The scan examines end indices in increasing order. A block of fixed length `size` has start `end-size+1`, which also increases with its end.

The first time a free-run counter reaches `size` is therefore the smallest possible end and smallest possible start of any fitting block. Returning immediately implements the leftmost requirement.

A longer free region causes allocation at its first `size` positions. The scan does not wait to see whether an even larger free run exists because size, not maximum capacity, determines the request.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[null, 0, 0]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"commands": ["Allocator", "freeMemory", "allocate"], "inputs": [[3], [9], [1, 9]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[null, 0, 0]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Free-interval tree:** Track free ranges for fa:** - **Free-interval tree:** Track free ranges for faster allocation, but merging after frees becomes more complex.
- **Segment tree:** Store maximum free prefix, suffix, and run lengths to find blocks faster when constraints are much larger.
- **Size one:** The first zero entry is allocated immediately.
- **Request fills all memory:** It succeeds only when the full array is free.
- **Enough total free units but fragmented:** Allocation correctly returns `-1` if no consecutive run is long enough.
- **Repeated `mID` allocations:** They may form separate blocks; freeing scans and releases all of them.
- **Unknown `mID` on free:** Return zero without changing state.
- **Leftmost rule:** Immediate return at the first completed run is essential.
- **Sentinel zero:** It is safe only because valid identifiers are positive.
- **Failed allocation:** It performs no partial write.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(qn)$. Let $n$ be the memory-array size and $q$ the total number of method calls.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
