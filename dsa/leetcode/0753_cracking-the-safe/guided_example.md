# Guided Example: Cracking the Safe

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 1, "k": 2}`
- **Required output:** `"10"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is a safe protected by a password. The password is a sequence of `n` digits where each digit can be in the range `[0, k - 1]`.

The objective is to compute `"10"` from `{"n": 1, "k": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The output must contain every possible password as a window

There are `k^n` possible passwords of length `n`. A typed string unlocks the safe for every possible password only if each of those strings occurs somewhere as a consecutive length-`n` window.

Writing every password separately would use `n * k^n` characters. The goal is to overlap passwords as much as possible. If one password’s final `n - 1` digits equal another password’s first `n - 1` digits, the second needs only one new typed digit.

This is exactly the structure of a de Bruijn sequence.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 1, "k": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Build an implicit directed graph

Treat every length-`n - 1` digit sequence as a graph node. A length-`n` password is an edge:

- Its first `n - 1` digits identify the source node.
- Its final `n - 1` digits identify the destination node.
- Its final digit is the edge label appended while moving.

For each node, appending any digit from zero through `k - 1` creates one outgoing edge. Every password corresponds to exactly one such edge.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Encode nodes and edges as integers

The solution represents the current `n - 1` digits as integer `u`. Appending digit `x` creates

`e = u * 10 + x`.

Because `k <= 10`, every symbol is one decimal digit. The edge integer uniquely represents the full length-`n` sequence, including conceptual leading zeroes within the fixed-width context.

The next node is

`v = e % 10^(n - 1)`,

which discards the oldest digit and retains the newest `n - 1` digits. For `n = 1`, the modulus is one and the only node is zero.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"10"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 1, "k": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"10"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Concatenate every password:** It is easy but produces `n * k^n` characters rather than the minimum.
- **Backtracking over output strings:** Searching arrangements directly creates enormous repeated work. Eulerian structure gives a constructive solution.
- **Append labels before recursion:** This loses Hierholzer’s cycle-splicing guarantee. Edge labels belong in postorder.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(k^n)$. There are `E = k^n` edges. The visited set and output contain `O(E)` items, and recursion can also be linear in `E`, so space is `O(k^n)`.
- **Auxiliary Space Complexity:** $O(k^n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
