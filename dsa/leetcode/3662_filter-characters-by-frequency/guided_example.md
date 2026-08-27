# Guided Example: Filter Characters by Frequency

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "aadbbcccca", "k": 3}`
- **Required output:** `"dbb"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s` consisting of lowercase English letters and an integer `k`.

The objective is to compute `"dbb"` from `{"s": "aadbbcccca", "k": 3}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The decision depends on the whole string

A character occurrence is kept when that character’s total frequency in `s` is strictly less than `k`. The decision cannot be made from the prefix seen so far.

For example, the first `'a'` might initially appear rare but later occurrences can raise its final count to `k`, requiring every `'a'`—including the first—to be removed. This is why the source uses two passes rather than filtering while it counts.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "aadbbcccca", "k": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Count every character first

`Counter(s)` builds a mapping from each distinct character to its total occurrence count. If `d` distinct letters appear, the map has `d` entries.

The input contains only lowercase English letters, so `d <= 26`, but describing the structure as `O(d)` keeps the method general.

Frequencies are global and based on the original string. Removing one character does not lower the frequency used to decide whether later occurrences qualify. The entire filter is determined before output construction begins.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `Counter(s)` builds a mapping from each distinct character t... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Scan the original order and keep all qualifying occurrences

The second loop visits characters in exactly the order they occur in `s`. For character `c`, it tests

`cnt[c] < k`.

If true, it appends that occurrence to `ans`. If false, it skips it.

The comparison is strict. A character appearing exactly `k` times is removed, as is one appearing more than `k` times.

When one character qualifies, every occurrence qualifies because all use the same total `cnt[c]`. The task does not ask to keep only one representative or only the first `k - 1` copies. The source appends each qualifying occurrence encountered.

Because the loop never reorders characters, the result is a stable subsequence of `s`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"dbb"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "aadbbcccca", "k": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"dbb"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Use a fixed 26-entry array:** Map each lowerca:** - **Use a fixed 26-entry array:** Map each lowercase letter to an index. This gives the same `O(n)` time with constant-sized count storage.
- **Call `s.count(c)` inside the filter:** Each count scans the string, producing `O(n^2)` time in the worst case.
- **Filter during the first pass:** A later occurrence can change a character from qualifying to disqualified, so early output decisions are unsafe.
- **Sort qualifying characters:** Sorting destroys the required original order.
- **Keep one copy per qualifying character:** The statement keeps every occurrence, not only distinct representatives.
- **Frequency exactly `k`:** All occurrences are removed because the condition is “fewer than,” not “at most.”
- **`k = 1`:** Every present character has frequency at least one, so the result is empty.
- **All characters occur once and `k > 1`:** Every occurrence qualifies and the original string is returned.
- **One character fills the string:** It is removed when its frequency is at least `k`; with `k <= n`, the result is empty.
- **Empty result:** Joining an empty list returns `""` without special handling.
- **Repeated qualifying character:** Every copy is appended in its original position.
- **Input preservation:** Strings are immutable, and the method creates new count and output structures.
- **Missing import:** The stored source uses `Counter` without importing it. Standalone Python needs `from collections import Counter` unless the harness supplies it.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the string length and `d` the number of distinct characters.
- **Auxiliary Space Complexity:** $O(d)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
