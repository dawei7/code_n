# Guided Example: Verify Preorder Sequence in Binary Search Tree

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"preorder": [5, 2, 1, 3, 6]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of **unique** integers `preorder`, return `true` *if it is the correct preorder traversal sequence of a binary search tree*.

The objective is to compute `true` from `{"preorder": [5, 2, 1, 3, 6]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Descending values mean continuing left

If a new value `x` is smaller than the stack top, it can lie in the current node's left subtree. Pushing it preserves a strictly decreasing stack. For example, the beginning `[10, 9, 8, 7]` can represent a chain of left children, and the stack becomes `[10, 9, 8, 7]`.

No lower bound changes while descending left because the traversal has not yet closed a left subtree and crossed into a right subtree of one of those ancestors.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"preorder": [5, 2, 1, 3, 6]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: A larger value means backtracking

When `x` is greater than the stack top, it cannot be inside that top node's left subtree. Preorder has finished that region and must climb toward an ancestor where `x` can belong on the right.

The loop



pops every smaller active ancestor. After the loop, either the stack is empty or its top is greater than `x`. The last value popped is the root whose right-side region has just been entered most specifically, so it becomes the new lower bound.

Because the stack is decreasing from bottom to top, popped values increase as the loop climbs. In `[5, 2, 1]` with `x = 3`, it pops `1` and then `2`, setting `last` first to `1` and finally to `2`. It stops below `5`, placing `3` in the right subtree of `2` but still in the left subtree of `5`. Future values must remain above `2`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | When `x` is greater than the stack top, it cannot be inside ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why a value below `last` is impossible

Once a node is popped because the traversal moved to its right, preorder can never return to that node's left subtree. All future nodes in the currently open right-side region must be greater than the popped ancestor. If a later `x` is less than `last`, it belongs on the forbidden left side of an ancestor whose left subtree has already been completed.

The solution checks `if x < last: return false` before performing new pops. This is enough under the guarantee that all input values are unique. A repeated value equal to `last` cannot occur in valid input. For a version allowing arbitrary inputs but still requiring a strict BST, the rejection would normally be `x <= last`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"preorder": [5, 2, 1, 3, 6]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Reuse `preorder` as the stack:** Maintain a st:** - **Reuse `preorder` as the stack:** Maintain a stack length and overwrite the already-read prefix. This preserves $O(n)$ time and reduces auxiliary space to $O(1)$, but mutates the input. It is the follow-up technique described by the manifest, not the exact source.
- **Recursive bounds parser:** Consume preorder values while they fit a `(lower, upper)` range, recursively assigning left and right subtrees. It can run in $O(n)$ time but uses $O(h)$ call-stack space and requires careful shared-index handling.
- **Build the BST explicitly:** Insert every value and compare the resulting preorder. A skewed sequence can make insertion $O(n^2)$, and allocating nodes is unnecessary for simple verification.
- **Strictly decreasing input:** No values are popped; it represents an all-left chain. The stack reaches size $n$.
- **Strictly increasing input:** Each new value pops the previous top and raises `last`; it represents an all-right chain and still runs in linear time.
- **One value:** It satisfies the unrestricted root position, is pushed, and the function returns `true`.
- **A late small value:** If traversal has already entered a right subtree, the lower-bound check detects the attempt to return to a completed left side.
- **Duplicate values:** The contract excludes them. With duplicates present, the source's strict `< last` check and pop condition would need adjustment based on a clearly defined duplicate-placement policy.
- **Negative values:** The local problem bounds values positively, but `last = -inf` means the algorithm itself also supports negative integers without a special sentinel collision.
- **Input preservation:** The explicit stack leaves `preorder` unchanged, which may be preferable even though it costs linear auxiliary memory.
- **Order of the bound check:** Testing `x < last` before popping is valid because `last` summarizes previously closed ancestors. The subsequent pops can only establish a new bound for future values after `x` is placed.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of preorder values. Every value is pushed exactly once. A value can be popped at most once, because it never reenters the stack. Although the `while` loop is nested inside the `for` loop, there are at most $n$ pops across the complete execution. Total time is therefore $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
