# Guided Example: Longest Almost-Palindromic Substring

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "abca"}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s` consisting of lowercase English letters.

The objective is to compute `4` from `{"s": "abca"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Deleting one character leaves an odd- or even-centered palindrome

If a substring becomes a palindrome after one deletion, the remaining characters have a palindrome center. That center is either:

- one character, for an odd-length palindrome;
- a gap between two characters, for an even-length palindrome.

The source tries both center types at every index:

- `f(i, i)` for an odd center;
- `f(i, i + 1)` for an even center.

This covers the center of every possible palindrome remaining after deletion.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "abca"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Expand the palindrome before spending the deletion

Inside `f(l, r)`, the first loop expands while both indices are in bounds and `s[l] == s[r]`.

These matching pairs require no deletion. When the loop stops, one of two situations holds:

- `l` or `r` crossed a string boundary;
- `s[l] != s[r]` is the first mismatch around this center.

The indices `l + 1` through `r - 1` form the largest ordinary palindrome reached from that center before any deletion is used.

Spending the one deletion earlier than the first mismatch is unnecessary: all earlier mirrored characters already match. Keeping them can only make the candidate longer.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: At the first mismatch, only two repairs are possible

When `s[l] != s[r]`, a palindrome spanning both sides cannot keep both mismatched characters. Exactly one must be deleted.

Delete the left mismatch `s[l]`. The next comparison becomes `s[l - 1]` against `s[r]`. The source initializes:

`l1, r1 = l - 1, r`.

Delete the right mismatch `s[r]`. The next comparison becomes `s[l]` against `s[r + 1]`:

`l2, r2 = l, r + 1`.

Each branch then expands normally while its mirrored characters agree. No second mismatch can be repaired because the one deletion has already been spent.

Trying both sides is essential. In `"abca"` around center `b`, the first matching core is `"b"` and the mismatch is `a` versus `c`. Deleting `c` allows the outer `a` characters to match and yields the full length 4. Deleting the other side does not.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "abca"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Enumerate substrings and deletions:** Testing every substring and every possible removed position can cost $O(N^4)$ with direct palindrome checks.
- **Interval dynamic programming:** Track whether each substring can become a palindrome with one deletion. It can achieve $O(N^2)$ time but uses $O(N^2)$ space.
- **Rolling hashes plus binary search:** Hash comparisons can jump across matching mirrored ranges, but collision handling and deletion alignment make it substantially more complex.
- **String already palindromic:** It still qualifies because one central character can be deleted while preserving a palindrome.
- **Length two:** Deleting either character leaves a one-character palindrome, so every length-two substring qualifies.
- **All characters equal:** The entire string is returned.
- **First mismatch near a boundary:** One branch may have no extra matched pair but still represents deleting the boundary character and keeping the palindrome core.
- **Delete left versus right:** Both must be tried; one-sided greedy deletion can miss the optimum.
- **Exactly one mismatch repair:** After a branch begins, a second mismatch stops expansion because no deletion remains.
- **Odd and even centers:** Trying only one parity would miss valid remaining palindromes of the other parity.
- **Length cap:** `min(n, ...)` prevents boundary arithmetic from claiming a substring longer than the input.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N^2)$. There are $N$ odd centers and $N$ attempted even centers. For one center, the initial expansion and two deletion branches can each traverse $O(N)$ characters. Total worst-case time is $O(N^2)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
