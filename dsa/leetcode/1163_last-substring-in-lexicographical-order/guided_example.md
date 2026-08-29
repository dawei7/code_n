# Guided Example: Last Substring in Lexicographical Order

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "abab"}`
- **Required output:** `"bab"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `s`, return *the last substring of* `s` *in lexicographical order*.

The objective is to compute `"bab"` from `{"s": "abab"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The maximum substring must extend to the end

Consider any substring that starts at index `p` but stops before the end of `s`. The suffix `s[p:]` has that substring as a prefix and then contains additional characters. Under lexicographic ordering, a string is smaller than a longer string when it is a proper prefix of the longer one.

Therefore, extending a candidate substring to the end never makes it smaller and makes it strictly larger when the original stopped early. The answer must be one of the `n` suffixes of `s`.

The problem is now to find the lexicographically greatest suffix without constructing and sorting all suffix strings.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "abab"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Maintain two suffix starts and one matched length

`i` is the start of the best surviving candidate, `j` is the start of another suffix being compared with it, and `k` is the number of equal characters already matched:

`s[i : i + k] == s[j : j + k]`.

Initially, suffix zero is the candidate, suffix one is the challenger, and no characters have been compared, so `i = 0`, `j = 1`, and `k = 0`.

The two starts remain distinct, with the challenger arranged after the candidate search boundary. The loop continues while `j + k < len(s)`, meaning the challenger still has a character available at the comparison offset.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Advance across a shared prefix

If `s[i + k] == s[j + k]`, those characters do not decide lexicographic order. The code increments `k` and compares the next pair.

No pointer is eliminated until the first differing character is found or the challenger reaches the end.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"bab"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "abab"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"bab"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Generate and sort all suffixes:** Constructing suffix strings can use quadratic total characters, and comparison sorting adds substantial time.
- **Compare every suffix against the current best directly:** Repeated long common prefixes can lead to `O(n^2)` character comparisons.
- **Suffix array:** A suffix array can identify the lexicographically last suffix, but general construction machinery and extra storage are unnecessary for this single maximum query.
- **Booth or Duval-style algorithms:** Related linear string algorithms use similar block elimination. The exact two-pointer form is specialized to the maximum suffix.
- **One-character string:** The loop never runs and the complete string is returned.
- **All characters equal:** The later suffix remains a shorter prefix of the first suffix, so index zero wins.
- **Strictly increasing characters:** Each larger character replaces the candidate, and the answer begins at the final character.
- **Repeated long prefixes:** `k` skips through them, while block jumps preserve linear amortized work.
- **Candidate and challenger must differ:** When advancing `i` crosses `j`, resetting `j = i + 1` avoids comparing a suffix with itself.
- **Proper-prefix rule:** If the challenger ends after matching, the longer candidate is lexicographically greater.
- **Returned slice allocation:** Python materializes `s[i:]`. It is output storage rather than search state, but complexity discussions should state the convention.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be `len(s)`. Equal-character comparisons increase `k`. At a mismatch, one of the starts advances by `k + 1`, skipping the block just compared, and `k` resets. Across the whole algorithm, these pointer advances and matched offsets account for only `O(n)` amortized comparisons. The search time is `O(n)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
