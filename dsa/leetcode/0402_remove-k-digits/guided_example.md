# Guided Example: Remove K Digits

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"num": "1432219", "k": 3}`
- **Required output:** `"1219"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given string num representing a non-negative integer `num`, and an integer `k`, return *the smallest possible integer after removing* `k` *digits from* `num`.

The objective is to compute `"1219"` from `{"num": "1432219", "k": 3}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Minimize the earliest possible digit

Removing exactly `k` digits preserves the relative order of all remaining digits. Every candidate therefore has the same raw length `len(num) - k` before leading-zero normalization. Among equal-length decimal strings, the first position where they differ determines which number is smaller.

This gives the greedy priority: improve a digit as far to the left as possible, even if that means sacrificing a larger digit immediately before it.

When a new digit `c` is smaller than the last kept digit, retaining that larger digit would place it earlier in the final number. If one deletion remains, removing the larger previous digit and allowing `c` to move left creates a smaller result than keeping the larger digit and deleting something later.

The exact solution implements this rule with a monotonically non-decreasing stack.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"num": "1432219", "k": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: What the stack represents

`stk` contains the digits provisionally kept from the processed prefix. Before appending a new digit, the method repeatedly checks:



All three conditions are necessary:

- `k` must be positive because no more than the requested number of deletions is allowed;
- the stack must be nonempty because there must be a previous digit to remove;
- `stk[-1] > c` means replacing that earlier larger digit with the current smaller digit improves the number at the first affected position.

Each successful iteration pops one kept digit and decrements `k`. Repeating rather than checking once is important: one small incoming digit may be better than several preceding digits.

After no further beneficial deletion is possible, the method appends `c`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `stk` contains the digits provisionally kept from the proces... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why equal digits are not popped

The condition uses strict `>` rather than `>=`. Removing an equal previous digit does not improve the current prefix. Keeping the earlier equal digit preserves more future deletion flexibility, while either choice begins with the same digit.

For example, with `112` and one deletion, popping the first `1` when the second `1` arrives provides no advantage. The later decision should remove the final `2`, yielding `11`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"1219"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"num": "1432219", "k": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"1219"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Enumerate deletion combinations:** There are $:** - **Enumerate deletion combinations:** There are $\binom{n}{k}$ choices, which is exponential in the worst case. Greedy monotonicity avoids exploring them.
- **- **Repeatedly remove the first descent from a str:** - **Repeatedly remove the first descent from a string:** Applying the same rule directly is correct but repeated string deletion and rescanning can cost $O(kn)$ time. The stack performs all deletions in one pass.
- **- **Non-decreasing input:** No stack pop occurs. T:** - **Non-decreasing input:** No stack pop occurs. The prefix slice removes the largest rightmost digits, which is optimal.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the length of `num`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
