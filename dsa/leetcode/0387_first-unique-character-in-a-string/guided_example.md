# Guided Example: First Unique Character in a String

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "leetcode"}`
- **Required output:** `0`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `s`, find the **first** non-repeating character in it and return its index. If it **does not** exist, return `-1`.

The objective is to compute `0` from `{"s": "leetcode"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Two separate facts determine the answer

A character qualifies only when both of these statements are true:

1. it occurs exactly once in the entire string;
2. its index is smaller than the index of every other character that also occurs exactly once.

The first fact is global. When the scan sees a character near the beginning, it cannot know that the character is unique until it knows whether the same character appears later. The second fact depends on original position, so merely knowing which character frequencies equal one is not enough; the algorithm must still respect the string’s left-to-right order.

The exact solution cleanly separates these responsibilities into two linear passes. `Counter(s)` computes the total frequency of every character. Then `enumerate(s)` visits the original positions from smallest to largest and returns the first index whose character has count one.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "leetcode"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: First pass: count total occurrences

`cnt = Counter(s)` builds a mapping from each character to the number of positions containing it. If `s = "loveleetcode"`, for example, the counter records that `l` appears twice, `o` appears twice, `v` appears once, and so on.

The exact order in which those dictionary entries are stored is irrelevant. This phase answers only the global uniqueness question. For any index `i`, the character `s[i]` is non-repeating if and only if `cnt[s[i]] == 1`.

Counting before choosing an answer prevents a common one-pass mistake. Seeing the first `l` in `"leetcode"` does not by itself prove that `l` is unique; only a complete count can establish that no later `l` exists. Here, the counter shows `l` has total frequency one, so it qualifies. In `"loveleetcode"`, the first `l` does not qualify because another `l` occurs later.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `cnt = Counter(s)` builds a mapping from each character to t... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Second pass: recover the earliest qualifying position

The loop `for i, c in enumerate(s)` produces each index `i` and its character `c` in increasing index order. The test `cnt[c] == 1` asks whether that character occurs at exactly one position in the whole string.

As soon as the test succeeds, the method returns `i`. This early return is safe because every smaller index was already examined and failed the same test. Therefore no earlier non-repeating character exists.

If the loop ends, every character occurrence belongs to a character with frequency at least two. No qualifying index exists, so `-1` is the required sentinel.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `0` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "leetcode"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `0` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Fixed 26-element array:** Use `ord(c) - ord('a:** - **Fixed 26-element array:** Use `ord(c) - ord('a')` as an index, count into an integer array, then scan the string. This has the same $O(n)$ time and explicit $O(1)$ space. `Counter` is shorter and expresses the frequency idea directly.
- **- **Repeated `s.count(c)`:** Testing the total cou:** - **Repeated `s.count(c)`:** Testing the total count separately for each character is concise but each `count` scans the string. In the worst case this costs $O(n^2)$ time.
- **- **Queue of provisional unique characters:** Duri:** - **Queue of provisional unique characters:** During one pass, keep first-seen characters in a queue and mark repeats in a count map, removing repeated entries from the front when possible. It can be linear but maintains more moving state and is easier to get wrong than the two-pass method.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the length of `s`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
