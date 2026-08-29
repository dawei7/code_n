# Guided Example: Remove Zeros in Decimal Representation

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 1020030}`
- **Required output:** `123`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **positive** integer `n`.

The objective is to compute `123` from `{"n": 1020030}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Read decimal digits arithmetically

The task removes zero digits while preserving the relative order of every nonzero digit. The exact Optimal source does this without converting the number to a string. It repeatedly extracts the least significant decimal digit with

`x = n % 10`

and removes that digit from `n` with

`n //= 10`.

This scan visits digits from right to left. Because the desired answer must keep their original left-to-right order, each retained digit must be placed in front of the nonzero digits already processed from its right.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 1020030}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Meaning of `ans` and `k`

After some least significant digits have been removed from the working `n`:

- `ans` is the integer formed by the nonzero processed digits in their original order.
- `k` is the next decimal place value immediately to the left of all digits currently stored in `ans`.

Initially, no digit has been retained. The empty constructed suffix is represented by `ans = 0`, and the first nonzero digit encountered should occupy the ones place, so `k = 1`.

When extracted digit `x` is nonzero, the update

`ans = k * x + ans`

places `x` at the decimal position immediately before the previously retained digits. Then `k *= 10` advances the next insertion place one position farther left.

When `x` is zero, the source performs neither update. This is exactly the removal operation: the zero contributes no digit position to the result, so `k` must not advance.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Trace a number with several zero groups

Consider `n = 1020030`. The digits are processed in this order:

| Extracted `x` | Action | `ans` afterward | `k` afterward |
| ---: | --- | ---: | ---: |
| 0 | Skip | 0 | 1 |
| 3 | Keep in ones place | 3 | 10 |
| 0 | Skip | 3 | 10 |
| 0 | Skip | 3 | 10 |
| 2 | Place before 3 | 23 | 100 |
| 0 | Skip | 23 | 100 |
| 1 | Place before 23 | 123 | 1000 |

The zeros disappear because they never change either constructed value or place. The nonzero digits one, two, and three remain in their original relative order even though they were discovered in reverse order.

If `k` were multiplied by ten for a skipped zero, the algorithm would preserve an empty decimal position and effectively keep the zero. For instance, advancing `k` after the zero between one and two would build 102 rather than 12. Updating `k` only for retained digits is therefore essential.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `123` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 1020030}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `123` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Convert to a string and filter characters:** `int("".join(c for c in str(n) if c != "0"))` is direct and also takes $O(D)$ time and $O(D)$ string space. The arithmetic method avoids conversion while preserving the same order.
- **Build the result while scanning left to right:** A string naturally supports this. Arithmetically, one could first reverse digits or use a highest power of ten; the exact right-to-left scan instead prepends retained digits with `k`.
- **Multiply `ans` by ten when a digit is retained:** That pattern appends digits and is appropriate when reading left to right. Used during this right-to-left scan, it would reverse the retained digit order.
- **Advance `k` for zero digits:** This would keep zero positions rather than remove them. `k` counts retained digits only.
- **Trailing zeros:** They are encountered first and skipped while `ans = 0` and `k = 1`, so they leave no trace.
- **Zeros between nonzero digits:** They do not advance `k`, allowing the nonzero digit on their left to be placed directly beside the retained suffix.
- **No zeros:** Every digit is retained, and the invariant reconstructs the original number exactly.
- **Only one nonzero digit:** All zeros are skipped and that digit is placed in the ones position, producing a positive one-digit result.
- **Input equal to zero:** The contract excludes it. If allowed, the loop would return zero, but no extra semantics are needed for the stated positive input.
- **Leading zeros:** A positive integer's decimal representation has none. The algorithm operates on the canonical numeric representation automatically.
- **Maximum input `10^15`:** The one followed by fifteen zeros is processed safely and reduces to one.
- **Relative order:** Prepending each newly discovered left-side nonzero digit is the crucial step. Sorting or merely summing digits would violate the required sequence.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(D)$. Let `D` be the number of decimal digits in the input. Every loop iteration removes exactly one digit with `n //= 10`, so there are `D` iterations. Under the standard fixed-width arithmetic model appropriate to `n <= 10^15`, modulo, division, multiplication, and addition are constant-time operations, giving $O(D)$ time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
