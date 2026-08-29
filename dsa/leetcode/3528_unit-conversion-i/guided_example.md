# Guided Example: Unit Conversion I

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"conversions": [[0, 1, 2], [1, 2, 3]]}`
- **Required output:** `[1, 2, 6]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are `n` types of units indexed from `0` to $n - 1$. You are given a 2D integer array `conversions` of length $n - 1$, where $\text{conversions}[i] = [\text{sourceUnit}_{i}, \text{targetUnit}_{i}, \text{conversionFactor}_{i}]$. This indicates that a single unit of type $\text{sourceUnit}_{i}$ is equivalent to $\text{conversionFactor}_{i}$ units of type $\text{targetUnit}_{i}$.

The objective is to compute `[1, 2, 6]` from `{"conversions": [[0, 1, 2], [1, 2, 3]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Model each conversion as a directed weighted edge

A conversion `[source, target, factor]` says:

one `source` unit equals `factor` `target` units.

Represent this as a directed edge:

`source -> target` with weight `factor`.

The direction matters. The contract guarantees that every unit is reachable from unit zero through a unique combination of conversions without reversing any edge. With `n` units and exactly `n-1` conversions, this reachable directed structure behaves as an arborescence rooted at zero: every non-root unit has one unique directed path from zero.

The protected source stores only the given direction:

`g[source].append((target, factor))`.

It does not add a reverse edge because reverse conversions are neither needed nor authorized by the stated path guarantee.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"conversions": [[0, 1, 2], [1, 2, 3]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: A path product is the conversion answer

Suppose the unique path from unit zero to unit `v` is:

`0 -> a -> b -> ... -> v`

with edge factors `w_1, w_2, ..., w_t`.

One unit of type zero becomes `w_1` units of type `a`. Each of those becomes `w_2` units of type `b`, so the amount is multiplied again. Continuing along the path gives:

`w_1 * w_2 * ... * w_t`

units of type `v`.

Therefore, if the conversion value at a parent `s` is `mul` and edge `s -> t` has factor `w`, then:

`answer[t] = mul * w`.

This local propagation is all the DFS needs.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why unit zero has value one

One unit of type zero is already exactly one unit of type zero. The empty path has an empty product, whose multiplicative identity is one.

The source begins:

`dfs(0, 1)`.

Inside the call, it assigns `ans[0] = 1`. Every descendant call receives the parent path product extended by one edge.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 2, 6]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"conversions": [[0, 1, 2], [1, 2, 3]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 2, 6]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Iterative DFS with a stack:** Store `(unit, path_product)` pairs and process the same recurrence without recursion depth limits. This is the direct robust repair while preserving `O(n)` time and space.
- **Breadth-first traversal:** A queue works equally well because each node has one unique root path; traversal order does not affect its path product.
- **Topological dynamic programming:** It can propagate values in a more general DAG, but the rooted unique-path guarantee makes a tree traversal simpler.
- **Add reverse conversion edges:** Reversing would require modular division or rational values and violates the source direction contract. Only forward edges belong in `g`.
- **Recompute a path per unit:** Following ancestors independently could repeat shared prefixes and become quadratic. One traversal shares the propagation work.
- **Root unit:** Its answer is one, even when it has many outgoing conversions.
- **Conversion factor one:** The child inherits the parent's modular amount unchanged.
- **Factor divisible by MOD:** That child and every descendant path product become zero modulo `MOD`.
- **Deep chain:** Algorithmically linear, but the exact recursive source can fail with `RecursionError`; an explicit stack is required for full constraint safety.
- **Wide star rooted at zero:** Recursion depth is only two, and each child receives its direct factor.
- **Input order:** Adjacency order changes DFS visit order but not any unique path product.
- **No visited set:** Safe only because the graph guarantee prevents multiple directed paths and reachable cycles.
- **Unreachable unit in invalid input:** Its answer would remain the initialization zero, but the contract excludes this situation.
- **Large raw product:** Reducing at every edge is mathematically exact for the requested residues.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the number of units. Building `g` creates one adjacency-list entry for each of `n-1` conversions, taking `O(n)` time and `O(n)` space.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
