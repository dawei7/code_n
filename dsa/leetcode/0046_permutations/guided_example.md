# Guided Example: Permutations

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [0, 1]}`
- **Required output:** `[[0, 1], [1, 0]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array `nums` of distinct integers, return all the possible permutations. You can return the answer in **any order**.

The objective is to compute `[[0, 1], [1, 0]]` from `{"nums": [0, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A permutation is a sequence of position choices

The input has $n$ distinct values, and a permutation must place each one into exactly one of $n$ output positions. The solution fills those positions from left to right. At depth `i`, positions 0 through `i - 1` are already fixed, position `i` is the next decision, and every not-yet-used input index is a legal choice.

This turns the problem into a backtracking tree. The root has $n$ choices for the first position, each child has $n-1$ choices for the second, and the number of leaves is

$$
n(n-1)(n-2)\cdots 1 = n!.
$$

Every leaf corresponds to one complete ordering, so visiting all leaves is unavoidable when all permutations must be returned.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [0, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the algorithm tracks indices with `vis`

`vis[j]` records whether input position `j` is already represented in the current partial permutation. A value becomes unavailable immediately after it is placed and becomes available again when backtracking leaves that branch.

Tracking indices is precise because the requirement is to use every input element once. The contract says the values are distinct, so tracking values in a set could also work, but an index-based Boolean list avoids hashing and maps directly to the iteration over `nums`.

At entry to `dfs(i)`, exactly `i` entries of `vis` are true, and `t[0:i]` contains those corresponding values in the order selected. This is the central invariant. It holds initially for `dfs(0)` because no positions are filled and every flag is false.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `vis[j]` records whether input position `j` is already repre... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Use a preallocated path array

`t = [0] * n` reserves all output positions once. When unused input index `j` is chosen at depth `i`, the code writes `t[i] = nums[j]`. This avoids appending and popping path values; recursion depth itself identifies which slot to overwrite.

The placeholder zeros have no semantic meaning. Even if zero is an actual input value, every slot is overwritten along a complete root-to-leaf path before a result is recorded. The algorithm never interprets an unfilled placeholder as a selected value; `vis` is the authoritative usage state.

After setting `vis[j] = true` and writing the value, `dfs(i + 1)` receives a state with one more filled position and one more used index, so the invariant is preserved. When the child returns, the code sets `vis[j] = false`. It does not clear `t[i]`, and that is safe: the next sibling choice overwrites the same slot before descending, and no snapshot is taken until all positions are filled.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[0, 1], [1, 0]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [0, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[0, 1], [1, 0]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Append/pop path:** Maintain a variable-length :** - **Append/pop path:** Maintain a variable-length list instead of preallocating `t`. This is equally correct and makes filled length visible directly, while the selected source avoids repeated path resizing.
- **In-place swapping:** At depth `i`, swap each suffix value into position `i`, recurse, and swap back. It removes the visited array but mutates the input temporarily and requires careful restoration.
- **Pass a sliced remaining list:** Recurse with all elements except the chosen one. The state is intuitive but repeated slicing and path concatenation increase allocation and copying costs.
- **Iterative next-permutation generation:** Sort the values and repeatedly transform to the next lexicographic permutation. It uses constant path overhead but mutates order and requires a separate snapshot for every result.
- **One input value:** The only branch fills position 0 and records the one-element permutation.
- **Placeholder zero:** It cannot leak into an answer because a leaf is reached only after every path slot has been assigned.
- **Distinctness guarantee:** If duplicate values were allowed, different index paths could produce identical value sequences. That separate problem needs depth-level duplicate suppression.
- **Input preservation:** The solution reads `nums` without swapping or sorting it, so the caller's array is unchanged.
- **Any output order:** Depth-first order follows the original input ordering, but the contract accepts any order.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n \cdot n!)$. There are $n!$ output permutations, each containing $n$ values. Copying the path at every leaf alone costs $\Theta(n \cdot n!)$ time. The internal search also loops over up to $n$ indices at its states, which remains within the same conventional $O(n \cdot n!)$ bound. This matches the manifest and is asymptotically optimal with respect to the size of the required output.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
