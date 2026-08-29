# Guided Example: Maximum Manhattan Distance After K Changes

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "NWSE", "k": 1}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s` consisting of the characters `'N'`, `'S'`, `'E'`, and `'W'`, where $s[i]$ indicates movements in an infinite grid:

The objective is to compute `3` from `{"s": "NWSE", "k": 1}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

**Manhattan distance is the best of four signed directions.** At position $(x,y)$,

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "NWSE", "k": 1}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

$$
\lvert x\rvert+\lvert y\rvert
=
\max(x+y,x-y,-x+y,-x-y).
$$

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

Each signed expression corresponds to moving outward toward one of four diagonal quadrants. For example, in one expression two movement letters contribute $+1$ and the opposite two contribute $-1$.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "NWSE", "k": 1}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Track coordinates and use the closed formula:** For each prefix, `min(prefix_length, original_distance + 2k)` also yields the optimum. The four-quadrant scan provides a constructive signed interpretation.
- **Try every changed character set:** There are exponentially many choices. All unfavorable changes have identical signed benefit within a fixed quadrant.
- **Change favorable moves:** This cannot increase that quadrant's score and wastes budget.
- **\(k=0\):** Every unfavorable move subtracts one, so the four scans reduce to the original prefix Manhattan distances.
- **\(k\ge\) prefix length:** Every move in that prefix can point outward, and the score reaches the prefix length, the largest possible distance after that many unit moves.
- **Maximum at an early time:** `ans` is updated on every character, so later movement back toward the origin cannot erase the recorded maximum.
- **Same movement string, different quadrants:** Each call is an alternative strategy; their change counters are intentionally independent.
- **One-character string:** A single move already has distance one, and every helper containing its direction records it.
- **At most \(k\):** Unused changes are harmless when no unfavorable move remains.
- **Infinite grid:** No boundary checks are required; only displacement matters.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(4n)$. Let $n=\lvert\texttt{s}\rvert$. Each of four helper calls scans all $n$ characters with constant work, so total time is $O(4n)=O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
