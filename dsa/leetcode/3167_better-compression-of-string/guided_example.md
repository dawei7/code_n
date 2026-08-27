# Guided Example: Better Compression of String

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"compressed": "a3c9b2c1"}`
- **Required output:** `"a3b2c10"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `compressed` representing a compressed version of a string. The format is a character followed by its frequency. For example, `"a3b1a1c2"` is a compressed version of the string `"aaabacc"`.

The objective is to compute `"a3b2c10"` from `{"compressed": "a3c9b2c1"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Parse one letter-number group at a time

The valid input alternates a lowercase letter with a positive decimal frequency, but a frequency may contain several digits.

Pointer `i` always points to the next letter. Pointer `j = i + 1` begins at its first digit. While characters are digits, the code builds the number with

`x = x * 10 + int(compressed[j])`.

Multiplying the existing prefix by ten shifts its decimal digits left, and adding the new digit appends it. For digits `'1'`, `'0'`, this produces 1 then 10.

When `j` reaches the next letter or end of string, `x` is the complete frequency belonging to `compressed[i]`. It is added to `cnt[letter]`, and `i = j` starts the next group.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"compressed": "a3c9b2c1"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Combine repeated letters

The same character may appear in several input groups. `Counter` accumulation adds their frequencies instead of overwriting them.

For `"a3c9b2c1"`, counts become $a:3$, $b:2$, and $c:10$.

The output requires each character once, in alphabetical order. The generator formats each counter item as `f"{k}{v}"`. Sorting these strings sorts by their first character. Since counter keys are distinct lowercase letters, later digits cannot affect the ordering between two items. Joining produces `"a3b2c10"`.


The parser invariant is that all characters before `i` have been divided into complete valid groups and their frequencies added exactly once to `cnt`.

The inner loop consumes precisely the maximal digit sequence after the current letter, reconstructing its numeric value. Adding it preserves the invariant, and the next `i` points to the next group. Valid-input guarantees prevent a missing frequency.

After parsing, `cnt[c]` equals the sum of all input frequencies for character $c$, which is its total decompressed multiplicity. Formatting one entry per key meets uniqueness, and alphabetical sorting meets ordering. The output therefore represents the same decompressed string multiset in the required better form.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The same character may appear in several input groups.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why decompression is unnecessary

Frequencies can reach $10^4$ per group and many groups may repeat. Expanding characters would create a much larger string only to count it again. Adding encoded counts directly preserves all needed information.

The problem explicitly permits character order to change, so aggregating by letter does not need to retain group positions.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"a3b2c10"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"compressed": "a3c9b2c1"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"a3b2c10"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Fixed 26-element integer array:** Matches the :** - **Fixed 26-element integer array:** Matches the manifest exactly and can emit indices in order without sorting.
- **Regular-expression parsing:** It can extract letter-number groups but adds engine overhead and hides the simple state machine.
- **Decompress then recount:** Potentially enormous and unnecessary.
- **Multi-digit frequency:** The multiply-by-ten recurrence parses it correctly.
- **Repeated letter groups:** Counts are added, not replaced.
- **Already better-compressed input:** Parsing and emission reproduce the same logical representation.
- **Input order not alphabetical:** Final sorting corrects it.
- **Frequency crossing a digit boundary:** Values such as 9 plus 1 become output count 10 normally.
- **No leading zeros:** The guarantee makes numeric reconstruction canonical, though the parser would still compute their numeric value.
- **One group:** It is returned in the same letter-count form.
- **Sorting formatted strings:** Safe because each begins with a unique one-character lowercase key.
- **Valid compression guarantee:** Every letter is followed by at least one digit, so `x` is never left zero for a group.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be compressed input length and $u\le26$ the number of distinct letters.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
