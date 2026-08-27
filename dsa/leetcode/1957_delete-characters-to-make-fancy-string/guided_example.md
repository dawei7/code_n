# Guided Example: Delete Characters to Make Fancy String

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "leeetcode"}`
- **Required output:** `"leetcode"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A **fancy string** is a string where no **three** **consecutive** characters are equal.

The objective is to compute `"leetcode"` from `{"s": "leeetcode"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Every maximal run can keep at most two characters

A violation consists of three equal consecutive characters. Consider a maximal run of one letter with length $L$. If $L\le2$, all of it can remain. If $L>2$, at least $L-2$ characters must be deleted, and keeping exactly the first two achieves that lower bound.

Different runs are separated by another letter. The algorithm never deletes an entire nonempty run—it keeps at least its first character—so deleting extras cannot merge two runs of the same letter across the separator. Each run can be optimized independently.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "leeetcode"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Read the exact condition

The solution scans the original string with index `i` and character `c`. It appends `c` when at least one of these is true:

- `i < 2`, meaning fewer than two original predecessors exist;
- `c != s[i - 1]`;
- `c != s[i - 2]`.

It skips a character only when $i\ge2$ and the current character equals both immediately preceding original characters. That is exactly the third or later position inside a run of equal characters.

For a run `"aaaaa"`, the first two positions are appended. Every later `a` has two original `a` predecessors and is skipped. For `"aabaa"`, no position is the third equal character of its run, so the entire string remains.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The solution scans the original string with index `i` and ch... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why comparing the original string is safe

Many streaming solutions compare the current character with the last two characters already kept. This exact code instead compares `s[i - 1]` and `s[i - 2]` in the original string.

That works because the decision is purely run-based. Inside a long run, every character from the third onward has two equal original predecessors and must be removed. At the beginning of a new run, at least one of the two original predecessors differs, so the first character is kept; the second is also kept. Since every separating run keeps characters, deletions never create a new cross-run triple that was not already inside one original run.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"leetcode"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "leeetcode"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"leetcode"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Compare against output tail:** Append unless t:** - **Compare against output tail:** Append unless the last two retained characters both equal the current one. This is more general and has the same $O(N)$ bounds.
- **Run-length encoding:** Explicitly find every run and append its first two characters. It expresses the proof directly but needs more indexing code.
- **Repeated string deletion:** Removing characters from immutable strings can cause quadratic copying.
- **Length below three:** Every character satisfies `i < 2` or no triple exists, so the string is returned unchanged.
- **Exactly three equal characters:** The first two are kept and the third is removed.
- **Very long run:** Exactly two copies survive regardless of length.
- **Run length one:** Its sole character is always retained and cannot form a triple.
- **Alternating letters:** No character equals both prior originals, so all are retained.
- **Two same, one different, two same:** Both runs of length two remain and the separator prevents merging.
- **Original-versus-output comparison:** It is safe here specifically because the property and optimal deletions operate independently on maximal runs.
- **Unique value result:** Different choices of identical occurrences to delete cannot change the resulting character sequence.
- **Input immutability:** The source does not modify `s`; it builds a new result.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the string length.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
