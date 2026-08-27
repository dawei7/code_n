# Guided Example: Closest Binary Search Tree Value II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"root": [4, 2, 5, 1, 3], "target": 3.714286, "k": 2}`
- **Required output:** `[4, 3]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given the `root` of a binary search tree, a `target` value, and an integer `k`, return *the *`k`* values in the BST that are closest to the* `target`. You may return the answer in **any order**.

The objective is to compute `[4, 3]` from `{"root": [4, 2, 5, 1, 3], "target": 3.714286, "k": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn the BST into a sorted stream

An inorder traversal visits a binary search tree in ascending value order: first the left subtree, then the node, then the right subtree. The exact protected solution exploits this order and keeps only a deque `q` containing at most `k` consecutive visited values.

The manifest describes a different optimal technique based on merging predecessor and successor iterators. The source actually uses recursive inorder traversal plus a sliding window. The two methods should not be conflated: this explanation follows the exact deque-based implementation and documents its true bounds.

Why does sorted order help? In a sorted sequence, the $k$ values closest to a fixed target form one contiguous block. Suppose two chosen values surround an unchosen value. The middle value lies numerically between them, so it cannot be farther from the target than both endpoints. Replacing a farther chosen endpoint with that middle value would produce an equally good or better selection. Under the guarantee that the closest set is unique, the answer is therefore one definite length-$k$ window in sorted order.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"root": [4, 2, 5, 1, 3], "target": 3.714286, "k": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Fill the initial window

During inorder traversal, the first `k` encountered values are appended to `q`. Before `q` reaches size `k`, no choice is necessary because the final answer must contain `k` values and fewer than `k` candidates have been seen.

The deque remains sorted because values arrive in ascending order and are appended on the right. Its left endpoint `q[0]` is the smallest value currently retained, and the next inorder value `root.val` is greater than every value already in the deque.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | During inorder traversal, the first `k` encountered values a... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Decide whether a new value should slide the window

Once `q` already has `k` elements, a newly visited value creates `k+1` candidates across the current window and its immediate right neighbor. A length-$k$ contiguous window cannot keep both extremes. The decision is therefore between:

- keeping the old left endpoint `q[0]` and rejecting the new right value; or
- removing `q[0]` and appending the new value, shifting the window one position right.

The source compares their absolute distances from `target`. If the new value is strictly closer, it removes the left endpoint with `popleft()` and appends the new value. The deque again has exactly `k` sorted, consecutive values.

If the new value is at least as far as `q[0]`, the source returns from that DFS call without changing the deque. The `>=` comparison retains the smaller, earlier value in a tie. The problem guarantees a unique set of `k` closest values, so a boundary tie that could create two different valid sets does not occur on legal inputs; either tie choice would otherwise require an explicit problem rule.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[4, 3]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"root": [4, 2, 5, 1, 3], "target": 3.714286, "k": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[4, 3]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Predecessor and successor iterators:** Build t:** - **Predecessor and successor iterators:** Build two stacks around the target, then repeatedly take the closer next predecessor or successor. This achieves $O(h+k)$ time and $O(h)$ iterator space, satisfies the balanced-tree follow-up, and is the algorithm described by the manifest rather than the exact source.
- **Inorder array plus two pointers:** Materialize all $n$ sorted values, locate the target insertion point, and expand toward the closer side until `k` values are chosen. It is easy to understand but requires $O(n)$ array space and $O(n+k)$ time.
- **Size-`k` max heap:** Traverse every node and retain the closest `k` values by distance. It works for any binary tree in $O(n\log k)$ time and $O(k+h)$ space, but it does not exploit sorted inorder order.
- **Sort all values by distance:** Collecting and sorting costs $O(n\log n)$ time and $O(n)$ storage, more than needed.
- **`k = 1`:** The deque holds the best single value seen. It slides while later values become closer and stops as soon as they cease improving.
- **`k = n`:** No comparison branch runs because the deque is not full until the final node. Every tree value is returned, as required.
- **Target below the minimum:** The first `k` inorder values are the closest. Once the next value is examined, it is farther than the smallest retained endpoint, so traversal stops.
- **Target above the maximum:** Distances decrease throughout inorder traversal. The window keeps sliding and finishes with the largest `k` values after visiting all nodes.
- **Boundary-distance tie:** The source keeps the existing smaller endpoint because it uses `>=` to reject the new value. The unique-answer guarantee excludes a tie that would make two different closest sets equally valid.
- **Answer order:** The deque is returned in ascending BST order. This is acceptable because the contract permits any order.
- **Skewed tree:** Recursion depth can reach $n$ and may exceed Python's interpreter recursion limit at the largest constraint. An iterative inorder traversal preserves the window logic while replacing call-stack risk with an explicit $O(h)$ stack.
- **Nonempty-tree guarantee:** The algorithm assumes `root` contains at least one node and `k >= 1`. An empty tree would return too few values and is outside the contract.
- **No global stop flag:** A local early return is sufficient because every ancestor and later inorder value lies still farther to the right and will also be rejected. Adding a propagated Boolean could avoid the small number of ancestor comparisons but would not change the worst-case bound.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(k)$. Let $n$ be the number of tree nodes and $h$ its height. Every node is visited at most once, and deque operations are $O(1)$. Early stopping may avoid a suffix of the inorder traversal, but in the worst case it does not. For example, if the target is larger than every node, each new value is closer than the old left endpoint, so traversal reaches all $n$ nodes. The exact source therefore has $O(n)$ worst-case time.
- **Auxiliary Space Complexity:** $O(h+k)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
