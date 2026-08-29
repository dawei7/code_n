# Guided Example: Largest Time for Given Digits

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"arr": [1, 2, 3, 4]}`
- **Required output:** `"23:41"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array `arr` of 4 digits, find the latest 24-hour time that can be made using each digit **exactly once**.

The objective is to compute `"23:41"` from `{"arr": [1, 2, 3, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Search times in the order the answer wants

There are only 24 possible hours and 60 possible minutes, for 1,440 valid 24-hour times. This domain size is fixed, independent of input values.

Instead of generating arrangements and later comparing them, the solution enumerates valid times from latest to earliest:

- hours from `23` down to `0`;
- for each hour, minutes from `59` down to `0`.

The first time whose four digits exactly match the supplied multiset is necessarily the latest constructible time.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"arr": [1, 2, 3, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Represent duplicate digits correctly

The input may contain repeated digits, so a set is insufficient. For example, `[1, 1, 2, 3]` must distinguish two copies of one from one copy.

Array `cnt` has ten positions. For each input digit `v`, `cnt[v]` increases. It is a frequency signature of the four available digits.

For each candidate time, a new ten-entry array `t` counts:

- `h // 10`, the hour tens digit;
- `h % 10`, the hour ones digit;
- `m // 10`, the minute tens digit;
- `m % 10`, the minute ones digit.

The condition `cnt == t` means every digit occurs exactly the same number of times in the candidate and input. This simultaneously proves that every input digit is used and no digit is reused too many times.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why integer division preserves leading zeros

For hour five, `h // 10` is zero and `h % 10` is five, so the candidate contributes digits zero and five. Similarly, minute seven contributes zero and seven.

Thus `05:07` is treated as the four digits `0, 5, 0, 7` even though the numeric variables are merely five and seven. Leading zeros are not lost from the frequency check.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"23:41"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"arr": [1, 2, 3, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"23:41"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Enumerate the 24 digit permutations:** Four positions have at most `4! = 24` arrangements. Validate each and keep the latest. This is also constant time, but duplicate permutations require care.
- **Backtracking with a used array:** It handles repeated positions explicitly but is more machinery than enumerating the small valid-time domain.
- **Greedily choose each digit:** A locally largest hour digit can make the remaining hour or minute invalid. Complete enumeration is safer.
- **Repeated digits:** Frequency arrays enforce exact multiplicity and avoid set-related mistakes.
- **Midnight:** Digits `0, 0, 0, 0` produce `00:00`, a valid answer rather than an empty string.
- **Leading-zero hour or minute:** Division and modulo count the zero, and two-digit formatting restores it visibly.
- **No valid arrangement:** Exhausting every valid time proves impossibility.
- **Several valid times:** Descending enumeration returns the latest without a separate maximum variable.
- **Exactly 24:00:** It is not a valid 24-hour representation under the contract; the hour loop correctly stops at 23.
- **Input order:** Only digit multiplicities matter, so the original array order has no effect.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The loops always examine at most `24 * 60 = 1440` candidates. Each candidate performs a constant number of digit operations and compares two fixed ten-entry arrays. Since the input always contains exactly four digits and the search domain never grows, time is `O(1)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
