# Guided Example: Reach End of Array With Max Score

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 3, 1, 5]}`
- **Required output:** `7`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` of length `n`.

The objective is to compute `7` from `{"nums": [1, 3, 1, 5]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 3

Interpret that jump as crossing each unit boundary between consecutive indices `i, i+1, ..., j-1`. It contributes `nums[i]` once for every crossed boundary. Thus any complete route assigns one departure value to each of the $n-1$ boundaries.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 3, 1, 5]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 4

For boundary after index `t`, the jump crossing it must have started at some index no greater than `t`. The greatest possible contribution for that boundary is therefore the maximum value seen in prefix `nums[0..t]`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Optimality Decision

Synthesize the final answer directly from validated sub-states.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `7` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 3, 1, 5]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `7` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Dynamic programming over destinations:** Trying every previous jump start costs $O(n^2)$. Prefix maxima collapse the transition structure.
- **Greedy jump to the next larger value:** This can construct an optimal route, but summing boundary maxima is simpler when only the score is needed.
- **Always jump one step:** It earns the sum of original departure values, which can miss carrying an earlier large value across many boundaries.
- **Always jump directly to the end:** This is optimal only when `nums[0]` remains the prefix maximum throughout.
- **Single element:** There are no jumps or boundaries; `nums[:-1]` is empty and the answer is zero.
- **Strictly increasing values:** Prefix maximum changes at every index, and unit jumps between records achieve the sum.
- **Strictly decreasing values:** The first value remains best, so a direct final jump is optimal.
- **Equal record values:** Jumping to the equal value is unnecessary but would not change score.
- **Last element's value:** It cannot be used as a departure because the route ends there, so excluding it is correct.
- **Input preservation:** The method never assigns into `nums`, though slicing creates a temporary copy.
- **Exact-space mismatch:** The mathematical algorithm is constant-space; the concrete slice prevents the submitted source from being strictly so.
- **Boundary-count identity:** A jump of length `j-i` crosses exactly `j-i` unit boundaries, which is why multiplying by `nums[i]` equals adding that departure value once per crossed boundary.
- **Route construction from records:** Whenever a new prefix maximum appears before the final index, the current route can jump to it. Skipping all other indices then realizes every prefix-max contribution simultaneously.
- **Why local contributions combine:** Every route crosses each boundary exactly once because indices only increase. Maximizing the permitted contribution independently at each boundary does not create incompatible choices; record-max jumps realize the complete set.
- **Positive-value assumption:** With legal positive values, more distance under a larger prefix maximum never hurts. The same formula can extend to arbitrary values with a corrected negative-infinity initialization.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. The scan visits $n-1$ elements and performs constant work at each, giving $O(n)$ time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
