# Guided Example: Maximum Number of Non-Overlapping Subarrays With Sum Equals Target

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 1, 1, 1, 1], "target": 2}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array `nums` and an integer `target`, return *the maximum number of **non-empty** **non-overlapping** subarrays such that the sum of values in each subarray is equal to* `target`.

The objective is to compute `2` from `{"nums": [1, 1, 1, 1, 1], "target": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Greedily choose the earliest finishing target-sum subarray

Every desired object is an interval. For maximizing the number of non-overlapping intervals, an interval that finishes earlier leaves at least as much room for all future choices as one that finishes later.

The stored solution scans from left to right. Starting immediately after the last selected subarray, it finds the first possible ending index of any target-sum subarray. It selects that subarray, increments the answer, discards all prefix-sum history, and begins a fresh search after the selected end.

This is the standard earliest-finish greedy principle specialized to subarrays discovered through prefix sums.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 1, 1, 1, 1], "target": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Detect a target sum with prefix differences

For the current search segment, `s` is the running sum through the current index. Set `vis` contains prefix sums observed before the current position, relative to the segment start.

A subarray ending at the current index has sum `target` exactly when an earlier prefix sum equals `s - target`:

$$
s-\text{earlier prefix}=\texttt{target}.
$$

The set begins as `{0}`, representing the empty prefix before the segment starts. This allows a target-sum subarray that begins exactly at the current segment's first index to be detected.

Negative array values cause no problem. Prefix sums need not be increasing because the algorithm asks only whether the required difference has appeared.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For the current search segment, `s` is the running sum throu... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Understand the exact index movement

At a nonmatching index, the inner loop increments `i` and then inserts the updated running sum into `vis`. That prefix can serve as the beginning boundary for a later subarray.

At a matching index, the source increments `ans` and breaks before incrementing `i` or inserting the current prefix. The outer code then executes one `i += 1`, moving directly to the element after the chosen subarray's end.

Thus no index is processed twice, and the next search cannot overlap the selected interval.

If the scan reaches the array end without finding another match, the inner loop has already advanced `i` to `n`. The outer increment makes it `n+1`, and the outer condition stops. That harmless extra increment does not access the array.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 1, 1, 1, 1], "target": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Dynamic programming over all intervals:** It c:** - **Dynamic programming over all intervals:** It can solve the problem but is unnecessary once earliest finishing is recognized.
- **Store every target-sum interval:** Generating and sorting intervals uses more time and space than selecting during the scan.
- **Global prefix set without reset:** It can detect overlapping intervals and overcount, so history must be cleared after a selection.
- **Sliding window:** It is invalid with negative numbers because expanding or shrinking does not change sums monotonically.
- **Target zero:** Repeated prefix sums detect nonempty zero-sum subarrays correctly.
- **Negative values:** Prefix differences remain valid without any ordering assumption.
- **Single matching element:** The empty-prefix zero allows it to be selected as a one-element subarray.
- **No matching subarray:** The scan reaches the end and returns zero for that suffix or the whole array.
- **Adjacent selected intervals:** They are allowed because the next search begins exactly one index after the previous end.
- **Nested candidate intervals:** The earliest ending one is selected, leaving the largest possible suffix.
- **Duplicate prefix sums:** A set is enough because only existence, not which starting index, matters for earliest-end selection.
- **Nonempty requirement:** The lookup uses a previously stored prefix, so a detected difference corresponds to at least one processed element.
- **Nested loops:** Their total work is linear because `i` never resets backward.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be array length. Although the source has nested `while` loops, index `i` only moves forward. Each array element is added to a running sum once and causes constant expected-time set work. Total expected time is $O(N)$.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
