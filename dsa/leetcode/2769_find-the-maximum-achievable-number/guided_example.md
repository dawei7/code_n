# Guided Example: Find the Maximum Achievable Number

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"num": 4, "t": 1}`
- **Required output:** `6`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given two integers, `num` and `t`. A **number **`x`** **is** achievable** if it can become equal to `num` after applying the following operation **at most** `t` times:

The objective is to compute `6` from `{"num": 4, "t": 1}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Focus on the gap between the two numbers

The operation changes `x` by one and simultaneously changes `num` by one. To make the largest possible starting `x` eventually meet `num`, the useful choice is to move them toward each other:

- decrease `x` by one;
- increase the current value of `num` by one.

One such operation reduces the gap `x - num` by two. The exact solution turns this observation directly into `num + 2 * t`.

The formula uses the original input `num`. Although the problem describes changing `num` during operations, the method receives its starting value and computes the largest starting `x` that can meet the moving number within the allowed number of steps.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"num": 4, "t": 1}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Construct a value that is achievable

Choose

$$
x = \text{num} + 2t.
$$

Initially, `x` is `2t` larger than `num`. Apply the toward-each-other operation exactly `t` times. After `r` operations:

- `x` has decreased to `num + 2t - r`;
- the moving copy of `num` has increased to `num + r`.

At `r = t`, both expressions equal `num + t`. Therefore the chosen starting value `num + 2t` is achievable in at most `t` operations. It actually uses exactly `t` when `t > 0`.

For the example `num = 4` and `t = 1`, choose `x = 6`. Decrease 6 to 5 while increasing 4 to 5. They meet after one operation.

For `num = 3` and `t = 2`, choose `x = 7`. The pairs of current values are initially `(7, 3)`, then `(6, 4)`, then `(5, 5)`. The starting value 7 is achievable.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Choose

$$
x = \text{num} + 2t.
$$

Initially, `x` is `2t` l... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Prove that nothing larger can work

Each operation changes each number by exactly one in some chosen direction. The largest possible reduction of the distance between them occurs when they move toward each other. That reduces the distance by two. Moving one or both in any other direction reduces the distance by less, leaves it unchanged, or increases it.

After at most `t` operations, the initial distance can therefore shrink by at most `2t`. If a starting value `x` is greater than `num + 2t`, then

$$
x - \text{num} > 2t.
$$

Even the best possible choices cannot close that entire gap in `t` steps. Such an `x` is not achievable.

The formula value reaches the upper bound and the construction demonstrates how to attain it. That combination—an impossibility bound plus a matching construction—proves it is the maximum.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `6` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"num": 4, "t": 1}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `6` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Simulate `t` operations:** Repeatedly decrease:** - **Simulate `t` operations:** Repeatedly decrease a candidate and increase `num` demonstrates achievability but costs `O(t)` and still requires determining the candidate first. The formula captures the same repeated change directly.
- **Binary search the answer:** A feasibility predicate based on distance could find the maximum, but the bound is already an exact linear expression, making search unnecessary.
- **Return `num + t`:** This is the final meeting value under the optimal construction, not the maximum starting `x` requested by the problem.
- **Move only `x` toward fixed `num`:** That closes only one unit per operation and misses that `num` is allowed to move simultaneously.
- **Move both in the same direction:** Their gap stays unchanged, so this cannot make a larger starting `x` achievable.
- **Use fewer than `t` operations:** It allows a gap of at most `2r` for `r < t`, which is never larger than the `2t` maximum.
- **`t = 0` outside the stated positive constraint:** The same formula returns `num`, the only value already equal without an operation.
- **Minimum inputs:** For `num = 1` and `t = 1`, the maximum is 3; they meet at 2 after one operation.
- **Maximum stated inputs:** `num = 50` and `t = 50` produce 150 with no overflow concern in Python.
- **Negative starting values outside the stated domain:** The gap proof still works algebraically; positivity is not needed by the formula itself.
- **“At most” versus “exactly”:** The maximum uses all available operations because each can expand the feasible starting gap by two.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The method performs one multiplication, one addition, and a return. The number of operations does not depend on `num` or `t`, so time complexity is `O(1)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
