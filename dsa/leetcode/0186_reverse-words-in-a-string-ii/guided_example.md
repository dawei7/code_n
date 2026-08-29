# Guided Example: Reverse Words in a String II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": ["a"]}`
- **Required output:** `["a"]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a character array `s`, reverse the order of the **words**.

The objective is to compute `["a"]` from `{"s": ["a"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Distinguish reversing words from reversing characters

The requested transformation changes the order of whole words while preserving
the character order inside every word. A direct character-array reversal does
only half the job. For example, reversing all characters of `the sky` produces
`yks eht`: the word order is now correct, but every word is spelled backward.

The standard in-place idea uses two kinds of reversal whose effects cancel in
the right places. The local editorial reverses the whole array first and then
each word. The exact stored solution performs the same operations in the
opposite order: it reverses each original word first, then reverses the entire
array. Both orders lead to the same required final arrangement.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": ["a"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Use an inclusive two-pointer reversal

The nested `reverse(i, j)` helper treats both endpoints as inclusive. While
`i < j`, it swaps `s[i]` with `s[j]`, moves `i` right, and moves `j` left.
The outermost characters of the interval reach their final mirrored positions
first, then the next pair, and so on.

When the pointers meet, the middle character of an odd-length interval is
already in the correct position and needs no swap. When they cross, every pair
has been exchanged. The helper mutates `s` directly and stores only two indices
and one swap's temporary values, so it does not allocate another character
array.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Find every original word boundary

The main scan uses `i` as the first index of the current word. It enumerates
the array with index `j` and character `c`. When `c` is a space, the word ends
at `j - 1`, so `reverse(i, j - 1)` reverses that word and `i = j + 1` points to
the next word's first character.

The space itself is never included in a word reversal. This preserves the
separator characters exactly. The Reference guarantees one space between
words and no leading or trailing space, so after a separator, `j + 1` really
is the beginning of another nonempty word.

The last word has no following space to trigger the first branch. The
`elif j == n - 1` branch handles that boundary explicitly by reversing the
inclusive interval from `i` through `j`. Without this branch, every word except
the last would be reversed and the final whole-array reversal would leave the
last word backward in the output.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `["a"]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": ["a"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `["a"]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Editorial operation order:** Reverse the whole array first, then scan and reverse each resulting word; it has the same $O(n)$ time and $O(1)$ space.
- **Split, reverse, and join:** Very concise for immutable strings, but allocates words and a new result, violating the in-place requirement.
- **Manual shifting of words:** Can preserve spelling but repeated movement may become $O(n^2)$ and is unnecessarily complicated.
- **Single character:** Both inclusive reversals are empty operations.
- **Single word:** It is reversed locally and globally, returning to its original spelling and position.
- **Two words:** Each is restored internally while their positions swap.
- **Digits and mixed case:** They are ordinary non-space characters and require no special logic.
- **Final word:** Must be handled at `n - 1` because it has no trailing delimiter.
- **Spacing guarantees:** The exact boundary logic relies on no leading, trailing, or repeated spaces; broader whitespace rules would need additional handling.
- **Missing typing import:** Add or provide `List` when running the file outside a harness that defines it.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of characters. The word-boundary scan visits $n$
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
