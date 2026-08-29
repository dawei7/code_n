# Guided Example: Score of Parentheses

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "()"}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a balanced parentheses string `s`, return *the **score** of the string*.

The objective is to compute `1` from `{"s": "()"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Every score ultimately comes from a primitive `()`

The rule `AB -> score(A)+score(B)` means concatenated components contribute independently.

The rule `(A) -> 2*score(A)` means every surrounding pair of parentheses doubles the score inside.

At the bottom of every balanced structure are adjacent primitive pairs `()`, each with base score one. A primitive pair surrounded by `d` outer pairs contributes `2^d` to the total.

The solution scans once, tracks nesting depth, and adds this contribution whenever it recognizes an adjacent `()`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "()"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Depth meaning

Variable `d` is the number of opening parentheses currently active after processing the current scan position's structural update:

- on `(`, increment `d`;
- on `)`, decrement `d` because that pair is closing.

For a closing parenthesis, the decremented value is the number of outer pairs surrounding the pair that just closed.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Recognize only primitive pairs

When current character is `)` and previous character `s[i-1]` is `(`, the two form an adjacent primitive `()`.

The code adds:

`1 << d`,

which equals `2^d`.

If the previous character is also `)`, the closing parenthesis ends a larger composite expression, not a new base primitive. Its score has already been accounted for through the primitives inside, so nothing is added.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "()"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Stack of partial scores:** Push a frame for each opening parenthesis and combine on closing. It mirrors the grammar but uses `O(n)` worst-case space.
- **Divide and conquer:** Find top-level balanced components recursively. It is conceptually direct but can rescan ranges or use recursion.
- **One primitive `()`:** Depth after closing is zero, so score is one.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n = len(s)`. The loop examines each character once and performs constant work, so time is `O(n)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
