# Guided Example: Longest Fibonacci Subarray

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 1, 1, 1, 2, 3, 5, 1]}`
- **Required output:** `5`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array of **positive** integers `nums`.

The objective is to compute `5` from `{"nums": [1, 1, 1, 1, 2, 3, 5, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Testing whether the current value extends the run

Starting at index two, the source checks:

`nums[i] == nums[i - 1] + nums[i - 2]`.

If this equality holds, the current element satisfies the required recurrence relative to the immediately preceding two elements.

The previous run counted by `f` ends at `i - 1` and includes `nums[i-2]` whenever its length is at least two. Appending `nums[i]` therefore extends that same contiguous Fibonacci subarray by one:

`f = f + 1`.

The new run length may be the largest so far, so:

`ans = max(ans, f)`.

For `[5, 2, 7, 9, 16]`:

- $7=5+2$, so the run grows to three;
- $9=2+7$, so it grows to four;
- $16=7+9$, so it grows to five.

The entire array is counted.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 1, 1, 1, 2, 3, 5, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Resetting after a failed recurrence

If the current value does not equal the sum of the previous two, no Fibonacci subarray of length at least three can end at `i` while including those immediately preceding positions.

However, the pair:

`nums[i - 1], nums[i]`

is always a valid Fibonacci subarray of length two because no recurrence must be checked until a third term exists. That pair is also the only possible starting base for a longer Fibonacci subarray that may continue at `i + 1`.

The correct reset is therefore:

`f = 2`,

not zero or one.

For `[1, 1, 1, 1, 2, 3, 5, 1]`, the early triples of ones fail because $1\ne1+1$. Each failure resets the ending run to two. At index four, $2=1+1$ begins a length-three run using indices two through four; the following values extend it to length five.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | If the current value does not equal the sum of the previous ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Meaning of `f` after every iteration

After processing index `i`, `f` equals the greatest length of a Fibonacci subarray whose right endpoint is exactly `i`.

If the recurrence succeeds, any valid length-three-or-more subarray ending at `i` must extend a valid subarray ending at `i - 1`, and the longest such extension has length old `f + 1`.

If the recurrence fails, no length-three candidate ending at `i` is valid, while the final pair remains valid, making two the exact maximum.

This local state is sufficient because a future extension depends only on the most recent two array values and the current run length. Older failed runs cannot jump across a break; that would violate contiguity.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `5` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 1, 1, 1, 2, 3, 5, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `5` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Check every subarray:** Extending from every l:** - **Check every subarray:** Extending from every left boundary repeats the same recurrence checks and can take $O(n^2)$ time.
- **Dynamic-programming array:** Storing the ending length for every index also works in $O(n)$ time but wastes $O(n)$ space because only the previous length is needed.
- **Treat it as a subsequence problem:** Skipping elements solves a different problem and can report a length that is not contiguous.
- **No valid triple:** The answer remains two, matching the note that every pair is Fibonacci.
- **Entire array valid:** `f` increases on every iteration and `ans` reaches $n$.
- **Break followed by a new run:** Resetting to two preserves the final pair as the seed for the next possible recurrence.
- **Equal values:** Equality alone neither helps nor hurts; the third value must equal their sum.
- **Large values:** Only exact integer addition and comparison are used, with no floating-point behavior.
- **Minimum allowed length:** For a three-element input, one recurrence test decides whether the answer is three or two.
- **Positive-value guarantee:** The rolling argument depends on the recurrence and contiguity, not positivity, though positivity is part of the contract.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be `len(nums)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
