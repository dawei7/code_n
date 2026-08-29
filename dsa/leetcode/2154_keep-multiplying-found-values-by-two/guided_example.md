# Guided Example: Keep Multiplying Found Values by Two

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [5, 3, 6, 1, 12], "original": 3}`
- **Required output:** `24`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array of integers `nums`. You are also given an integer `original` which is the first number that needs to be searched for in `nums`.

The objective is to compute `24` from `{"nums": [5, 3, 6, 1, 12], "original": 3}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Build a reusable membership structure

The exact solution creates `s = set(nums)`. A set stores each distinct input value once and supports expected $O(1)$ membership testing.

Duplicates do not affect the process. Finding one occurrence is enough to trigger a doubling, and the array is not consumed: even if a value appears once, it remains considered present for every lookup. Collapsing duplicates into a set therefore preserves exactly the needed information.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [5, 3, 6, 1, 12], "original": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Follow the forced doubling chain

The loop condition is `while original in s`. When it is true, the next value is not a choice; the rules require doubling.

The source performs `original <<= 1`. A left bit shift by one multiplies a nonnegative integer by two:

$$
\textit{original}\ll1=2\cdot\textit{original}.
$$

All legal values are positive, so this bit operation has the same meaning as `original *= 2`.

The loop immediately tests the new value. For `nums = [5,3,6,1,12]` and `original = 3`, set membership drives the chain $3\to6\to12\to24$. Since 24 is absent, the loop ends and returns 24.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the first missing value is the answer

At every loop iteration, the current value occurs in the input, so the mandated operation is performed. The loop cannot legally stop at any earlier value.

When the condition becomes false, the current value does not occur. The problem says the process must stop in exactly that situation. Therefore the returned value is neither premature nor delayed; it is the unique final value of the deterministic process.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `24` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [5, 3, 6, 1, 12], "original": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `24` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Sort then scan:** Sort ascending and double `original` whenever the current sorted value matches. Because `original` only increases, one pass after sorting suffices, for $O(n\log n)$ time and implementation-dependent sort space.
- **Repeated list membership:** This follows the statement directly but can take $O(nd)$ time, up to $O(n^2)$ under the distinct-chain bound.
- **Frequency map:** A counter also supports membership but stores counts that the process never uses.
- **Original absent initially:** The loop body never runs, and the input value is returned unchanged.
- **One successful match:** The value doubles once and stops if that doubled value is absent.
- **Long chain:** Values such as `1,2,4,8,...` trigger every corresponding doubling in order.
- **Duplicates:** Multiple copies trigger only the same one doubling step because membership is boolean and elements are not consumed.
- **Unrelated values:** Set elements not on the doubling chain never affect the result.
- **Original greater than every array value:** It is absent unless equal to some entry, so the method usually returns it immediately.
- **Final value above 1000:** This is valid and is represented safely by Python.
- **Positive-value guarantee:** Strict growth and termination reasoning use `original > 0`. A zero start would double to zero forever if zero were present, but zero is excluded by the contract.
- **Bit shift meaning:** `<<= 1` is exact integer multiplication by two, not a floating-point operation.
- **Input preservation:** Constructing `s` does not sort or modify `nums`.
- **Set expected complexity:** Hash membership is expected constant time; adversarial collision behavior is not the standard model used by the manifest.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the input length. Building `set(nums)` takes $O(n)$ expected time and $O(n)$ space in the worst case.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
