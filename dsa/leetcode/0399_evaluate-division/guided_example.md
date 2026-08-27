# Guided Example: Evaluate Division

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"equations": [["a", "b"], ["b", "c"]], "values": [2, 3], "queries": [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]}`
- **Required output:** `[6, 0.5, -1, 1, -1]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array of variable pairs `equations` and an array of real numbers `values`, where $\text{equations}[i] = [A_{i}, B_{i}]$ and $\text{values}[i]$ represent the equation $A_{i} / B_{i} = \text{values}[i]$. Each $A_{i}$ or $B_{i}$ is a string that represents a single variable.

The objective is to compute `[6, 0.5, -1, 1, -1]` from `{"equations": [["a", "b"], ["b", "c"]], "values": [2, 3], "queries": [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn equations into connected components with ratios

Each equation connects two variables. If `a / b = 2` and `b / c = 3`, then `a`, `b`, and `c` belong to one connected component, and `a / c = 6`. Variables in different components have no determined ratio.

Ordinary union–find can answer whether two variables are connected. This solution augments it with multiplicative weights so it can also recover their quotient.

It maintains two mappings:

- `p[x]` is the current parent of variable `x`;
- `w[x]` is the ratio $x / p[x]$.

For a root, `p[x] == x` and its weight is one, because $x/x=1$.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"equations": [["a", "b"], ["b", "c"]], "values": [2, 3], "queries": [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Initialize every known variable before merging

The first loop over `equations` assigns each encountered variable as its own parent. All of this initialization happens before any equation is processed by union, so repeated assignments cannot destroy an already-built component.

The weight dictionary is a `defaultdict` whose missing value is one. Thus every newly initialized root begins with the correct self-ratio.

Variables that appear only in queries are deliberately not inserted. The problem defines them as unknown, even for a query such as `x / x`; the correct result for an undefined variable is `-1.0`, not one.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The first loop over `equations` assigns each encountered var... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: What `find(x)` returns and repairs

`find(x)` returns the root of `x`’s component. It also compresses the path and updates `w[x]` so that after the call:

$$
\texttt{p}[x]=\text{root}
\quad\text{and}\quad
\texttt{w}[x]=\frac{x}{\text{root}}.
$$

Suppose `x` currently points to `origin`, and `origin` eventually points to a root. Before compression, the weight invariant gives

$$
\texttt{w}[x]=\frac{x}{\text{origin}}.
$$

The recursive call `find(origin)` compresses `origin` and makes

$$
\texttt{w}[\text{origin}]=\frac{\text{origin}}{\text{root}}.
$$

Multiplying the weights yields

$$
\frac{x}{\text{origin}}
\cdot
\frac{\text{origin}}{\text{root}}
=
\frac{x}{\text{root}}.
$$

That is exactly why the code saves `origin`, recursively updates the parent, and then performs `w[x] *= w[origin]`. Saving the old parent is essential: after `p[x] = find(p[x])`, `p[x]` is already the root, but the multiplication needs the updated weight of the old intermediate parent.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[6, 0.5, -1, 1, -1]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"equations": [["a", "b"], ["b", "c"]], "values": [2, 3], "queries": [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[6, 0.5, -1, 1, -1]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Weighted graph plus DFS:** Add edges `a -> b` :** - **Weighted graph plus DFS:** Add edges `a -> b` with weight `v` and `b -> a` with weight `1/v`. For each query, search a path and multiply weights. This is simpler to derive but can revisit the graph for every query, costing $O(eq)$ in the worst case.
- **- **Weighted graph plus BFS:** Uses the same ratio:** - **Weighted graph plus BFS:** Uses the same ratio-product idea with an explicit queue instead of recursion. It has similar per-query complexity.
- **- **Union by rank or size:** Tracking component ra:** - **Union by rank or size:** Tracking component rank/size while retaining the weight algebra would prevent tall trees and, together with path compression, support the manifest’s inverse-Ackermann amortized bound.

---

## 7. Complexity Derivation

- **Time Complexity:** $O((e + q) \alpha(v))$. Let $e$ be the number of equations, $q$ the number of queries, and $v$ the number of distinct variables.
- **Auxiliary Space Complexity:** $O(v)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
