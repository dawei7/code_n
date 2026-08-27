# Guided Example: Sum of All Odd Length Subarrays

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"arr": [1, 4, 2, 5, 3]}`
- **Required output:** `58`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of positive integers `arr`, return *the sum of all possible **odd-length subarrays** of *`arr`.

The objective is to compute `58` from `{"arr": [1, 4, 2, 5, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Group subarrays by their ending index

Every odd-length subarray has exactly one right endpoint. The solution processes endpoints from left to right and keeps two dynamic-programming sums:

- `f[i]` is the sum of the sums of all odd-length subarrays ending at index `i`;
- `g[i]` is the sum of the sums of all even-length subarrays ending at index `i`.

Once `f[i]` is known, it can be added to the final answer because it contains the complete contribution from all odd-length subarrays whose final index is `i`. Summing `f[i]` over every endpoint counts every required subarray once.

This is different from storing one ordinary prefix sum. A prefix sum quickly computes the sum of one chosen subarray, while `f` and `g` aggregate the sums of many subarrays at once and exploit how their length parity changes when a new element is appended.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"arr": [1, 4, 2, 5, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why parity alternates when extending a subarray

Take any subarray ending at `i - 1` and append `arr[i]`:

- an even-length subarray becomes odd;
- an odd-length subarray becomes even.

Therefore, all non-singleton odd subarrays ending at `i` come from even subarrays ending at `i - 1`. All even subarrays ending at `i` come from odd subarrays ending at `i - 1`.

The sum of an extended subarray is its previous sum plus `arr[i]`. If several subarrays are extended, their old sums are already aggregated in `g[i - 1]` or `f[i - 1]`, and `arr[i]` must be added once for every extended subarray. The only remaining task is to know how many previous subarrays have the relevant parity.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Take any subarray ending at `i - 1` and append `arr[i]`:

- ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Deriving the odd-ending recurrence

There are `i` non-empty subarrays ending at `i - 1`, with lengths one through `i`. Among those lengths, exactly `i // 2` are even. Extending each of those even subarrays contributes:

- its old sum, whose aggregate is `g[i - 1]`;
- one new copy of `arr[i]` for each of the `i // 2` subarrays.

There is also the one-element subarray `[arr[i]]`. It has odd length and contributes another copy of `arr[i]`.

Consequently:

`f[i] = g[i - 1] + arr[i] * (i // 2 + 1)`.

The factor `i // 2 + 1` combines the extended even subarrays with the new singleton. It is not an arbitrary rounding formula.

For example, at `i = 4`, subarrays ending at index three have lengths one, two, three, and four. The even ones have lengths two and four, so two are extended into odd lengths three and five. The singleton creates length one. Thus `arr[4]` appears three times, and `4 // 2 + 1` is three.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `58` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"arr": [1, 4, 2, 5, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `58` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Contribution counting per element:** Count how:** - **Contribution counting per element:** Count how many odd-length subarrays contain each index and multiply that occurrence count by `arr[i]`. It also runs in $O(N)$ time and can use $O(1)$ space, but derives the result through combinatorial endpoint choices rather than parity DP.
- **Scalar parity DP:** Replace arrays `f` and `g` with two previous-state variables. It preserves the exact recurrence and $O(N)$ time while achieving the manifest’s $O(1)$ auxiliary space.
- **Enumerate all subarrays with rolling sums:** Maintaining a sum for every start avoids a third loop but still takes $O(N^2)$ time.
- **Recompute every subarray sum:** Three nested loops are conceptually direct but take $O(N^3)$ time.
- **One element:** Initialization returns that value. The loop is empty, and the sole subarray has odd length.
- **Two elements:** Only the two singleton subarrays are odd. The recurrence’s `f[1]` contains only the second singleton, so the answer is their sum.
- **Odd full-array length:** The recurrence includes the full array in `f[n - 1]` because its parity is odd.
- **Even full-array length:** The full array contributes to `g[n - 1]` and is intentionally not added to `ans`.
- **Positive input values:** Positivity is part of the contract but not required by the recurrence; parity grouping would also work for zero or negative values.
- **Large totals:** A fixed-width implementation may need a wider integer type. Python avoids overflow.
- **Array allocation mismatch:** Although only the previous state is mathematically needed, this source stores every `f[i]` and `g[i]`. Documentation and memory analysis must reflect that exact choice.
- **No empty subarray:** The initialization and recurrences include only non-empty subarrays. The empty subarray contributes nothing and is not part of the problem definition.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the length of `arr`.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
