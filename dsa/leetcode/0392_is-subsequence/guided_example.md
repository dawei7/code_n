# Guided Example: Is Subsequence

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "abc", "t": "ahbgdc"}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given two strings `s` and `t`, return `true`* if *`s`* is a **subsequence** of *`t`*, or *`false`* otherwise*.

The objective is to compute `true` from `{"s": "abc", "t": "ahbgdc"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: What must be preserved

A subsequence may delete any characters from `t`, but it may not reorder the characters that remain. Therefore the task is not to ask whether every character of `s` occurs somewhere in `t`; it is to ask whether those occurrences can be chosen at strictly increasing positions.

The exact solution uses two indices:

- `i` is the index of the next character of `s` that still needs a match;
- `j` is the current position being inspected in `t`.

Both begin at zero. The algorithm scans `t` only from left to right. When `t[j]` matches `s[i]`, it accepts that occurrence and increments `i`. Whether it matches or not, it increments `j`, because the current source position has now been fully considered and can never be useful again.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "abc", "t": "ahbgdc"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the pointer into `t` always moves

If `s[i] != t[j]`, the current `t` character cannot satisfy the next required character. It may be deleted from the prospective subsequence, so moving `j` forward loses nothing.

If `s[i] == t[j]`, the algorithm uses this occurrence. It advances `i` to the next requirement and advances `j` because one physical position in `t` cannot be reused for two positions of `s`. This preserves the strictly increasing order of selected indices.

Thus every iteration consumes exactly one character from `t` and consumes either zero or one character from `s`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The greedy choice: accept the earliest available match

When characters match, another strategy might skip this occurrence and hope to use a later equal character. The algorithm never does that; it greedily accepts the earliest possible occurrence.

This choice is safe because an earlier match leaves at least as much of `t` available for the remaining characters as any later match would. Suppose some valid embedding matches `s[i]` at a later index `q`, while the algorithm finds the same character at earlier index `j < q`. Replacing `q` with `j` preserves order with all already chosen positions, and every position used for later characters remains after `j`. The rest of the valid embedding still works.

Therefore accepting an early match cannot destroy a solution. It can only leave a longer suffix in which to find the remaining characters.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "abc", "t": "ahbgdc"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Recursive greedy scan:** Apply the same match-or-skip rule recursively. It is correct and linear but uses up to $O(T)$ call-stack space in Python, while the iterative form is constant space.
- **Dynamic programming:** A table over prefixes of `s` and `t` can determine subsequence membership in $O(ST)$ time and space. It solves a more general alignment problem than necessary; the greedy property makes the table wasteful here.
- **Character counts:** Frequencies can reject some impossible inputs but cannot prove subsequence order. Strings may have enough copies of every character in the wrong order.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(T)$. Let $S = \lvert s \rvert$ and $T = \lvert t \rvert$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
