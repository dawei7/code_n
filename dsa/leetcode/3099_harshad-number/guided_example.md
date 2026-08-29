# Guided Example: Harshad Number

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"x": 18}`
- **Required output:** `9`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

An integer divisible by the **sum** of its digits is said to be a **Harshad** number. You are given an integer `x`. Return the sum of the digits of `x` if `x` is a **Harshad** number, otherwise, return `-1`.

The objective is to compute `9` from `{"x": 18}` while avoiding redundant calculations and unnecessary overhead.

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

**The definition gives the algorithm directly.** A positive integer is a Harshad number exactly when it is divisible by the sum of its decimal digits. The required output is that digit sum when divisibility holds and -1 otherwise. The source therefore needs two phases: compute the digit sum, then perform one remainder test.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"x": 18}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

**Preserve the original value.** The method begins with `s, y = 0, x`. Variable `x` remains unchanged because it is needed for the final divisibility test. Variable `y` is a working copy that can be repeatedly shortened while extracting digits. Without the copy, the loop would reduce the only version of the input to zero and lose the dividend.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Extract the last decimal digit.** For a positive integer `y`:

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `9` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"x": 18}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `9` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **String conversion:** `sum(map(int, str(x)))` is concise and also $O(\log x)$ time, but allocates a decimal string and temporary iteration state.
- **Recursive digit sum:** It follows the same remainder/division recurrence but adds $O(\log x)$ call-stack space.
- **Lookup table:** The tiny `x <= 100` domain could be precomputed, but that obscures the definition and is unnecessary.
- **One-digit input:** Every value from one through nine is divisible by its own single digit.
- **`x = 10`:** Digit sum is one, so the result is one.
- **`x = 100`:** Digit sum is one, and 100 is divisible by one.
- **Internal zero digits:** They add zero but are still correctly removed one position at a time.
- **Repeated digits:** Each occurrence is extracted and added independently.
- **Positive guarantee:** It ensures `s > 0` and prevents a remainder-by-zero error.
- **Original preservation:** `y` is consumed by the loop while `x` remains available for the final test.
- **Right-to-left processing:** Addition order does not affect the final digit sum.
- **Divisibility equality:** A remainder of exactly zero is required; approximate division has no role.
- **Return contract:** A Harshad input returns the digit sum, not `true`, `x`, or the quotient.
- **No floating point:** Integer remainder and division avoid rounding entirely.
- **No mutation outside the method:** Integers are immutable, and only local bindings change.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log x)$. Let $d$ be the number of decimal digits of `x`. Each loop iteration removes one digit, so there are exactly $d$ iterations. Since:
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
