# Guided Example: Smallest Subsequence of Distinct Characters

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "bcabc"}`
- **Required output:** `"abc"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `s`, return *the **lexicographically smallest* *subsequence** of* `s` *that contains all the distinct characters of* `s` *exactly once*.

The objective is to compute `"abc"` from `{"s": "bcabc"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Choose one occurrence of every distinct character

The answer must preserve source order because it is a subsequence. It must contain every distinct character exactly once, and among all such choices it must be lexicographically smallest.

Choosing a smaller character earlier is desirable, but an earlier chosen character can be removed only if another copy remains later. Otherwise the final answer would lose that distinct character.

The solution maintains the current best subsequence as a stack and uses last-occurrence positions to decide which earlier choices are safely replaceable.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "bcabc"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Record the final opportunity for each character

The dictionary is:



The comprehension processes indices from left to right. Reassigning the same key overwrites its previous value, so `last[c]` ends as the final index where `c` occurs.

When processing position `i`, the condition `last[x] > i` means character `x` will appear again later. A selected `x` may be removed now without making it impossible to include `x` eventually.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Track the current subsequence and membership

The algorithm uses:



`stk` stores selected characters in their subsequence order. `vis` contains exactly the characters currently in `stk`.

The set makes the exactly-once rule efficient. Membership lookup avoids scanning the stack for every source character.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"abc"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "bcabc"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"abc"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Remaining-count array:** Decrement a character's remaining frequency while scanning and allow a pop when that frequency stays positive. It is equivalent to comparing with the last index.
- **Recursive greedy selection:** Repeatedly choose the smallest character whose suffix still contains all remaining distinct characters. It is correct but can rescan and slice the string many times.
- **Enumerate subsequences:** Testing every subsequence is exponential and unnecessary.
- **All characters distinct and increasing:** Nothing is popped and the input is returned.
- **All characters distinct and decreasing:** No top has a later copy, so none can be popped; the input is the only valid full distinct-character subsequence.
- **Repeated one character:** The first copy is selected and all later copies are skipped, returning one character.
- **Current character already visited:** Skipping prevents duplicates without harming feasibility.
- **Larger top appears later:** It is safe to pop and reinsert from its future copy.
- **Larger top has no future copy:** It must remain even if current is smaller.
- **Multiple pops:** The loop removes the entire safely replaceable larger suffix, not only one character.
- **Last-occurrence dictionary:** Absolute positions remove the need to decrement frequency counters.
- **Lowercase constraint:** Fixed alphabet size justifies constant auxiliary-space notation.
- **Input preservation:** The immutable source is only scanned; result state is separate.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the string length and `A` the alphabet size.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
