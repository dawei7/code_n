# Guided Example: Largest Number After Mutating Substring

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"num": "132", "change": [9, 8, 5, 0, 3, 6, 4, 2, 6, 8]}`
- **Required output:** `"832"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `num`, which represents a large integer. You are also given a **0-indexed** integer array `change` of length `10` that maps each digit `0-9` to another digit. More formally, digit `d` maps to digit $\text{change}[d]$.

The objective is to compute `"832"` from `{"num": "132", "change": [9, 8, 5, 0, 3, 6, 4, 2, 6, 8]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Compare equal-length numbers from left to right

Every mutation replaces one digit with one digit, so the result always has the same length as `num`. Among equal-length digit strings, numeric order is lexicographic order: the first position where two strings differ determines which number is larger.

Therefore the best mutation should start at the earliest position where the mapped digit is strictly larger than the original. Any improvements later cannot compensate for voluntarily making an earlier digit smaller, and equal earlier digits do not affect the comparison.

The solution converts `num` to a mutable character list `s` and scans left to right. For current digit character `c`, it computes mapped character `d = str(change[int(c)])`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"num": "132", "change": [9, 8, 5, 0, 3, 6, 4, 2, 6, 8]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Delay the substring until a strict improvement

While `changed` is false:

- if `d < c`, mutating here would worsen the first differing digit, so the algorithm skips it;
- if `d == c`, including or excluding this position produces the same visible result, so it also skips it;
- if `d > c`, this is the earliest profitable start. The code sets `changed = true` and stores `d`.

Starting later than this first strict improvement would preserve the smaller original digit at this decisive position and could never yield a larger final number.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | While `changed` is false:

- if `d < c`, mutating here would... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Continue through neutral or improving positions

Once mutation has started, all changed positions must form one contiguous substring. A mapped digit larger than the original should be written. A mapped digit equal to the original can remain physically unchanged, but the chosen conceptual substring may pass through it; the output is identical either way.

The exact code writes only strict improvements. When `d == c` after starting, neither the break nor assignment executes, `changed` remains true, and the scan continues. This correctly allows a later improvement within the same substring.

At the first position where `d < c` after mutation began, the code breaks. Including that position would make the result worse at the earliest difference after an already fixed prefix. Ending the substring immediately before it preserves all earlier gains. Because only one substring may be mutated, no position after this break may be changed.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"832"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"num": "132", "change": [9, 8, 5, 0, 3, 6, 4, 2, 6, 8]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"832"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Try every substring:** Mutate each of $O(N^2)$:** - **Try every substring:** Mutate each of $O(N^2)$ intervals and compare results, leading to at least quadratic and often cubic work with string construction.
- **Dynamic programming states:** States for “not started,” “inside,” and “finished” can model the rule, but lexicographic greed makes the transitions deterministic.
- **Start on an equal mapping:** It is harmless but unnecessary. Delaying the recorded start until the first strict improvement leaves the output and future options unchanged.
- **Equal mapping after start:** It must not end the interval; the code continues so later improvements remain reachable.
- **First harmful mapping after start:** The method stops before it and never mutates later digits because a second substring is forbidden.
- **No improving digit:** `changed` remains false and the original number is returned.
- **Single digit:** It is replaced only if its mapped digit is larger.
- **Leading zero:** It is treated like any digit. Mapping it upward can create the most important possible improvement.
- **Mapped digit smaller before start:** It is skipped because the chosen substring can start later.
- **Same-length comparison:** The greedy proof relies on every mapping producing exactly one digit, which the length-ten change array guarantees.
- **Input preservation:** `num` is immutable; the result is built through a separate list.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the number of digits.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
