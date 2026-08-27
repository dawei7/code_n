# Guided Example: Intervals Between Identical Elements

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"arr": [2, 1, 3, 1, 2, 3, 3]}`
- **Required output:** `[4, 2, 7, 2, 4, 4, 5]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** array of `n` integers `arr`.

The objective is to compute `[4, 2, 7, 2, 4, 4, 5]` from `{"arr": [2, 1, 3, 1, 2, 3, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Group indices by value

Distances for index `i` involve only other indices holding `arr[i]`. The first pass builds `d[value]` as the increasing list of positions where that value occurs.

Indices are appended during a left-to-right scan, so every group list is already sorted. No explicit sorting is required.

Once groups are separated, each group's distance sums can be computed independently and written into the corresponding positions of `ans`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"arr": [2, 1, 3, 1, 2, 3, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Compute the distance sum at the first occurrence

For one group with sorted positions

$$
v_0<v_1<\cdots<v_{m-1},
$$

the distance from `v[0]` to every group position is `v[q] - v[0]` because all positions lie to its right or equal it.

The source calculates

`val = sum(v) - v[0] * m`,

which equals

$$
\sum_q(v_q-v_0).
$$

The self-distance contributes zero automatically.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For one group with sorted positions

$$
v_0<v_1<\cdots<v_{m-... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Update the sum when moving to the next occurrence

Suppose the center moves from `v[i - 1]` to `v[i]`. Let

`delta = v[i] - v[i - 1]`.

There are `i` positions to the left of `v[i]`. Their distances each increase by `delta`, contributing `i * delta`.

There are `m - i` positions at or to the right of `v[i]`. Relative to the previous center, their distances each decrease by `delta`, contributing `-(m - i) * delta`.

Therefore,

`val += i * delta - (m - i) * delta`.

The updated `val` is written at original position `p = v[i]`.

For `i = 0`, `delta` is defined as zero, so the initial value is written unchanged.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[4, 2, 7, 2, 4, 4, 5]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"arr": [2, 1, 3, 1, 2, 3, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[4, 2, 7, 2, 4, 4, 5]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Compare every equal pair for every index:** Th:** - **Compare every equal pair for every index:** This can become $O(n^2)$ when all values match. The recurrence is linear.
- **Two prefix-sum passes per value:** Prefix index sums can compute left and right contributions directly. It is equivalent in complexity to the delta recurrence.
- **Global prefix sums:** They cannot separate only identical values without grouping.
- **Singleton value:** Its only distance is to itself, zero.
- **All values distinct:** Every answer is zero.
- **All values identical:** One group is processed in linear time.
- **Large gaps between occurrences:** `delta` captures their true index distance.
- **Self-distance:** Included algebraically as zero and requires no special removal.
- **Sorted group requirement:** It is satisfied automatically by left-to-right insertion.
- **Original output positions:** `ans[p]` restores results from group order to array order.
- **Large sums:** Python integers safely hold total distances.
- **Input preservation:** `arr` is only scanned.
- **Current occurrence coefficient:** It is included in the decreasing side of the transition because its prior distance becomes zero.
- **Group multiplicity:** Lists preserve every occurrence position.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the array length.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
