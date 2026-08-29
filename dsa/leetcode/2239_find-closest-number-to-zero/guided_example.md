# Guided Example: Find Closest Number to Zero

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [-4, -2, 1, 4, 8]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums` of size `n`, return *the number with the value **closest** to *`0`* in *`nums`. If there are multiple answers, return *the number with the **largest** value*.

The objective is to compute `1` from `{"nums": [-4, -2, 1, 4, 8]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Measure closeness with absolute value

The distance from an integer `x` to zero is `abs(x)`. Negative and positive values with the same magnitude are equally close, so distance alone does not always determine the answer. When distances tie, the larger numeric value must win; between `-a` and `a`, that is the positive value.

The solution scans once while storing:

- `ans`, the best value seen so far;
- `d`, its distance from zero.

It initializes `ans = 0` and `d = inf`. Positive infinity is larger than every finite input distance, so the first array element always becomes a genuine candidate. The initial zero is only a placeholder used by the tie expression; it cannot prevent the first update because every finite distance is below infinity.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [-4, -2, 1, 4, 8]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Evaluate one candidate

For each `x`, the assignment expression `y := abs(x)` calculates its distance once and stores it in `y` for both comparisons.

The update condition is:

`y < d or (y == d and x > ans)`.

The first part accepts a strictly closer value. The second handles equal distance and accepts only a larger numeric value. If either is true, `ans, d = x, y` updates the value and its matching distance together.

Keeping the two variables synchronized is important. After an update, `d` must describe the new `ans`, not the prior one.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The maintained best-candidate rule

After processing any prefix of `nums`, `ans` is the correct answer for that prefix: it has the smallest absolute value, and among values at that distance it is the largest.

The statement holds after the first element because it replaces the infinite placeholder. For a later `x`:

- if `x` is closer, every earlier candidate loses on the primary rule, so replacing `ans` is correct;
- if it ties in distance but is larger, it wins the secondary rule;
- otherwise, the existing `ans` remains at least as good.

By induction, after the final element `ans` is the required answer for the entire array.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [-4, -2, 1, 4, 8]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Sort with a custom key:** Sorting by `(abs(x), -x)` and taking the first value works, but costs `O(n \log n)` time and extra storage or input mutation.
- **Use `min` with a key:** `min(nums, key=lambda x: (abs(x), -x))` compactly expresses the same ordering, though the explicit scan makes the tie logic visible.
- **Track only minimum absolute value:** Without storing the chosen signed value, the larger-value tie cannot be resolved.
- **Return the first closest value:** This fails when `-a` appears before `a`.
- **Zero present:** It is always the answer.
- **All values positive:** The smallest positive value is closest.
- **All values negative:** The negative value nearest zero is also the numerically largest among them.
- **Both `-a` and `a`:** The positive `a` wins.
- **Duplicate values:** They do not affect the returned number.
- **Single element:** It replaces the infinite sentinel and is returned.
- **Maximum magnitudes:** Absolute values within the constraints are represented safely.
- **Input preservation:** The method never sorts or modifies `nums`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n = len(nums)`. The loop examines every element exactly once and performs constant work per element. Time complexity is `O(n)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
