# Guided Example: Set Mismatch

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 2, 4]}`
- **Required output:** `[2, 3]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You have a set of integers `s`, which originally contains all the numbers from `1` to `n`. Unfortunately, due to some error, one of the numbers in `s` got duplicated to another number in the set, which results in **repetition of one** number and **loss of another** number.

The objective is to compute `[2, 3]` from `{"nums": [1, 2, 2, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Use the promise about the original set

Before the error, the collection contains every integer from one through `n` exactly once. After the error, one value appears twice and one different value disappears. This guarantee is much stronger than merely saying that the array contains arbitrary repeated numbers. It lets us recover both answers by comparing three sums.

The exact solution computes:

- `s1`: the expected sum of all integers from one through `n`;
- `s2`: the sum of the distinct values that actually occur;
- `s`: the sum of every array element, including the second copy of the duplicate.

Each difference isolates one unknown.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 2, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Compute the expected perfect-set sum

The well-known arithmetic-series formula gives:

`s1 = n * (n + 1) // 2`.

The implementation writes the factors as `(1 + n) * n // 2`, which is the same calculation. This is the sum the array would have if no replacement error had occurred.

Integer division is exact here because one of two consecutive integers `n` and `n + 1` is even. Python integers also grow as needed, so the multiplication cannot overflow. In a fixed-width language, the factors may need a wider type or division before multiplication.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The well-known arithmetic-series formula gives:

`s1 = n * (... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the set sum removes exactly the extra copy

Calling `set(nums)` keeps one occurrence of every value and discards repeated occurrences. Under the problem guarantee, every number except the missing one occurs at least once, and the duplicate is the only number occurring more than once. Therefore, the set contains:

`{1, 2, ..., n}` with only the missing value absent.

The duplicate still appears once in this set, which is correct because it belonged to the original perfect set. Only its erroneous second occurrence is removed.

If the missing value is `m` and the duplicate is `d`, then the distinct-value sum is:

`s2 = s1 - m`.

Rearranging immediately gives `m = s1 - s2`. That is why the second returned component is `s1 - s2`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[2, 3]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 2, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[2, 3]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **In-place sign marking:** Use each value as an :** - **In-place sign marking:** Use each value as an index and negate the element at that position. Encountering an already negative slot identifies the duplicate, and the one positive slot later identifies the missing value. This gives `O(n)` time and `O(1)` auxiliary space, but mutates `nums` and requires careful absolute-value handling.
- **- **XOR partitioning:** XOR all array values with :** - **XOR partitioning:** XOR all array values with one through `n` to obtain the XOR of the two unknowns, split values by a differing bit, and recover two candidates. A final membership check distinguishes duplicate from missing. It achieves `O(n)` time and `O(1)` space without arithmetic overflow, but is less intuitive.
- **- **Sum and sum-of-squares equations:** The differ:** - **Sum and sum-of-squares equations:** The differences of sums and squared sums form two equations for the missing and duplicate values. This uses constant space but is more error-prone and can overflow fixed-width types quickly.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the length of `nums`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
