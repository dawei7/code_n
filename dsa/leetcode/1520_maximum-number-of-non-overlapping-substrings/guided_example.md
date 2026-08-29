# Guided Example: Maximum Number of Non-Overlapping Substrings

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "adefaddaccc"}`
- **Required output:** `["e", "f", "ccc"]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `s` of lowercase letters, you need to find the maximum number of **non-empty** substrings of `s` that meet the following conditions:

The objective is to compute `["e", "f", "ccc"]` from `{"s": "adefaddaccc"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A valid substring is determined by character occurrence ranges

If a substring contains character `c`, it must include every occurrence of `c`. The source first records `first[c]` and `last[c]` for each lowercase letter.

Any minimal valid substring must begin at the first occurrence of some character. Starting later would omit that character's earlier occurrence, while starting earlier without necessity would only increase length. The outer loop therefore considers an index only when `first[label] == left`.

The two arrays have fixed length 26. Missing letters keep sentinel first position `len(s)` and last position minus one.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "adefaddaccc"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Expanding one candidate to closure

For a candidate starting at `left`, the initial right boundary is the last occurrence of its starting character. The algorithm scans from left through the current right boundary.

Whenever it encounters character `inner`, a valid interval containing that position must also contain every occurrence of `inner`. Two checks follow:

- If `first[inner] < left`, this candidate is impossible. It already contains `inner` but starts after an earlier occurrence, and moving left would mean it is not the minimal candidate for this outer start. The loop breaks.
- Otherwise, `right = max(right, last[inner])` extends the interval far enough to include the character's final occurrence.

Extending right may expose new characters, whose last occurrences may extend it again. The while loop continues until the scan passes the final closed boundary.

Python's `while ... else` executes the `else` block only when the loop ends normally, not when `break` rejects the candidate. Thus only fully closed valid intervals reach selection.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why a successful closure is valid and minimal

When the scan completes, every character appearing between `left` and `right` has its first occurrence no earlier than `left` and last occurrence no later than the final `right`. Therefore, all occurrences of every contained character lie inside the interval.

The starting character requires both endpoints initially, and every later boundary extension is forced by a contained character. No shorter right endpoint can make the substring valid for this start. It is the minimal valid interval beginning at `left`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `["e", "f", "ccc"]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "adefaddaccc"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `["e", "f", "ccc"]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Generate intervals then sort by end:** Build every valid minimal character interval and run standard earliest-finish interval scheduling. It is equivalent but uses an explicit candidate list.
- **Dynamic programming over positions:** It can optimize count and total length but is more state than the fixed-alphabet greedy structure needs.
- **One repeated character:** Its only minimal valid substring spans all occurrences.
- **Unique character:** Its candidate can be the one-character substring, maximizing count and minimizing length.
- **Invalid candidate start:** Encountering a character whose first occurrence lies earlier forces rejection rather than leftward expansion.
- **Nested valid intervals:** The later, smaller interval replaces the previous selection to improve length without reducing count.
- **Disjoint valid intervals:** Each is appended, increasing the count.
- **Adjacent intervals:** They are nonoverlapping because the next left is greater than the previous end.
- **Substring copying:** Python slices allocate new strings even though the index algorithm uses constant fixed state.
- **Lowercase alphabet:** The constant 26 factor is essential to the linear-time bound.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The initial occurrence scan is $O(n)$. There are at most 26 candidate starts, one per lowercase letter. Each closure scan can traverse up to $n$ characters, so a direct bound is $O(26n)=O(n)$ because the alphabet size is fixed.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
