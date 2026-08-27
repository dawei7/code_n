# Guided Example: Count Smaller Elements With Opposite Parity

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [5, 2, 4, 1, 3]}`
- **Required output:** `[2, 1, 2, 0, 0]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` of length `n`.

The objective is to compute `[2, 1, 2, 0, 0]` from `{"nums": [5, 2, 4, 1, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why two ordered collections match the conditions

The score requires both:

$$
\texttt{nums}[j]<\texttt{nums}[i]
$$

and opposite parity.

The list `sl` contains two `SortedList` objects:

- `sl[0]` stores even suffix values;
- `sl[1]` stores odd suffix values.

Keeping the parity classes separate means a query never has to inspect or subtract same-parity values. Keeping each class sorted means the strict value threshold can be answered with binary search.

These are multisets rather than ordinary sets. If the same qualifying value occurs at several different suffix indices, every index must contribute separately. `SortedList` retains duplicate entries, so its rank counts their multiplicity.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [5, 2, 4, 1, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: The suffix invariant

The loop runs through

$$
i=n-1,n-2,\ldots,0.
$$

Immediately before computing `ans[i]`:

- `sl[0]` contains every even value `nums[j]` with $j>i$;
- `sl[1]` contains every odd value `nums[j]` with $j>i$; and
- neither structure contains `nums[i]` or any value to its left.

At $i=n-1$, both structures are empty, matching the empty suffix. After answering index $i$, the source inserts `nums[i]` into its own parity structure. This establishes the invariant for the next iteration at $i-1$.

The order “query first, insert second” is essential. Inserting first could allow the current index to count itself when the value test permitted it in a modified problem; more generally, it would violate the exact $j>i$ interpretation.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The loop runs through

$$
i=n-1,n-2,\ldots,0.
$$

Immediatel... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Selecting the opposite parity

The low bit

$$
\texttt{nums}[i]\mathbin{\&}1
$$

is 0 for an even value and 1 for an odd value. XOR with 1 flips that bit:

$$
(\texttt{nums}[i]\mathbin{\&}1)\mathbin{\hat{}}1.
$$

Thus:

- current even parity 0 becomes index 1, selecting odd suffix values;
- current odd parity 1 becomes index 0, selecting even suffix values.

The source writes `nums[i] & 1 ^ 1`. Under Python operator precedence, `&` binds before `^`, so this evaluates as `(nums[i] & 1) ^ 1`.

For insertion, `nums[i] & 1` chooses the current value's own parity list.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[2, 1, 2, 0, 0]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [5, 2, 4, 1, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[2, 1, 2, 0, 0]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Coordinate-compressed Fenwick trees:** This is:** - **Coordinate-compressed Fenwick trees:** This is the method described by the manifest and also achieves $O(N\log N)$ time and $O(N)$ space, but it is not the checked-in implementation.
- **Merge-sort counting:** A divide-and-conquer method can count cross-half qualifying pairs, though parity filtering complicates the merge bookkeeping.
- **Quadratic suffix scan:** Checking every pair directly is $O(N^2)$ and too slow for $N=10^5$.
- **Equal values:** `bisect_left` excludes them, correctly enforcing strict `<` rather than `<=`.
- **Duplicate smaller values:** Every duplicate occupies its own multiset entry and contributes once for its distinct index.
- **Last index:** No values lie to its right, so both structures are empty and its score is zero.
- **All values same parity:** The opposite-parity multiset is empty at every query, so every answer is zero.
- **All values equal:** Equal values are not strictly smaller even when parity could differ; in fact equal integers also share parity, so no pair qualifies.
- **Expression precedence:** `nums[i] & 1 ^ 1` relies on Python parsing `&` before `^`; explicit parentheses would make the intent clearer.
- **Query-before-insert order:** This preserves the strict right-side condition $j>i$.
- **External dependency:** `SortedList` is generally supplied by the `sortedcontainers` package and must be available in the execution environment.
- **Input preservation:** The source reads `nums` without sorting or changing it.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N\log N)$. Let $N$ be the array length. The loop processes every index once. Each iteration performs one ordered-multiset rank query and one insertion.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
