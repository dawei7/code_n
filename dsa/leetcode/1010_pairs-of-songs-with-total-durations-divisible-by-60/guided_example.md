# Guided Example: Pairs of Songs With Total Durations Divisible by 60

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"time": [30, 20, 150, 100, 40]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a list of songs where the $i^{\text{th}}$ song has a duration of $\text{time}[i]$ seconds.

The objective is to compute `3` from `{"time": [30, 20, 150, 100, 40]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Only remainders modulo sixty matter

Write a duration as `60q + r`, where `r` is between zero and fifty-nine. Complete groups of sixty do not affect whether a sum is divisible by sixty.

For two durations with remainders `x` and `y`:

`(x + y) % 60 == 0`.

The needed complement of `x` is:

`y = (60 - x) % 60`.

The final modulo handles `x = 0` correctly: its complement is zero rather than sixty, since valid stored remainders stop at fifty-nine.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"time": [30, 20, 150, 100, 40]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Count complementary earlier songs online

`cnt[r]` stores how many already-processed songs have remainder `r`. When the current song arrives:

1. reduce it with `x %= 60`;
2. calculate complementary remainder `y`;
3. add `cnt[y]` to the answer;
4. increment `cnt[x]`.

Every earlier song with remainder `y` forms a valid pair with the current song, so all can be counted at once.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why lookup happens before increment

The required pairs satisfy `i < j`. During a left-to-right scan, the current song acts as index `j` and the counter contains only possible indices `i`.

Incrementing after the lookup prevents pairing a song with itself. It also means each unordered index pair is counted exactly once—when its later endpoint is processed.

No division by two or duplicate correction is required.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"time": [30, 20, 150, 100, 40]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Nested pair loops:** Directly test every `i < j` pair in `O(N^2)` time.
- **Frequency array after a separate counting pass:** Count all sixty remainders, then combine complementary groups using products and combinations. It is also linear but requires careful handling of remainder zero and thirty.
- **Set of remainders:** Presence alone loses multiplicity and cannot count index pairs.
- **Remainder zero:** Its complement formula maps back to zero, not sixty.
- **Remainder thirty:** Two thirty-remainder songs sum to sixty modulo sixty.
- **Repeated equal durations:** Different indices form distinct pairs and are preserved by frequencies.
- **Only one song:** No earlier complement exists, so the answer remains zero.
- **All songs divisible by sixty:** The result is `N(N - 1)/2`, accumulated online as `0 + 1 + ... + N - 1`.
- **Durations above sixty:** Modulo reduction retains all divisibility information.
- **Input preservation:** The loop rebinds local `x` to its remainder but never changes `time`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let `N` be the number of songs.
- **Auxiliary Space Complexity:** $O(60)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
