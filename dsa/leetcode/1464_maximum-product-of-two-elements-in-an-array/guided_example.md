# Guided Example: Maximum Product of Two Elements in an Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [3, 4, 5, 2]}`
- **Required output:** `12`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given the array of integers `nums`, you will choose two different indices `i` and `j` of that array. *Return the maximum value of* $(\text{nums}[i]-1)*(\text{nums}[j]-1)$.

The objective is to compute `12` from `{"nums": [3, 4, 5, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

**Evaluate every unordered pair of indices.** The result must use two different array positions. The outer loop chooses the first position `i` and binds its value to `a`. The inner loop iterates over `nums[i + 1:]`, so every chosen `b` comes from a strictly later position.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [3, 4, 5, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

This arrangement automatically enforces distinct indices. It also avoids checking the same pair twice: if positions two and five are evaluated when `i = 2`, the reversed ordering cannot appear later because position two will never belong to a suffix beginning after five.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | This arrangement automatically enforces distinct indices.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

For each pair, the code calculates `(a - 1) * (b - 1)` exactly as the problem requests. `ans = max(ans, ...)` retains the greatest product seen so far.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `12` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [3, 4, 5, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `12` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Track the two largest values:** Update a maxim:** - **Track the two largest values:** Update a maximum and second maximum during one scan, then multiply their decremented values. This achieves the manifest's `O(n)` time and `O(1)` space.
- **Sort the array:** The final two values are the largest. This takes `O(n log n)` time and may mutate the input or allocate a copy.
- **Index-based pair loops:** Use `j` from `i + 1` through `n - 1`. It preserves the exact quadratic search but avoids suffix allocation, reducing auxiliary space to `O(1)`.
- **Use only the largest distinct value:** This is wrong when the same maximum occurs at two indices; both occurrences may form the best pair.
- **Two elements:** Exactly one pair is evaluated and returned.
- **Duplicate maximum:** Separate indices may choose equal values, as in `[1, 5, 4, 5]`.
- **All ones:** Every decremented factor is zero, so the answer is zero.
- **One factor equals zero:** Any pair containing value one has product zero, but other pairs may be larger.
- **Input order:** It has no effect on the mathematical maximum; enumeration covers all unordered pairs.
- **Distinct-index requirement:** Beginning the suffix at `i + 1` prevents self-pairing.
- **Nonnegative guarantee:** It makes zero initialization safe and ensures the two-largest shortcut is valid.
- **Slice accounting:** Python list slicing allocates; report `O(n)` peak auxiliary space for this exact source.
- **Complexity reporting:** The exact implementation is `O(n^2)` time, not the manifest's linear alternative.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. Let `n` be the length of `nums`. The inner loop examines `n - i - 1` partners for outer index `i`. The total number of products is `n(n - 1) / 2`, so arithmetic and comparisons take `O(n^2)` time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
