# Guided Example: Check Distances Between Same Letters

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "abaccb", "distance": [1, 3, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** string `s` consisting of only lowercase English letters, where each letter in `s` appears **exactly** **twice**. You are also given a **0-indexed** integer array `distance` of length `26`.

The objective is to compute `true` from `{"s": "abaccb", "distance": [1, 3, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Measure a letter when its second occurrence arrives

Each appearing letter occurs exactly twice. During one left-to-right scan, the algorithm remembers the position of the first occurrence. At the second, it computes how many characters lie strictly between them and compares that count with the letter's required distance.

If any comparison fails, the whole string is not well-spaced and the method returns false immediately. If every appearing letter passes, it returns true.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "abaccb", "distance": [1, 3, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Use one-based positions so zero means unseen

The scan is:



`i` begins at one rather than zero. `d` is a `defaultdict(int)`, so an unseen letter returns stored position zero. Because real stored positions start at one, the condition `if d[j]` cleanly distinguishes first and second occurrences.

With zero-based positions, a genuine first occurrence at index zero would also store zero and be mistaken for unseen on its second occurrence. The one-based convention avoids needing a separate sentinel such as `-1` or a membership test.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The scan is:



`i` begins at one rather than zero.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Map characters to distance indices

`map(ord, s)` converts each character to its Unicode code point. Subtracting `ord("a")` maps lowercase letters to integers zero through twenty-five:



This `j` indexes both the required `distance` array and the remembered-position dictionary.

Letters absent from `s` never enter the loop, so their `distance[j]` entries are naturally ignored.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "abaccb", "distance": [1, 3, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **26-entry position array:** Initialize all slot:** - **26-entry position array:** Initialize all slots to `-1` and store zero-based first positions. This avoids hashing and keeps the same $O(1)$ space.
- **Find first and last occurrence per letter:** Repeated string searches can still be acceptable for 26 letters but scan the string multiple times.
- **Adjacent occurrences:** The computed between-count is zero.
- **Letter beginning at index zero:** One-based storage records it as one, so it is not confused with the unseen sentinel.
- **Absent letter:** Its distance entry is ignored because its key is never processed.
- **Immediate mismatch:** Early false is final; later positions cannot change the measured pair.
- **Exactly two occurrence guarantee:** It makes the unconditional overwrite after validation harmless.
- **All appearing letters valid:** Completing the loop proves true.
- **Fixed lowercase alphabet:** Dictionary storage is constant despite using a mapping type.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the string length. `map` and `enumerate` are lazy, and the loop processes every character at most once. Dictionary access and arithmetic take expected $O(1)$ time, giving $O(n)$ total time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
