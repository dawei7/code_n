# Guided Example: Shuffle String

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "codeleet", "indices": [4, 5, 6, 7, 0, 2, 1, 3]}`
- **Required output:** `"leetcode"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s` and an integer array `indices` of the **same length**. The string `s` will be shuffled such that the character at the $i^{\text{th}}$ position moves to $\text{indices}[i]$ in the shuffled string.

The objective is to compute `"leetcode"` from `{"s": "codeleet", "indices": [4, 5, 6, 7, 0, 2, 1, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Read indices as destinations

The contract says the character currently at position `i` must move to position `indices[i]`. This is a destination mapping, not a list of source positions to read in result order.

The stored solution allocates `ans = [null] * len(s)`, giving one output slot for every character. It then iterates with `zip(s, indices)`. Each pair contains current character `c` and that character's destination `j`, so `ans[j] = c` places it directly where it belongs.

After every character has been placed, `"".join(ans)` converts the list of one-character strings into the returned string.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "codeleet", "indices": [4, 5, 6, 7, 0, 2, 1, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why a list is necessary in Python

Python strings are immutable. Assigning directly to a position of `s` is not allowed. A list provides mutable slots during reconstruction, and joining once is efficient.

Initializing with `null` is safe because the permutation guarantee ensures every slot is overwritten with a string before `join`. If the indices were malformed, an unfilled `null` would cause joining to fail, which would expose the violated contract rather than silently inventing a character.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The permutation guarantee

Every `indices[i]` lies from zero through `n-1`, so no assignment is out of bounds. All index values are unique and there are exactly `n` of them. Therefore, they form a permutation of every valid output position.

Uniqueness means two characters never compete for the same slot. Having `n` distinct destinations within an `n`-element range also means no output slot is omitted.

This is the central reason direct placement works without collision handling.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"leetcode"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "codeleet", "indices": [4, 5, 6, 7, 0, 2, 1, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"leetcode"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Sort by destination:** Zip each character with its index, sort pairs, and join characters. It is correct but unnecessarily costs $O(N\log N)$.
- **Build the inverse permutation:** First record which source belongs to each destination, then read the string. It adds an extra pass without improving bounds.
- **Identity permutation:** Every assignment writes to the same position and returns the original string.
- **Single character:** Its only valid destination is zero.
- **Repeated letters:** Each occurrence is placed according to its own paired destination.
- **Destination zero or n minus one:** Both endpoints are ordinary valid list indices.
- **Malformed duplicate destination:** It would overwrite a slot and leave another unfilled, but uniqueness excludes this case.
- **Unequal input lengths:** `zip` would truncate, but equal lengths are guaranteed.
- **String immutability:** The list is required for indexed writes; repeated string concatenation would be less efficient.
- **Required type import:** `List` must be available for the annotation in a standalone module.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be string length. Creating the result list takes $O(N)$ time. The loop performs $N$ constant-time assignments, and joining copies $N$ characters into the final string. Total time is $O(N)$.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
