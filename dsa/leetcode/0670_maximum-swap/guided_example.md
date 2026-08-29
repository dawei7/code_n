# Guided Example: Maximum Swap

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"num": 2736}`
- **Required output:** `7236`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer `num`. You can swap two digits at most once to get the maximum valued number.

The objective is to compute `7236` from `{"num": 2736}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Maximize the earliest digit that can improve

Decimal place values make an earlier digit more important than every combination of later digits. If one swap can increase position zero, that improvement dominates any swap whose first change occurs at position one or later.

Therefore, the greedy goals are:

1. find the leftmost position that can receive a larger digit from its suffix;
2. place the largest available suffix digit there;
3. if that largest digit occurs more than once, use its rightmost occurrence.

The exact two-pass solution precomputes the best suffix index for every position and then performs the first beneficial swap.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"num": 2736}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Convert digits into a mutable list

`str(num)` exposes the decimal digits in order, and `list(...)` makes them individually swappable. Character comparison works for single decimal digits because their character ordering is the same as numeric ordering.

Let `n` be the number of digits.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Meaning of the suffix-index array

`d[i]` stores the index of the largest digit in suffix `s[i:n]`. When the largest value occurs several times, it stores the rightmost occurrence.

The array begins as `[0, 1, ..., n - 1]`, so every position initially points to itself. The backward loop then propagates better choices from the right.

At position `i`:

- `d[i + 1]` already identifies the rightmost maximum in the suffix strictly after `i`;
- if `s[i] <= s[d[i + 1]]`, assign `d[i] = d[i + 1]`;
- otherwise, leave `d[i] = i`.

The less-than-or-equal comparison is deliberate. When digits tie, it chooses the later index from the suffix rather than the current one.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `7236` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"num": 2736}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `7236` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Last-position table for digits zero through nine:** Record each digit's last occurrence, then scan left to right looking for the largest greater digit available later. This uses constant-size metadata because the alphabet has ten digits.
- **Try every pair:** Swap every pair, convert, and retain the maximum. With `D` digits this takes roughly `O(D^3)` if each conversion copies `D` characters, though the small numeric constraint may hide the cost.
- **Swap with the first maximum occurrence:** This can be suboptimal when the maximum repeats; the displaced smaller digit should be moved as far right as possible.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(D)$. Let `D` be the number of decimal digits.
- **Auxiliary Space Complexity:** $O(D)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
