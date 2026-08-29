# Guided Example: Largest 3-Same-Digit Number in String

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"num": "6777133339"}`
- **Required output:** `"777"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `num` representing a large integer. An integer is **good** if it meets the following conditions:

The objective is to compute `"777"` from `{"num": "6777133339"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: There are only ten possible good strings

A good integer must contain exactly three copies of one decimal digit. Therefore, regardless of how long `num` is, every possible answer belongs to this fixed list:

`"999"`, `"888"`, `"777"`, ..., `"111"`, `"000"`.

The solution exploits that tiny answer space directly. It does not need to parse the entire input as an integer, construct every length-three window, or retain every match. It tests these ten candidates from largest to smallest and returns the first one present as a substring.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"num": "6777133339"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Generate candidates in descending order

The range `range(9, -1, -1)` begins at nine, stops before minus one, and moves by minus one. Its values are exactly nine through zero in descending order.

For a current digit `i`, `str(i)` converts it to its one-character decimal representation. Multiplying that string by three forms the corresponding good candidate. The assignment expression

`s := str(i) * 3`

both constructs the candidate and stores it in `s` for the immediate return.

The containment test `s in num` asks whether that exact three-character string occurs contiguously anywhere in `num`. Contiguity matters because the definition requires a substring, not merely three appearances at unrelated indices.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the first match is the maximum

Every candidate contains the same number of characters. Among equal-length decimal strings, the one with the greater repeated digit is the greater integer. For example, every occurrence of `"777"` is greater than `"666"`, and `"000"` is smaller than every other good string.

The loop examines candidates strictly in this numeric order. If it returns `s` at digit `i`, every larger repeated-digit candidate has already been tested and found absent. The returned string is present and hence valid, while no larger valid answer exists. That makes it the maximum good integer.

This descending-search argument means the method may stop immediately. Once `"777"` is found, the presence of `"333"` or any smaller candidate cannot change the answer.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"777"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"num": "6777133339"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"777"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Single pass over length-three windows:** Check `num[i] == num[i + 1] == num[i + 2]` and retain the largest matching character. This also takes `O(n)` time and `O(1)` space, but it is not the exact descending-candidate implementation.
- **Run-length counting:** Track the current digit and consecutive-run length; whenever a run reaches three, update the best digit. This is useful if the required repetition length varies.
- **Convert windows to integers:** Numeric conversion is unnecessary and mishandles the required representation of `"000"` unless special care is added.
- **Sort all matching windows:** Collecting and sorting matches uses extra space and time even though only ten different answers are possible.
- **Exactly three input digits:** The sole length-three window is found if all characters match; otherwise, the result is empty.
- **Run longer than three:** A run such as `"7777"` contains overlapping `"777"` substrings, and the containment test correctly recognizes the candidate once.
- **Several occurrences of one candidate:** Presence is all that matters; repeated matches do not change the maximum.
- **Several different good candidates:** Descending iteration returns the largest digit's candidate regardless of where it occurs.
- **Only zeros form a match:** `"000"` is returned as a three-character string, preserving its leading zeros.
- **No good substring:** All ten containment checks fail and the method returns `""`.
- **Digits are characters:** Character preservation avoids arithmetic overflow even though `num` may represent a large integer.
- **Substring rather than subsequence:** `s in num` requires adjacent characters, so separated copies of a digit are never accepted.
- **Loop bounds:** Stopping before minus one is what includes zero while excluding invalid negative candidates.
- **Early return:** It is valid only because candidates are checked from nine downward; ascending order would return the minimum instead.
- **Input preservation:** String searches are read-only and create only constant-size candidate strings.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the length of `num`. Each containment operation searches for a pattern of fixed length three and takes `O(n)` time in the worst case. There are exactly ten candidates, so the total is `O(10n) = O(n)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
