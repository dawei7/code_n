# Guided Example: Number of Different Integers in a String

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"word": "a123bc34d8ef34"}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `word` that consists of digits and lowercase English letters.

The objective is to compute `3` from `{"word": "a123bc34d8ef34"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: An integer is one maximal run of digits

Letters act as separators. Each maximal consecutive digit run represents one integer, so the solution scans the string with indices rather than actually replacing letters with spaces.

A set `s` stores one canonical string for every distinct integer encountered. Canonicalization is necessary because `"1"`, `"01"`, and `"001"` represent the same numerical value.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"word": "a123bc34d8ef34"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Skip leading zeros before capturing the run

When index `i` points to a digit, the first inner loop advances `i` while the current character is `'0'`. After that:

- `i` points to the first nonzero digit of the same run;
- or `i` points to the separator after the run;
- or `i == n` when the all-zero run reaches the string's end.

The solution sets `j = i` and advances `j` through all remaining digits. It inserts slice `word[i:j]` into the set.

For a run such as `"000123"`, the slice is `"123"`. For `"45"`, no zero is skipped and the slice remains `"45"`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why an all-zero integer becomes the empty string

If a digit run contains only zeros, the leading-zero loop consumes the entire run. Then `j == i` and `word[i:j]` is `""`.

This is intentional and correct as a set key. Every all-zero representation—`"0"`, `"00"`, or `"0000"`—becomes the same empty string, while no positive integer becomes empty. The empty string therefore acts as the canonical representation of numerical zero.

Using `"0"` instead would also be understandable, but the exact protected code uses `""` and still produces the correct distinct count.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"word": "a123bc34d8ef34"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Replace letters and split:** It is concise but creates another full string plus token lists; the pointer scan controls normalization directly.
- **Convert runs to integers:** It naturally removes leading zeros, but string normalization avoids large-integer parsing and is sufficient for equality.
- **Regular expression extraction:** It finds digit runs but adds regex machinery and still needs canonicalization.
- **Keep raw runs:** This incorrectly treats `"1"` and `"001"` as different.
- **All-zero run:** It becomes the empty-string key representing zero.
- **Several all-zero runs:** They all share one set entry and count once.
- **No digits:** No set entry is added, so the answer is zero.
- **Entire string is digits:** One run is normalized and counted once.
- **Digit at the end:** The scan reaches `n` safely and the bottom increment terminates the loop.
- **Adjacent letters:** Each is merely skipped; they do not create empty integers.
- **Repeated positive integer:** Identical canonical slices collapse in the set.
- **Different lengths after normalization:** They necessarily represent different positive integers.
- **Zero followed by nonzero digits in one run:** Leading zeros are discarded but the remaining digits stay together.
- **No signs or decimal points:** The input contract makes every digit run a nonnegative integer.
- **Input preservation:** Slices are read from `word`; the original string is unchanged.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be `len(word)`. Pointer scans cover disjoint portions of the string. Slicing and hashing a canonical run take time proportional to that run's retained length, and retained runs have total length at most $n$. Expected total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
