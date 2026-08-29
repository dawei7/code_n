# Guided Example: Longest Palindromic Substring

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "babad"}`
- **Required output:** `"bab"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `s`, return *the longest* *palindromic* *substring* in `s`.

The objective is to compute `"bab"` from `{"s": "babad"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Build larger palindromes from smaller inner substrings

A string is a palindrome when it reads the same from left to right and right to left. For a substring with inclusive endpoints `i` and `j`, two facts are needed:

1. the outer characters match: `s[i] == s[j]`;
2. everything between them, `s[i + 1:j]`, is itself a palindrome.

This gives the recurrence

$$
f[i][j] = (s[i] = s[j]) \land f[i+1][j-1].
$$

Here `f[i][j]` means “the contiguous substring `s[i:j+1]` is a palindrome.” The table remembers answers for inner substrings, allowing an outer substring to be classified in constant time instead of comparing all its character pairs again.

The method is dynamic programming because a state for one interval is derived from a smaller state whose answer has already been stored.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "babad"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the table starts entirely `True`

The code creates



At first this can look surprising: surely not every substring is a palindrome. Most meaningful entries are overwritten by the nested loops. The initial `true` values serve two base cases through their table positions:

- `f[i][i]` represents a one-character substring, which is always a palindrome;
- `f[i + 1][i]` represents the empty interior of a two-character substring `s[i:i+2]`, and an empty string is considered palindromic.

The second case is stored below the main diagonal, where the left boundary is greater than the right boundary. For adjacent endpoints `j = i + 1`, the recurrence reads `f[i + 1][j - 1] = f[i + 1][i]`. Leaving that entry `true` means two equal adjacent characters, such as `"bb"`, are recognized as a palindrome without a separate length-two branch.

Entries above the diagonal correspond to real substrings of length at least two. Every such entry visited by the loops is explicitly set to `false` before the matching-character test, so the broad initialization does not falsely mark an examined substring.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Choose an order that computes the inner state first

The recurrence for `f[i][j]` depends on `f[i + 1][j - 1]`. Therefore the row with the larger start index `i + 1` must already be complete before row `i` is processed.

The outer loop moves `i` backward:



It begins at `n - 2` because the final one-character state on the diagonal already has its base value. The inner loop moves `j` from `i + 1` to the end:



When the algorithm reaches `(i, j)`, the dependency `(i + 1, j - 1)` lies in the next row, which was processed during an earlier outer-loop iteration, or on/below the diagonal, where the base initialization is correct.

This ordering is essential. Scanning `i` from left to right would ask for states in row `i + 1` before that row had been computed.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"bab"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "babad"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"bab"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Manacher's algorithm:** Transform the string to unify odd and even centers, reuse mirrored palindrome radii, and expand only beyond the farthest known boundary. It achieves $O(n)$ time and $O(n)$ space, matching the manifest, but is substantially more intricate than this DP recurrence.
- **Expand around every center:** Treat each character and each gap as a possible palindrome center. It uses $O(1)$ auxiliary space and $O(n^2)$ worst-case time, avoiding the full table while remaining interview-friendly.
- **Check all substrings independently:** Testing $O(n^2)$ substrings with an $O(n)$ two-pointer palindrome check costs $O(n^3)$ in the worst case and repeats inner comparisons that DP reuses.
- **Store only recent DP rows:** Because `f[i][j]` depends on row `i + 1`, memory can be compressed with careful iteration. However, reconstructing or tracking the answer must remain explicit, and center expansion is often simpler for $O(1)$ auxiliary space.
- **One-character string:** The loops do not run, and the initialized `k = 0`, `mx = 1` returns that character.
- **Two equal characters:** The below-diagonal empty-interior state is `true`, so the pair is recognized and becomes the answer.
- **Two different characters:** Their state stays false, and the valid one-character initial answer is returned.
- **All characters equal:** Every interval is palindromic. The table still visits all $O(n^2)$ states, and the full string eventually becomes the best answer.
- **Several longest answers:** The strict update keeps whichever maximum-length palindrome was found first in this traversal order. For `"babad"`, either `"bab"` or `"aba"` is valid under the contract.
- **Odd and even lengths:** A diagonal `true` state anchors odd palindromes, while a below-diagonal `true` state anchors equal adjacent characters for even palindromes.
- **Contiguous requirement:** Every state uses a complete inclusive interval `s[i:j+1]`; the recurrence never skips interior characters, so it cannot return a subsequence.
- **Digits and letter case:** Characters are compared exactly. Digits participate like letters, and uppercase and lowercase letters are distinct.
- **Input preservation:** The string and table states are read independently; the method never changes `s`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. Let $n$ be `len(s)`.
- **Auxiliary Space Complexity:** $O(n^2)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
