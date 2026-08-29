# Guided Example: Minimum Number of Keypresses

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "apple"}`
- **Required output:** `5`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You have a keypad with `9` buttons, numbered from `1` to `9`, each mapped to lowercase English letters. You can choose which characters each button is matched to as long as:

The objective is to compute `5` from `{"s": "apple"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Separate letter frequency from keypad placement

Once a letter is assigned to a button position, every occurrence of that letter has the same cost. A first-position letter costs one press per occurrence, a second-position letter costs two, and a third-position letter costs three.

The physical button number does not affect cost. First position on button one costs the same as first position on button nine. Therefore, the available placement costs form a multiset:

- nine slots cost one press each;
- nine slots cost two presses each;
- nine slots cost three presses each.

There are 27 slots for 26 lowercase letters, so every letter can be assigned while leaving one slot unused. The optimization is solely about matching letter frequencies to these costs.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "apple"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Count how often each letter matters

`Counter(s)` builds a mapping from every character that occurs in `s` to its frequency. If a letter occurs `x` times and is assigned to a position costing `k` presses, its contribution to the total is `kx`.

Letters absent from `s` do not appear in the counter. That is safe even though all 26 letters must be mapped: absent letters have frequency zero and can fill any remaining keypad slots without changing the cost of typing `s`. The algorithm only needs to optimize positions for positive-frequency letters.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Give cheap positions to frequent letters

The frequencies are sorted in descending order. The first nine receive multiplier one, the next nine receive multiplier two, and any remaining frequencies receive multiplier three.

This greedy order follows an exchange argument. Suppose two letters have frequencies `a \ge b`, but the more frequent letter is assigned a more expensive cost `q` while the less frequent letter has cheaper cost `p`, with `p < q`. Their current contribution is

$$
aq + bp.
$$

Swapping their placements gives

$$
ap + bq.
$$

The current cost minus the swapped cost is

$$
(a-b)(q-p) \ge 0.
$$

Therefore, placing the more frequent letter in the cheaper slot never makes the answer worse and makes it strictly better when both inequalities are strict. Repeatedly removing such inversions produces the descending-frequency, ascending-cost assignment used by the solution.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `5` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "apple"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `5` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Explicitly construct the keypad:** It can realize the same greedy assignment, but button identities are irrelevant when only total cost is requested.
- **Try all letter mappings:** There are far too many permutations; the exchange argument removes the need to search assignments.
- **Alphabet-sized frequency array:** A 26-entry list can replace `Counter` and gives the same bounds.
- **Ascending frequency sort:** It would place rare letters in cheap positions and frequent letters in expensive ones, maximizing the wrong tendency.
- **Priority queue:** Repeatedly taking the largest frequency works but is more machinery than sorting 26 values once.
- **At most nine distinct used letters:** Every used letter receives a one-press slot, so the answer equals `len(s)`.
- **Ten distinct used letters:** Nine use cost one and the least frequent one uses cost two.
- **All 26 letters used:** The tier sizes are nine, nine, and eight; the unused 27th slot has no effect.
- **Absent letters:** They can occupy leftover expensive or unused positions because their typing contribution is zero.
- **Equal frequencies:** Swapping their positions leaves the total unchanged, so any order among ties is optimal.
- **One overwhelmingly frequent letter:** Descending sorting guarantees it receives a one-press position.
- **Repeated string order:** Only frequency matters; rearranging `s` without changing counts does not change the optimum.
- **Tier boundary after nine:** `k` increases only after the ninth contribution, preserving all nine one-press slots.
- **Tier boundary after eighteen:** Entries nineteen onward correctly receive multiplier three.
- **Capacity guarantee:** Nine buttons times three characters gives 27 positions, enough for the 26-letter alphabet.
- **Input preservation:** Counting and sorting derived frequencies do not alter `s`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the length of `s` and `A = 26` be the alphabet size. Building the counter takes `O(n)` time. Sorting at most `A` frequencies takes `O(A \log A)`, and the final loop takes `O(A)`. Because `A` is fixed, total time is `O(n)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
