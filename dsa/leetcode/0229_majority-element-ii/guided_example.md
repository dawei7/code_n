# Guided Example: Majority Element II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [3, 2, 3]}`
- **Required output:** `[3]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array of size `n`, find all elements that appear more than $⌊n / 3⌋$ times.

The objective is to compute `[3]` from `{"nums": [3, 2, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: There can be at most two qualifying values

A qualifying value occurs more than $\lfloor n/3 \rfloor$ times. Three
different values cannot each occur more than one third of an array: their
combined occurrences would exceed $n$. Therefore the answer contains at most
two values.

This bound suggests keeping two candidate slots rather than a frequency map for
every distinct number. The generalized Boyer-Moore voting algorithm uses
candidates `m1` and `m2` with counters `n1` and `n2`. The first pass does not
try to preserve exact frequencies. It repeatedly cancels groups of three
different values so that any value too frequent to be completely canceled must
remain in one of the two slots.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [3, 2, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Interpret the counters as unmatched candidate votes

For each current value `m`, the exact source evaluates these cases in order:

1. If `m == m1`, increment `n1`.
2. Otherwise, if `m == m2`, increment `n2`.
3. Otherwise, if `n1 == 0`, place `m` in the first slot with count 1.
4. Otherwise, if `n2 == 0`, place `m` in the second slot with count 1.
5. Otherwise `m` differs from both active candidates, so decrement both counts.

The final case can be understood as deleting one unmatched occurrence of
`m1`, one of `m2`, and the current third distinct value `m`. Removing three
different values cannot change which original value occurs more than one third
of the total in the sense needed for candidate survival: a truly frequent
value cannot be canceled away without consuming enough nonmatching values.

When a counter reaches zero, its candidate value becomes stale and the slot may
represent a new distinct value later. No array elements are physically removed;
the counters compactly record the same cancellation effect.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For each current value `m`, the exact source evaluates these... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the branch order matters

Candidate comparisons occur before zero-count replacement. A slot whose count
is zero may still contain an old value. If the current value equals it, simply
incrementing the corresponding count reactivates that candidate. More
importantly, checking both candidate equalities before filling an empty slot
prevents the same value from occupying both slots.

The source initializes `m1 = 0` and `m2 = 1`, two different arbitrary values,
with both counts zero. These are not assumed to occur in the input. If the
first input value equals one of them, its equality branch correctly raises that
slot's count. Otherwise an empty slot is replaced. Because replacement occurs
only after confirming the new value differs from both stored candidates, `m1`
and `m2` remain distinct.

Using concrete initial values is safe because the second pass verifies real
frequency. An unused sentinel cannot enter the answer merely by remaining in a
candidate variable.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[3]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [3, 2, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[3]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Frequency dictionary:** Count every value, the:** - **Frequency dictionary:** Count every value, then filter counts above $\lfloor n/3\rfloor$. It is simpler but uses $O(n)$ space in the all-distinct case, missing the constant-space follow-up.
- **Sorting:** Equal values become contiguous, allowing run counts in $O(n\log n)$ time. It may mutate the input or require a copy and does not improve on voting.
- **General threshold $n/k$:** Keep at most $k-1$ candidates, cancel one vote from all when a new distinct value finds every slot occupied, then verify. This solution is the $k=3$ case.
- **One element:** Since the threshold is `0`, its real count 1 qualifies. One initialized candidate slot is activated and verification returns that value.
- **Two different elements:** The threshold is also `0`, so both occur more than it and both correctly survive verification.
- **Exactly one-third frequency:** Verification uses strict greater-than and excludes a candidate occurring only `len(nums) // 3` times.
- **No qualifying element:** Candidates may still exist after voting, but both exact counts fail and the result is empty.
- **Two qualifying elements:** Both fit the mathematical maximum and survive in separate slots.
- **Initial values 0 and 1 absent from input:** Their zero counts make the slots replaceable, and final verification prevents them from appearing spuriously.
- **Initial values 0 or 1 present:** Equality increments the relevant zero-count slot, which is equivalent to selecting that value as a candidate.
- **Negative and large integers:** Only equality and counting are used, so numeric range and sign do not affect the algorithm.
- **Input preservation:** Voting changes only local candidates and counters; `nums` remains unchanged.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be `len(nums)`. The voting pass processes each element once in $O(n)$
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
