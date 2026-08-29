# Guided Example: Positions of Large Groups

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "abbxxxxzzy"}`
- **Required output:** `[[3, 6]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

In a string `s` of lowercase letters, these letters form consecutive groups of the same character.

The objective is to compute `[[3, 6]]` from `{"s": "abbxxxxzzy"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Process one maximal group at a time

A group is a maximal run of equal adjacent characters. The answer needs the inclusive start and end indices of every run whose length is at least three.

The two-pointer solution maintains:

- `i` as the first index of the current group;
- `j` as the first index after that group.

Once `j` is known, the group occupies the half-open interval `[i,j)`. Its length is `j-i`, and its inclusive final index is `j-1`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "abbxxxxzzy"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Find the right boundary

At the start of each outer-loop iteration, `i < n` and therefore `s[i]` is the character defining the new group. The code sets `j = i` and advances while

`j < n and s[j] == s[i]`.

Every position passed by `j` contains the group character. The loop stops for exactly one of two reasons:

- `j == n`, so the group reaches the end of the string;
- `s[j] != s[i]`, so index `j` begins the next group.

Therefore, all indices from `i` through `j-1` belong to the group, and the run cannot be extended farther right. It is also maximal on the left because `i` was set to the end boundary of the preceding group, or zero for the first group.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Record only large groups

The test `j - i >= 3` implements the definition of large. When it succeeds, the code appends `[i, j - 1]`.

Subtracting one is necessary because `j` is exclusive while the output interval's end is inclusive. For a run beginning at 3 and stopping before index 7, the length is `7-3=4` and the reported interval is `[3,6]`.

Groups of length one or two are fully scanned but not appended.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[3, 6]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "abbxxxxzzy"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[3, 6]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Run-length encoding:** Build character/count/start triples, then filter counts at least three. It is correct but stores information for every group when only large intervals are needed.
- **Track a start and detect boundary events in one loop:** This is equivalent and can use a sentinel at the end. The exact two-pointer form makes the exclusive boundary explicit.
- **Check every length-three window:** It can detect that a large run exists but needs additional logic to merge overlapping windows and find maximal endpoints.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n = len(s)`. Pointer `j` advances across every character once in total, while `i` jumps from one group boundary to the next. All work besides pointer movement and output appends is constant. The time complexity is `O(n)`.
- **Auxiliary Space Complexity:** $O(g)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
