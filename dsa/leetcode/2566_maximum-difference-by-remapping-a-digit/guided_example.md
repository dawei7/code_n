# Guided Example: Maximum Difference by Remapping a Digit

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"num": 11891}`
- **Required output:** `99009`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer `num`. You know that Bob will sneakily **remap** one of the `10` possible digits (`0` to `9`) to another digit.

The objective is to compute `99009` from `{"num": 11891}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A remapping changes every occurrence

Choosing source digit $a$ and destination digit $b$ replaces all occurrences of $a$ in the decimal numeral, not just one position. The remapping used for the maximum may differ from the one used for the minimum, so the two extremes can be optimized independently.

The solution converts `num` to string `s`. String replacement naturally applies a mapping to every occurrence of one digit. Because leading zeros are allowed, the resulting string may begin with zero; converting it with `int` correctly interprets those zeros as having no numeric value.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"num": 11891}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Construct the smallest possible value

The most significant digit `s[0]` is nonzero because `num` is a normal positive integer. Replacing that digit with `'0'` creates the largest possible decrease at the earliest decimal position. The code computes

`mi = int(s.replace(s[0], '0'))`.

Why is this globally minimal? Suppose a different source digit first appears at position $p>0$. Any decrease produced by changing it begins at a less significant position, while the original leading digit remains unchanged. Replacing the leading digit with zero lowers the number at the very first position, which dominates every possible combination of changes in later positions.

Among mappings of the leading digit, zero is the smallest destination. Replacing all later occurrences of that same digit with zero can only decrease the value further. Therefore this one replacement gives the minimum.

For `num = 11891`, replacing all ones with zero produces string `"00890"`, interpreted as $890$.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The most significant digit `s[0]` is nonzero because `num` i... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Construct the largest possible value

To maximize the number, scan from left to right for the first digit that is not nine. Call it $c$. Replacing every occurrence of $c$ with nine makes the earliest improvable position as large as possible:

`s.replace(c, '9')`.

All earlier digits are already nine and cannot be increased. Any remapping whose first changed position comes later leaves digit $c$ smaller than nine at this earliest point, so its result is smaller regardless of later digits. Once $c$ is chosen, nine is the greatest destination digit, and replacing every later occurrence of $c$ with nine can only help.

The function returns immediately when it finds this first non-nine digit, calculating the maximum value minus `mi`.

For `11891`, the first non-nine digit is `'1'`. Replacing every one by nine gives `99899`. Subtracting $890$ yields $99009$.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `99009` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"num": 11891}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `99009` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Try every source and destination digit:** Test:** - **Try every source and destination digit:** Testing all 100 mappings for each endpoint is still constant in digit-alphabet size, but it repeats full scans and hides the simple place-value greedy rule.
- **Arithmetic digit rebuilding:** Digits can be extracted and reconstructed numerically, but string replacement expresses “all occurrences” more directly.
- **All digits are nine:** The maximum cannot increase; remapping nine to itself keeps `num` valid under the exactly-one-remapping rule.
- **Leading zeros in the minimum:** They are explicitly allowed, and `int` discards them naturally when computing the numeric value.
- **Repeated leading digit:** Every occurrence is replaced, so later copies become zero in the minimum as required.
- **First digit already nine for maximum:** The scan skips it and improves the first later non-nine digit.
- **Single-digit number:** A digit below nine can become nine for the maximum and zero for the minimum; digit nine keeps nine as its maximum.
- **Digit absent from the number:** Remapping an absent digit changes nothing and is allowed conceptually, but it cannot beat the greedy maximum or minimum.
- **Different mappings:** The maximum and minimum constructions intentionally choose source digits independently.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(d)$. Let $d$ be the number of decimal digits in `num`. Converting to a string takes $O(d)$ time and space. Replacing the leading digit scans the string once. Finding the first non-nine digit scans at most $d$ positions, and the maximum replacement performs another $O(d)$ scan. Integer parsing is also $O(d)$.
- **Auxiliary Space Complexity:** $O(d)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
