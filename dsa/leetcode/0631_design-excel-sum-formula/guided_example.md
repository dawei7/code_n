# Guided Example: Design Excel Sum Formula

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"operations": ["Excel", "set", "sum", "set", "get"], "arguments": [[3, "C"], [1, "A", 2], [3, "C", ["A1", "A1:B2"]], [2, "B", 2], [3, "C"]]}`
- **Required output:** `[null, null, 4, null, 6]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Design the basic function of **Excel** and implement the function of the sum formula.

The objective is to compute `[null, null, 4, null, 6]` from `{"operations": ["Excel", "set", "sum", "set", "get"], "arguments": [[3, "C"], [1, "A", 2], [3, "C", ["A1", "A1:B2"]], [2, "B", 2], [3, "C"]]}` while avoiding redundant calculations and unnecessary overhead.

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

**Store both current values and dependency information.** A formula cell cannot be treated as a one-time sum. If one of its sources changes later, the formula cell and anything depending on it must change too. The exact class maintains three synchronized structures:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"operations": ["Excel", "set", "sum", "set", "get"], "arguments": [[3, "C"], [1, "A", 2], [3, "C", ["A1", "A1:B2"]], [2, "B", 2], [3, "C"]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

- `values` is the rectangular matrix of current integer values;
- `formulas[target]` is a `Counter` mapping every direct source cell to how many times it appears in the target's formula;
- `dependents[source]` is the reverse mapping from a source to formula targets that use it, again with multiplicity.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

The forward formula answers “what does this target read?” The reverse graph answers “which targets must change when this source changes?” Keeping both directions makes overwriting formulas and propagating updates efficient.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[null, null, 4, null, 6]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"operations": ["Excel", "set", "sum", "set", "get"], "arguments": [[3, "C"], [1, "A", 2], [3, "C", ["A1", "A1:B2"]], [2, "B", 2], [3, "C"]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[null, null, 4, null, 6]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Topological recomputation:** After a change, collect affected cells and evaluate each once in dependency order. This gives a firmer $O(N+F)$ affected-subgraph bound and avoids repeated work from converging paths.
- **Lazy formula evaluation:** Store formulas but calculate on `get`. It simplifies updates but can repeatedly traverse large dependency graphs and needs cycle protection.
- **Scan all formulas after every change:** The editorial approach can discover dependents without reverse edges, but repeated whole-sheet scans are expensive.
- **Overlapping ranges:** Counter multiplicities ensure a cell included twice contributes twice.
- **Formula overwritten by `set`:** Old reverse edges are removed, so former sources stop affecting the target.
- **Formula overwritten by another `sum`:** The old graph links are removed before the new formula is registered.
- **Reference to a zero cell:** It contributes zero initially but remains connected, so a later change propagates.
- **Difference zero:** Downstream values do not change, and propagation stops immediately.
- **Diamond-shaped dependencies:** A downstream cell receives deltas along both paths, which is numerically correct but may cause repeated traversal.
- **Circular formulas:** The contract forbids them. Without that guarantee, recursive propagation could loop forever and values would be ill-defined.
- **Inclusive rectangles:** Both endpoint rows and columns are included by the `+ 1` loop bounds.
- **Multi-digit rows:** `reference[1:]` correctly parses rows such as `A26` rather than assuming one digit.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N + F)$. Let $N$ be the number of sheet cells, $F$ the number of stored distinct direct dependency entries, $E$ the number of cell occurrences expanded by one new formula, and $D$ the maximum dependency depth.
- **Auxiliary Space Complexity:** $O(N + F)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
