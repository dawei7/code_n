# Guided Example: Construct Binary Search Tree from Preorder Traversal

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"preorder": [8, 5, 1, 7, 10, 12]}`
- **Required output:** `[8, 5, 10, 1, 7, null, 12]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of integers preorder, which represents the **preorder traversal** of a BST (i.e., **binary search tree**), construct the tree and return *its root*.

The objective is to compute `[8, 5, 10, 1, 7, null, 12]` from `{"preorder": [8, 5, 1, 7, 10, 12]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Use both preorder order and the BST ordering rule

Preorder traversal lists a subtree in this order:

1. the subtree root;
2. every node in its left subtree;
3. every node in its right subtree.

For a binary search tree with unique values, every left-subtree value is smaller than the root and every right-subtree value is larger.

Therefore, within the preorder segment belonging to one subtree, the first value is its root, followed by one contiguous block of smaller values and then one contiguous block of larger values. Finding the boundary between those two blocks completely determines the recursive subproblems.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"preorder": [8, 5, 1, 7, 10, 12]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Define the recursive interval

Helper `dfs(i, j)` constructs the BST whose preorder traversal is the inclusive subarray `preorder[i..j]`.

If `i > j`, the segment is empty and the corresponding child is `null`.

Otherwise, `preorder[i]` is the first value in this subtree's preorder segment, so the method creates:

`root = TreeNode(preorder[i])`.

The remaining task is to divide indices `i + 1` through `j` into the root's left and right subtree segments.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the smaller and larger values form contiguous blocks

Preorder completely traverses the left subtree before entering the right subtree. Every value in the left block is below the current root value, and every value in the right block is above it.

Thus the predicate

`preorder[index] > preorder[i]`

is false for all left-subtree indices and true for all right-subtree indices. It is monotone across this valid subtree segment, making binary search applicable.

This would not be safe for an arbitrary permutation. It is safe because the input is guaranteed to be the preorder traversal of some BST with unique values.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[8, 5, 10, 1, 7, null, 12]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"preorder": [8, 5, 1, 7, 10, 12]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[8, 5, 10, 1, 7, null, 12]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Recursive upper bound with one shared index:** Consume preorder once, creating a node only when the next value fits the current bound. It runs in `O(N)` time and `O(H)` stack space.
- **Monotonic stack:** Attach smaller values as left children and pop smaller ancestors to find a larger value's right parent. It is iterative and linear.
- **Repeated BST insertion:** Simple, but a sorted preorder creates `O(N^2)` work.
- **Sort to obtain inorder:** Combine sorted inorder with preorder to reconstruct the tree in `O(N \log N)` time and `O(N)` extra storage.
- **Strictly increasing preorder:** Every left segment is empty, producing a right-skewed tree.
- **Strictly decreasing preorder:** Every right segment is empty, producing a left-skewed tree.
- **Single value:** The search interval is empty and both recursive child calls return `null`.
- **Boundary at `j + 1`:** It means no right subtree; the left call receives all remaining values.
- **Boundary at `i + 1`:** It means no left subtree; the right call receives all remaining values.
- **Valid-preorder guarantee:** The monotone partition property depends on it; malformed input would require validation.
- **Input preservation:** The preorder list is only read and is not sorted or modified.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let `N` be the preorder length and `H` the height of the resulting tree.
- **Auxiliary Space Complexity:** $O(H)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
