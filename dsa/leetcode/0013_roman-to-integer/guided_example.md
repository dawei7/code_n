# Guided Example: Roman to Integer

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "III"}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.

The objective is to compute `3` from `{"s": "III"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A symbol's next neighbor determines whether it adds or subtracts

Most Roman symbols are written from larger value to smaller value and are added. The six subtractive forms are exactly the places where a smaller symbol occurs immediately before a larger one:



Therefore a symbol at index `i` contributes

$$
\begin{cases}
-\text{value}(s[i]), & \text{if value}(s[i]) < \text{value}(s[i+1]), \\
+\text{value}(s[i]), & \text{otherwise}.
\end{cases}
$$

The final symbol has no larger symbol after it and is always added. This local sign rule converts a subtractive pair such as `IV` into $-1+5=4$ while treating an additive sequence such as `VIII` as $5+1+1+1=8$.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "III"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Map the seven letters to their numerical values

The dictionary `d` contains the fixed symbol table. Dictionary access makes each comparison and contribution constant time. The input is guaranteed to be a valid Roman numeral, so every character is a dictionary key and every increase corresponds to one of the permitted subtractive relationships. The method does not need to validate illegal strings such as `IC`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Use adjacent pairs without manual indices

`pairwise(s)` yields



For each `(a, b)`, the generator expression chooses `-1` when `d[a] < d[b]` and `1` otherwise, then multiplies by `d[a]`:



Every character except the last appears once as `a`, so every one of those symbols receives exactly one signed contribution. The separate `+ d[s[-1]]` supplies the final always-positive symbol.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "III"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Consume subtractive pairs explicitly:** Scan with an index; when the current value is smaller than the next, add their difference and advance two positions. It is equally linear but needs variable pointer increments and an end check.
- **Scan right to left:** Start with the last value and subtract a current symbol when it is smaller than the symbol to its right. This expresses the same sign rule without `pairwise`.
- **Thirteen-token lookup:** Recognize the six two-character forms before falling back to one-character symbols. This is clear but uses substring/token checks rather than the simple value comparison.
- **One symbol:** The adjacent generator is empty and the last symbol is returned.
- **Pure additive notation:** No adjacent increase exists, so every symbol is added.
- **Several subtractive pairs:** Each smaller-left symbol is independently negated, as in `MCMXCIV`.
- **Repeated symbols:** Equal neighbors are added because the comparison is strict.
- **Invalid notation:** The algorithm may assign a numerical value to malformed input, but validation is outside the guaranteed contract.
- **Non-empty guarantee:** `d[s[-1]]` depends on at least one character, which the Reference guarantees.
- **Immediate-neighbor rule:** A symbol is never subtracted merely because some larger symbol appears later; only a larger next symbol changes its sign in valid canonical notation.
- **Strict comparison:** Equal repeated symbols remain additive, which is required for values such as `III`, `XXX`, and `CCC`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the Roman numeral length.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
