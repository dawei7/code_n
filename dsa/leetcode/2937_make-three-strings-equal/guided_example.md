# Guided Example: Make Three Strings Equal

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s1": "abc", "s2": "abb", "s3": "ab"}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given three strings: `s1`, `s2`, and `s3`. In one operation you can choose one of these strings and delete its **rightmost** character. Note that you **cannot** completely empty a string.

The objective is to compute `2` from `{"s1": "abc", "s2": "abb", "s3": "ab"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Total original length

Variable `s` stores `len(s1) + len(s2) + len(s3)`. Once the common-prefix length is known, `s - 3 * L` computes the exact number of removed suffix characters.

Each deletion removes one character from exactly one string, so this arithmetic is both a lower bound and an achievable operation count.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s1": "abc", "s2": "abb", "s3": "ab"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Scan only while all three have characters

`n = min(len(s1), len(s2), len(s3))` is the greatest possible common-prefix length. The loop checks positions `0..n-1`.

At index $i$, condition

`s1[i] == s2[i] == s3[i]`

tests whether all three prefixes can extend through this character.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `n = min(len(s1), len(s2), len(s3))` is the greatest possibl... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: First mismatch determines the answer

Suppose the first mismatch occurs at index $i$.

- Characters at positions $0$ through $i-1$ match in all strings, so a common prefix of length $i$ exists.
- Any prefix of length $i+1$ includes the mismatching characters, so no longer equal result is possible.

Thus $L=i$. If $i>0$, the source returns `s - 3 * i`.

If $i=0$, the strings share no first character. Their only common prefix is empty, but completely emptying a string is forbidden. The source returns `-1`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s1": "abc", "s2": "abb", "s3": "ab"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Repeatedly delete from the longest string:** S:** - **Repeatedly delete from the longest string:** Simulation can eventually work but obscures the fact that the target must be a common prefix and may perform unnecessary string construction.
- **Generate all prefixes:** Comparing prefix sets uses extra time and space; the first mismatch identifies the longest one directly.
- **First characters differ:** Returning the empty string is illegal, so the correct answer is `-1`.
- **All strings already equal:** $L$ equals every length and the formula returns zero.
- **One string is a prefix of both others:** Keep it and delete the two remaining suffixes.
- **Shortest string length one:** If all first characters agree, that single character is a valid target; otherwise equality is impossible.
- **Mismatch after a long prefix:** Only suffix characters at and after the mismatch are deleted. Earlier matching characters remain.
- **No left deletions:** A common substring that is not a prefix is unreachable and must not be considered.
- **Operation count:** Deleting $q$ characters always costs exactly $q$ operations because each operation removes only one rightmost character.
- **Lowercase alphabet:** Character comparisons need no normalization; case or Unicode equivalence is outside the contract.
- **Deleting from only one string may be insufficient:** Equality requires all three final lengths and contents to match. The formula separately accounts for each suffix, even when two strings already have the same length.
- **Why operations commute:** Deleting a suffix character from one string does not affect the available prefixes of the others. Once the target prefix is fixed, deletions may occur in any order and always total the same count.
- **A mismatch cannot be repaired:** Rightmost deletion never changes characters before the new endpoint. If position $i$ differs while retained, deleting later characters cannot alter it; the common result must end before $i$.
- **Different total lengths:** Total `s` may be much larger than $3L$, but every extra character is necessarily outside the shared prefix and must be removed exactly once.
- **Impossible versus costly:** `-1` is used only when the shared prefix length is zero. Any positive common first character gives a valid result, even if nearly every other character must be deleted.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(L)$. Let $L=\min(|s_1|,|s_2|,|s_3|)$. At most $L$ positions are compared, with constant work per position. Time complexity is $O(L)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
