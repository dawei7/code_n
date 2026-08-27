# Guided Example: Satisfiability of Equality Equations

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"equations": ["a==b", "b!=a"]}`
- **Required output:** `false`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array of strings `equations` that represent relationships between variables where each string $\text{equations}[i]$ is of length `4` and takes one of two different forms: $"x_{i} = y_{i}"$ or $"x_{i}\neq y_{i}"$.Here, $x_{i}$ and $y_{i}$ are lowercase letters (not necessarily different) that represent one-letter variable names.

The objective is to compute `false` from `{"equations": ["a==b", "b!=a"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Treat equality as membership in the same component

Equality has three crucial properties: every variable equals itself, equality works in both directions, and equality is transitive. If `a == b` and `b == c`, then `a` and `c` must receive the same integer even when no direct equation joins them.

These properties mean that all variables connected by equality equations form one equivalence class. The only possible contradiction occurs when an inequality demands two variables from the same class to differ.

A disjoint-set union structure, also called union-find, maintains exactly these equality classes while equations are processed.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"equations": ["a==b", "b!=a"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Represent the twenty-six variables

Lowercase letters are converted to indices zero through twenty-five with

`ord(letter) - ord('a')`.

Array `p = list(range(26))` starts with `p[x] = x` for every variable. Initially, each letter is the representative, or root, of its own one-element component. No equality has yet forced two different variables together.

An equation always has length four. The code reads its variables from `e[0]` and `e[-1]`, while `e[1]` distinguishes `'='` from `'!'`. Using `e[-1]` is equivalent to `e[3]` and emphasizes that the second variable is the final character.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Lowercase letters are converted to indices zero through twen... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Find the representative of a component

Function `find(x)` follows parent pointers until it reaches an index whose parent is itself. That self-parent is the representative shared by all variables in the component.

The recursive step

`p[x] = find(p[x])`

also performs path compression. After discovering the root, it rewires `x` directly to that root. Future calls for `x`, and often for nodes along the same path, need fewer pointer traversals.

Path compression changes only the shape of the internal forest. It never changes which variables belong to the same component.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `false` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"equations": ["a==b", "b!=a"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `false` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Equality graph plus DFS:** Add undirected edge:** - **Equality graph plus DFS:** Add undirected edges for `==` equations, label connected components, and test inequalities afterward. It is equally sound but stores an adjacency structure that can include many repeated edges.
- **Repeated reachability search:** For every inequality, search an equality graph to see whether its endpoints connect. This repeats component work that union-find performs once.
- **Check equations in one input-order pass:** This is unsafe because a later equality may create a contradiction with an earlier inequality. Equalities must be finalized first.
- **Union individual nodes instead of roots:** Assigning `p[a] = b` without `find` can break the representation of existing components. Root-to-root linking preserves equivalence classes.
- **Self-equality `a==a`:** Both roots are already identical, so the union changes nothing and the equation is always satisfied.
- **Self-inequality `a!=a`:** Both endpoints necessarily have the same root, so the second pass immediately returns `false`.
- **Duplicate equations:** Repeating an equality performs an idempotent merge; repeating a compatible inequality does not alter the result.
- **Indirect chains:** Any length of equality chain is compressed into one component, so an inequality between its endpoints is detected.
- **Variables absent from equalities:** They remain singleton components and can freely receive values distinct from incompatible variables.
- **No inequalities:** Equalities alone are always satisfiable by assigning one integer per component, so the method returns `true`.
- **No equalities:** Every letter remains separate; only a self-inequality can be contradictory.
- **Representative identity:** The numeric root chosen for a component is an implementation detail. Only whether roots are equal matters.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(Q\alpha(26)$. Let `Q` be the number of equations and let the variable universe contain `26` elements.
- **Auxiliary Space Complexity:** $O(26)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
