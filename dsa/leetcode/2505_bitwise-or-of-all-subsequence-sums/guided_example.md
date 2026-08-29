# Guided Example: Bitwise OR of All Subsequence Sums

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, 1, 0, 3]}`
- **Required output:** `7`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums`, return *the value of the bitwise ***OR*** of the sum of all possible **subsequences** in the array*.

The objective is to compute `7` from `{"nums": [2, 1, 0, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Think of each set bit as a power-of-two unit

Every nonnegative integer is a sum of powers of two. If bit `i` is set in a number, that number contributes one unit worth $2^i$ whenever it is selected.

When adding selected numbers, two units of $2^i$ can carry into one unit of $2^{i+1}$. The question asks which bit positions can be set in at least one subsequence sum, because bitwise OR keeps a bit exactly when some sum has that bit.

The solution counts available units at each bit and propagates all possible pairs upward.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, 1, 0, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Count original set-bit occurrences

`cnt` has 64 entries. For every input value `v`, the inner loop examines bit positions 0 through 30. The constraint `v<=10^9<2^{30}` means these positions cover every possible original set bit.

The test

`(v>>i)&1`

shifts bit `i` into the least significant position and isolates it. When the result is one, `cnt[i]` increases.

After this pass, `cnt[i]` is the number of input values that directly contain a $2^i$ contribution.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: A bit is possible whenever a unit reaches it

The second loop processes bit positions from low to high. If `cnt[i]` is positive, the algorithm sets bit `i` in `ans`:

`ans |= 1<<i`.

The underlying subset-sum bit lemma is that for nonnegative integers, a bit appears in the OR of all subset sums exactly when at least one original or carried unit can reach that position. Direct set bits clearly qualify by choosing the one-element subsequence containing that number. Pairs of lower units can create carries in suitable selections, making higher bits attainable as well.

The low-to-high count propagation summarizes those possibilities without enumerating subsets.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `7` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, 1, 0, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `7` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **OR elements and running prefix sums:** Another known linear characterization captures direct bits and carries, but it follows a different implementation.
- **Enumerate subsequences:** There are $2^n$ choices and this is infeasible.
- **All zeroes:** No bit units exist, so the answer remains zero.
- **One number:** Its singleton sum makes the answer equal that number.
- **Two equal low bits:** The lower bit and their carried higher bit can both appear across different subsequences.
- **Empty subsequence:** Its zero sum contributes no bits.
- **Nonnegative values:** The unit-and-carry interpretation relies on ordinary unsigned-style binary addition without negative sign extension.
- **Original-bit bound:** Positions 0 through 30 cover every value up to $10^9$.
- **Carry capacity:** Sixty-four slots safely exceed the maximum possible sum width.
- **Low-to-high order:** Carries must be processed again at subsequent bit positions.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. The first pass checks 31 fixed bit positions for each of $n$ numbers, taking $O(31n)=O(n)$ time. The carry pass has 63 iterations, which is constant. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
