# Guided Example: First Letter to Appear Twice

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "abccbaacz"}`
- **Required output:** `"c"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `s` consisting of lowercase English letters, return *the first letter to appear **twice***.

The objective is to compute `"c"` from `{"s": "abccbaacz"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The answer is determined at a second occurrence

A letter “appears twice” at the position where its running frequency first reaches two. The requested letter is the one whose second occurrence has the smallest index.

Scanning `s` from left to right encounters positions in exactly that priority order. The first character whose count becomes two must therefore be the answer.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "abccbaacz"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Maintain running frequencies

`cnt = Counter()` begins as an empty frequency mapping. For each character `c`, the method increments `cnt[c]`.

Immediately after the increment:

- count one means this is the first occurrence;
- count two means this is the second occurrence;
- a larger count would mean the second occurrence happened earlier.

The method returns as soon as `cnt[c] == 2`.

Because it returns at the earliest second occurrence in the scan, no character can later qualify earlier.

The Counter represents information about the processed prefix, not about the complete string. That distinction is what makes it useful for ordering. At index `i`, `cnt[c]` answers how many copies of `c` have actually appeared no later than `i`. A final frequency table built after the scan could say that both `a` and `c` repeat, but it would not by itself reveal whether `a`'s second copy or `c`'s second copy occurred first. Updating and testing immediately preserves that temporal fact.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the first appearance does not decide anything

The order of first occurrences is irrelevant. A letter seen early may not repeat until much later, while another letter first seen later can receive its second occurrence sooner.

For `"abccbaacz"`, `a` is first at index zero, but its second occurrence is index five. `c` first appears at index two and repeats at index three, so the scan returns `c` when that second copy is processed.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"c"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "abccbaacz"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"c"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **26-bit seen mask:** Test the bit for each character; if already set, return it, otherwise set it. This matches the manifest summary and uses one integer.
- **Boolean array of length 26:** It expresses first-seen state without full counts and remains constant-space.
- **Set of seen letters:** If `c in seen`, return it; otherwise insert it. This is simpler than a Counter for the exact need.
- **Compute all frequencies first:** Final counts do not reveal which second occurrence came earliest; scan order must be retained.
- **Return the first character with final count at least two:** Iterating unique characters by first appearance can give the wrong answer because second-occurrence order differs.
- **Immediate pair such as `"aa"`:** The second character raises the count to two and is returned.
- **Only one repeated letter:** Its second occurrence is necessarily the answer.
- **Several repeated letters:** The left-to-right early return selects the smallest second-occurrence index.
- **A letter appearing many times:** It triggers on its second copy; later copies are never reached after return.
- **First repeated letter may not be first distinct letter:** Only second-occurrence position matters.
- **Guaranteed repetition:** The function has no fallback return because valid input always triggers the condition.
- **Lowercase alphabet:** At most 26 Counter keys exist.
- **Input preservation:** Counting does not modify `s`.
- **Counter availability:** The exact source relies on `Counter`, conventionally from `collections`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the string length. The scan may return early, but in the worst case the first second occurrence is near the end, so time is `O(n)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
