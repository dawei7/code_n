# Guided Example: Average Salary Excluding the Minimum and Maximum Salary

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"salary": [4000, 3000, 1000, 2000]}`
- **Required output:** `2500`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array of **unique** integers `salary` where $\text{salary}[i]$ is the salary of the $i^{\text{th}}$ employee.

The objective is to compute `2500` from `{"salary": [4000, 3000, 1000, 2000]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Reducing the requested average to three statistics

An arithmetic mean is the sum of the included values divided by how many values are included. The input has $N$ salaries. Exactly one is the minimum and exactly one is the maximum because all salaries are unique. After excluding those two employees, $N-2$ salaries remain.

Instead of constructing a filtered list, the stored solution computes the sum of all salaries and subtracts the two excluded values:

$$
S_{\text{middle}}
=
\left(\sum_{i=0}^{N-1} salary[i]\right)
- \min(salary)
- \max(salary).
$$

The line `s = sum(salary) - min(salary) - max(salary)` implements this identity. The return statement divides `s` by `len(salary) - 2`, the number of remaining employees.

This is an algebraic filtering technique. Every salary initially contributes once to the total. Subtracting the minimum removes its one contribution, and subtracting the maximum removes its one contribution. Every other salary remains exactly once.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"salary": [4000, 3000, 1000, 2000]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Following the exact Python behavior

`sum(salary)` iterates through the list and adds every integer. `min(salary)` makes another traversal to find the least value, and `max(salary)` makes a third traversal to find the greatest value. The expression then performs two integer subtractions and assigns the middle-salary total to `s`.

`len(salary)` is constant time for a Python list because the list stores its current length. The denominator is at least one under the constraint $N \ge 3$, so division by zero cannot occur.

Python's slash operator performs true division. Even when both operands are integers, `s / (len(salary) - 2)` returns a floating-point value. No manual cast is needed, unlike languages in which integer divided by integer truncates the fractional part.

The function does not sort, overwrite, or otherwise mutate `salary`. The three built-ins inspect it and the remaining operations use scalar values.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why uniqueness matters

Uniqueness makes the phrase “the minimum and maximum salary” correspond to two distinct employees and two distinct values. Subtracting each extreme once removes exactly those employees.

Even if duplicate extreme values were allowed, the formula would still subtract one occurrence of each numeric extreme, but that might not match a different contract that intended to exclude every employee tied for minimum or maximum. The given uniqueness guarantee removes that ambiguity. It also ensures the minimum and maximum cannot be the same because there are at least three distinct values.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2500` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"salary": [4000, 3000, 1000, 2000]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2500` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Single explicit pass:** Maintain running total, minimum, and maximum together, then apply the same formula. It has identical asymptotic bounds and one traversal, but more source code and initialization details.
- **Sorting:** Sort salaries and average the middle slice. This is easy to visualize but takes $O(N \log N)$ time and may mutate the input or allocate a copy.
- **Filtering by value:** Find both extremes, then sum values unequal to them. It is correct under uniqueness but requires additional passes and can become semantically wrong if a future contract allows tied extremes but excludes only one employee at each end.
- **Smallest valid length:** With three salaries, one middle employee remains. The denominator is one, so the result is exactly that employee's salary as a float.
- **Fractional average:** Python true division retains a fractional result instead of truncating it.
- **Unique extremes:** The guarantees ensure that subtracting minimum and maximum removes two different list elements.
- **Input order:** Salaries may appear in any order; sum, minimum, and maximum are order-independent.
- **No mutation:** The source leaves the caller's list unchanged, unlike an in-place sorting solution.
- **Floating-point tolerance:** A repeating or non-binary-exact average is acceptable within the stated tolerance; rounding the result to an integer would not be acceptable.
- **Hypothetical fewer than three values:** The denominator could be zero or negative, but those inputs are excluded by the contract.
- **Large numeric total:** The bounded data is safe, and Python integer summation does not overflow fixed-width storage.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. Let $N$ be the number of salaries. `sum` scans $N$ elements, `min` scans $N$ elements, and `max` scans $N$ elements. Three linear passes take $3N$ element visits, which simplifies to $O(N)$ time. The exact implementation is therefore linear even though it is not literally a single-pass loop.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
