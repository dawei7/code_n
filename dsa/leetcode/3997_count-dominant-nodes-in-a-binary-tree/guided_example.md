# Guided Example: Count Dominant Nodes in a Binary Tree

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"root": [5, 3, 8, 2, 4, 7, 1]}`
- **Required output:** `5`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given the `root` of a complete binary tree.

The objective is to compute `5` from `{"root": [5, 3, 8, 2, 4, 7, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

**A node can be decided only after its descendants are known.**  A node `x` is dominant when its own value equals the maximum value anywhere in the subtree rooted at `x`. That subtree contains:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"root": [5, 3, 8, 2, 4, 7, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

- the node itself;
- every node in its left subtree;
- every node in its right subtree.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

Consequently, the information needed at `x` is just the maximum from each child subtree. Once those two numbers are available, the subtree maximum at `x` is

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `5` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"root": [5, 3, 8, 2, 4, 7, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `5` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Recompute every subtree separately:** Scanning a node's entire subtree to find its maximum and repeating that work at every node is correct but redundant. On a complete tree it can take `O(n \log n)` time, whereas postorder reuses each child maximum and takes `O(n)`.
- **Return both maximum and count:** Instead of a `nonlocal` counter, `dfs` could return a pair containing the subtree maximum and number of dominant nodes. That is equally asymptotic and can make the data flow more explicit, but it is not the structure used by the exact source.
- **Iterative postorder traversal:** An explicit stack can avoid recursion. It needs a visited marker or another way to recognize when both children have been processed, so it is more verbose while retaining `O(n)` time.
- **Breadth-first traversal:** Level order visits nodes before their descendants' maxima are known. It would need stored per-node information and a later reverse pass, while postorder produces the needed summaries directly.
- **Leaf nodes:** Every leaf is dominant because its subtree contains only itself. The negative-infinity child sentinel makes this fall out of the ordinary logic.
- **Single-node tree:** The answer should be `1`. The intended recurrence obtains that result, but the exact stored file currently raises `NameError` first because `inf` is undefined.
- **Duplicate maximum values:** A node tied with a descendant maximum is dominant. The `mx == node.val` comparison handles ties correctly.
- **Root node:** The root is dominant exactly when its value equals the maximum value in the whole tree.
- **Positive-value constraint:** All values are at least `1`, so a sentinel such as `0` would also be below every legal value. Negative infinity expresses the general intent more clearly, but it must actually be defined.
- **Missing children near the last level:** A complete tree may have absent children only at the end of its last level. The same base case handles all of them without special completeness logic.
- **Not a binary search tree:** Completeness describes shape, not value order. Neither the left nor right subtree can be skipped based on the current value.
- **Undefined `inf` dependency:** The solution explanation and complexity describe the intended Optimal algorithm. They do not erase the exact source defect; a valid execution environment must provide `inf` or the source must be corrected separately.
- **Platform-provided `TreeNode`:** The annotation and child fields rely on the standard harness type. Users are not expected to recreate that helper inside the solution method.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the number of nodes. Every real node is visited exactly once. At that visit, the algorithm performs two already-returned recursive calls, one maximum over three values, one comparison, and at most one counter increment.
- **Auxiliary Space Complexity:** $O(\log n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
