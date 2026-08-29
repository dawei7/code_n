# Guided Example: Apply Operations to an Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 2, 1, 1, 0]}`
- **Required output:** `[1, 4, 2, 0, 0, 0]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** array `nums` of size `n` consisting of **non-negative** integers.

The objective is to compute `[1, 4, 2, 0, 0, 0]` from `{"nums": [1, 2, 2, 1, 1, 0]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Simulate in the required left-to-right order

The adjacent operations are sequential. An operation can change a value that a later index will inspect, so all comparisons cannot be made from the original array at once.

The first loop visits `i=0` through `n-2`. When `nums[i] == nums[i+1]`, it doubles the left value using `nums[i] <<= 1` and sets the right value to zero. Left shift by one bit multiplies a non-negative integer by two.

Because the array is modified immediately, iteration `i+1` sees the result of iteration `i`. For example, if an operation zeros `nums[i+1]`, the next comparison uses that zero. This matches the statement's sequential semantics.

Equal zeros also satisfy the equality condition. Doubling zero and setting the next value to zero leaves both unchanged, so the code may execute the branch without affecting the result.

A doubled value is written at index `i` after that index's comparison has begun, so it is never compared again as the left member of a later operation. The zero written at `i+1` is compared in the next iteration. For a run such as `[2,2,2]`, the first operation makes `[4,0,2]`; the second compares 0 with 2 and does nothing. It would be incorrect to combine the last two original twos after the first pair has already changed the shared middle position.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 2, 1, 1, 0]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Separate combination from zero shifting

After all adjacent operations, the problem asks for a stable compaction: nonzero values keep their relative order, and enough zeros fill the remaining suffix.

The exact source allocates `ans = [0] * n`. Pointer `i` identifies the next output position for a nonzero value. Scanning the mutated `nums` from left to right:

- If `x` is zero, it is skipped.
- If `x` is nonzero, it is written to `ans[i]` and `i` increments.

Since `ans` started entirely zero, every position not overwritten remains zero. Nonzero values are written in encounter order, so compaction is stable.

For `[1,2,2,1,1,0]`, sequential operations produce `[1,4,0,2,0,0]`. The second pass writes 1, 4, and 2 into the first three answer positions, leaving the last three zeros.

For `[0,1]`, no equality operation changes the array. Compaction skips the leading zero, writes 1 at answer index zero, and returns `[1,0]`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why every operation is simulated exactly once

The first loop's index corresponds one-to-one with the $n-1$ prescribed operations. At each index it checks the current adjacent values, applies exactly the specified update when equal, and does nothing otherwise. Induction over the loop proves the mutated `nums` equals the statement's array after the same number of operations.

The compaction pass then produces the unique sequence consisting of all nonzero values from that final intermediate array followed by all its zeros. It neither invents nor loses a value: each nonzero is copied once, while the preallocated length preserves the correct total number of positions.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 4, 2, 0, 0, 0]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 2, 1, 1, 0]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 4, 2, 0, 0, 0]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **In-place stable compaction:** Use a write pointer to move nonzero values forward in `nums` after operations, then fill the suffix with zeros. This matches the manifest's $O(1)$ auxiliary-space claim.
- **Combine operation and compaction carefully:** A one-pass method is possible but must respect that a newly produced zero participates in the next prescribed comparison. Separating phases is easier to verify.
- **Apply all comparisons simultaneously:** This is incorrect because later operations must observe earlier mutations.
- **Adjacent equal zeros:** The branch executes but changes nothing.
- **No equal adjacent values:** Only the compaction phase changes the arrangement.
- **All zeros:** Every operation is harmless and the returned array remains all zeros.
- **All nonzero after operations:** Every value is copied to the same relative position and no trailing zero is added.
- **Stable order:** Nonzero values must not be sorted; the write pointer preserves encounter order.
- **Input mutation:** The first phase changes `nums` even though the final shifted result is stored separately.
- **Exact array length:** Preallocating $n$ positions guarantees that the count of removed interior zeros reappears at the end.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. The operation loop examines $n-1$ adjacent pairs. The compaction loop examines $n$ values. Every iteration does constant work, so total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
