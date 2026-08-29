# Guided Example: Unique Number of Occurrences

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"arr": [1, 2, 2, 1, 1, 3]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of integers `arr`, return `true` *if the number of occurrences of each value in the array is **unique** or *`false`* otherwise*.

The objective is to compute `true` from `{"arr": [1, 2, 2, 1, 1, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Map each value to its occurrence count

`cnt = Counter(arr)` scans the array and creates one mapping entry per distinct integer. If a value appears three times, its counter entry is three regardless of where those occurrences appear.

For `[1, 2, 2, 1, 1, 3]`, the mapping is conceptually one to three, two to two, and three to one. The frequency multiset is therefore three, two, one.

Negative values require no special treatment. They are ordinary hash-map keys.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"arr": [1, 2, 2, 1, 1, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: A set reveals duplicate frequencies

`cnt.values()` provides one count for every distinct input value. Converting those counts to a set keeps only unique frequency numbers.

If two different values share a frequency, the values view contains two entries but the set collapses them into one. Its size becomes smaller than the number of counter keys.

If every frequency is unique, inserting them into a set removes nothing. The set size equals the number of distinct values.

The return expression compares:

`len(set(cnt.values())) == len(cnt)`.

`len(cnt)` is the number of distinct input values, exactly the number of frequencies that must be unique.

For `[1, 2]`, the two values each occur once. The counter has two keys but the frequency set contains only `{1}`, so sizes one and two differ and the method returns false.

For the first example, both sizes are three because frequencies one, two, and three are distinct, so it returns true.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the cardinality comparison is a complete test

Mapping each distinct value to its frequency defines a collection of $k$ integers, where $k$ is the number of distinct values. A set built from those integers has size $k$ exactly when no two are equal.

If the sizes are equal, every original frequency survived as a separate set element, proving pairwise uniqueness. If the set is smaller, at least two original frequency entries mapped to the same set value, proving that two input values have equal occurrence counts.

This is an application of the one-to-one principle: the frequency mapping from distinct input values to count numbers is injective precisely when its image has the same cardinality as its domain.

No sorting is required because the problem asks only whether a collision exists, not which counts collide or in what order.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"arr": [1, 2, 2, 1, 1, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Frequency map plus incremental seen set:** Iterate counts and return false immediately when a count already exists in the set. This can short-circuit instead of constructing the complete set first.
- **Sort the frequencies:** After counting, sort the $k$ counts and compare adjacent entries. This costs $O(k\log k)$ time and is unnecessary for a collision test.
- **Fixed counting array:** The bounded value range permits an array of 2001 counters, followed by a set or sorted uniqueness check over nonzero entries.
- **One distinct value:** There is one frequency and therefore nothing it can collide with; the method returns true.
- **All values distinct:** Every frequency equals one. The result is true only when there is one value; with two or more values it is false.
- **Negative and zero values:** They work as ordinary counter keys with no offset calculation.
- **Different values with the same count:** Set cardinality shrinks even though the values themselves are unrelated.
- **Frequency zero:** Values absent from the array are not counter keys, so zero is not part of the frequency collection.
- **Nonempty guarantee:** The method would also return true for an empty array because both sizes would be zero, but the contract always supplies at least one element.
- **Expected hashing complexity:** Adversarial collision details are abstracted by the normal expected $O(1)$ dictionary and set model.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the length of `arr` and $k$ be the number of distinct values.
- **Auxiliary Space Complexity:** $O(k)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
