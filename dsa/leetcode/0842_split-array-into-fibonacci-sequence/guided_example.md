# Guided Example: Split Array into Fibonacci Sequence

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"num": "1101111"}`
- **Required output:** `[11, 0, 11, 11]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string of digits `num`, such as `"123456579"`. We can split it into a Fibonacci-like sequence `[123, 456, 579]`.

The objective is to compute `[11, 0, 11, 11]` from `{"num": "1101111"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Only the first two values are free choices

A Fibonacci-like sequence satisfies:

$$
f[i+2]=f[i]+f[i+1].
$$

Once the first two values are chosen, every later value is forced. The main uncertainty is where the first two digit substrings end. Backtracking tries possible numeric pieces, but after two selections it accepts only the required sum.

The shared list `ans` stores the sequence chosen along the current search path.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"num": "1101111"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: State meaning

`dfs(i)` asks whether the suffix `num[i:]` can complete the values already in `ans` into a valid Fibonacci-like split.

If `i == n`, all digits have been consumed. This is a valid completion only when `len(ans) > 2`, enforcing the minimum sequence length of three. Consuming the string as only one or two numbers is not enough.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Build the next number digit by digit

Variable `x` begins at zero. For each end index `j` from `i` onward:

`x = x * 10 + int(num[j])`

appends the next decimal digit. This avoids repeatedly converting overlapping substrings and makes `x` grow monotonically as `j` moves right.

Each iteration treats `num[i:j+1]` as one candidate piece.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[11, 0, 11, 11]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"num": "1101111"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[11, 0, 11, 11]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Enumerate only the first two substring endpoints, then verify greedily:** This makes the “later values are forced” structure explicit and has the same bounded behavior.
- **Memoize by index alone:** It is invalid because feasibility at an index depends on the previous two selected values. The exact bounded search does not need memoization.
- **Leading zero first number:** Only the single character `"0"` may be chosen; longer pieces beginning there are rejected.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n = len(num)`. The 32-bit constraint limits each candidate number to at most ten digits. Therefore, there are only a constant number of possible first-number lengths and second-number lengths—at most about 100 pairs.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
