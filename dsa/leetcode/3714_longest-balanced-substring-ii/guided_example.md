# Guided Example: Longest Balanced Substring II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "abbac"}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s` consisting only of the characters `'a'`, `'b'`, and `'c'`.

The objective is to compute `4` from `{"s": "abbac"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Use the three-letter alphabet to split the problem into exhaustive cases

The string contains only `'a'`, `'b'`, and `'c'`. A nonempty substring can therefore contain exactly one, exactly two, or exactly three distinct characters. There is no fourth possibility. The solution deliberately solves these three cases separately:

- `calc1` finds the longest balanced substring with one distinct character.
- Three calls to `calc2` find the longest balanced substring with exactly two distinct characters, one call for each pair `(a, b)`, `(b, c)`, and `(a, c)`.
- `calc3` finds the longest balanced substring with all three distinct characters.

The final answer is `max(x, y, z)`, where `x`, `y`, and `z` are the best lengths from those cases. This division is what makes a linear-time solution possible. Instead of maintaining a general frequency structure for every possible left endpoint, each helper uses the simplest invariant appropriate to its number of distinct letters.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "abbac"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Case one: a balanced substring containing one character

If a substring contains only one distinct character, all its present characters automatically have the same frequency because there is only one frequency to compare. Such a substring is simply a consecutive run of identical letters.

The helper `calc1` scans these runs. It places `i` at the first character of a run, advances `j` while `s[j] == s[i]`, records the run length `j - i`, and then moves `i` directly to `j`, the beginning of the next run. Each character belongs to exactly one run and is passed once. The greatest run length is exactly the best answer among one-letter substrings.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Case two: equal counts of one chosen pair

Consider `calc2(s, a, b)` for two chosen character names. A valid substring for this case must contain those two characters equally often and must not contain the alphabet's third character. That third character acts as a separator: a candidate substring cannot cross it, because crossing would include a third distinct character.

The outer part of `calc2` skips characters that are neither `a` nor `b`. It then processes one maximal segment containing only the chosen pair. Inside that segment, it maintains a prefix difference

$$
d = \#a - \#b.
$$

Reading `a` adds one to `d`; reading `b` subtracts one. Suppose `d` had the same value immediately before a candidate substring and at its right endpoint. The changes made within that substring must sum to zero, so the substring added equally many `a` and `b` characters. Conversely, any substring with equal counts contributes net difference zero and therefore has matching prefix differences at its two boundaries.

The map `pos` stores the earliest index at which each difference was seen in the current pair-only segment. It starts as `{0: i - 1}`. The index `i - 1` represents the empty prefix immediately before the segment, whose difference is zero. This seed is essential: if a balanced candidate starts at the segment's first character, a later return to difference zero gives length `right - (i - 1)`, which includes that first character.

When the current difference has appeared before at `pos[d]`, the balanced substring ends at the current index and has length `i - pos[d]`. The code compares that length with `res`. When a difference is new, the code stores its index. It intentionally does not replace an existing index: for a fixed right endpoint, subtracting the earliest equal-difference index gives the longest possible substring.

After a separator is encountered, the inner loop ends. The next outer iteration skips the separator or separators and creates a fresh map for the next maximal pair-only segment. Prefix differences cannot be matched across a forbidden third character.

The solution runs this helper for all three unordered pairs. A balanced two-letter substring must use exactly one of those pairs, so one of the calls will examine it inside the correct separator-bounded segment.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "abbac"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Quadratic substring expansion:** Fixing every left endpoint, extending every right endpoint, and maintaining three counts gives an easy $O(n^2)$ solution. That is suitable for the smaller version of the problem but not for a length up to $10^5$.
- **One general prefix-frequency map:** One can derive separate normalized signatures depending on which letters are present, but mixing absent-letter semantics into one state is easy to get wrong. The three-case split makes the completeness argument explicit and keeps each state minimal.
- **Binary balance without separator resets:** Running the `a` versus `b` difference across a `c` would incorrectly allow a reported interval that contains `c`. Every unchosen letter must end the current pair-only segment and reset `pos`.
- **Keeping the latest prefix position:** Replacing `pos[d]` or `pos[k]` on every occurrence would still find some balanced substrings, but it could lose the longest one. The earliest matching boundary always maximizes the length for a fixed right endpoint.
- **Missing the empty-prefix seed:** Without `{0: i - 1}` in `calc2` or `{(0, 0): -1}` in `calc3`, a balanced substring beginning at the start of a segment or at index zero would not be measured correctly.
- **All characters identical:** `calc1` returns the entire string. The pair and three-letter helpers may return smaller values, but the final maximum preserves the correct full length.
- **Only two letters occur in the entire string:** The matching `calc2` call can return the whole string when their totals are equal. `calc3` does not need to manufacture a three-letter answer; the exhaustive maximum includes the two-letter case independently.
- **A single character:** `calc1` records its run length as one. All loops terminate safely, and the answer is one.
- **Several forbidden characters in a row:** The initial loop in `calc2` keeps advancing until it reaches a chosen letter or the end. It cannot become stuck, and a fresh `pos` is created only for a real next segment.
- **Difference values becoming negative:** Negative values are expected when the second chosen letter is more frequent. Dictionary keys can be negative, and equality of prefix differences—not their sign—is what matters.
- **Why two differences suffice for three counts:** Requiring `A - B = 0` and `B - C = 0` already implies `A = B = C`. A third difference `A - C` would be redundant because it is the sum of the first two.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the string length. `calc1` advances its indices only forward and takes $O(n)$ time. A single `calc2` call also takes $O(n)$ time: the skip loop and segment loop together consume every character at most once. It is called exactly three times, which is a constant factor, so all pair processing remains $O(n)$. `calc3` performs one pass and takes expected $O(n)$ time using hash-table lookups.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
