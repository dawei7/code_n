# Guided Example: Find Mirror Score of a String

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "aczzx"}`
- **Required output:** `5`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s`.

The objective is to compute `5` from `{"s": "aczzx"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

**The current index needs the closest available mirror on its left.** The process is fixed: scan from left to right, and whenever index $i$ can pair with an earlier unmarked mirror character, choose the closest such index $j$. Once paired, both positions are marked and can never participate again.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "aczzx"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

For each letter, the source stores the indices of its currently unmarked occurrences in a list. These lists act as stacks. As the scan proceeds left to right, indices are appended in increasing order. Therefore, the last index in a letter's list is always its closest unmatched occurrence to the current position. A stack provides exactly the required choice without searching backward through the string.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For each letter, the source stores the indices of its curren... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

The dictionary `d` is a `defaultdict(list)`. A key is a lowercase letter and its value is the stack of unmatched indices holding that letter. Across all stacks, an index appears if and only if it has been scanned but not marked.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `5` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "aczzx"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `5` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Backward scan for every index:** Searching lef:** - **Backward scan for every index:** Searching left through the string for the closest unmarked mirror directly can take $O(n^2)$ time and requires a separate marked array.
- **Queue per letter:** Removing the earliest stored index chooses the farthest unmatched mirror, violating the closest-index rule. The per-letter container must be LIFO.
- **One global stack:** The closest unmatched character overall may not be the required mirror. Separate stacks allow direct access to the correct letter class.
- **Fixed array of 26 stacks:** A list indexed by alphabet position works equally well and avoids dictionary key creation. The protected source uses a dictionary for concise character-based access.
- **No possible mirrors:** For a string such as `"abcdef"`, every index is pushed and none is popped, so the score remains zero.
- **Repeated same letter:** Identical letters do not mirror each other. They accumulate on one stack until their opposite letter appears, at which point the most recent is consumed first.
- **Nested pairings:** A later mirror always pops the closest currently unmatched index, regardless of earlier completed pairs. Marked indices were removed and cannot interfere.
- **Current index after a match:** It must not be pushed after pairing. Both positions become marked immediately, so storing `i` would allow an illegal second use.
- **Empty mirror stack:** Access through `defaultdict` yields an empty list, and the source correctly stores the current index instead of attempting a pop.
- **Large score:** Distances can accumulate beyond a small fixed-width integer in related constraints. Python's arbitrary-precision integer makes the addition safe.
- **Lowercase-only contract:** The character-code formula relies on the contiguous lowercase English alphabet and should not be generalized to arbitrary Unicode characters without a different mapping.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n=\lvert\texttt{s}\rvert$. Each index is visited once. It is either appended to one list or immediately paired. An appended index can be popped at most once later. Dictionary access, list append, and list pop from the end take expected $O(1)$ time. Mirror computation is constant work. Total expected time is therefore $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
