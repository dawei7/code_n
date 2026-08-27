# Guided Example: Three Consecutive Odds

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"arr": [2, 6, 4, 1]}`
- **Required output:** `false`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `arr`, return `true` if there are three consecutive odd numbers in the array. Otherwise, return `false`.

The objective is to compute `false` from `{"arr": [2, 6, 4, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Track the current suffix of odd values

The property is local and sequential: three odd numbers must occupy adjacent array positions. The solution scans left to right and stores `cnt`, the number of consecutive odd values ending at the most recently processed position.

When the current value `x` is odd, it extends that suffix, so `cnt` increases by one. When `x` is even, no odd run can cross it, so `cnt` resets to zero.

As soon as `cnt == 3`, the last three processed positions are all odd and consecutive. The method returns `true` immediately.

If the scan ends without reaching three, no position served as the end of a three-odd block, so it returns `false`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"arr": [2, 6, 4, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Recognize oddness with the low bit

The expression `x & 1` inspects the least significant binary bit. Every even integer is divisible by two and ends in bit zero. Every odd integer has remainder one modulo two and ends in bit one.

In a Python conditional, zero is false and one is true. Thus `if x & 1` enters the odd branch without an explicit comparison.

The input values are positive, although Python's bitwise representation also makes this test work for negative odd integers. Only the stated positive range is needed here.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The expression `x & 1` inspects the least significant binary... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why a reset is required

Suppose the current element is even. Odd values before it and odd values after it are not consecutive because the even position lies between them.

Keeping a partial count across that boundary would invent a nonexistent block. Resetting to zero precisely states that the longest odd suffix ending at an even value has length zero.

The next odd value then begins a new run at one rather than extending the earlier separated run.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `false` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"arr": [2, 6, 4, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `false` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Check every length-three window:** Test the pa:** - **Check every length-three window:** Test the parity of positions `i`, `i+1`, and `i+2`. It is also $O(N)$ time and $O(1)$ space but repeats parity checks.
- **Multiply each triple:** An odd product implies three odd factors, but multiplication is less direct and may overflow in fixed-width settings with larger constraints.
- **Store a queue of three parities:** It works but adds unnecessary state when a streak counter is enough.
- **Array shorter than three:** The counter cannot reach three, so the answer is false.
- **Exactly three odds:** The function returns true on the last element.
- **Run longer than three:** It returns as soon as the first three have been seen.
- **Even separator:** It resets the streak completely.
- **Odd values of different magnitudes:** Only parity matters; their actual values are irrelevant.
- **All even values:** The count remains zero.
- **All odd values:** Any legal array length at least three returns true at index two.
- **Early qualifying block:** Later values are irrelevant once existence has been proven.
- **Bitwise test:** `x & 1` is equivalent to checking `x % 2 == 1` for the stated positive integers.
- **No mutation:** The scan is read-only and leaves `arr` unchanged.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be array length. In the worst case, the loop examines all $N$ elements and performs constant bitwise, arithmetic, and comparison work for each. Time is $O(N)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
