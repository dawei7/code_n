# Guided Example: Minimum Distance to the Target Element

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3, 4, 5], "target": 5, "start": 3}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums` **(0-indexed)** and two integers `target` and `start`, find an index `i` such that $\text{nums}[i] = target$ and $abs(i - start)$ is **minimized**. Note that `abs(x)` is the absolute value of `x`.

The objective is to compute `1` from `{"nums": [1, 2, 3, 4, 5], "target": 5, "start": 3}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

**Evaluate every valid target occurrence.** The target may appear once or many times. For any index `i` where `nums[i] == target`, its distance from the starting index is `abs(i - start)`. The required answer is simply the minimum of those distances.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3, 4, 5], "target": 5, "start": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The exact solution expresses that definition as one generator passed to `min`:

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The exact solution expresses that definition as one generato... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

`min(abs(i - start) for i, x in enumerate(nums) if x == target)`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3, 4, 5], "target": 5, "start": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Expand outward from `start`:** Check equal-dis:** - **Expand outward from `start`:** Check equal-distance positions on both sides and stop at the first target. It can return early but needs boundary handling.
- **Explicit running minimum:** Initialize a sentinel and update it inside a loop. This is longer but may be more familiar to beginners.
- **Map values to sorted positions:** Useful for many repeated queries on the same array, but unnecessary extra `O(n)` storage for one query.
- **Target at `start`:** Zero is generated and returned, the minimum possible distance.
- **Target only to the left:** Absolute value converts the negative index difference to the correct positive distance.
- **Target only to the right:** The ordinary positive difference is returned.
- **Several equally close occurrences:** They generate the same minimum; only distance is requested, so no index tie rule is needed.
- **Every element equals target:** The occurrence at `start` produces zero.
- **Single-element array:** The guaranteed target is at index zero and the result is zero.
- **Guaranteed existence:** Without it, `min` on the empty generator would fail and a default or explicit branch would be required.
- **Lazy evaluation:** The generator avoids allocating a length-`n` candidate list.
- **No early exit in exact code:** Even after seeing distance zero, `min` finishes consuming the generator, preserving `O(n)` runtime.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n = nums.length`. `enumerate` visits all `n` elements, and each equality test and distance calculation is constant time. Python’s `min` consumes the entire filtered generator, so the running time is `O(n)` even when `nums[start]` already equals the target.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
