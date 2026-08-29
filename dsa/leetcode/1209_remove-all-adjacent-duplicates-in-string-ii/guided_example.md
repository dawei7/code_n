# Guided Example: Remove All Adjacent Duplicates in String II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "abcd", "k": 2}`
- **Required output:** `"abcd"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s` and an integer `k`, a `k` **duplicate removal** consists of choosing `k` adjacent and equal letters from `s` and removing them, causing the left and the right side of the deleted substring to concatenate together.

The objective is to compute `"abcd"` from `{"s": "abcd", "k": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Process one maximal original run at a time

Pointers `i` and `j` find the maximal run beginning at `i`. When the inner loop ends, `cnt = j - i` is its length.

`cnt %= k` removes every complete group of `k` identical letters inside that run. Only the remainder can affect later characters. If the remainder is zero, that original run vanishes entirely.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "abcd", "k": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Merge with the reduced prefix

If the stack is nonempty and its final character equals `s[i]`, all original material between that stored run and the current run has already vanished. They are now adjacent and must combine.

The code replaces the top count by `(old + cnt) % k`. Modulo removes any newly formed groups of `k`. If the new count is zero, it pops the run completely. That pop may expose an earlier character, which can merge with a future run processed later.

If the top character differs and `cnt` is nonzero, the current remainder becomes a new stack run. A zero remainder adds nothing.

For `"deeedbbcccbdaa"` with `k = 3`, the `eee` and `ccc` runs reduce to zero. Their disappearance lets surrounding runs eventually combine: the three `b` characters vanish, then separated `d` portions merge to three and vanish, leaving `aa`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why one pass captures repeated removals

After each original run is processed, the stack represents exactly the fully reduced form of the input prefix. It contains no count reaching `k` and no adjacent equal run entries.

For the next run, internal groups are removed by modulo. If its character differs from the stack top, appending preserves reduction. If it matches, combining is the only new interaction created at the boundary; modulo and a possible pop fully resolve it. This maintains the invariant by induction.

Because the final reduced string is unique, the stack’s deterministic left-to-right reductions produce the required result regardless of another possible removal order.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"abcd"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "abcd", "k": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"abcd"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Character-by-character run stack:** Push or increment one character at a time and pop at count `k`. It has the same $O(n)$ bounds and may be simpler to recognize.
- **Repeated immutable-string deletion:** Rescanning and slicing after every removal can take quadratic time.
- **No removable group:** Every residual run remains and reconstruction returns the original string.
- **Whole run length is a multiple of `k`:** Its remainder is zero and it contributes nothing.
- **Run longer than `k`:** Modulo correctly removes several complete groups at once.
- **Cascade across deleted text:** Matching the current character against the stack top detects newly adjacent equal runs.
- **Combined count exactly `k`:** Modulo makes it zero and the stack entry is popped.
- **`k = 2`:** Counts are only one after reduction, and matching adjacent runs cancel in pairs.
- **Unique final answer:** The invariant computes the canonical reduced prefix, so no removal-order branching is needed.
- **Output may be empty:** An empty stack reconstructs to `""` through `join`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the length of `s`. The run pointers advance only forward, so all original characters are examined $O(n)$ times in total. Each run causes constant stack work, and every stack entry is pushed and popped at most once. Reconstruction writes exactly the output characters, at most $n$. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
