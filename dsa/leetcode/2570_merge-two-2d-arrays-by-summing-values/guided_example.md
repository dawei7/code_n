# Guided Example: Merge Two 2D Arrays by Summing Values

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums1": [[1, 2], [2, 3], [4, 5]], "nums2": [[1, 4], [3, 2], [4, 1]]}`
- **Required output:** `[[1, 6], [2, 3], [3, 2], [4, 6]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two **2D** integer arrays `nums1` and `nums2.`

The objective is to compute `[[1, 6], [2, 3], [3, 2], [4, 6]]` from `{"nums1": [[1, 2], [2, 3], [4, 5]], "nums2": [[1, 4], [3, 2], [4, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Aggregate every record by its ID

The result needs one record for each ID appearing in either input, with all values for that ID added together. A map from ID to running total directly represents this requirement.

The exact solution uses `Counter`, a dictionary-like collection whose missing keys start at zero. It iterates through `nums1 + nums2` and performs

`cnt[i] += v`

for each record `[i,v]`. If an ID appears in only one input, its total is that one value. If it appears in both, the second visit adds to the first value.

The uniqueness guarantee within each individual array means an ID appears at most twice across the combined inputs, but the accumulation would remain correct even without that guarantee.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums1": [[1, 2], [2, 3], [4, 5]], "nums2": [[1, 4], [3, 2], [4, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why input ordering is not used during aggregation

Both inputs are already sorted, which would permit a linear two-pointer merge. The checked-in implementation instead concatenates the lists, aggregates through hashing, and sorts the resulting map entries.

Hash aggregation deliberately ignores encounter order. This makes the value-combination logic very simple, but it means output order must be restored afterward.

The expression `nums1 + nums2` creates a new outer list containing references to all pair records. It does not modify either input and does not copy the inner two-element lists themselves.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Sort the unique result entries

`cnt.items()` produces one `(id, total)` pair per distinct ID. Calling `sorted` on these pairs uses tuple ordering, whose first comparison component is the ID. Since IDs are unique among the map entries, the first component alone determines their final ascending order.

The result therefore contains:

- every ID from the union of both inputs;
- exactly one record per ID;
- the sum of all associated values;
- records in ascending ID order.

The exact Python expression returns a list of two-element tuples rather than a list of two-element lists. These are equivalent pair sequences for the usual judge serialization, although a caller requiring the annotation's literal mutable `List[List[int]]` shape could convert each tuple to a list.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[1, 6], [2, 3], [3, 2], [4, 6]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums1": [[1, 2], [2, 3], [4, 5]], "nums2": [[1, 4], [3, 2], [4, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[1, 6], [2, 3], [3, 2], [4, 6]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Two-pointer merge:** Compare the next ID in each already-sorted input, append the smaller one, and sum on equality. This achieves $O(n+m)$ time and $O(1)$ auxiliary state excluding output.
- **Fixed ID array:** Because IDs are bounded by $1000$, an array of totals can aggregate in linear time and then scan the fixed domain, using constant space relative to input size.
- **Counter plus sorting:** The implemented method is concise and robust even if input order were not sorted, but it gives up the linear merge advantage.
- **No common IDs:** Every input record appears once in the output after sorting.
- **All IDs common:** Every output value is the sum of exactly two records.
- **One array exhausts early:** The Counter approach has no special tail case; all records are simply visited.
- **Positive values:** Totals cannot cancel to zero, so every encountered ID must remain in the output.
- **Input preservation:** List concatenation creates a new outer list and neither original input is changed.
- **Tuple result records:** `sorted(cnt.items())` returns tuples. Convert with a list comprehension if a strict consumer requires inner lists.
- **Manifest distinction:** The optimal two-pointer idea is documented as an alternative, while complexity claims for the exact solution reflect hashing and sorting.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n + m)$. Let $n=|\texttt{nums1}|$, $m=|\texttt{nums2}|$, and $u$ be the number of distinct IDs across both arrays. Concatenating and scanning the records takes $O(n+m)$ expected time. Counter updates take expected $O(1)$ each. Sorting $u$ item pairs takes $O(u\log u)$ time.
- **Auxiliary Space Complexity:** $O(u)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
