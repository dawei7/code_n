# Guided Example: Minimum Increment to Make Array Unique

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 2]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`. In one move, you can pick an index `i` where $0 \le i < \text{nums.length}$ and increment $\text{nums}[i]$ by `1`.

The objective is to compute `1` from `{"nums": [1, 2, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Sort to expose the cheapest legal final value

Each move increases one value by exactly one; no value may decrease. After sorting `nums`, process values from smallest to largest and assign each element the smallest final value that is both at least its original value and strictly greater than the preceding assigned value.

This produces unique final values while never spending an increment earlier than necessary.

Variable `y` stores the final value assigned to the previously processed element. It starts at `-1` because inputs are nonnegative. This lets the first zero, if present, remain zero.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Deriving the formula

Suppose current original value is `x`.

Because decrementing is forbidden, its final value must be at least `x`. Because processed final values are strictly increasing and `y` is their largest value, the new final value must also be at least `y + 1`.

The smallest integer satisfying both requirements is `max(y + 1, x)`. The code assigns this to `y` and adds `y - x` to `ans`.

If `x > y`, there is no collision and `x` remains unchanged. If `x <= y`, it moves just beyond `y`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Suppose current original value is `x`.

Because decrementing... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why sorting is legitimate

The problem asks only for the minimum move count, not which original index receives which final value. Equal or reordered elements are interchangeable for this cost calculation.

Sorting lets final assignments be treated in increasing order. Any feasible unique destinations can be matched to sorted originals in sorted order without increasing total increment cost. Crossing two assignments would send a smaller original farther while assigning a smaller destination to a larger original, which cannot help under increment-only moves.

Thus the ordered problem has the same optimum as the original one.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Frequency counting:** Count occurrences throug:** - **Frequency counting:** Count occurrences through maximum value `M` and carry duplicates forward. This can achieve `O(n + M)` time and `O(M)` space when the value range is affordable.
- **Hash-set probing:** Increment duplicates until an unused value appears. Without acceleration, long duplicate runs repeatedly test the same occupied values.
- **Disjoint-set next-free lookup:** Map occupied values to their next candidates and compress paths. It can avoid sorting but is more complicated.
- **Already unique values:** Each `x` exceeds `y`, so all values remain unchanged and the answer is zero.
- **All values identical:** They receive consecutive destinations beginning at their common original value. Any gap would add needless cost.
- **Large gaps:** Whenever `x > y`, the formula keeps `x` unchanged.
- **Zero values:** Initial `y = -1` allows the first zero to remain zero.
- **Input mutation:** `nums.sort()` changes the caller's order. Sort a copy if preservation is required.
- **Thirty-two-bit result guarantee:** It protects fixed-width implementations. Python integers remain safe regardless.
- **Original indices:** The code does not reconstruct destinations by input position because only the minimum total is requested.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the number of values.
- **Auxiliary Space Complexity:** $O(M)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
