# Guided Example: Number of Beautiful Pairs

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, 5, 1, 4]}`
- **Required output:** `5`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed **integer array `nums`. A pair of indices `i`, `j` where $0 \le i < j < \text{nums.length}$ is called beautiful if the **first digit** of $\text{nums}[i]$ and the **last digit** of $\text{nums}[j]$ are **coprime**.

The objective is to compute `5` from `{"nums": [2, 5, 1, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: At each right endpoint, only earlier first digits matter

A beautiful pair $(i,j)$ uses the first digit of `nums[i]` and the last digit of `nums[j]`. Process `nums` from left to right, treating current value `x` as the right endpoint `j`.

Store how many earlier numbers have each possible first digit. Then the current last digit can be compared with only ten digit buckets instead of every earlier index.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, 5, 1, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Frequency array meaning

`cnt[d]` is the number of already processed values whose first decimal digit is `d`.

Positive integers have first digits one through nine. The array has length ten for direct digit indexing; bucket zero remains unused.

The current last digit is `x % 10`. The constraint guarantees it is nonzero, although the gcd computation itself would still have defined behavior with zero.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `cnt[d]` is the number of already processed values whose fir... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Count all compatible earlier values

For every digit `y` from zero through nine, the code checks whether `cnt[y]` is positive and:

`gcd(x % 10, y) == 1`.

If so, every earlier number in that bucket forms a beautiful pair with current `x`. Adding `cnt[y]` counts all of them at once.

The actual earlier number values do not matter after their first digits are known, because the pair definition uses no other information from the left endpoint.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `5` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, 5, 1, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `5` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Check every index pair:** Directly follows the:** - **Check every index pair:** Directly follows the definition but costs $O(n^2)$.
- **Arithmetic first-digit extraction:** Repeatedly divide by ten instead of creating a string; useful for generalized large values.
- **Precompute a 10-by-10 coprime table:** Replaces repeated gcd calls with constant table lookups.
- **First digit one:** Compatible with every legal nonzero last digit.
- **Equal digits:** Only digit one is coprime with itself.
- **Bucket zero:** Never receives a positive number's first digit.
- **Nonzero-last-digit guarantee:** Avoids pairs involving gcd with zero.
- **Repeated numbers:** Allowed; indices remain distinct and bucket counts handle multiplicity.
- **Update after query:** Prevents pairing an index with itself.
- **Maximum pair count:** Python integers safely store up to $n(n-1)/2$.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the array length. The outer loop runs $n$ times and the inner digit loop always runs ten times. GCD on single decimal digits is constant time. With values limited to four digits, first-digit string conversion is constant time. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
