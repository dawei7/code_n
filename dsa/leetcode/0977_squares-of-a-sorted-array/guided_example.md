# Guided Example: Squares of a Sorted Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [-4, -1, 0, 3, 10]}`
- **Required output:** `[0, 1, 9, 16, 100]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums` sorted in **non-decreasing** order, return *an array of **the squares of each number** sorted in non-decreasing order*.

The objective is to compute `[0, 1, 9, 16, 100]` from `{"nums": [-4, -1, 0, 3, 10]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The largest square must come from an end

The input is non-decreasing, but squaring destroys ordinary order around zero. Large negative values can produce large positive squares.

Within a sorted interval `nums[i:j+1]`, the value with greatest absolute magnitude must be at one of the two ends:

- left endpoint may be the most negative;
- right endpoint may be the most positive.

Therefore, the largest remaining square is always `nums[i]^2` or `nums[j]^2`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [-4, -1, 0, 3, 10]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Two pointers

Pointer `i` starts at zero and `j` at the final index.

Each iteration computes:

- `a = nums[i] * nums[i]`;
- `b = nums[j] * nums[j]`.

The larger square is appended to `ans`, and only the pointer that supplied it moves inward.

If squares are equal, the `else` branch chooses the right value. Either choice is correct because both output values are identical.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Pointer `i` starts at zero and `j` at the final index.

Each... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why output is built backward

The algorithm repeatedly selects the largest remaining square. Thus `ans` is non-increasing.

The required answer is non-decreasing, so the final expression `ans[::-1]` reverses it.

One could instead preallocate an array and fill it from right to left. The exact code uses append plus one final reversal.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[0, 1, 9, 16, 100]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [-4, -1, 0, 3, 10]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[0, 1, 9, 16, 100]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Square then sort:** Correct but costs `O(N log:** - **Square then sort:** Correct but costs `O(N log N)`.
- **Fill result from the end:** Avoids the final reversed copy while keeping linear time.
- **All nonnegative:** Right pointer supplies values in reverse order.
- **All nonpositive:** Left pointer usually supplies the largest magnitudes.
- **Array crossing zero:** Both endpoints must be compared.
- **Equal squares:** Either endpoint may be consumed first.
- **Single element:** It is appended and reversal changes nothing.
- **Zero:** Its square is zero and naturally appears near the final descending position.
- **Duplicate values:** Each occurrence contributes one square.
- **Input preservation:** The method reads but does not mutate `nums`.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let `N` be input length.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
