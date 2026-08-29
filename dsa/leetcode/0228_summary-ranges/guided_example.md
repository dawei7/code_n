# Guided Example: Summary Ranges

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [0, 1, 2, 4, 5, 7]}`
- **Required output:** `["0->2", "4->5", "7"]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **sorted unique** integer array `nums`.

The objective is to compute `["0->2", "4->5", "7"]` from `{"nums": [0, 1, 2, 4, 5, 7]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The answer consists of maximal consecutive runs

Because `nums` is sorted and contains unique values, neighboring array entries
have one of two relationships. If `nums[j + 1] == nums[j] + 1`, they are
consecutive integers and belong in the same range. If not, there is at least
one missing integer between them, so putting both in one inclusive range would
cover a value absent from `nums` and violate the contract.

Therefore the unique smallest exact cover is obtained by splitting the array
at every non-consecutive gap. Each resulting block is a maximal consecutive
run: it cannot extend left or right without encountering the array boundary or
a missing integer.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [0, 1, 2, 4, 5, 7]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Use `i` for the run start and `j` for its expanding end

At the beginning of each outer-loop iteration, `i` is the first index not yet
represented in the answer. The source sets `j = i`, so the current run starts
as the one-element range containing `nums[i]`.

The inner loop checks two facts before extending:

- `j + 1 < n` guarantees that a next element exists;
- `nums[j + 1] == nums[j] + 1` guarantees that the next value follows with no
  integer gap.

While both hold, incrementing `j` includes that next value. Each new comparison
uses the latest endpoint, so a run can grow across any number of consecutive
values. The loop stops exactly at the last index of the maximal run.

Once `[i, j]` has been formatted and appended, `i = j + 1` moves directly to
the first element after the run. No element is reconsidered as the start of a
second range.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Format one value differently from a true interval

The nested helper `f(i, j)` receives endpoint indices, not endpoint values. If
`i == j`, the run contains one array element and must be represented simply as
`str(nums[i])`. If the indices differ, at least two consecutive values belong
to the run, and the helper returns the exact format
`f'{nums[i]}->{nums[j]}'`.

Only the first and last values are needed. Every integer between them is
implicitly covered, and the inner-loop condition has already proved that all
of those integers appear consecutively in `nums`.

For `nums = [0, 1, 2, 4, 5, 7]`, the first run expands from indices 0 through 2
and formats as `"0->2"`. The gap from 2 to 4 ends it. The next run covers
indices 3 and 4 and formats as `"4->5"`. The final index stands alone and
formats as `"7"`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `["0->2", "4->5", "7"]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [0, 1, 2, 4, 5, 7]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `["0->2", "4->5", "7"]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Track endpoint values instead of indices:** Save `start = nums[i]`, advance one pointer to the run end, and format `start` with the final value. It is equivalent; the exact helper uses indices to access both endpoints uniformly.
- **Build ranges incrementally in the answer:** Start a new mutable range at each gap and update its endpoint for consecutive values. This can work but mixes detection with string formatting and may require revising earlier output.
- **Set-based expansion:** Put all values in a set and grow from values lacking predecessors. It loses the useful sorted-input order and uses $O(n)$ extra space for a task solvable by one scan.
- **Empty input:** The outer condition `i < n` is false immediately, so the method returns an empty list.
- **One value:** `j` cannot advance, the helper uses its singleton branch, and one plain number string is returned.
- **All values consecutive:** The inner loop reaches the final index and the method emits exactly one range.
- **No values consecutive:** Every run has `i == j`, producing one singleton string per element.
- **Negative values:** `str` includes the minus sign, and arithmetic consecutiveness still uses a difference of one, so ranges such as `"-3->-1"` are formatted correctly.
- **Crossing zero:** Values `[-1,0,1]` form one consecutive run and become `"-1->1"`.
- **Minimum and maximum 32-bit values:** Python arithmetic and formatting handle both endpoints without overflow.
- **Uniqueness guarantee:** If duplicates were allowed, equality would fail the `+1` test and the same value could appear in separate output ranges, violating exact-cover intent. The algorithm correctly relies on the stated unique-input contract.
- **Input preservation:** Only indices and output strings change; `nums` remains sorted and untouched.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be `len(nums)`. Although the code has nested loops, `j` moves right
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
