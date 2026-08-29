# Guided Example: Reorganize String

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "aab"}`
- **Required output:** `"aba"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `s`, rearrange the characters of `s` so that any two adjacent characters are not the same.

The objective is to compute `"aba"` from `{"s": "aab"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The most frequent character determines feasibility

Let the string length be `n` and let one character occur `mx` times. To separate all copies, at least `mx - 1` other characters must fit between them.

The string contains `n - mx` other characters, so feasibility requires

`mx - 1 <= n - mx`,

equivalently

`mx <= (n + 1) // 2`.

If this condition fails, no rearrangement can avoid adjacent equal copies and the solution returns the empty string.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "aab"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Reserve alternating positions

When a rearrangement is possible, the even indices `0, 2, 4, ...` form the largest set of mutually nonadjacent slots. There are exactly `ceil(n / 2)` of them, enough for the most frequent character.

The solution allocates an answer list of length `n` and fills characters in descending frequency order using `Counter.most_common()`.

Index `i` begins at zero and advances by two after every placement. Once it passes the final index, it wraps to one and continues through odd positions `1, 3, 5, ...`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the most frequent character is separated

Because it is processed first, all of its copies occupy even positions. Consecutive even indices differ by two, so another slot lies between every pair.

The feasibility check guarantees it does not need more even positions than exist.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"aba"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "aab"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"aba"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Max-heap with a held-back previous character:** Repeatedly choose the most frequent character different from the last. It is more general and runs in `O(n log A)` for alphabet size `A`.
- **Random shuffling:** It offers no correctness or termination guarantee.
- **Skip the feasibility check:** Placement could run out of separating slots for a dominant character.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the string length. Counting and filling take `O(n)` time. Sorting distinct character counts through `most_common` involves at most 26 lowercase letters, so it is constant with respect to `n`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
