# Guided Example: Rearrange String k Distance Apart

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "aabbcc", "k": 3}`
- **Required output:** `"abcabc"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `s` and an integer `k`, rearrange `s` such that the same characters are **at least** distance `k` from each other. If it is not possible to rearrange the string, return an empty string `""`.

The objective is to compute `"abcabc"` from `{"s": "aabbcc", "k": 3}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why frequency determines priority.

High-frequency characters are the hardest to separate. Each copy after the first needs enough other positions between it and the preceding copy. If scarce separator characters are consumed while a frequent character remains unscheduled, the final copies may become impossible to place.

Choosing the eligible character with the greatest remaining count handles the most constrained work first. A less frequent eligible character has no greater future placement pressure. Swapping it later with the more frequent choice does not create an advantage: both are legal now, while delaying the character with more copies can only leave at least as much repeated work for fewer remaining positions.

The heap implements a max-priority rule using Python's min-heap. Each entry is `(-remaining_count, character)`. A larger remaining count produces a more negative number, which is popped first. When counts tie, tuple comparison uses the character as a deterministic secondary key. That lexicographic tie-break affects which valid answer is produced, not whether the distance rule is satisfied.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "aabbcc", "k": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Building the initial eligible heap.

`Counter(s)` records how many copies of every distinct lowercase letter are required. The list comprehension converts each `(character, count)` pair to `(-count, character)`, and `heapify` creates the priority queue. Initially every character is eligible because nothing has yet been placed.

`ans` stores output characters in order. The deque starts empty because no character is cooling down.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `Counter(s)` records how many copies of every distinct lower... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: One scheduling iteration.

The loop runs while at least one character is eligible in the heap. It pops `(v, c)`, appends `c` to the answer, and appends `(v + 1, c)` to the cooldown queue.

Because `v` is the negative remaining count before use, adding one consumes one copy. For example, a count of three is stored as `-3`; after placing one copy, the record becomes `-2`, meaning two remain. A value of zero means all copies have been scheduled.

The record enters the queue even when its new count is zero. This is intentional in the exact implementation: queue length represents how many output positions have elapsed, so every placed character contributes one chronological slot. An exhausted record will later leave the queue but will not return to the heap.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"abcabc"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "aabbcc", "k": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"abcabc"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Repeatedly scan all 26 counts:** At every posi:** - **Repeatedly scan all 26 counts:** At every position, choose the most frequent character whose next-allowed index has arrived. This costs $O(26n)=O(n)$ under the fixed alphabet and may be simpler than a heap, though less general for large alphabets.
- **- **Sort counts once without updates:** This is in:** - **Sort counts once without updates:** This is insufficient because remaining frequencies and eligibility change after every placement. The priority structure must reflect those changes.
- **- **Segment construction by maximum frequency:** D:** - **Segment construction by maximum frequency:** Distribute the most frequent letters among frequency-sized segments and verify that all but the last reach length `k`. This can run in linear time but requires careful handling of ties and segment filling.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(a)$. Let $n$ be the string length and let $a$ be the number of distinct characters. Here $a\le26$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
