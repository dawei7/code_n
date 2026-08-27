# Guided Example: Lexicographically Smallest Permutation Greater Than Target

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "abc", "target": "bba"}`
- **Required output:** `"bca"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two strings `s` and `target`, both having length `n`, consisting of lowercase English letters.

The objective is to compute `"bca"` from `{"s": "abc", "target": "bba"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Lexicographic order is decided at the first differing position

Every answer must use exactly the same multiset of letters as `s`, but its order may change. To be strictly greater than `target`, the result must have some first position where it differs from `target`, and its letter at that position must be larger. Everything after that decisive position can then be made as small as possible.

This leads to the structure of the desired result:

1. Match a prefix of `target` exactly.
2. At one pivot position, use an available letter strictly larger than `target[pivot]`.
3. Arrange every remaining letter in ascending order.

For a fixed pivot and fixed matching prefix, the smallest valid pivot letter is best. Once the pivot is larger, the suffix cannot affect the greater-than relationship, so sorting the suffix ascending makes the complete result lexicographically smallest for that pivot.

The only difficult part is selecting the pivot. A later pivot preserves a longer prefix equal to `target` and is therefore lexicographically smaller than any solution forced to differ earlier. The solution first tries to push the exact match as far right as possible, then backtracks only when no larger pivot letter is available.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "abc", "target": "bba"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Represent the unused letters by frequencies

The array `counts` has 26 entries. Entry zero counts `'a'`, entry one counts `'b'`, and so forth. Scanning `s` fills this array, preserving duplicate multiplicities exactly.

The list `prefix` contains letters already committed to equal the corresponding positions of `target`. Whenever a letter is appended to `prefix`, one copy is removed from `counts`. Therefore, at every point:

- `prefix` uses real letters from `s`.
- `counts` describes exactly the letters of `s` that remain unused.
- The concatenation of `prefix` and all letters represented by `counts` has the same multiset as `s`.

This invariant prevents both losing a duplicate and using a letter too many times.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The array `counts` has 26 entries.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Match the target for as long as the multiset allows

Starting at `position = 0`, the first loop examines `target[position]`. If an unused copy exists, it appends that character to `prefix`, decrements its count, and moves to the next position.

Matching the target character is always the smallest possible choice that does not make the result smaller at this position. Choosing a smaller character would make the whole permutation lexicographically smaller than `target` immediately and could never be repaired by a later suffix. Choosing a larger character would make a valid pivot now, but if an exact match can be continued and a valid pivot can be placed later, that later difference produces a smaller overall answer.

The loop stops in one of two situations:

- `position < n` and no unused copy of `target[position]` exists.
- `position == n`, meaning the letters of `s` can reproduce all of `target` exactly.

In the second situation, equality is not enough because the result must be strictly greater. The algorithm must backtrack to change some earlier matched letter into a larger one.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"bca"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "abc", "target": "bba"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"bca"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Generate and sort all distinct permutations:**:** - **Generate and sort all distinct permutations:** This directly follows the definition but can require up to $n!$ candidates and is infeasible even far below `n = 300`. Frequency-guided pivot selection constructs only the single best candidate.
- **Take the next permutation of a sorted copy of `s` repeatedly:** Advancing until passing `target` can still traverse exponentially many permutations. The exact method jumps directly to the latest feasible pivot.
- **Choose a larger letter at the earliest opportunity:** That makes a valid answer but not necessarily the smallest one. Preserving an equal prefix for more positions has higher lexicographic priority than optimizing any suffix.
- **Use the largest feasible pivot letter:** Once the pivot position is fixed, a larger chosen letter only makes the result worse. The ascending alphabet scan correctly takes the first available greater letter.
- **Leave the suffix in original `s` order:** The original positions are irrelevant because any permutation is allowed. Sorting the remaining multiset ascending gives the minimum suffix.
- **Duplicate letters:** Counts preserve multiplicity, and consuming or restoring one copy changes only one array entry. A target character can be matched only as many times as `s` supplies it.
- **`s` can equal `target` exactly:** Equality is not strictly greater. Reaching `position == n` causes backtracking, which searches for the nearest possible increase; if none exists, the result is empty.
- **Target is smaller at the first position:** If the smallest available letter greater than `target[0]` can be chosen immediately, the remaining letters are sorted and returned without unnecessary matching.
- **All permutations are at most the target:** Backtracking eventually reaches position zero, finds no greater available letter, and returns `""`. For example, if `target` is the greatest permutation of `s`, no strict successor exists.
- **Target contains a letter unavailable during matching:** This is not automatically failure. An available larger letter at that position can create the answer, as `"eelt"` versus `"code"` demonstrates.
- **A smaller available letter at the failed position:** Choosing it would make the result smaller than `target` at the first difference, so the code correctly ignores it and either chooses a greater letter or backtracks.
- **Length one:** The sole permutation is `s`. The algorithm returns it only if its character is greater than `target`; equality or a smaller character yields `""`.
- **Restoring on backtrack:** Without adding the popped target character back to `counts`, later pivot attempts would operate on an incomplete multiset and could falsely report failure or build a non-permutation.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the common length. Building `counts` takes $O(n)$ time. The forward matching phase advances `position` at most `n` times. During backtracking, each previously matched position is popped at most once. At every attempted pivot, the code scans at most 26 alphabet entries, a fixed constant, so all pivot searches take $O(26n)=O(n)$ time.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
