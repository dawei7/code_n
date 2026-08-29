# Guided Example: Number of Good Pairs

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3, 1, 1, 3]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of integers `nums`, return *the number of **good pairs***.

The objective is to compute `4` from `{"nums": [1, 2, 3, 1, 1, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Counting pairs when their right endpoint arrives

A good pair requires equal values and indices `i < j`. Instead of storing every earlier index, the stored solution records how many times each value has appeared.

When the loop reaches a current value `x` at index `j`, suppose `cnt[x] = c`. There are exactly `c` earlier indices whose values equal `x`. Each can be paired with the current index, so this one occurrence creates `c` new good pairs.

The code adds `cnt[x]` to `ans` and then increments `cnt[x]`. This order is important. The current occurrence must not pair with itself, so it contributes to the count only after all pairs ending here have been counted.

`Counter()` begins empty and supplies zero for a missing key. The first occurrence of any value therefore adds no pairs and creates count one without special-case code.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3, 1, 1, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: A trace with repeated values

Consider three occurrences of value one:

- The first sees zero earlier ones and adds zero.
- The second sees one earlier one and adds one pair.
- The third sees two earlier ones and adds two pairs.

The total is three, matching the index pairs among three positions. A fourth occurrence would add three more, bringing the total to six.

Values are independent. Seeing a three changes only `cnt[3]` and adds the number of earlier threes. It cannot create a pair with a one because equality is required.

For `[1, 2, 3, 1, 1, 3]`, the second one adds one, the third one adds two, and the second three adds one, giving four.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The invariant after processing a prefix

After processing the first `j` elements:

1. `cnt[v]` equals the number of occurrences of value `v` in that prefix.
2. `ans` equals the number of good pairs whose two indices are both in that prefix.

Both statements hold for the empty prefix. When the next value `x` arrives, existing good pairs remain unchanged. The only new pairs are those whose right index is the new position and whose left value is also `x`. There are exactly `cnt[x]` of them, so adding that count updates `ans` correctly. Incrementing the counter then restores the frequency fact for the extended prefix.

By induction, the returned `ans` counts all good pairs in the complete array.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3, 1, 1, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Count all frequencies first:** Sum `f * (f - 1) // 2` for every value. It has the same $O(N)$ time and $O(U)$ space but uses two conceptual phases.
- **Check every index pair:** Nested loops are simple but take $O(N^2)$ time.
- **Fixed frequency array:** Because values lie from one through one hundred, a small list can replace the hash counter.
- **All values distinct:** Every lookup sees zero earlier matches, so the answer remains zero.
- **All values equal:** Contributions are zero through $N-1$, totaling $N(N-1)/2$.
- **Single element:** No pair exists, and the loop returns zero.
- **Update order:** Incrementing before adding would incorrectly count each element paired with itself.
- **Repeated values far apart:** Position distance is irrelevant; every earlier equal value forms a valid pair.
- **Index order:** Left-to-right processing ensures only pairs with the earlier index first are counted.
- **Required import:** `Counter` must be available from `collections`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the array length and $U$ the number of distinct values. The loop processes each element once. `Counter` lookup and update take expected $O(1)$ time, so total expected time is $O(N)$.
- **Auxiliary Space Complexity:** $O(u)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
