# Guided Example: Maximum Binary Tree

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [3, 2, 1, 6, 0, 5]}`
- **Required output:** `[6, 3, 5, null, 2, 0, null, null, 1]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` with no duplicates. A **maximum binary tree** can be built recursively from `nums` using the following algorithm:

The objective is to compute `[6, 3, 5, null, 2, 0, null, null, 1]` from `{"nums": [3, 2, 1, 6, 0, 5]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Translate the recursive definition directly

The tree is defined by the maximum element of each current subarray:

- the maximum becomes that subtree's root;
- everything before the maximum builds the left subtree;
- everything after the maximum builds the right subtree.

The exact solution follows this definition literally. Its helper `dfs(nums)` returns the maximum binary tree for the list segment passed to it.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [3, 2, 1, 6, 0, 5]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: The empty-segment base case

If the current list is empty, there is no value from which to create a node, so `dfs` returns `null`. This is how missing children are represented.

The base case also ensures that `max(nums)` is called only for a nonempty list. A one-element list proceeds through the ordinary logic: its only value is the maximum, both slices are empty, and the resulting node has two null children.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | If the current list is empty, there is no value from which t... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Choose the root and divide the input

For a nonempty list, the helper performs:

1. `val = max(nums)` to find the largest value.
2. `i = nums.index(val)` to find its position.
3. Create `TreeNode(val)`.
4. Recursively construct the left child from `nums[:i]`.
5. Recursively construct the right child from `nums[i + 1:]`.

The source guarantee that all values are unique matters. It ensures the maximum has one unambiguous index. Without uniqueness, `index` would choose the first maximum, but the problem's construction rule would need to specify how ties are handled.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[6, 3, 5, null, 2, 0, null, null, 1]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [3, 2, 1, 6, 0, 5]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[6, 3, 5, null, 2, 0, null, null, 1]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Monotonic decreasing stack:** Scan values once:** - **Monotonic decreasing stack:** Scan values once. Pop smaller nodes to become the current node's left child, and make the current node the right child of the remaining stack top. This constructs the same tree in `O(N)` time and `O(N)` space and matches the manifest.
- **- **Recursion with index boundaries:** Pass `left`:** - **Recursion with index boundaries:** Pass `left` and `right` rather than slices. This avoids quadratic slice storage but still rescans ranges for maxima, so worst-case time remains `O(N^2)`.
- **- **Range-maximum data structure:** Preprocess max:** - **Range-maximum data structure:** Preprocess maximum-index queries, then recurse by boundaries. It can reduce repeated maximum search but is more machinery than the linear stack.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N^2)$. Let `N` be the number of input values and let `m` be a current subarray length.
- **Auxiliary Space Complexity:** $O(N^2)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
