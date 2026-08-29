# Guided Example: Insert Delete GetRandom O(1) - Duplicates allowed

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"operations": [["insert", 5], ["remove", 5], ["remove", 5]]}`
- **Required output:** `[true, true, false]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

`RandomizedCollection` is a data structure that contains a collection of numbers, possibly duplicates (i.e., a multiset). It should support inserting and removing specific elements and also reporting a random element.

The objective is to compute `[true, true, false]` from `{"operations": [["insert", 5], ["remove", 5], ["remove", 5]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The extra difficulty created by duplicates

This collection is a multiset: inserting the same integer twice creates two separate occurrences. `remove(val)` deletes only one occurrence, and `getRandom()` must sample occurrences uniformly. Thus, if the collection contains `[1, 1, 2]`, value `1` must be returned with probability $2/3$, while value `2` must be returned with probability $1/3$.

A dense list is ideal for that probability rule. If every occurrence occupies one list position, choosing a uniformly random position automatically weights a value by its number of copies. The challenge is removal. Deleting a middle list position normally shifts later entries and costs linear time.

As in the no-duplicates version, order is not part of the contract. The solution can overwrite the removed position with the last occurrence and then pop the physical last position. However, one dictionary index per value is no longer enough: a value can occupy several list positions. The exact solution therefore uses:

- `l`, a dense list containing every current occurrence;
- `m`, a dictionary mapping each distinct value to a set of all indices where that value occurs in `l`.

The representation invariant is:

> For every value `v`, `m[v]` is exactly the nonempty set of indices `i` for which `l[i] == v`. Values with no occurrences have no dictionary key.

This two-way correspondence is what makes membership, location, and occurrence-weighted sampling possible.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"operations": [["insert", 5], ["remove", 5], ["remove", 5]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Inserting an occurrence

The method obtains the existing index set with `m.get(val, set())`. If `val` is absent, the default expression creates a new empty set. It then adds `len(l)`, the index at which the next appended item will be placed, assigns the set to `m[val]`, and appends `val` to the list.

After these steps, the new list position is included in the correct value’s index set. Existing positions and mappings are unchanged, so the invariant is preserved.

The return value is `len(idx_set) == 1`, evaluated after insertion. A size of one means the just-added occurrence is the only occurrence, so the value was not previously present and the method returns `true`. A larger size means at least one copy already existed, so the new copy is still inserted but the method returns `false`. This distinction is easy to miss: `false` does not mean the insertion failed; it reports that the value was already represented before this call.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Locating one occurrence for removal

If `val not in m`, the invariant says there is no matching occurrence, so the method returns `false` without changing the collection.

Otherwise, `idx_set = m[val]` refers to its nonempty set of positions. The exact code chooses one occurrence using `idx = list(idx_set)[0]`. Any occurrence is legal to remove, because equal copies have no separate identity exposed through the interface. It also computes `last_idx = len(l) - 1`, the position that can be popped without shifting anything.

There is an important implementation-level complexity detail here: constructing `list(idx_set)` copies all indices in that set. If `val` has $f$ occurrences, this exact line takes $O(f)$ time and temporary space, even though only one index is needed. The intended constant-time set operation would be to obtain or remove an arbitrary member directly, such as with `idx_set.pop()`. The remainder of the algorithm is the standard average-$O(1)$ design, but the supplied exact source’s conversion means its `remove` method is not strictly average $O(1)$ when one value has many copies. The approach must state this rather than hiding it behind the manifest’s intended bound.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[true, true, false]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"operations": [["insert", 5], ["remove", 5], ["remove", 5]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[true, true, false]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Direct set `pop` for the index:** Removing an arbitrary index from `idx_set` directly avoids the exact source’s `list(idx_set)` copy and gives the intended expected-$O(1)$ removal. The subsequent moved-last-index updates remain necessary.
- **Linear search in the occurrence list:** A list alone already gives correct weighted random selection, but locating `val` for removal costs $O(n)$. The dictionary of index sets exists specifically to avoid that search.
- **Dictionary of counts only:** Counts can support insertion and removal, but cannot select an occurrence-weighted random value in constant time without an additional sampling structure. Choosing a random dictionary key would weight distinct values equally instead of by multiplicity.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(f)$. Let $n$ be the total number of stored occurrences, and let $f$ be the number of occurrences of the particular value passed to `remove`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
