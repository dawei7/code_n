# Guided Example: Remove Letter To Equalize Frequency

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"word": "abcc"}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** string `word`, consisting of lowercase English letters. You need to select **one** index and **remove** the letter at that index from `word` so that the **frequency** of every letter present in `word` is equal.

The objective is to compute `true` from `{"word": "abcc"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Removing a position is equivalent to choosing its letter

The operation must remove exactly one character. If a letter `c` appears several times, deleting any one of its occurrences has the same effect on the frequency table: `cnt[c]` decreases by one, while every other count stays unchanged. Therefore there is no need to try all positions. It is sufficient to try each distinct letter type once.

The method begins with `cnt = Counter(word)`, which stores the frequency of every letter present in the original string. Since the input contains only lowercase English letters, there can be at most 26 keys.

For each `c` in `cnt.keys()`, the algorithm temporarily performs the removal by executing `cnt[c] -= 1`. It then examines the positive counts:

`set(v for v in cnt.values() if v)`.

The `if v` filter deliberately excludes a zero count. If the removed character was the only occurrence of `c`, that letter is no longer present in the resulting word. The contract requires equal frequencies only among letters that remain present, so zero must not be compared with their positive frequencies.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"word": "abcc"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why a set detects equality

A set stores each distinct frequency value once. If all remaining letters have the same positive frequency $f$, the generated set is exactly `{f}` and has length 1. If two remaining letters have different frequencies, both values appear and the set has length at least 2.

The resulting word cannot be empty under the stated constraints: its original length is at least 2 and exactly one character is removed. Therefore there is always at least one positive count, and a set length of 1 means precisely that every present letter has equal frequency. The code can immediately return `true`.

If the test fails, `cnt[c] += 1` restores the original frequency before the next letter type is tried. This restoration is essential. Without it, later iterations would simulate several deletions at once rather than the required single deletion.

After every distinct letter has been tried without producing one positive frequency value, the method returns `false`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Tracing successful and unsuccessful cases

For `word = "abcc"`, the original counts are one each for `a` and `b` and two for `c`. Trying removal of `a` leaves positive frequencies 1 and 2, so it fails and the count is restored. The same happens for `b`. Trying `c` changes its count from 2 to 1, leaving all three positive counts equal to 1. The set has one member, and the method returns true.

For `word = "aazz"`, both letters initially have frequency 2. Removing an `a` creates positive counts 1 and 2; removing a `z` creates 2 and 1. Neither trial has a one-element frequency set, so the result is false. This example highlights “exactly one”: the original frequencies are already equal, but doing nothing is not allowed, and every permitted deletion destroys equality.

Consider `word = "abb"`. Trying the only `a` reduces its count to zero, which is filtered out. The only remaining letter `b` has frequency 2, so all letters still present have equal frequency and the answer is true. The target common frequency does not have to be 1.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"word": "abcc"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Delete every position and recount:** Constructing `word[:i] + word[i+1:]` for all $n$ positions is easy to imagine but can require $O(n^2)$ time and repeated string allocation.
- **Reason from the frequency-of-frequencies table:** One can derive a constant-case characterization, such as removing the sole letter of frequency 1 or reducing one uniquely high frequency by one. That can be slightly faster after counting, but it is easier to miss the “exactly one” condition; trying at most 26 letter types is already constant-sized.
- **Sort the frequencies:** For each possible removed letter, sorting remaining counts would test equality but adds unnecessary work. A set directly asks how many distinct positive values exist.
- **All characters identical:** Removing one occurrence leaves one letter type with a positive frequency, so the answer is always true for length at least 2.
- **All characters distinct:** Removing any character leaves the others each with frequency 1, so the answer is true.
- **Already equal frequencies with multiple repeated types:** Equality before removal does not automatically mean success. For `"aazz"`, the mandatory deletion makes one frequency smaller and returns false.
- **Removing the only occurrence of a letter:** Its count becomes zero and must be ignored because the letter is absent afterward. The `if v` filter handles this case.
- **A common frequency greater than one:** A result such as a single remaining letter with frequency 2 is valid; equal frequency does not mean every count must equal 1.
- **Exactly one removal:** The counter is restored after every failed trial, ensuring each experiment contains one deletion rather than an accumulation of deletions.
- **Repeated positions of the same letter:** They are behaviorally identical at the frequency level, so testing the letter once loses no possible outcome.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the length of `word` and let $\sigma$ be the number of distinct letters, with $\sigma \le 26$. Building the counter takes $O(n)$ time. There are $\sigma$ trials, and each trial scans the $\sigma$ stored values to build a set, for $O(\sigma^2)$ additional time. Thus the general expression is $O(n + \sigma^2)$. Because the alphabet is fixed to 26 lowercase letters, $\sigma^2$ is a constant, yielding the manifest's $O(n)$ time bound.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
