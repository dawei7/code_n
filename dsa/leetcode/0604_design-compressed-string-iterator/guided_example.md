# Guided Example: Design Compressed String Iterator

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"compressedString": "z1", "operations": [["next"], ["next"], ["next"], ["hasNext"]]}`
- **Required output:** `["z", " ", " ", false]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Design and implement a data structure for a compressed string iterator. The given compressed string will be in the form of each letter followed by a positive integer representing the number of this letter existing in the original uncompressed string.

The objective is to compute `["z", " ", " ", false]` from `{"compressedString": "z1", "operations": [["next"], ["next"], ["next"], ["hasNext"]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Parsing the encoded input once

The constructor scans `compressedString` from left to right. At the start of a run, `compressedString[i]` is the character `c`. It advances once, then parses all following digits into integer `x`:



Multiplying the existing value by ten shifts its decimal digits left, and adding the new digit appends that digit. Thus, characters `'1'`, `'2'`, and `'3'` become count 123 rather than three separate counts.

The pair `[c, x]` is appended to `d`. A list rather than tuple is used because `next` will decrement the stored count in place.

The input grammar guarantees alternating letters and positive decimal counts, so the constructor does not need error recovery for missing digits, zero counts, or punctuation.

For `"L1e2t1"`, the parsed state becomes logically:



This storage is proportional to the compressed representation, not the potentially much larger expansion `"Leet"`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"compressedString": "z1", "operations": [["next"], ["next"], ["next"], ["hasNext"]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: The pointer invariant

`p` is the index of the first run that may still have output remaining. For a valid active iterator:

- every run before `p` has remaining count zero;
- run `p` has a positive count;
- later runs have their original positive counts.

The constructor establishes this with `p = 0` and positive counts. `next` preserves it by decrementing the current count and advancing exactly when that count becomes zero.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `p` is the index of the first run that may still have output... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Checking availability

`hasNext` returns:



The first half ensures the pointer still names a run. Python’s short-circuit `and` prevents out-of-range access if all runs are exhausted. The second half verifies a remaining occurrence.

Under the pointer invariant, an in-range current run always has positive count, so the second test is defensive and documents the required state.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `["z", " ", " ", false]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"compressedString": "z1", "operations": [["next"], ["next"], ["next"], ["hasNext"]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `["z", " ", " ", false]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Demand parsing:** Keep an index into the compr:** - **Demand parsing:** Keep an index into the compressed string and parse the next run only when the current count reaches zero. Uses constant iterator state beyond the stored input.
- **Fully uncompress:** Makes `next` simple but takes $O(E)$ time and space and fails for counts near $10^9$.
- **Regex precomputation:** Split letters and counts into parallel arrays. Similar $O(C)$ storage, with more parsing machinery.
- **Multi-digit count:** Decimal accumulation must read all consecutive digits; treating digits individually is incorrect.
- **Count of one:** The first return exhausts the run and advances immediately.
- **Huge count:** Only one integer is stored; no repeated characters are allocated.
- **Exhausted iterator:** `hasNext` is false and `next` returns one space.
- **Repeated `hasNext` calls:** They do not consume data.
- **Uppercase and lowercase:** Both are stored as exact characters; case is preserved.
- **Adjacent runs with same letter:** If valid input supplied them separately, the iterator would return them consecutively; merging is unnecessary for correctness.
- **Positive-count guarantee:** Prevents constructor-created empty runs from violating the pointer invariant.
- **Short-circuit bound check:** Pointer range is tested before indexing the current pair.
- **Space fidelity:** Run precomputation is $O(C)$, not $O(1)$, even though it is exponentially smaller than a possible $O(E)$ expansion.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(C+q)$. Let $C$ be encoded length, $r$ the number of runs, $q$ the number of operations, and $E$ the expanded length. Constructor parsing visits each encoded character once, taking $O(C)$ time. Each `hasNext` and `next` performs constant work, so all operations cost $O(q)$ and total lifetime time is $O(C+q)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
