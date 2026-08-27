# Guided Example: Greatest English Letter in Upper and Lower Case

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "lEeTcOdE"}`
- **Required output:** `"E"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string of English letters `s`, return *the **greatest **English letter which occurs as **both** a lowercase and uppercase letter in* `s`. The returned letter should be in **uppercase**. If no such letter exists, return *an empty string*.

The objective is to compute `"E"` from `{"s": "lEeTcOdE"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Separate existence from alphabetic priority

A letter qualifies only if two distinct character forms are present in `s`: its uppercase character and its lowercase character. Among all qualifying letters, the answer must be greatest alphabetically and must be returned in uppercase.

The solution handles these two concerns separately. It first records which exact characters occur. It then examines candidate uppercase letters in descending alphabetic order. The first candidate whose uppercase and lowercase forms both occur is automatically the greatest valid answer.

The line `ss = set(s)` creates the presence collection. A set does not preserve multiplicity, but multiplicity is irrelevant: one occurrence of `E` and one occurrence of `e` are enough, and seeing either character additional times cannot make the letter more valid. Set membership directly answers the only needed question—whether a particular form appears at least once.

Uppercase and lowercase characters remain distinct keys. For example, `'A'` and `'a'` are two different set elements. This is essential because converting the entire string to one case would lose the information needed to prove that both original forms occurred.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "lEeTcOdE"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Search from the greatest letter downward

`ascii_uppercase` denotes the ordered sequence `ABCDEFGHIJKLMNOPQRSTUVWXYZ` in the solution environment. Slicing it with `[::-1]` produces `ZYXWVUTSRQPONMLKJIHGFEDCBA`. The loop therefore considers `Z` first, then `Y`, and eventually `A`.

For each uppercase candidate `c`, the condition checks:

`c in ss and c.lower() in ss`.

The first part verifies an uppercase occurrence. The second converts the single candidate to its corresponding lowercase character and verifies a lowercase occurrence. Both must be true because Python's `and` operator requires both operands to succeed.

If the condition holds, `return c` ends the method immediately. Since every alphabetically greater uppercase letter was checked earlier and failed at least one presence test, none of them qualifies. The current `c` is therefore not merely a valid answer; it is the greatest valid answer.

If all 26 candidates fail, execution reaches `return ''`. Exhausting the complete English uppercase alphabet proves that no letter appears in both forms, so the empty string is exactly the required result.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `ascii_uppercase` denotes the ordered sequence `ABCDEFGHIJKL... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why descending search avoids extra comparison state

An alternative scan through `s` might update a “best so far” letter whenever it finds a qualifying character. Descending candidate order makes that unnecessary. Search order itself establishes priority, so the method can return as soon as existence is confirmed.

For the string containing `a`, `A`, `f`, `F`, `r`, and `R`, the set records all six forms. The descending loop rejects `Z` down through `S`, reaches `R`, finds both `R` and `r`, and returns `R`. It never needs to inspect `F` or `A` because neither can outrank an already validated `R`.

For a string containing uppercase `A` and lowercase `b`, the checks remain letter-specific. `B` fails because uppercase `B` is missing, and `A` fails because lowercase `a` is missing. The method correctly returns the empty string rather than combining the case evidence from different letters.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"E"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "lEeTcOdE"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"E"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Two 26-entry boolean arrays:** Record lowercas:** - **Two 26-entry boolean arrays:** Record lowercase and uppercase presence separately by alphabet index, then scan indices from 25 down to 0. This has the same `O(n)` time and `O(1)` space but requires explicit character-to-index arithmetic.
- **Two bit masks:** Use one bit per lowercase letter and one per uppercase letter, intersect the masks, and locate the highest set bit. This is compact and fast but less immediately readable to beginners than direct set membership.
- **Scan candidates upward while saving the latest match:** This is correct but cannot return early; it needs an extra result variable and must finish all 26 candidates. Descending order states the priority directly.
- **Sort the input:** Sorting all `n` characters is unnecessary and costs `O(n \log n)` time. The answer depends on presence and alphabetic priority, not on the positions or multiplicities of characters.
- **Convert the whole string to lowercase:** That would show that a letter appears in some case, but it destroys whether both cases were present. `"A"` alone would become indistinguishable from evidence containing lowercase `a`.
- **Check `c.swapcase()` for characters encountered in `s`:** This can work with a best-so-far comparison, but duplicate characters repeat the same work and traversal order does not correspond to alphabetical priority.
- **Only uppercase occurrences:** A string such as `"ABC"` has no valid answer because no lowercase counterparts occur. The conjunction rejects every candidate.
- **Only lowercase occurrences:** A string such as `"abc"` likewise returns the empty string because every uppercase membership test fails.
- **Several qualifying letters:** The descending loop returns the greatest one, not the first one appearing in `s`. Input position has no effect on the answer.
- **Repeated characters:** Hundreds of copies of `A` still become one set entry. A single lowercase `a` is enough to make `A` qualify; repetition does not affect correctness or the scan.
- **Mixed evidence for different letters:** Uppercase `Q` and lowercase `r` do not form a valid pair. Both membership tests use forms of the same candidate `c`.
- **Smallest possible input:** With one character, its opposite-case form cannot also occur, so the loop finds no match and returns `''`.
- **Return casing:** The loop variable is always uppercase, so a successful return automatically obeys the requirement without another conversion.
- **Non-English characters:** The source constraints exclude them. Even if they appeared, they would be inserted into `ss` but never considered as candidates because the loop intentionally covers only English uppercase letters.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the length of `s`. Constructing `set(s)` visits all `n` characters, so it takes `O(n)` expected time. The subsequent loop performs at most 26 iterations, each with two expected constant-time set lookups and one constant-size lowercase conversion. Its cost is `O(26) = O(1)`. Total expected time is therefore `O(n)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
