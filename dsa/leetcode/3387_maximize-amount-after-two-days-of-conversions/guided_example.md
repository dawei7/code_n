# Guided Example: Maximize Amount After Two Days of Conversions

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"initialCurrency": "EUR", "pairs1": [["EUR", "USD"], ["USD", "JPY"]], "rates1": [2.0, 3.0], "pairs2": [["JPY", "USD"], ["USD", "CHF"], ["CHF", "EUR"]], "rates2": [4.0, 5.0, 6.0]}`
- **Required output:** `720.0`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `initialCurrency`, and you start with `1.0` of `initialCurrency`.

The objective is to compute `720.0` from `{"initialCurrency": "EUR", "pairs1": [["EUR", "USD"], ["USD", "JPY"]], "rates1": [2.0, 3.0], "pairs2": [["JPY", "USD"], ["USD", "CHF"], ["CHF", "EUR"]], "rates2": [4.0, 5.0, 6.0]}` while avoiding redundant calculations and unnecessary overhead.

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

**Represent each day's rates as a reciprocal graph.** A pair `[a,b]` with rate `r` means one unit of `a` becomes `r` units of `b`. The reverse conversion is guaranteed at rate `1/r`. `build` inserts both directed weighted edges.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"initialCurrency": "EUR", "pairs1": [["EUR", "USD"], ["USD", "JPY"]], "rates1": [2.0, 3.0], "pairs2": [["JPY", "USD"], ["USD", "CHF"], ["CHF", "EUR"]], "rates2": [4.0, 5.0, 6.0]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The no-contradiction guarantee means every path between the same currencies produces the same product. There is no arbitrage cycle within one day, so one DFS value per currency is sufficient.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Measure every reachable currency relative to the initial one.** `dfs(init,1)` assigns `d[init]=1`. If current currency `a` has amount multiplier `v` and edge to `b` has rate `r`, then `d[b]=v*r`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `720.0` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"initialCurrency": "EUR", "pairs1": [["EUR", "USD"], ["USD", "JPY"]], "rates1": [2.0, 3.0], "pairs2": [["JPY", "USD"], ["USD", "CHF"], ["CHF", "EUR"]], "rates2": [4.0, 5.0, 6.0]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `720.0` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Floyd–Warshall:** It computes all-pairs rates but is unnecessary when only ratios relative to one initial currency are needed.
- **Repeated path search per overnight currency:** It duplicates graph work; one DFS assigns every consistent multiplier.
- **Logarithmic weights:** They can turn products into sums and improve numerical handling for large graphs, but constraints are tiny.
- **No conversions:** Initial-currency ratio one guarantees a valid baseline.
- **Currency reachable only on day one:** It cannot return on day two and is not considered.
- **Currency reachable only on day two:** `d1.get` contributes zero.
- **Different day graphs:** Their rates are independent, which is precisely why profitable ratios can exceed one.
- **Reciprocal edge:** It uses `1/r`, allowing reverse traversal.
- **No contradictions:** It makes DFS's first path value definitive.
- **No cycles guarantee:** It removes arbitrage concerns, though visited checks would still terminate ordinary cycles.
- **Same currency through both days:** Ratio can be above, below, or equal to one.
- **Maximum baseline:** Ratios below one never force a loss because doing nothing yields one.
- **Floating-point output:** Small rounding differences are expected within platform tolerance.
- **Dictionary as visited set:** Assignment occurs before exploring neighbors, preventing immediate reciprocal recursion.
- **Required imports:** `defaultdict`, `Dict`, and `List` must be available.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n+m)$. Let $n$ and $m$ be the numbers of day-one and day-two pairs. Building reciprocal adjacency lists and DFS traversals takes $O(n+m)$ time. Comparing day-two dictionary entries is linear in the number of reachable currencies, also $O(n+m)$.
- **Auxiliary Space Complexity:** $O(n+m)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
