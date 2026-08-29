# Guided Example: Sum of Even Numbers After Queries

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3, 4], "queries": [[1, 0], [-3, 1], [-4, 0], [2, 3]]}`
- **Required output:** `[8, 6, 2, 4]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` and an array `queries` where $\text{queries}[i] = [\text{val}_{i}, \text{index}_{i}]$.

The objective is to compute `[8, 6, 2, 4]` from `{"nums": [1, 2, 3, 4], "queries": [[1, 0], [-3, 1], [-4, 0], [2, 3]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Maintain the answer instead of recomputing it

After every query, the requested value is the sum of all even elements currently in `nums`. A straightforward solution could scan the complete array after each update. That repeats almost all work, because one query changes exactly one position and every other contribution stays the same.

The optimal idea is to maintain a running sum `s`. Before processing queries, the generator

`sum(x for x in nums if x % 2 == 0)`

computes the even-element sum once. From then on, a query repairs only the contribution of the modified index.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3, 4], "queries": [[1, 0], [-3, 1], [-4, 0], [2, 3]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: The invariant carried between queries

Immediately before and immediately after every query, `s` equals

> the sum of precisely those current elements of `nums` that are even.

This statement is stronger than merely saying `s` was correct initially. It explains why the same constant-time update can be repeated for thousands of queries, including many updates to the same index.

Suppose a query is `[v, i]`. Only `nums[i]` changes. All other values retain both their numeric values and their parity, so their combined contribution to `s` must remain untouched. The code removes the old contribution at index `i`, changes the number, and adds its new contribution.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Remove the old value only when it currently contributes

Before mutation, the code checks

`if nums[i] % 2 == 0:`

and subtracts `nums[i]` from `s` when the value is even. If the old value is odd, it contributes nothing to the even sum, so there is nothing to subtract.

This removal must occur before `nums[i] += v`. After mutation, the old value is no longer available at that index, and checking its old parity would require storing an extra variable. The chosen ordering keeps the logic direct.

Subtracting a negative even value is also correct. For example, if the running sum includes `-4`, removing that contribution performs `s -= -4`, which increases `s` by four. That is exactly what happens to a sum when a negative term is deleted.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[8, 6, 2, 4]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3, 4], "queries": [[1, 0], [-3, 1], [-4, 0], [2, 3]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[8, 6, 2, 4]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Rescan after every query:** Update the index and sum all even values from scratch. It is easy to understand but costs `O(NQ)` time.
- **Segment tree:** Maintain a tree of even contributions with point updates and a root sum. It supports each update in `O(\log N)` but is unnecessary because the required aggregate can be repaired in constant time.
- **Track only parity changes:** One can derive cases from the parity of `v`, but the running sum still needs the old and new numeric values. Direct removal and addition is clearer.
- **Negative even values:** They contribute negatively to `s`. Subtracting the old negative value and adding the new negative value follow normal arithmetic.
- **Zero:** Zero passes the even test but changes the sum by zero, so no special handling is needed.
- **Repeated queries at one index:** Every iteration reads the current mutated value, removes its current contribution, and applies the next update correctly.
- **An update value of zero:** The old contribution is removed and then the identical new contribution is restored when even; the reported sum remains unchanged.
- **Odd-to-odd update:** Both conditionals skip the value, leaving `s` unchanged even though the stored number changes.
- **Single-element array:** The invariant reduces to whether that one current value is even, and the same code produces one answer per query.
- **Input mutation:** Callers that need the original `nums` afterward would have to pass a copy. The solution itself intentionally preserves the required cumulative query state in the given list.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N + Q)$. Let `N` be the length of `nums` and `Q` the number of queries. Computing the initial even sum scans `N` values once, taking `O(N)` time. Every query performs a constant number of arithmetic operations, parity tests, one array update, and one append, so all queries take `O(Q)` time. Total time is `O(N + Q)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
