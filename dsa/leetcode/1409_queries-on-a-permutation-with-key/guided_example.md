# Guided Example: Queries on a Permutation With Key

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"queries": [3, 1, 2, 1], "m": 5}`
- **Required output:** `[2, 1, 2, 1]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given the array `queries` of positive integers between `1` and `m`, you have to process all $\text{queries}[i]$ (from `i=0` to `i=queries.length-1`) according to the following rules:

The objective is to compute `[2, 1, 2, 1]` from `{"queries": [3, 1, 2, 1], "m": 5}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Maintain the permutation exactly as the rules describe

The stored Optimal implementation uses direct list simulation. It begins with the required permutation:



`range(1, m + 1)` produces every integer from 1 through `m`, and converting it to a list makes the order mutable. The invariant before each query is simple: `p` is exactly the permutation that would exist after applying all earlier move-to-front operations.

The answer list `ans` starts empty. Each query contributes exactly one zero-based position, so values are appended in query order.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"queries": [3, 1, 2, 1], "m": 5}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Find the current position, not the original position

For a query value `v`, the statement



scans `p` from the beginning and returns the zero-based index at which `v` currently appears. The current qualifier matters because previous queries may have moved several values. A precomputed formula based only on the initial permutation would become stale after the first update.

Every query is between 1 and `m`, and `p` always remains a permutation of those values. Therefore, `v` is guaranteed to be present, and `index` will not raise a missing-value error.

The code immediately executes `ans.append(j)`. The requested output for this query is its position before moving it, not the position zero it will have afterward.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Move exactly that occurrence to the front

The two update statements are:



`pop(j)` removes the element at the recorded position. Because the list is a permutation, that element is exactly `v` and there is no second copy to worry about. Every element after index `j` shifts one position left.

Then `insert(0, v)` places `v` at the beginning. Existing elements shift one position right to make room. The relative order of every value other than `v` is preserved. This is precisely the specified move-to-front operation.

It would be wrong to insert first and remove using the old index afterward: insertion changes positions, so the later removal could delete a different element or leave two copies. Removing first and then inserting is the safe order.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[2, 1, 2, 1]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"queries": [3, 1, 2, 1], "m": 5}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[2, 1, 2, 1]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Fenwick tree with reserved front positions:** Place initial values after $q$ empty positions, store each value's current coordinate, and use prefix sums to count active elements before it. Each query and move then costs $O(\log(m+q))$, matching the manifest's advertised asymptotic time.
- **Segment tree:** A tree of active-position counts supports the same prefix-count and point-update operations as a Fenwick tree, but uses more code and typically larger constants.
- **Linked list:** Moving a known node to the front can be constant time, but locating a value's numerical position still requires a linear traversal unless an additional order-statistics structure is maintained.
- **Array of positions alone:** Updating only the queried value's position is insufficient because moving it changes the ranks of all values formerly before it.
- **Rebuilding with slicing:** Constructing `[v] + p[:j] + p[j+1:]` expresses the update compactly but allocates a new list on every query and remains $O(m)$ per update.
- **Query already at index zero:** The answer is zero, and removing then reinserting the value leaves the permutation unchanged.
- **Repeated query value:** Immediately repeated queries produce zero after the first occurrence because that value was just moved to the front.
- **Smallest permutation:** When `m = 1`, every valid query is 1, every reported index is zero, and every update preserves `[1]`.
- **Maximum value:** The value `m` initially appears at index $m-1$, but earlier moves can change its later index; the algorithm always searches current state.
- **Zero-based indexing:** Python's `list.index` already returns the required zero-based index. Adding one would produce incorrect one-based positions.
- **Guaranteed membership:** The input range and permutation invariant ensure `p.index(v)` always succeeds. Without that guarantee, a missing value would need explicit handling.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(m)$. Let $q$ be the length of `queries`. Creating the initial permutation takes $O(m)$ time and $O(m)$ storage. For each query, `p.index(v)` may scan all $m$ elements, so it costs $O(m)$ in the worst case. `p.pop(j)` may shift up to $m-1$ references, and `p.insert(0, v)` shifts the current list to the right; each is also $O(m)$.
- **Auxiliary Space Complexity:** $O(q)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
