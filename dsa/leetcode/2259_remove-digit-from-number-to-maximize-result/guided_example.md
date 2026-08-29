# Guided Example: Remove Digit From Number to Maximize Result

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"number": "123", "digit": "3"}`
- **Required output:** `"12"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `number` representing a **positive integer** and a character `digit`.

The objective is to compute `"12"` from `{"number": "123", "digit": "3"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Enumerate exactly the legal choices

The operation must remove exactly one occurrence of the character `digit` from `number`. The solution scans `number` with `enumerate`, so each loop item provides both the position `i` and the character `d` stored there. The condition `if d == digit` filters the scan to precisely the positions that are legal to delete.

For every legal position, the expression

`number[:i] + number[i + 1:]`

constructs the result of deleting that one character. The first slice contains every character before position `i`. The second starts immediately after `i` and contains all later characters. Joining them omits exactly `number[i]` and preserves the relative order of every other digit. It cannot accidentally remove two occurrences, reorder digits, or substitute a different character.

The problem guarantees that `digit` appears in `number` at least once. Therefore, the generator passed to `max` always produces at least one candidate, and `max` is never applied to an empty sequence.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"number": "123", "digit": "3"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why comparing the candidates as strings is valid

Python's `max` compares strings lexicographically. At first glance, that might seem different from choosing the greatest integer, but all candidates have exactly the same length: each begins with the same length-`n` input and removes exactly one character. For two equal-length decimal strings, lexicographic order and numeric order agree.

To see why, consider the first position where two candidates differ. Every earlier digit is equal, so those shared positions contribute the same amount to both numbers. At the first differing position, the candidate with the larger digit is numerically larger because that digit has a higher place value than all later positions combined can overturn. Lexicographic comparison makes exactly the same decision at that first difference.

The input consists of decimal digits from `'1'` through `'9'`, so removing a character cannot create an ambiguous leading-zero representation. Even if zero were present, equal length would still be the central comparison fact, but the stated digit range makes the representation especially direct.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: How deleting one copy changes the remaining alignment

When occurrence `i` is removed, every digit before `i` remains in the same position and every digit after it shifts one place to the left. Thus, different deletion choices often share a long prefix. The first point at which their retained sequences differ determines which candidate is larger.

For example, suppose two copies of the target occur at positions `i < j`. Deleting the earlier occurrence causes `number[i + 1]` to move into position `i`. Deleting the later occurrence leaves `digit` at position `i`. If the character immediately after the earlier occurrence is greater than `digit`, deleting the earlier copy produces a larger digit at the first differing position and must be better. If it is smaller, preserving the earlier `digit` is better. This observation leads to a greedy alternative, but the exact implementation does not need to encode or prove all such cases: it materializes every legal result and asks `max` to compare them.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"12"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"number": "123", "digit": "3"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"12"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Greedy first improving deletion:** Scan target occurrences from left to right and remove the first one whose following digit is larger than `digit`; if none exists, remove the last occurrence. This can run in `O(n)` time, but it is an alternative to the submitted enumeration, not what the exact solution executes.
- **Build a list of every candidate:** A list comprehension would make the same choice but retain all generated strings, increasing peak space to `O(kn)`.
- **Convert every candidate to an integer:** Numeric conversion is unnecessary because all candidates have equal length. It adds work and obscures the useful ordering argument.
- **Delete a globally smallest digit:** The removable character is fixed by `digit`, and position affects the remaining place values. Choosing by digit magnitude alone does not solve the problem.
- **Only one target occurrence:** The generator yields one candidate, so `max` returns the uniquely legal result.
- **Target at the first position:** `number[:0]` is the empty string, and concatenating the remaining suffix correctly removes the first character.
- **Target at the final position:** `number[i + 1:]` is empty, and the prefix is the complete result.
- **Adjacent target occurrences:** Two deletion positions may produce identical strings. Duplicate candidates are harmless.
- **Every character equals the target:** Every deletion produces the same length-`n - 1` string, which is necessarily the answer.
- **Long common prefixes:** String comparison may inspect nearly the entire candidate, which is included in the `O(kn)` time bound.
- **Guaranteed occurrence:** The source guarantee is essential to this concise use of `max`; without it, the generator would be empty and Python would raise `ValueError`.
- **Exactly one deletion:** Returning the original number is never considered, even when it would be numerically larger due to having an extra digit, because it is not a legal result.
- **String immutability:** The input is not modified. Every slice and concatenation creates a new string.
- **Lexicographic ordering:** It is safe specifically because all candidates contain exactly `n - 1` decimal digits. Comparing arbitrary unequal-length numeric strings lexicographically would not generally be valid.
- **No leading-zero complication:** The stated characters range from `'1'` to `'9'`, so every candidate remains an ordinary length-`n - 1` decimal representation.
- **Small input bound:** With `n \le 100`, the enumeration's quadratic worst case is modest, which supports the solution's preference for transparency.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n + kn)$. Let `n` be the length of `number` and let `k` be the number of occurrences of `digit`. The scan itself visits `n` characters. For each of the `k` matching positions, two slices and one concatenation construct a length-`n - 1` candidate, taking `O(n)` time. Comparing that candidate with the current maximum can also examine up to `O(n)` characters when the strings share a long prefix.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
