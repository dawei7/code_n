# Guided Example: Vowel-Consonant Score

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "cooear"}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s` consisting of lowercase English letters, spaces, and digits.

The objective is to compute `2` from `{"s": "cooear"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Classify only letters

The string may contain lowercase English letters, spaces, and digits. Spaces and digits must contribute to neither count, so the first decision for every character is whether it is a letter at all. The source uses `ch.isalpha()` for that test. Under the stated input alphabet, it is true exactly for the lowercase letters `a` through `z` and false for every permitted space or digit.

Once a character is known to be a letter, it belongs to exactly one of two disjoint groups:

- it is a vowel when it appears in the fixed string `"aeiou"`;
- otherwise, it is a consonant.

The source arrives at those two totals in a slightly compressed way. The variable named `c` initially counts every alphabetic character, not consonants alone. Whenever the letter is a vowel, `v` is incremented as well. After the scan, `c -= v` subtracts all vowels from the total number of letters. If $L$ is the number of letters and $V$ is the number of vowels, the resulting value is

$$
C=L-V,
$$

which is exactly the number of consonants because every allowed letter is either one of the five vowels or a consonant.

It is worth understanding that temporary meaning of `c`. During the loop, `c` should be read as “letters seen so far.” It becomes the consonant count only after `c -= v`. Treating it as a consonant counter during the loop would make the code appear to count vowels twice, but the final subtraction is deliberately converting an inclusive count into the desired exclusive count.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "cooear"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Trace the character classes

For `s = "cooear"`, the loop encounters six alphabetic characters, so the temporary `c` becomes 6. Four of those characters—`o`, `o`, `e`, and `a`—belong to `"aeiou"`, so `v` becomes 4. Subtracting gives the final consonant count $6-4=2$, representing `c` and `r`. Integer division then gives $4\mathbin{//}2=2$.

For `s = "au 123"`, the two vowels increment both the all-letter counter and the vowel counter. The space and three digits fail `isalpha()` and change neither value. The totals before subtraction are `c = 2` and `v = 2`, so the final consonant count is zero.

This organization automatically ignores every permitted nonletter. There is no separate branch for a space and no loop over the ten possible digits. Both categories simply fail the outer condition.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Compute the defined floor safely

When at least one consonant exists, the required score is

$$
\left\lfloor\frac{V}{C}\right\rfloor.
$$

Both values are nonnegative integers, so Python's `v // c` is exactly the requested floor. For example, five vowels and three consonants give `5 // 3 == 1`. It is not necessary to use floating-point division followed by `floor`, and avoiding floating point also avoids needless conversion and rounding concerns.

Division is not defined when $C=0$. More importantly, the contract explicitly assigns score 0 in that case, regardless of how many vowels exist. The conditional return `0 if c == 0 else v // c` checks this case before division, so an all-vowel string, a string containing only spaces and digits, or any mixture with no consonant returns zero without raising an error.

If there are consonants but no vowels, `v` is zero and `v // c` naturally returns zero. This is a different route to the same numerical score: division is valid because the denominator is positive.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "cooear"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Count consonants directly:** An explicit branch can increment `v` for vowels and increment `c` for other lowercase letters. That avoids the temporary “all letters” meaning of `c` but has the same $O(N)$ time and $O(1)$ space.
- **Repeated built-in counts:** Summing `s.count(ch)` for the five vowels can find $V$, but a separate letter count is still needed and the string is scanned several times. Five is constant, so the asymptotic time stays $O(N)$, though the single pass is clearer and does less work.
- **Regular expressions or filtered strings:** Building collections of matching characters can express the classification, but it introduces $O(N)$ temporary space for a task requiring only two integers.
- **No consonants:** The answer must be zero even when vowels are present. The conditional return prevents division by zero and implements the special rule.
- **No vowels:** A positive consonant count makes the ordinary formula valid, and zero floor-divided by that count remains zero.
- **Only spaces and digits:** No character passes `isalpha()`, so both counts remain zero and the answer is zero.
- **The letter y:** It is a consonant for this problem because the vowel set contains exactly `a`, `e`, `i`, `o`, and `u`.
- **Mixed digits and letters:** Digits do not become consonants merely because they are not vowels. The outer alphabetic test is essential.
- **Unicode outside the contract:** Python's `isalpha()` recognizes many non-English letters. Such characters would be counted as consonants unless they were one of the five literal vowels, but the input guarantee excludes them, so this does not affect valid cases.
- **Maximum length:** Even though the stated maximum is only 100, the one-pass method remains the natural optimal solution and scales linearly for longer strings as well.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N=\lvert\texttt{s}\rvert$. The loop examines all $N$ characters once. `isalpha()` operates on one character, and membership in the five-character literal `"aeiou"` is bounded by a constant amount of work. The final subtraction and conditional division are constant-time operations for the small counts allowed here. Total time is therefore $O(N)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
