# Guided Example: Elimination Game

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 9}`
- **Required output:** `6`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You have a list `arr` of all integers in the range `[1, n]` sorted in a strictly increasing order. Apply the following algorithm on `arr`:

The objective is to compute `6` from `{"n": 9}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Represent the surviving list as an arithmetic progression

Materializing the list is impossible for the largest input, where `n` can be $10^9$. Fortunately, after every elimination pass, the survivors remain evenly spaced and sorted. They can be described using only:

- `a1`: the first surviving value;
- `an`: the last surviving value;
- `step`: the difference between adjacent survivors;
- `cnt`: the number of survivors.

Initially the list is `1, 2, 3, ..., n`, so `a1 = 1`, `an = n`, `step = 1`, and `cnt = n`.

After one pass, every other element survives. The distance between neighboring survivors doubles, and the number of survivors becomes its integer half. The exact identities of the new endpoints depend only on the direction and whether the old count is odd or even.

This compressed representation is the central idea: update four integers instead of deleting up to a billion list elements.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 9}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: What one left-to-right pass does

Index the current progression’s positions from one. A left-to-right pass deletes positions `1, 3, 5, ...` and keeps positions `2, 4, 6, ...`.

The first position is always deleted, so the new first survivor is the old second value. Since adjacent values differ by `step`, the exact code always executes



on a left-to-right pass.

The fate of the old last value depends on `cnt`:

- if `cnt` is even, the final position is even and survives, so `an` stays unchanged;
- if `cnt` is odd, the final position is odd and is deleted, so the new last value is one step smaller: `an -= step`.

This is why the even-direction branch contains an unconditional update of `a1` and a conditional update of `an` when `cnt % 2` is true.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Index the current progression’s positions from one.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: What one right-to-left pass does

From the right, the rightmost position is deleted first, so `an` always moves one step inward:



Again, parity decides what happens at the opposite endpoint.

- If `cnt` is even, deletions counted from the right remove the positions that are even when numbered from the left; the original first position survives, so `a1` does not move.
- If `cnt` is odd, the alternating deletion pattern reaches the original first position, so it is removed and `a1 += step`.

The odd-direction branch of the code therefore updates `an` unconditionally and `a1` only for an odd count.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `6` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 9}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `6` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Explicit list simulation:** Build `[1, ..., n]:** - **Explicit list simulation:** Build `[1, ..., n]`, keep every other value, reverse direction, and repeat. It is intuitive but requires $O(n)$ memory and substantial element-copying work, which is infeasible for $n = 10^9$.
- **- **Recursive recurrence:** The game has a compact:** - **Recursive recurrence:** The game has a compact mathematical recurrence relating the left-to-right result for `n` to a reflected result on `n // 2`. This yields $O(\log n)$ time and $O(\log n)$ call-stack space. The iterative endpoint model avoids recursion and is easier to trace operationally.
- **- **Head-only iterative model:** Track the first v:** - **Head-only iterative model:** Track the first value, gap, remaining count, and direction. The head moves on every left pass and on a right pass only when the count is odd. This is equivalent and slightly smaller; the exact solution additionally maintains the tail.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log n)$. Each pass replaces `cnt` with `cnt // 2`. Starting from $n$, the number of passes before one survivor remains is $O(\log n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
