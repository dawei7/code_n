# Guided Example: Average Value of Even Numbers That Are Divisible by Three

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 3, 6, 10, 12, 15]}`
- **Required output:** `9`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums` of **positive** integers, return *the average value of all even integers that are divisible by* `3`*.*

The objective is to compute `9` from `{"nums": [1, 3, 6, 10, 12, 15]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Combine the two divisibility requirements

An integer is even exactly when it is divisible by 2. The task also requires divisibility by 3. Because 2 and 3 are coprime, satisfying both conditions is equivalent to being divisible by their least common multiple:

$$
\operatorname{lcm}(2,3)=6.
$$

Therefore the single test `x % 6 == 0` identifies exactly the values that belong in the average. It includes numbers such as 6, 12, and 18 and excludes values satisfying only one condition, such as 4 or 9.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 3, 6, 10, 12, 15]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Maintain only a sum and a count

The variables `s` and `n` begin at zero. Here `n` is a local count of qualifying values; it is unrelated to any conventional use of $n$ as the input length.

For each `x`:

- If `x % 6 != 0`, the value contributes nothing and is skipped.
- If `x % 6 == 0`, `s += x` adds it to the qualifying total and `n += 1` records one more term.

After the scan, the arithmetic mean is `s / n`. The problem requires rounding down, and all included values are positive, so integer floor division `s // n` gives the required integer.

The conditional return `0 if n == 0 else s // n` prevents division by zero and implements the specified result when no value qualifies.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Trace the first example

For `nums=[1,3,6,10,12,15]`:

- 1 and 3 are not divisible by 6.
- 6 qualifies, making `s=6` and `n=1`.
- 10 does not qualify.
- 12 qualifies, making `s=18` and `n=2`.
- 15 is divisible by 3 but not even, so it is excluded.

The returned floor average is `18//2=9`.

For `[1,2,4,7,10]`, no value is divisible by 6. The count remains zero, and the method returns 0.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `9` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 3, 6, 10, 12, 15]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `9` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Separate tests:** Use `x % 2 == 0 and x % 3 == 0`. This is equally correct but performs two remainder checks instead of one least-common-multiple test.
- **Build a filtered list:** Select all qualifying values and compute `sum(values)//len(values)`. It is concise but uses $O(N)$ extra space and still needs an empty-case check.
- **Functional aggregation:** A generator can feed qualifying values to a sum, but the count must also be obtained, often requiring another pass or materialization.
- **No qualifying values:** Returning zero avoids division by zero and matches the contract.
- **One qualifying value:** Its average is the value itself.
- **Duplicate qualifying values:** Every occurrence contributes; using a set would incorrectly discard multiplicity.
- **Divisible by 3 but odd:** Values such as 9 are excluded because they are not divisible by 6.
- **Even but not divisible by 3:** Values such as 10 are also excluded.
- **Flooring:** `//` performs the required round down for the positive total and count.
- **Variable naming:** Local `n` counts qualifying values rather than representing the full array length; reading it with that meaning avoids confusion.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the length of `nums`. The loop visits every element once and performs one modulo test plus constant-time additions for qualifying values. Total time is $O(N)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
