# Guided Example: Two Sum IV - Input is a BST

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"root": [5, 3, 6, 2, 4, null, 7], "k": 9}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given the `root` of a binary search tree and an integer `k`, return `true` *if there exist two elements in the BST such that their sum is equal to* `k`, *or* `false` *otherwise*.

The objective is to compute `true` from `{"root": [5, 3, 6, 2, 4, null, 7], "k": 9}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn pair search into complement lookup

For a current node value `v`, a pair sums to `k` exactly when some other node has value `k - v`. Instead of comparing `v` with every node seen before, the algorithm stores visited values in a hash set. Membership lookup then answers the complement question directly.

The traversal order is not important for this reasoning. The exact solution uses depth-first search, visiting a node before recursively visiting its left and right subtrees.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"root": [5, 3, 6, 2, 4, null, 7], "k": 9}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Meaning of the visited set

At the moment `dfs(root)` examines a non-null node, `vis` contains the values of all nodes that have already been processed earlier in the traversal. It does not yet contain the current node's value.

The order of operations is:

1. Compute the needed complement `k - root.val`.
2. Check whether that complement is in `vis`.
3. If it is, return `true`.
4. Otherwise, add the current value to `vis`.
5. Search the left and right subtrees.

Checking before inserting is essential because the problem requires two nodes. If `k` equals twice the current value, inserting first would allow one node to match itself. With the actual order, that pair is found only if an earlier distinct node with the same value was already visited.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the BST ordering is not required by this implementation

The input is guaranteed to be a binary search tree, but the hash-set method treats it as an ordinary binary tree. It does not compare values to decide which branch to enter. Both subtrees may contain a useful complement depending on which current value is being considered, so it traverses them as needed.

Ignoring the ordering is not incorrect. The set provides constant-time expected complement lookup, and visiting every node is still linear. A different solution could exploit inorder sorting and two pointers, but the exact source chooses the simpler traversal-plus-memory tradeoff.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"root": [5, 3, 6, 2, 4, null, 7], "k": 9}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Inorder list plus two pointers:** Inorder traversal of a BST produces sorted values. Two pointers can then find a target sum in `O(N)` time and `O(N)` list space. It uses the BST property explicitly but still stores all values.
- **Two BST iterators:** One ascending and one descending iterator can imitate two pointers with `O(H)` space, but carefully ensuring the iterators refer to distinct nodes makes the implementation more complex.
- **Search the BST for each node's complement:** Searching from the root for every node takes `O(NH)` time, which becomes `O(N^2)` in a skewed tree.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let `N` be the number of nodes and `H` the tree height.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
