# Guided Example: Sum of Beauty of All Substrings

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "aabcb"}`
- **Required output:** `5`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

The **beauty** of a string is the difference in frequencies between the most frequent and least frequent characters.

The objective is to compute `5` from `{"s": "aabcb"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Enumerate every substring by its start and end

Every non-empty substring has a unique start index `i` and end index `j >= i`. The exact solution loops over every start and expands the end one character at a time.

For each new start, `cnt = Counter()` begins empty. When `j` advances, `cnt[s[j]] += 1` updates frequencies for exactly substring `s[i : j + 1]`.

Incremental counting avoids rescanning the entire substring for each end.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "aabcb"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Compute beauty from present characters only

The beauty is the maximum frequency minus the minimum frequency among characters that occur in the substring.

`cnt.values()` contains counts only for characters already seen in the current range. Therefore:

`max(cnt.values()) - min(cnt.values())`

uses the correct positive frequencies and does not mistakenly include zero for absent alphabet letters.

This detail is essential. If absent letters with count zero participated, almost every substring would receive an inflated beauty equal to its maximum frequency.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The beauty is the maximum frequency minus the minimum freque... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why max and min are constant-factor work

The string contains only 26 lowercase English letters. The Counter has at most 26 entries, so scanning its values for maximum and minimum takes at most 26 comparisons each.

Although those scans occur inside nested substring loops, 26 is a fixed constraint-domain constant. Thus each end extension has $O(1)$ alphabet work in asymptotic terms.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `5` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "aabcb"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `5` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Recount every substring:** Scanning each range:** - **Recount every substring:** Scanning each range from scratch can take $O(n^3)$ time.
- **Fixed array of 26 counts:** It avoids hash overhead and makes the bounded alphabet explicit, while retaining the same complexity.
- **Maintain frequency-of-frequencies:** It can update minima and maxima more cleverly, but is unnecessary for only 26 letters.
- **One-character string:** Its sole substring has beauty zero.
- **All characters equal:** Every substring has one frequency value, so total beauty is zero.
- **All characters distinct within a substring:** Every present count is one and beauty is zero.
- **Absent characters:** They must not contribute zero to the minimum.
- **Repeated substring text:** Different positions are distinct substrings and each contributes.
- **Counter reset per start:** Frequencies from earlier start positions must not leak.
- **End expansion:** Adding one character preserves exact counts without rescanning prior characters.
- **Non-zero beauty:** It requires at least two present characters with different frequencies.
- **Lowercase guarantee:** It bounds Counter size by 26.
- **No modulo:** The problem requests the full integer sum, and Python handles its magnitude.
- **Input preservation:** The string is read only and no substrings are materialized.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. Let $n$ be the string length and $A=26$ the fixed alphabet size. There are $n(n+1)/2=O(n^2)$ substrings. Updating one count is expected $O(1)$, and scanning at most $A$ frequencies is $O(A)=O(1)$ under the fixed alphabet. Total time is $O(n^2)$, matching the manifest.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
