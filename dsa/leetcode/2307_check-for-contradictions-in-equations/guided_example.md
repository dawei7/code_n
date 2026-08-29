# Guided Example: Check for Contradictions in Equations

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"equations": [["a", "b"], ["b", "c"], ["a", "c"]], "values": [3.0, 0.5, 1.5]}`
- **Required output:** `false`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a 2D array of strings `equations` and an array of real numbers `values`, where $\text{equations}[i] = [A_{i}, B_{i}]$ and $\text{values}[i]$ means that $A_{i} / B_{i} = \text{values}[i]$.

The objective is to compute `false` from `{"equations": [["a", "b"], ["b", "c"], ["a", "c"]], "values": [3.0, 0.5, 1.5]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Treat equations as multiplicative connections

Each equation `a / b = value` connects two variables by a known ratio. A sequence of equations can imply another ratio: if `a / b = 2` and `b / c = 3`, then `a / c = 6`. A contradiction occurs when a new equation connects variables that are already related but gives a ratio different from the one implied by the earlier equations, outside the permitted floating-point tolerance.

Weighted union-find is useful because ordinary union-find can answer whether two variables belong to the same connected component, while the added weights preserve their ratio. Every distinct variable is first mapped to an integer ID. The parent array `p` initially makes every ID its own root, and every corresponding weight starts at `1.0`.

The most important detail is the direction of the stored weight. Before path compression, the invariant is

`w[x] = p[x] / x`.

After `find(x)` finishes, `p[x]` is the component root and the same invariant becomes

`w[x] = root / x`.

Here the symbols represent the positive numerical quantities associated with the equation variables. Remembering the ratio as “parent divided by node” is essential; assuming the opposite direction would reverse the union formula.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"equations": [["a", "b"], ["b", "c"], ["a", "c"]], "values": [3.0, 0.5, 1.5]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Path compression must update the ratio as well as the parent

If `x` is not a root, `find(x)` first recursively finds and compresses its current parent. Before that recursive call, `w[x] = oldParent / x`. After the call, `w[oldParent] = root / oldParent`. Multiplying them gives

`(oldParent / x) \cdot (root / oldParent) = root / x`.

That is exactly why the code performs `w[x] *= w[p[x]]` before replacing `p[x]` with the returned root. The old parent entry must still be available for the multiplication. Once both updates are complete, `x` points directly to the root and its weight correctly represents `root / x`.

For a root, `p[x] == x` and `w[x] == 1.0`, matching `x / x = 1`. Repeated calls remain correct because a node already compressed to the root simply multiplies through a root weight of one if compression is needed again.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Join two previously separate components

Consider a new equation `a / b = v`. After calling `find` on both endpoints, let their roots be `pa` and `pb`. The weights now mean

`w[a] = pa / a` and `w[b] = pb / b`.

If `pa != pb`, the earlier equations do not yet impose any ratio between these components, so the new equation cannot contradict them. The solution attaches root `pb` beneath root `pa` by assigning `p[pb] = pa`. It must also choose `w[pb]`, whose required meaning is now `pa / pb`.

From the known weights,

`a = pa / w[a]` and `b = pb / w[b]`.

Substituting these expressions into `a / b = v` gives

`(pa / w[a]) / (pb / w[b]) = v`,

so

`pa / pb = v \cdot w[a] / w[b]`.

The assignment `w[pb] = v * w[a] / w[b]` therefore establishes exactly the required parent-to-node ratio for the newly attached root. All existing ratios inside both components remain unchanged, and the new edge makes their combined component satisfy the new equation.

The implementation always attaches `pb` under `pa`. It does not use a rank or size heuristic. That choice keeps the weight formula simple but matters when describing the strongest theoretical time bound.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `false` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"equations": [["a", "b"], ["b", "c"], ["a", "c"]], "values": [3.0, 0.5, 1.5]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `false` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Weighted graph traversal for every equation:** Store both directed ratios for each accepted equation, then run DFS or BFS to discover the implied ratio when checking a new connection. This is conceptually direct but may revisit much of a component for many equations, leading to roughly `O(M(V + M))` work in a dense repeated-query scenario.
- **Logarithmic transformation:** Convert multiplicative equations into additive differences with logarithms and use a potential-based structure. This can clarify the algebra but still uses floating-point approximations and adds logarithm operations; positive values make it possible, but the direct ratios are simpler.
- **Union by rank or size:** Maintain a balancing array and attach the smaller or shallower component beneath the other. This improves the formal amortized bound, but the root-weight formula must be inverted appropriately when the attachment direction is reversed.
- **Ordinary unweighted union-find:** It can tell whether `a` and `b` are connected but cannot recover the ratio implied between them, so it cannot decide whether a cycle-forming equation is consistent.
- **Assuming `w[x] = x / root`:** That interpretation reverses every derived ratio. In this implementation, `w[x]` is parent divided by node before compression and root divided by node afterward.
- **Updating the parent before the compression weight:** The multiplication needs the old parent's root-relative weight. Carelessly overwriting references or using a stale direction can destroy the invariant even if connectivity remains correct.
- **Equation joining two separate components:** It is never immediately contradictory because no earlier equation relates those components. The new value defines their relative scale through `w[pb]`.
- **Repeated equation:** If its value agrees with the already implied ratio within tolerance, it changes nothing. If it disagrees by at least `10^{-5}` under the implementation's comparison, the method returns `true`.
- **Reciprocal equation:** After accepting `a / b = v`, an equation `b / a = 1 / v` should agree through the same root-relative weights. A materially different reciprocal is detected as a contradiction.
- **Self-equation:** For `a / a = v`, both endpoints have the same root and equal weights, so consistency requires `v` to be within tolerance of `1`. No special branch is necessary.
- **Disconnected groups at the end:** Different components may remain unrelated. That is not a contradiction; it only means the equations never specify a ratio between those groups.
- **Tolerance boundary:** The code accepts only differences strictly smaller than `1e-5`. A difference exactly equal to `1e-5` satisfies the `>=` test and is reported as contradictory.
- **Relative versus absolute error:** The implementation uses the absolute comparison required by the local contract. Replacing it with relative error would change behavior for very large or very small ratios.
- **Long parent chain:** Always attaching `pb` under `pa` can temporarily create a deep tree. Path compression flattens every traversed route, but Python recursion depth is still a practical reason that rank or an iterative `find` could be preferable for much larger unconstrained inputs.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(m alpha(v))$. Let `V` be the number of distinct variables and `M` the number of equations. Building the mapping takes `O(M)` expected dictionary operations and creates arrays of length `V`. Processing each equation performs two `find` operations and at most one constant-time union or consistency comparison.
- **Auxiliary Space Complexity:** $O(v)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
