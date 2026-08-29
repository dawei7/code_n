# Guided Example: Minimum Insertions to Balance a Parentheses String

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "(()))"}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a parentheses string `s` containing only the characters `'('` and `')'`. A parentheses string is **balanced** if:

The objective is to compute `1` from `{"s": "(()))"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Treat two right parentheses as one closing unit

In this problem, one opening parenthesis must be matched by the consecutive pair `))`. It is helpful to regard that pair as a single closing token that consumes one earlier unmatched `(`.

The source scans left to right with index `i`. Variable `x` counts opening parentheses already seen but not yet matched by a complete closing pair. Variable `ans` counts insertions that have become unavoidable.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "(()))"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Record unmatched opening parentheses

When `s[i]` is `(`, the code increments `x`. No insertion is needed immediately because a future `))` pair may close it.

Keeping only a count is sufficient. Opening parentheses are interchangeable for feasibility, and the required nesting order is preserved by matching a later closing unit to an available earlier opener.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Complete every encountered right parenthesis into a pair

When the current character is `)`, the algorithm asks whether the next original character is also `)`.

If so, the two characters already form a complete closing unit. The code increments `i` inside the branch so that the second right parenthesis is consumed together with the first. The common increment at the end of the loop then moves past the pair.

If the next character is absent or is `(`, the current `)` cannot form a consecutive pair with a later original right parenthesis without crossing an intervening character. The cheapest repair is to insert one `)` immediately beside it. The source adds one to `ans` and treats the current character plus insertion as a complete closing unit.

This insertion is forced: every legal balanced result must give that lone right parenthesis a consecutive partner somewhere, and one insertion is the minimum way to do so.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "(()))"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Build the repaired string:** It can visualize insertions but requires $O(N)$ additional storage that the count-only scan avoids.
- **Stack of openings:** A stack is unnecessary because only the number of unmatched openers matters.
- **Need-count formulation:** Track how many right parentheses are currently required and repair odd requirements before an opener. It is an equivalent constant-space greedy approach.
- **Already balanced:** Every closing pair consumes an opener and the answer remains zero.
- **Single opening parenthesis:** Two right parentheses must be inserted.
- **Single right parenthesis:** One right partner and one preceding opener must be inserted, for two total.
- **Lone right before opening:** It receives an inserted adjacent right parenthesis before scanning the new opener.
- **Closing pair with no opener:** Exactly one opening parenthesis must be inserted before it.
- **Many unmatched openings:** Each independently requires a `))` pair at the end.
- **Consecutive right run:** The scan consumes it in pairs; an odd final right parenthesis needs one inserted partner.
- **Order requirement:** An opener inserted after a closing unit would not match it, so the algorithm inserts before when `x == 0`.
- **Bit shift:** `x << 1` means exactly `2 * x` and is not a change to the string.
- **Input alphabet:** Only the two parenthesis characters occur, so the two top-level branches are exhaustive.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be string length. Index `i` moves forward through the input and never retreats. A `))` pair may advance it twice in one iteration, but every original character is consumed once. Time is $O(N)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
