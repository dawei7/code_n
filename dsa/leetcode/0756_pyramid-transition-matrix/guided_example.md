# Guided Example: Pyramid Transition Matrix

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"bottom": "BCD", "allowed": ["BCC", "CDE", "CEA", "FFF"]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are stacking blocks to form a pyramid. Each block has a color, which is represented by a single letter. Each row of blocks contains **one less block** than the row beneath it and is centered on top.

The objective is to compute `true` from `{"bottom": "BCD", "allowed": ["BCC", "CDE", "CEA", "FFF"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Each adjacent pair determines choices for the row above

For an allowed triple `ABC`, bottom pair `AB` may support top block `C`. The solution groups all triples by their ordered first two characters:

`d[(a, b)].append(c)`.

Order matters. Choices for `AB` do not automatically apply to `BA`.

Given a current row `s`, every adjacent pair must choose one permitted top character. Those choices, in order, form the entire next row, which has length one less.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"bottom": "BCD", "allowed": ["BCC", "CDE", "CEA", "FFF"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Reject a row as soon as one pair has no option

DFS uses `pairwise(s)` to inspect every neighboring pair. For each pair it retrieves its list of possible top characters.

If any list is empty, no next row can be built from `s`, regardless of choices for other pairs. The method returns false immediately.

Otherwise the option lists are collected in `t`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Enumerate complete next rows with a Cartesian product

`product(*t)` chooses one character from each adjacent pair’s option list. Each resulting tuple `nxt` is one complete candidate row above `s`.

Joining the tuple produces the string passed to recursive DFS. `any(...)` short-circuits as soon as one candidate row can reach the top; remaining combinations do not need exploration.

It is important to choose the whole next row consistently. Adjacent triangles share bottom blocks, but their top blocks simply become neighboring blocks in the next row; the Cartesian product represents every allowed combination.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"bottom": "BCD", "allowed": ["BCC", "CDE", "CEA", "FFF"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Backtrack one top position at a time:** Build a candidate row incrementally and recurse when complete. This avoids materializing product tuples and allows additional pruning.
- **Bitmask transitions:** Encode each pair’s possible top letters as six bits for faster combination checks, at the cost of less beginner-friendly code.
- **Greedily choose the first allowed top:** A locally legal choice may block the next level while another choice succeeds. All alternatives may need exploration.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(a^{n(n-1)/2})$. Let `n` be the bottom length and let `a` be the maximum number of top choices for one ordered pair. A complete pyramid has `n(n - 1)/2` non-bottom positions. A coarse worst-case search bound is therefore `O(a^(n(n - 1)/2))` combinations.
- **Auxiliary Space Complexity:** $O(a^n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
