# Guided Example: Find the Longest Substring Containing Vowels in Even Counts

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "eleetminicoworoep"}`
- **Required output:** `13`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given the string `s`, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.

The objective is to compute `13` from `{"s": "eleetminicoworoep"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Track parity, not exact counts

The condition asks whether each vowel count is even. The exact number of occurrences is unnecessary: only its parity, even or odd, matters. One bit can store that information for one vowel. Reading another copy of the vowel flips its parity, which is exactly what XOR with that bit does.

The variable `mask` represents vowel parities in the prefix ending at the current index. A zero bit means the corresponding vowel has appeared an even number of times in that prefix; a one bit means it has appeared an odd number of times.

The exact code chooses bit position `ord(c) - ord("a")`. Thus `a` uses position zero, `e` position four, `i` position eight, `o` position fourteen, and `u` position twenty. These bits are not adjacent, but they are distinct, which is all correctness requires. Only five bits can ever vary, so there are still only $2^5=32$ reachable masks despite the largest bit position being twenty.

When `c` is a vowel, `mask ^= 1 << (...)` flips its unique bit. When `c` is a consonant, the condition is false and `mask` remains unchanged because consonants do not affect the requirement.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "eleetminicoworoep"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why equal prefix masks identify a valid substring

Suppose the parity mask after index $j$ equals the mask after index $i$, where $j<i$. For each vowel, the parity accumulated through $j$ and through $i$ is the same. Removing the earlier prefix means XORing those parities; equal bits cancel to zero. Therefore every vowel occurs an even number of times in substring `s[j + 1:i + 1]`.

The converse is also true. If every vowel count in that substring is even, moving from the prefix at $j$ to the prefix at $i$ flips every vowel bit an even number of times, leaving the mask unchanged. Hence valid substrings correspond exactly to pairs of equal prefix masks.

This converts a substring search into a repeated-state search: at each right endpoint $i$, find an earlier endpoint with the same mask and measure the distance.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Suppose the parity mask after index $j$ equals the mask afte... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why only the first occurrence of a mask is stored

The dictionary `d` maps each seen mask to its earliest prefix-ending index. If the current mask has been seen at index $j$, the valid substring length is `i - j`. For a fixed current $i$, the smallest possible $j$ produces the longest substring. Therefore replacing the stored index with a later occurrence could only make future candidates shorter.

The `else` branch stores `d[mask] = i` only when the mask is new. Once recorded, its earliest index remains unchanged for the entire scan.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `13` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "eleetminicoworoep"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `13` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Five-bit contiguous mapping:** Map `a, e, i, o:** - **Five-bit contiguous mapping:** Map `a, e, i, o, u` to bit positions zero through four. It is more compact visually and has the same 32 states; the exact code derives distinct positions directly from character codes.
- **Array of 32 first positions:** With contiguous bits, a fixed array can replace the dictionary. The current sparse masks are not indices from zero through 31, so a dictionary is convenient.
- **Five parity booleans:** A tuple of booleans can serve as the prefix state. It is correct but more verbose to update and hash than one integer mask.
- **Brute-force substrings:** Count vowels for every possible substring. Even with prefix counts, examining $O(n^2)$ endpoint pairs is too slow for strings up to $5\cdot10^5$ characters.
- **No vowels:** The mask stays zero, and the virtual index $-1$ makes the entire string the answer.
- **All vowels already even:** The final mask matches an earlier state, often zero, allowing the complete qualifying span to be measured.
- **Odd total counts:** The full string may fail, but equal masks inside it can still identify a long valid interior substring.
- **Repeated state:** The earliest index must not be overwritten; later copies can never produce a longer future span.
- **Substring starting at zero:** `d[0] = -1` handles it without branching.
- **Consonants:** They leave `mask` unchanged but extend the distance from the stored state, which can increase the answer.
- **Empty string outside the contract:** The loop would not run and zero would be returned, consistent with an empty valid substring.
- **Lowercase guarantee:** The membership test explicitly recognizes lowercase `aeiou`, matching the stated input alphabet.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the length of `s`. The loop reads every character once. Membership testing, bit operations, dictionary lookup, and arithmetic are expected $O(1)$ operations, so total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
