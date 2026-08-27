# Guided Example: Form Smallest Number From Two Digit Arrays

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums1": [4, 1, 3], "nums2": [5, 7]}`
- **Required output:** `15`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given two arrays of **unique** digits `nums1` and `nums2`, return *the **smallest** number that contains **at least** one digit from each array*.

The objective is to compute `15` from `{"nums1": [4, 1, 3], "nums2": [5, 7]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A shared digit gives the best possible number

The result must contain at least one digit from each array. If digit $d$ occurs in both, the one-digit number $d$ satisfies both requirements simultaneously.

Every allowed digit is from one through nine, so any one-digit candidate is smaller than every two-digit candidate. Therefore, when common digits exist, the answer is the smallest common digit.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums1": [4, 1, 3], "nums2": [5, 7]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Without a shared digit, two digits are necessary

If the arrays are disjoint, no single digit can represent both. A valid number needs at least one digit $a$ from `nums1` and one digit $b$ from `nums2`.

The smallest possible valid number then has exactly two digits. Adding more digits would create a number of at least three decimal places and make it larger because leading zero is impossible under the digit constraints.

For a chosen pair $(a,b)$, either order is allowed:

$$
10a+b
\quad\text{or}\quad
10b+a.
$$

The smaller order places the smaller digit in the tens position.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | If the arrays are disjoint, no single digit can represent bo... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Enumerate every cross-array pair

The exact solution initializes `ans = 100`. Every valid result is at most 99, so this is a safe sentinel larger than all candidates.

For every `a in nums1` and `b in nums2`:

- when `a == b`, update with one-digit candidate `a`;
- otherwise update with both two-digit orders.

`min` retains the smallest candidate seen across all pairs.

This direct enumeration combines common-digit detection and disjoint-digit construction in one compact loop.

There is no risk that the sentinel survives. Both input arrays are nonempty, so the nested loops execute at least once. That first pair always produces either its shared one-digit value or two valid two-digit values, each strictly below 100. From then on, `ans` is always a real feasible result, and later iterations can only improve it. This detail explains both why no special initialization branch is needed and why returning `ans` after the loops is safe.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `15` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums1": [4, 1, 3], "nums2": [5, 7]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `15` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Set intersection:** Find the smallest common d:** - **Set intersection:** Find the smallest common digit directly, then use both array minima if none exists.
- **Sort both arrays:** Sorting is unnecessary for at most 81 direct candidates and would add mutation or copies.
- **Multiple common digits:** The nested minimum keeps the smallest one.
- **No common digit:** Exactly two digits are necessary, and both orders are tested.
- **Smaller digit from second array:** Testing `10*b+a` ensures it can occupy the tens place.
- **One-element arrays:** The sole pair yields either their shared digit or the smaller of the two orders.
- **No zero digits:** Every constructed two-digit candidate truly has two decimal digits.
- **Sentinel 100:** All valid candidates lie from one through 99, so it is safely replaced.
- **Input preservation:** Neither array is modified.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. Let $n_1$ and $n_2$ be the array lengths. The nested loops take $O(n_1n_2)$ time and $O(1)$ auxiliary space.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
