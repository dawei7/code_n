# Guided Example: Group the People Given the Group Size They Belong To

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"groupSizes": [3, 3, 3, 3, 3, 1, 3]}`
- **Required output:** `[[5], [0, 1, 2], [3, 4, 6]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are `n` people that are split into some unknown number of groups. Each person is labeled with a **unique ID** from `0` to $n - 1$.

The objective is to compute `[[5], [0, 1, 2], [3, 4, 6]]` from `{"groupSizes": [3, 3, 3, 3, 3, 1, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: People requiring different sizes can never share a group

If person `i` has `groupSizes[i] = q`, everyone placed with that person must belong to a group containing exactly `q` people. Therefore a person requesting size two cannot share a group with one requesting size three. The first step is to bucket people by their required group size.

The dictionary `g` maps a size to the list of person identifiers requesting it. Iterating with `enumerate(groupSizes)` provides each unique identifier `i` and its required size `v`. The statement `g[v].append(i)` records the person in exactly one bucket.

Because `g` is a `defaultdict(list)`, the first person for a size automatically creates an empty list. No separate existence check is necessary.

For `[3,3,3,3,3,1,3]`, bucket three becomes `[0,1,2,3,4,6]` and bucket one becomes `[5]`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"groupSizes": [3, 3, 3, 3, 3, 1, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Split each bucket into consecutive chunks of its key size

In the return comprehension, `i` is the dictionary key representing a required group size, while `v` is the complete list of people requesting that size. The inner range `range(0, len(v), i)` produces chunk starts zero, `i`, `2 * i`, and so on.

Slice `v[j : j + i]` copies exactly `i` consecutive identifiers into one output group. In the size-three bucket above, starts zero and three produce `[0,1,2]` and `[3,4,6]`. The size-one bucket produces `[5]`.

The variable name `i` serves a different role in the comprehension than it did in the earlier enumeration. Python's comprehension scope and completed first loop make this safe, although names such as `size` and `members` would be more descriptive.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why every chunk is complete

The problem guarantees that at least one valid grouping exists. For any requested size $q$, the number of people requesting $q$ must therefore be divisible by $q$. Otherwise, after forming full $q$-person groups, an incomplete remainder would be unavoidable.

This divisibility guarantee means the final slice in every bucket contains exactly its requested number of people. The code does not explicitly validate it because the contract proves it.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[5], [0, 1, 2], [3, 4, 6]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"groupSizes": [3, 3, 3, 3, 3, 1, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[5], [0, 1, 2], [3, 4, 6]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Emit full buckets immediately:** Append each identifier to a temporary list for its size and move that list to the answer when full. It has the same asymptotic bounds and may retain fewer waiting identifiers.
- **Sort people by required size:** Sorting then chunking works but costs $O(n\log n)$ time when hashing already gives linear grouping.
- **Incomplete final chunk:** It cannot occur under the valid-solution guarantee; without that guarantee, the exact source would return an undersized invalid group.
- **Group size one:** Every person in that bucket becomes a singleton slice.
- **One group of size `n`:** All identifiers share one bucket and one output slice.
- **Several groups with the same size:** Consecutive chunks arbitrarily divide that bucket, which is allowed because any valid grouping may be returned.
- **Every person exactly once:** Bucket insertion and nonoverlapping slices guarantee no omission or duplication.
- **Output order:** Dictionary and list order make one deterministic answer, but callers must not depend on a particular order because the contract permits any.
- **Unique identifiers:** Array indices provide the required IDs from zero through $n-1$ without a separate field.
- **Positive sizes:** The lower bound of one prevents a zero step in `range` and makes every group meaningful.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of people. Building the buckets performs $n$ expected constant-time dictionary appends. Across all buckets, slicing copies exactly $n$ identifiers into result groups. Total expected time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
