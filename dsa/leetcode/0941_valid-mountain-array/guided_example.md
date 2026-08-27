# Guided Example: Valid Mountain Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"arr": [2, 1]}`
- **Required output:** `false`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of integers `arr`, return *`true` if and only if it is a valid mountain array*.

The objective is to compute `false` from `{"arr": [2, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn the definition into two monotone walks

A valid mountain must have one internal peak. Every step before that peak is strictly upward, and every step after it is strictly downward. There can be no flat step, no second rise after descending begins, and neither endpoint may be the peak.

The solution approaches the unknown peak from both ends:

- pointer `i` walks right across the strictly increasing prefix;
- pointer `j` walks left across the strictly decreasing suffix.

If these two maximal walks meet at the same internal index, that index is the single valid peak and the whole array has the required shape.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"arr": [2, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Reject arrays that are too short

An array needs at least three elements to have a first slope, an internal peak, and a second slope. The explicit `n < 3` check returns false immediately.

This guard also makes the later boundary expressions easier to reason about. Once the two pointer loops run, there is at least one possible internal index.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | An array needs at least three elements to have a first slope... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Walking up from the left

The first loop advances while `i + 1 < n - 1` and `arr[i] < arr[i + 1]`. The first condition keeps the pointer from walking onto the final element, and the second requires a strictly increasing step.

When it stops, `i` is the last index reachable from the left through strict increases, subject to remaining before the last position.

The boundary `i + 1 < n - 1` is slightly unusual. A more common version walks as far as possible and then explicitly rejects a peak at the last index. This implementation instead prevents `i` from moving beyond `n - 2`. Consequently, an entirely increasing array ends with `i = n - 2` rather than `n - 1`. The right pointer remains at `n - 1`, so they do not meet and the array is rejected.

Any equality stops the walk because a mountain is strictly increasing, not non-decreasing.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `false` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"arr": [2, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `false` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **One pointer in two phases:** Walk upward, reje:** - **One pointer in two phases:** Walk upward, reject if the peak is an endpoint, then walk downward and require reaching the last index. This is the most common formulation and has the same `O(n)` time and `O(1)` space.
- **Track a phase flag:** Scan adjacent differences once, changing from rising to falling at most once. This can work, but it needs careful checks that both phases occurred and that equality is never allowed.
- **Count sign changes:** Compute differences and verify a positive block followed by a negative block. Materializing the difference array adds `O(n)` space unnecessarily.
- **Length below three:** Always false because no internal peak with two sides can exist.
- **Exactly three elements:** The only valid form satisfies `arr[0] < arr[1] > arr[2]`. The two pointers meet at index one precisely in that case.
- **Plateau on either side or at the top:** Equality makes both strict loops stop. The remaining gap prevents acceptance.
- **Strictly increasing input:** The last element would be the only peak candidate, which is forbidden. The loop boundary keeps `i` at `n - 2` and the pointers differ.
- **Strictly decreasing input:** The first element would be the only peak candidate. The right boundary keeps `j` at one and the pointers differ.
- **Multiple peaks:** The left pointer stops at the first failed increase, while the right pointer stops at the last failed descent. They cannot cover the entire middle with one shared index.
- **Valley shape:** Neither monotone walk can cross the central change from decreasing to increasing, so the pointers do not meet.
- **Repeated numeric values far apart:** Repeating a value is not itself forbidden; only adjacent steps must remain strict in the required directions. The pointer comparison enforces the actual local slopes.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the array length.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
