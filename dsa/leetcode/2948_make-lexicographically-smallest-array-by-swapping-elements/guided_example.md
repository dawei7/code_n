# Guided Example: Make Lexicographically Smallest Array by Swapping Elements

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 5, 3, 9, 8], "limit": 2}`
- **Required output:** `[1, 3, 5, 8, 9]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** array of **positive** integers `nums` and a **positive** integer `limit`.

The objective is to compute `[1, 3, 5, 8, 9]` from `{"nums": [1, 5, 3, 9, 8], "limit": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Sort values together with original indices

`arr = sorted(zip(nums, range(n)))`

creates pairs `(value, original_index)` ordered first by value. Keeping indices attached records where each component's values are allowed to end.

In sorted value order, start group at `i` and extend `j` while

`arr[j][0] - arr[j - 1][0] <= limit`.

If the gap between consecutive sorted values is small enough, those two occurrences can swap directly and connect their surrounding chains.

If the gap is greater than `limit`, no value on the lower side can swap with a value on the upper side: every cross-gap difference is at least that consecutive gap. The connected component ends.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 5, 3, 9, 8], "limit": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why an entire chain can be permuted

Within one group, consecutive sorted values are connected by allowed swaps. A connected graph's items can be permuted among its vertices using swaps along paths. Even if the smallest and largest values differ by more than `limit` and cannot swap directly, intermediate values can transport them through the component.

Thus the group values may be assigned arbitrarily to the original indices belonging to that group, while values cannot cross a group boundary.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Lexicographically minimize each component

For `arr[i:j]`, values are already sorted increasingly. The source extracts and sorts their original indices:

`idx = sorted(k for _, k in arr[i:j])`.

It then zips the increasing indices with the increasing value pairs and writes

`ans[k] = x`.

This places the smallest available component value at the earliest component index, the next smallest at the next index, and so on.

Lexicographic order gives absolute priority to the earliest position. Any assignment placing a larger component value at an earlier index while a smaller one occupies a later index can be improved by swapping those two values. Repeating this exchange yields the sorted-to-sorted assignment.

Components do not share reachable indices or values, so optimizing each independently produces the global lexicographically smallest array.


Every output assignment stays within a connected swap component, so it is reachable through allowed operations. No value is lost or duplicated because each sorted occurrence is zipped to exactly one group index.

For optimality, consider the first output index where another reachable array differs. Both arrays must draw from the same component at that index. The source assigns the smallest component value not already used at earlier component indices, so the other array cannot place a smaller value there. Therefore no reachable array is lexicographically smaller.

Duplicates are handled as separate `(value,index)` pairs. Their ordering among themselves is irrelevant, but multiplicity is preserved.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 3, 5, 8, 9]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 5, 3, 9, 8], "limit": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 3, 5, 8, 9]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Union-find over all value pairs:** Connecting every directly swappable pair is quadratic. Sorted consecutive gaps reveal the same components efficiently.
- **Map values to group queues:** Another method groups sorted values and pops the smallest group value while scanning original indices.
- **Sort the entire array blindly:** Incorrect when a gap greater than `limit` separates unreachable components.
- **Large endpoint difference inside a group:** It is still reachable through a chain of intermediate values.
- **Gap exactly equal to limit:** It connects groups because swaps allow `<= limit`.
- **Duplicate values:** Difference zero always connects them, and each occurrence remains represented.
- **One component:** The whole output is globally sorted.
- **Every gap too large:** Each component has one item and the output equals the input.
- **Index sorting:** Sorting only values is insufficient; smallest values must go to earliest reachable original positions.
- **Reachability versus one operation:** The solution relies on unlimited swaps and transitive component connectivity.
- **Why only consecutive sorted gaps matter:** If every neighboring pair along an interval is connected, the entire interval is one component. If one neighboring gap breaks, all cross-gap pairs differ by even more and no hidden edge can reconnect it.
- **Component indices need not be adjacent:** Swaps may choose any two array indices; connectivity depends on current values, so one component can occupy scattered original positions.
- **Assignment exchange proof:** If two component indices $p<q$ receive values $u>v$, exchanging them makes the first changed position smaller and therefore strictly improves lexicographic order.
- **Returned array is fresh:** Writing into `ans` preserves the original input while ensuring each index is assigned exactly once by its component.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Sorting $n$ value-index pairs takes $O(n\log n)$. Across groups, sorting their index lists costs at most $O(n\log n)$ in total. Group scans and assignments are linear. Overall time is $O(n\log n)$.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
