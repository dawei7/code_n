# Guided Example: Reverse Vowels of a String

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "IceCreAm"}`
- **Required output:** `"AceCreIm"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `s`, reverse only all the vowels in the string and return it.

The objective is to compute `"AceCreIm"` from `{"s": "IceCreAm"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Reverse the vowel subsequence while leaving every other position fixed.

Imagine extracting only the vowels from left to right. If they are

$$
v_0,v_1,\ldots,v_{q-1},
$$

then the output must place $v_{q-1}$ into the original position of $v_0$, place $v_{q-2}$ into the position of $v_1$, and so on. Every consonant, digit, space, or punctuation character must remain at its original index.

Two pointers can find these mirrored vowel occurrences directly. The left pointer searches for the earliest unprocessed vowel, and the right pointer searches for the latest unprocessed vowel. Swapping them performs exactly one pair in the reversed vowel order.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "IceCreAm"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Make a mutable character buffer.

Python strings cannot be changed at individual indices. The source therefore creates `cs = list(s)`, a mutable list containing the same characters in the same order.

All pointer searches and swaps operate on `cs`. At the end, `''.join(cs)` combines the final characters into the required new string. The original input string remains immutable, which is appropriate because this function's contract returns a string rather than requiring mutation of a character-array argument.

The conversion and final join do not alter character content. They only provide a representation in which swapping positions is possible.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Recognize both lowercase and uppercase vowels.

The string `vowels = "aeiouAEIOU"` lists all ten accepted vowel characters. Testing `cs[i] not in vowels` asks whether the current character is absent from that fixed collection.

Case is preserved. An uppercase `A` is recognized as a vowel but remains uppercase when moved; the algorithm swaps complete characters and never normalizes them. Printable ASCII characters not in this list are treated as non-vowels.

Because the membership collection always has length ten, each membership check is constant time in asymptotic analysis. A set could also provide constant expected membership, but is unnecessary for such a fixed tiny group.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"AceCreIm"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "IceCreAm"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"AceCreIm"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Collect vowel indices or values first:** Store every vowel, reverse that list, and write values back into vowel positions. This is easy to structure but uses additional space proportional to the number of vowels on top of the mutable output buffer.
- **Use a vowel set:** Replacing the ten-character string with a set makes membership expected $O(1)$, but asymptotic behavior is unchanged because the current membership scan has a fixed bound of ten.
- **Repeated string concatenation:** Building the result one character at a time can become quadratic in languages with immutable strings. The list buffer plus one final join avoids that cost.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be `len(s)`. Converting the string to `cs` takes $O(n)$ time. Although the code contains inner loops inside an outer loop, `i` only moves right and `j` only moves left. Across the entire execution, each pointer advances through at most $n$ positions, so all searching and swapping is $O(n)$ total. Joining the result is another $O(n)$ operation. Overall time complexity is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
