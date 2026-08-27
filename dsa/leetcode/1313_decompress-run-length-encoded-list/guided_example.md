# Guided Example: Decompress Run-Length Encoded List

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3, 4]}`
- **Required output:** `[2, 4, 4, 4]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

We are given a list `nums` of integers representing a list compressed with run-length encoding.

The objective is to compute `[2, 4, 4, 4]` from `{"nums": [1, 2, 3, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Stepping through pair starts

`range(0, len(nums), 2)` produces indices

$$
0,2,4,\ldots,\texttt{len(nums)}-2.
$$

The length is guaranteed even, so every produced `i` is a frequency position and `i + 1` is a valid value position. No incomplete final pair exists.

At pair start `i`:

- `nums[i]` is the frequency, and
- `nums[i + 1]` is the value.

Advancing by two preserves the pair boundaries. Advancing by one would mistakenly interpret a value as the next frequency.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Repeating one value

For a fixed `i`, `range(nums[i])` has exactly `nums[i]` iterations. The variable name `_` signals that the particular repetition number is irrelevant. Only the number of iterations matters.

On each of those iterations, the expression `nums[i + 1]` is evaluated and appended to the new result list. Consequently, that value appears exactly its requested number of times.

The inner repetition completes before the outer loop advances to the next pair. This is the same order as:

`for i in pair starts`, then `for each repetition`, then `append the pair's value`.

It therefore concatenates runs rather than interleaving them.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For a fixed `i`, `range(nums[i])` has exactly `nums[i]` iter... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Tracing the first example

For `nums = [1,2,3,4]`, the outer index first equals zero. The frequency is one and the value is two, so the inner loop emits one `2`.

The next outer index is two. The frequency is three and the value is four, so the inner loop emits `4` three times.

Because the first run finishes before the second starts, the final list is `[2,4,4,4]`.

For `[1,1,2,3]`, pair zero emits one `1` and pair one emits two `3` values, producing `[1,3,3]`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[2, 4, 4, 4]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[2, 4, 4, 4]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Explicit nested loops:** Initialize `ans`, ite:** - **Explicit nested loops:** Initialize `ans`, iterate pair starts, and append in an inner loop. It has identical behavior and complexity and may be easier to debug for beginners.
- **List multiplication and extension:** `ans.extend([value] * frequency)` handles one run compactly. It creates a temporary list for each pair in addition to the final output.
- **Iterator repetition utilities:** Functions such as `repeat` and `chain` can express runs lazily, but returning a list still requires materializing all $S$ entries.
- **Single pair:** The outer range contains only index zero, and the output is that value repeated by its frequency.
- **Frequency one:** The inner range has one iteration, so the value appears once.
- **Repeated values in adjacent pairs:** Their runs become adjacent identical values in the output. They need not be merged because the returned decompression is the same either way.
- **Even-length guarantee:** It ensures `nums[i + 1]` is always valid. Malformed odd-length input would need validation.
- **Positive-frequency guarantee:** Every run contributes at least one value; the code would also naturally skip a zero-frequency run outside the contract.
- **Output can exceed input:** Space and time must be measured using $S$, not only the compressed length $n$.
- **Order of comprehension clauses:** Swapping them would not preserve independent pair-specific repetition and would either be invalid or emit a different order.
- **Underscore variable:** `_` is an ordinary loop variable by language rules, but convention indicates its value is intentionally unused.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n+S)$. Let $n$ be the compressed list length and define
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
