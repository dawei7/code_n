# Guided Example: Reconstruct Original Digits from English

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "owoztneoer"}`
- **Required output:** `"012"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `s` containing an out-of-order English representation of digits `0-9`, return *the digits in **ascending** order*.

The objective is to compute `"012"` from `{"s": "owoztneoer"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Letter order is lost, but letter counts are preserved

The input was formed by spelling some multiset of digits in English and shuffling all letters. Shuffling destroys word boundaries and order, so searching for contiguous words cannot work. It does preserve how many times each letter occurs. `Counter(s)` captures exactly this surviving information.

The goal is then to solve a small system of letter-count equations. A naive plan that repeatedly removes `"zero"`, then `"one"`, and so on is order-dependent because many digit names share letters. For example, `o` occurs in `zero`, `one`, `two`, and `four`. Consuming it prematurely could assign letters to the wrong digit.

The optimal method chooses marker letters in an elimination order. It first counts digit names that contain a globally unique letter. Once those digits are known, subtracting their contribution makes other marker letters unique among the unresolved names.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "owoztneoer"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: First recover the five digits with unique marker letters

Across the English names `zero` through `nine`:

- `z` appears only in `zero`, so `cnt[0] = counter['z']`;
- `w` appears only in `two`, so `cnt[2] = counter['w']`;
- `u` appears only in `four`, so `cnt[4] = counter['u']`;
- `x` appears only in `six`, so `cnt[6] = counter['x']`; and
- `g` appears only in `eight`, so `cnt[8] = counter['g']`.

Each marker occurs exactly once in its digit name. Therefore its frequency equals the number of copies of that digit directly; no division is needed.

For instance, if `z` occurs three times, the valid-input guarantee means exactly three copies of `zero` were present. No other digit could have supplied those `z` characters.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Use the known even digits to isolate three more names

The letter `h` appears in `three` and `eight`. Since the number of eights is already known, every remaining `h` must come from `three`:

`cnt[3] = counter['h'] - cnt[8]`.

Similarly, `f` appears in `four` and `five`. Removing the known fours isolates fives:

`cnt[5] = counter['f'] - cnt[4]`.

The letter `s` appears in `six` and `seven`. Removing the known sixes isolates sevens:

`cnt[7] = counter['s'] - cnt[6]`.

Again, each relevant name contains its marker once. The order is crucial: these formulas are valid only because counts for `8`, `4`, and `6` were established first.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"012"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "owoztneoer"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"012"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Repeatedly search for whole digit names:** Shuffling removes contiguity, and greedy word removal can misassign shared letters. It also performs avoidable repeated scans.
- **General backtracking over digit counts:** Trying combinations could eventually match letter frequencies, but the unique-marker dependency makes exponential search unnecessary.
- **Solve a full linear system:** Ten digit variables and letter equations can be handled algebraically, but the elimination order used here is that system reduced to simple integer formulas.
- **Use `n` to find one:** The name `nine` contains two `n` characters while `one` and `seven` contain one, making the equation easier to mishandle. The exact solution uses `o` after zero, two, and four are known.
- **Repeated digits:** Marker frequencies scale linearly, and string multiplication preserves every multiplicity.
- **Only one digit:** Its markers and dependent equations recover one count, and the output is the corresponding one-character digit string.
- **No occurrence of a digit:** Its formula evaluates to zero and contributes an empty piece to the join.
- **Invalid shuffled letters:** Subtractions could become negative for arbitrary input. The contract guarantees validity, so defensive rejection logic is unnecessary.
- **Ascending order:** Iterating indices `0..9` is essential; iterating a counter's arbitrary discovery order would not satisfy the output contract.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n = \lvert s \rvert$. Building `Counter(s)` takes $O(n)$ time. The ten count formulas perform constant work. Constructing the output writes one character per reconstructed digit, at most $O(n)$ characters because every digit name contains at least three letters. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
