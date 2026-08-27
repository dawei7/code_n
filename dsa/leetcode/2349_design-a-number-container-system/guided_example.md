# Guided Example: Design a Number Container System

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"operations": ["NumberContainers", "find", "change", "change", "change", "change", "find", "change", "find"], "arguments": [[], [10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]]}`
- **Required output:** `[null, -1, null, null, null, null, 1, null, 2]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Design a number container system that can do the following:

The objective is to compute `[null, -1, null, null, null, null, 1, null, 2]` from `{"operations": ["NumberContainers", "find", "change", "change", "change", "change", "find", "change", "find"], "arguments": [[], [10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Maintain both directions of the relationship

The class must replace the value at an index and find the smallest index for a value. One mapping alone does not support both efficiently.

The exact solution stores:

- `d[index] = number` for the current content of every assigned index;
- `g[number]` as a `SortedSet` of all indices currently containing that number.

The first mapping identifies what must be removed during replacement. The second keeps candidate indices unique and ordered so the smallest is accessible.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"operations": ["NumberContainers", "find", "change", "change", "change", "change", "find", "change", "find"], "arguments": [[], [10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Change removes the old reverse association first

If `index in d`, the index already contains `old_number = d[index]`. Before assigning the new value, the method executes

`g[old_number].remove(index)`.

This eager removal preserves the reverse-map invariant: after replacement, the old number's set no longer claims the index.

The implementation does not delete the number key when its sorted set becomes empty. Keeping an empty set is harmless because `find` checks truthiness.

If the new number equals the old number, the method removes the index and immediately adds it back. This is redundant work but leaves the state correct.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | If `index in d`, the index already contains `old_number = d[... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Install the new forward and reverse associations

`d[index] = number` records the current value. Then `g[number].add(index)` inserts the index into the new number's ordered set.

`SortedSet.add` is idempotent, so no duplicate index can appear. This matters for repeated identical `change` calls.

After these steps, the following invariant holds:

> index `i` belongs to `g[x]` exactly when `d[i] == x`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[null, -1, null, null, null, null, 1, null, 2]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"operations": ["NumberContainers", "find", "change", "change", "change", "change", "find", "change", "find"], "arguments": [[], [10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[null, -1, null, null, null, null, 1, null, 2]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Min-heaps with lazy deletion:** Push every cha:** - **Min-heaps with lazy deletion:** Push every changed index into the new number's heap and use `d` to discard stale heap tops during find. Change avoids eager removal, but heaps may accumulate stale entries.
- **Unordered sets:** Replacement is easy, but finding the minimum requires scanning all indices for that number.
- **One global scan of `d` per find:** This uses less reverse structure but makes every query `O(q)`.
- **Change an unused index:** No old removal occurs; both new associations are inserted.
- **Replace with a different number:** The index disappears from the old set before entering the new set.
- **Replace with the same number:** Remove-then-add preserves state despite extra work.
- **Find an unseen number:** The default dictionary creates an empty set and returns `-1`.
- **Find a number whose set became empty:** Truthiness fails and `-1` is returned.
- **Several indices for one number:** Sorted order makes the least one appear at position zero.
- **Remove the current smallest through replacement:** The next ordered index automatically becomes the minimum.
- **Large sparse indices:** Storage depends on assigned indices, not on the numeric maximum `10^9`.
- **Duplicate reverse membership:** Sorted-set uniqueness prevents it.
- **External dependency:** The exact source requires `SortedSet` from its supporting library.
- **Persistent state:** Internal maps are intentionally mutated across API calls.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(q log q)$. Let `q` be the total number of operations and `r` the number of indices associated with a particular number. Hash-map lookup is expected `O(1)`. Sorted-set removal and insertion are `O(\log r)`, so `change` is `O(\log q)` in the worst case.
- **Auxiliary Space Complexity:** $O(q)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
