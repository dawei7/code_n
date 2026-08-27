# Guided Example: Buddy Strings

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "ab", "goal": "ba"}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given two strings `s` and `goal`, return `true`* if you can swap two letters in *`s`* so the result is equal to *`goal`*, otherwise, return *`false`*.*

The objective is to compute `true` from `{"s": "ab", "goal": "ba"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: One swap preserves length and character counts

Swapping two positions cannot change string length or the multiset of characters. Therefore, two immediate necessary conditions are:

- `len(s) == len(goal)`;
- `Counter(s) == Counter(goal)`.

If lengths differ, the function returns false before indexing. If Counters differ, no rearrangement by swapping—let alone exactly one swap—can transform `s` into `goal`.

After these checks, only the positions of equal multiset characters remain to analyze.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "ab", "goal": "ba"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Count mismatched positions

`diff` is:

`sum(s[i] != goal[i] for i in range(n))`.

Each Boolean contributes one exactly where the strings differ.

A swap touches two distinct indices, so there are only two successful structural cases:

1. exactly two positions differ, and swapping them repairs both;
2. no positions differ, but swapping two equal characters leaves the string unchanged.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `diff` is:

`sum(s[i] != goal[i] for i in range(n))`.

Each ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Case one: exactly two mismatches

Suppose mismatch positions are `i` and `j`. Because the complete character Counters are equal and every other position already matches, the two characters must cross:

$$
s[i]=goal[j],\qquad s[j]=goal[i].
$$

Swapping `s[i]` and `s[j]` makes both positions correct and leaves all other positions unchanged.

Thus, after multiset equality has been established, `diff == 2` is sufficient.

It is also necessary for transforming two unequal strings with one swap: a swap can change at most two positions, and it cannot repair exactly one mismatch under equal character counts.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "ab", "goal": "ba"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Collect mismatch indices:** Store up to three :** - **Collect mismatch indices:** Store up to three and stop early. It makes the cross-character test explicit, though Counter equality already guarantees it when there are two.
- **- **Try every pair of indices:** This takes `O(n^2:** - **Try every pair of indices:** This takes `O(n^2)` swaps and repeated comparison, unnecessary once mismatch structure is known.
- **- **Different lengths:** Return false immediately.:** - **Different lengths:** Return false immediately.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the common string length. Building both Counters takes `O(n)` time. Counting mismatches takes another `O(n)`. Total time is `O(n)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
