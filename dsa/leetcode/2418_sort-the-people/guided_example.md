# Guided Example: Sort the People

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"names": ["Mary", "John", "Emma"], "heights": [180, 165, 170]}`
- **Required output:** `["Mary", "Emma", "John"]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array of strings `names`, and an array `heights` that consists of **distinct** positive integers. Both arrays are of length `n`.

The objective is to compute `["Mary", "Emma", "John"]` from `{"names": ["Mary", "John", "Emma"], "heights": [180, 165, 170]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Keep the two parallel arrays connected

At every index `i`, `names[i]` and `heights[i]` describe the same person. The required output changes the order of the names according to height, so the central danger is losing that index relationship. Sorting only `heights` would reveal the correct height order but would no longer say which original name belonged to each moved value.

The solution avoids mutating either input array. It creates

`idx = list(range(len(heights)))`,

which initially contains `0, 1, ..., n - 1`. Each number is a compact reference to one person. Through that reference, both attributes remain available: the person's height is `heights[i]` and the person's name is `names[i]`. The algorithm sorts these references and then uses them to read names in the resulting order.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"names": ["Mary", "John", "Emma"], "heights": [180, 165, 170]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why sorting indices solves the ordering problem

The call

`idx.sort(key=lambda i: -heights[i])`

assigns index `i` the key `-heights[i]`. Python's list sort arranges keys in ascending order. Negation reverses the desired numeric relationship: if one person is taller, then their height is larger but their negative height is smaller. For example, heights 180, 165, and 170 produce keys -180, -165, and -170. Ascending key order is -180, -170, -165, corresponding to descending height order 180, 170, 165.

The constraints guarantee that all heights are distinct. Therefore every sorting key is distinct as well, and the required order is unambiguous. No tie-breaking rule is needed. Python's sort is stable, but stability has no effect under this guarantee.

After sorting, `idx[j]` is the original position of the person who belongs at output position `j`. The list comprehension

`[names[i] for i in idx]`

visits those positions in sorted order and extracts only the requested names. It does not return heights or indices, and it does not confuse equal names: names may repeat, but each index still identifies the correct person. In the example with two people named `"Bob"`, the two Bob strings are indistinguishable as values, yet their separate indices have different heights and are placed correctly.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The call

`idx.sort(key=lambda i: -heights[i])`

assigns ind... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Step-by-step trace

For `names = ["Mary", "John", "Emma"]` and `heights = [180, 165, 170]`, the initial index list is `[0, 1, 2]`. The associated negative keys are -180 for index 0, -165 for index 1, and -170 for index 2. Sorting by those keys changes the index list to `[0, 2, 1]`. Reading `names[0]`, `names[2]`, and `names[1]` produces `["Mary", "Emma", "John"]`.

Notice that no association needs to be rebuilt after sorting. The association is the index itself. This is especially clean because the problem already presents the data as parallel arrays.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `["Mary", "Emma", "John"]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"names": ["Mary", "John", "Emma"], "heights": [180, 165, 170]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `["Mary", "Emma", "John"]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Pair and sort:** Construct pairs such as `(hei:** - **Pair and sort:** Construct pairs such as `(height, name)`, sort them by descending height, and extract each name. This is equally asymptotic and often concise, but the exact solution's index permutation avoids duplicating the association into tuple objects.
- **Height-to-name dictionary:** Unique heights allow a map followed by a sort of the heights. It works in $O(n \log n)$ time and $O(n)$ space, but would be invalid without the distinct-height guarantee because duplicate keys could overwrite people.
- **Sort both arrays in place:** A custom sort could swap names whenever it swaps heights. That can avoid an explicit index result but mutates the inputs and is easier to implement incorrectly because the arrays must remain synchronized.
- **Counting sort:** Heights are bounded by $10^5$, so a bucket-based method could run in $O(n + H)$ time for height range $H$. Its memory and range-scanning cost are unnecessary for $n \le 1000$, and comparison sorting is simpler.
- **Single person:** `idx` contains only zero, sorting does nothing, and the one name is returned.
- **Repeated names:** Names do not serve as keys. Separate people with the same spelling retain their separate indices and are ordered by their distinct heights.
- **Distinct heights:** This guarantee removes all tie ambiguity. If it were removed, the problem would need to specify how equal-height people should be ordered; Python's stable sort would retain their original relative order.
- **Input preservation:** Neither original list is rearranged. Only the newly allocated index and result lists change, which can be useful when callers still need the original alignment.
- **Descending versus ascending:** Omitting the minus sign would return the shortest person first. The sign inversion is the exact detail that converts Python's default ascending key order into the required descending height order.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n \log n)$. Let $n$ be the common length of `names` and `heights`. Creating `idx` takes $O(n)$ time. Sorting $n$ indices takes $O(n \log n)$ comparisons in the worst case relevant to the stated bound, and evaluating each simple key is constant time. Building the result examines all $n$ sorted indices once, taking another $O(n)$ time. Sorting dominates, so total time is $O(n \log n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
