# Guided Example: Shortest Completing Word

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"licensePlate": "1s3 PSt", "words": ["step", "steps", "stripe", "stepple"]}`
- **Required output:** `"steps"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `licensePlate` and an array of strings `words`, find the **shortest completing** word in `words`.

The objective is to compute `"steps"` from `{"licensePlate": "1s3 PSt", "words": ["step", "steps", "stripe", "stepple"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Reduce the license plate to required letter counts

Digits and spaces in `licensePlate` do not matter. Letters are case-insensitive, and repeated letters create repeated requirements.

The exact solution builds

`cnt = Counter(c.lower() for c in licensePlate if c.isalpha())`.

Each alphabetic character is converted to lowercase before counting. If the plate contains two copies of `s`, `cnt["s"]` is two; a candidate with only one `s` cannot complete it.

Under the input contract, alphabetic characters are English letters. The 26-letter alphabet keeps the count structure constant-sized.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"licensePlate": "1s3 PSt", "words": ["step", "steps", "stripe", "stepple"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Test whether a word covers the multiset

For a candidate word `w`, `t = Counter(w)` records its lowercase letter frequencies. Candidate words are already guaranteed lowercase.

The condition

`all(v <= t[c] for c, v in cnt.items())`

checks every required letter. A candidate may contain extra letters or extra copies; only shortages matter.

This is multiset containment, not ordinary set containment. Checking only whether each distinct letter appears would incorrectly accept a word with too few repetitions.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For a candidate word `w`, `t = Counter(w)` records its lower... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Keep the shortest eligible word

`ans` begins as `null`. Whenever a completing word is found, it becomes the current best.

Before counting a later word, the solution skips it when

`ans and len(w) >= len(ans)`.

If `w` is longer, it cannot improve the objective. If it has equal length, the earlier current answer must win the tie, so it also must not replace `ans`. This early skip both preserves the first-occurrence rule and avoids constructing an unnecessary counter.

Only a strictly shorter word is tested after an answer exists.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"steps"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"licensePlate": "1s3 PSt", "words": ["step", "steps", "stripe", "stepple"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"steps"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Fixed 26-element arrays:** Convert letters to :** - **Fixed 26-element arrays:** Convert letters to indices and compare counts. This avoids hash maps and has the same linear time and constant alphabet space.
- **- **Sort plate letters and candidate letters:** A :** - **Sort plate letters and candidate letters:** A two-pointer containment check can work, but sorting every word adds unnecessary logarithmic factors.
- **- **Use sets instead of counters:** This loses mul:** - **Use sets instead of counters:** This loses multiplicity and fails when a plate letter appears more than once.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(C)$. Let `C` be the total number of characters in the license plate and all words. Building the plate counter is linear in plate length. Each word that is not skipped is counted in time proportional to its length, and checking requirements examines at most 26 letters.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
