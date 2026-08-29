# Guided Example: Lexicographically Smallest String After a Swap

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "45320"}`
- **Required output:** `"43520"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `s` containing only digits, return the lexicographically smallest string that can be obtained after swapping **adjacent** digits in `s` with the same **parity** at most **once**.

The objective is to compute `"43520"` from `{"s": "45320"}` while avoiding redundant calculations and unnecessary overhead.

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

**Understand what makes one string lexicographically smaller.** Compare two equal-length strings from left to right. The first position where they differ decides which string is smaller. A smaller digit at that earliest differing position wins, regardless of every later character.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "45320"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

One adjacent swap at indices $i$ and $i+1$ changes no position before $i$. At position $i$, it replaces `s[i]` by `s[i+1]`. Such a swap improves the string only when the right digit is smaller:

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

If the pair is already increasing, swapping makes the string larger. If the digits are equal, swapping changes nothing.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"43520"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "45320"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"43520"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Convert to a character list:** Scan adjacent digits, swap the first legal inversion in place, and join. It is often easier to read but always allocates an $O(n)$ list.
- **Try every legal swap and take `min`:** Correct for $n\le100$, but it constructs up to $O(n)$ strings of length $n$, costing $O(n^2)$ time and space traffic.
- **Swap the largest difference:** Incorrect. Lexicographic order prioritizes the earliest changed index, not the magnitude of a later improvement.
- **Different parity:** The pair cannot be swapped even when it is descending.
- **Equal digits:** They have the same parity, but swapping has no effect and is unnecessary.
- **Already optimal:** Returning `s` is valid because the operation is optional.
- **First pair is a legal inversion:** It is immediately optimal; no later position can compete with improving index zero.
- **Leading zeros:** They are ordinary string digits. Moving a zero left can make the result smaller, and no numeric conversion should remove it.
- **Two-character string:** There is one pair; it is swapped exactly when parity matches and it descends.
- **Character-code parity:** The trick relies on consecutive decimal digit code points. It should not be generalized blindly to arbitrary characters.
- **`pairwise` availability:** The exact source assumes an environment providing Python's adjacent-pair iterator and `map`/`ord` built-ins.
- **Input preservation:** Strings are immutable, so the original value is never modified.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be string length. At most $n-1$ adjacent pairs are examined, with constant work per pair, so time is $O(n)$. If a swap occurs, slicing and concatenating the $n$ output characters also takes $O(n)$; the total remains linear.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
