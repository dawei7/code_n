# Guided Example: Minimum Deletions for At Most K Distinct Characters

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "abc", "k": 2}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s` consisting of lowercase English letters, and an integer `k`.

The objective is to compute `1` from `{"s": "abc", "k": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A character stops being distinct only when all copies are deleted

Suppose character `c` appears `f_c` times. Deleting fewer than `f_c` copies leaves at least one `c` in the string, so `c` still contributes one distinct character.

Therefore, partial deletion of a character class cannot help satisfy the distinct-count limit. In an optimal solution, every character is either:

- kept with all its occurrences;
- removed by deleting all its occurrences at cost `f_c`.

The order of characters in the string is irrelevant. Only the frequency of each distinct letter matters.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "abc", "k": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: How many classes must disappear

Let `d` be the current number of distinct letters.

If `d <= k`, the string already meets the requirement and the answer is zero.

If `d > k`, at least `d-k` character classes must be removed completely. Removing more classes would add positive deletion cost without being required, so an optimum removes exactly `d-k` classes.

The problem becomes:

choose `d-k` frequencies with minimum possible sum.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Delete the least frequent classes

Sort the frequencies in non-decreasing order:

`f_1 <= f_2 <= ... <= f_d`.

The minimum sum of any `d-k` frequencies is the sum of the first `d-k`. Equivalently, keep the `k` most frequent character classes and delete everything else.

An exchange argument proves this. If a proposed solution deletes a class of frequency `b` but keeps another class of smaller frequency `a < b`, swap their roles. The resulting string still has the same number of distinct characters, while deletion cost decreases from `b` to `a`. Repeating removes every such inversion and leaves exactly the least frequent classes deleted.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "abc", "k": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Delete arbitrary occurrences greedily:** Removing some copies of a still-present letter cannot lower the distinct count and wastes deletions.
- **Keep the k most frequent classes:** This is exactly equivalent and may be implemented by sorting descending and subtracting their sum from `n`.
- **Use a 26-slot count array:** It avoids hashing and retains the same linear/fixed-space bounds.
- **Try every subset of letters:** At most 26 makes it theoretically bounded, but frequency sorting gives the optimum directly.
- **Already at most k distinct:** The slice is empty and the answer is zero.
- **k larger than the string length:** Distinct count is at most string length, so no deletion is needed.
- **All characters identical:** One class is within every legal `k>=1`, so answer zero.
- **Every character unique:** All frequencies are one; delete exactly `d-k` arbitrary characters.
- **Tied frequencies:** Any tied classes can be removed; deletion total is identical.
- **k equals one:** Keep only a most frequent letter and delete all other classes.
- **k equals zero:** Not allowed; the compact negative-zero slice would need special handling in a generalized problem.
- **Lowercase guarantee:** It is what makes the Counter's maximum size a constant 26.
- **Partial class deletion:** Never useful for the distinct-count objective, which is the key reduction.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n = len(s)` and `U` be the number of distinct letters. Building the Counter takes `O(n)` expected time. Sorting its `U` frequencies costs `O(U log U)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
