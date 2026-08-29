# Guided Example: Max Difference You Can Get From Changing an Integer

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"num": 555}`
- **Required output:** `888`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer `num`. You will apply the following steps to `num` **two** separate times:

The objective is to compute `888` from `{"num": 555}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Maximize one independent result and minimize the other

The two replacement operations are applied independently to the original number. Therefore, maximizing $a-b$ separates into:

- Make `a` as large as any legal single all-occurrences replacement can make it.
- Make `b` as small as any legal replacement can make it without a leading zero or a zero result.

The code stores two independent decimal strings:



Changing `a` never changes `b`, which matches the problem's independent operations.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"num": 555}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the earliest changed digit dominates

Decimal place values decrease from left to right. Improving the first position where two candidate numbers differ has more effect than every possible change to later positions combined.

For example, increasing the thousands digit by one adds 1000, while all three later digits together can change by at most 999. Thus both the maximum and minimum strategies should make the best legal replacement involving the earliest digit that can improve the number.

Because one chosen digit must be replaced at all its occurrences, the algorithm selects which original digit to change based on its first relevant appearance, then uses `replace` globally.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Construct the largest possible result

The loop scans `a` from most significant digit to least:



A digit already equal to 9 cannot be increased. The first digit that is not 9 is the earliest improvable position. Replacing its digit value with 9 gives the largest possible value at that decisive position. Every later occurrence of the same digit must also be replaced under the operation rule, and changing it to 9 can only further increase the result.

Choosing a later original digit would leave this earlier non-9 position unchanged and produce a smaller number. Choosing a replacement below 9 would also be smaller at the first changed position.

If every digit is already 9, no replacement can increase the number. The loop performs no change, which is legal because the selected replacement digits may be equal.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `888` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"num": 555}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `888` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Enumerate all digit replacements:** Try every original and replacement digit pair, reject leading-zero results, and retain maximum and minimum. It is correct but obscures the place-value greedy insight.
- **Arithmetic digit manipulation:** Compute place values without strings. It avoids string methods but makes replacing every equal digit more verbose.
- **All nines:** The maximum result is unchanged because no digit can increase.
- **Single digit nine:** Maximum is 9, minimum is 1, and the difference is 8.
- **Leading digit already one:** It cannot be changed to zero, so minimization searches the suffix.
- **Suffix contains only zero and one:** No legal replacement can reduce the number further.
- **Repeated chosen digit:** Every occurrence must change; `replace` enforces this rule exactly.
- **Replacement digit equals original:** This permits leaving an already optimal maximum or minimum unchanged.
- **No leading zero:** The minimum uses 1 for a changed leading digit and never replaces a leading one with zero.
- **Independent operations:** The digit choice used for `a` has no effect on which digit may be chosen for `b`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(d)$. Let $d$ be the number of decimal digits. Each scan visits at most $d$ characters. Python's `str.replace` also scans and creates a length-$d$ string, and integer conversion is linear in the digit count. Total time is $O(d)$.
- **Auxiliary Space Complexity:** $O(d)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
