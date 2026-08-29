# Guided Example: Self Dividing Numbers

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"left": 1, "right": 22}`
- **Required output:** `[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A **self-dividing number** is a number that is divisible by every digit it contains.

The objective is to compute `[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]` from `{"left": 1, "right": 22}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Test the definition directly for every number

A number is self-dividing when every decimal digit is nonzero and divides the complete number evenly. The requested range is inclusive, so the exact solution checks every integer from `left` through `right` and keeps precisely those that pass a helper function.

There is no useful monotone boundary in the number line: a passing number may be followed by a failing one and then another passing one. Direct per-number validation is therefore the natural method within the small range constraint.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"left": 1, "right": 22}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Keep the original number separate from the digit scanner

The helper receives a candidate `x` and copies it into `y`. These variables have different roles:

- `x` remains unchanged because every divisibility test must divide the complete candidate number.
- `y` is progressively shortened to expose its digits.

On each iteration, `y % 10` is the current last digit. Integer division `y //= 10` then removes that digit. Repeating until `y` becomes zero visits every decimal digit exactly once, from right to left.

If the code modified `x` itself while extracting digits, later tests would divide a shortened prefix rather than the original number and would no longer implement the definition.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Reject zero before attempting division

The condition is

`if y % 10 == 0 or x % (y % 10):`

Python evaluates `or` from left to right and short-circuits. When the digit is zero, the first part is true, so the modulo expression `x % 0` is never evaluated. The helper safely returns `false` instead of raising division-by-zero.

If the digit is nonzero, `x % digit` is zero exactly when the digit divides `x` evenly. In a Boolean context, zero is false and a nonzero remainder is true. Therefore the second condition rejects precisely the non-dividing digits.

The expression is compact, but its meaning is:

- Reject if the digit equals zero.
- Otherwise reject if the original number has a nonzero remainder when divided by that digit.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"left": 1, "right": 22}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Convert the candidate to a string:** Iterate through character digits, reject `"0"`, and convert each other character back to an integer for modulo. This is readable and has the same `O(D)` per-number time, but it creates a string representation. Arithmetic extraction uses constant working space.
- **Precompute valid numbers:** Because the stated domain is small, a fixed table of all self-dividing numbers could answer ranges quickly. That shifts work and data into preprocessing and is less general than checking the supplied interval.
- **Generate numbers digit by digit:** A backtracking generator can avoid all zero-containing candidates, but divisibility by every constructed digit still needs checking and the extra complexity is unnecessary for the domain.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(WD)$. Let `W = right - left + 1` be the number of candidates and let `D` be the maximum number of decimal digits among them.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
