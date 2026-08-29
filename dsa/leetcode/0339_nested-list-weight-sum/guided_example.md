# Guided Example: Nested List Weight Sum

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nestedList": [[1, 1], 2, [1, 1]]}`
- **Required output:** `10`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a nested list of integers `nestedList`. Each element is either an integer or a list whose elements may also be integers or other lists.

The objective is to compute `10` from `{"nestedList": [[1, 1], 2, [1, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The recursive structure of the data already matches the calculation.

Every `NestedInteger` is one of two things:

- an integer, which contributes its value multiplied by its current depth;
- a list, whose contained elements must be processed one level deeper.

The source mirrors those two cases with a recursive helper. It does not convert the interface objects into ordinary Python lists, flatten the input, or store a separate depth for every integer. The call stack naturally remembers which enclosing list is being processed.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nestedList": [[1, 1], 2, [1, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Define the helper's contract.

`dfs(nestedList, depth)` returns the complete weighted sum of all integers contained in the supplied list, assuming elements directly inside that list have the given `depth`.

The public call is `dfs(nestedList, 1)`. This starting value is crucial because every top-level integer is inside the outer input list once and therefore has depth one. Starting at zero would underweight every integer by one level.

Inside a call, `depth_sum` begins at zero and accumulates the contributions of the list's direct elements. Each direct element is processed exactly once in the `for` loop.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Handle an integer element.

When `item.isInteger()` is true, `item.getInteger()` retrieves its stored value. Because the item is directly inside the list represented by the current call, its required contribution is

$$
\text{item.getInteger()}\times\text{depth}.
$$

The source adds that product to `depth_sum`. It does not recurse because an integer has no children.

The interface check must happen before calling `getInteger()`. The contract says that accessor returns an integer only when the object actually stores one. The source respects the abstraction instead of assuming how `NestedInteger` is implemented internally.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `10` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nestedList": [[1, 1], 2, [1, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `10` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Breadth-first traversal:** Put all top-level objects in a queue, process one depth layer at a time, and enqueue child-list elements for the next layer. This also takes $O(N)$ time but can require $O(N)$ queue space for a wide level rather than the DFS stack's $O(D)$.
- **Explicit depth stack:** Store `(object, depth)` pairs and iteratively process them. It avoids recursion and retains $O(N)$ worst-case storage, which can be helpful if nesting exceeds the language's call-stack limit.
- **Flatten first:** Producing a list of `(integer, depth)` pairs and summing afterward works, but stores information that the recursive accumulation can consume immediately.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the total number of `NestedInteger` elements across all list levels, counting both integer-holding objects and list-holding objects, and let $D$ be the maximum nesting depth.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
