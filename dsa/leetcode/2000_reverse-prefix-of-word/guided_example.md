# Guided Example: Reverse Prefix of Word

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"word": "abcdefd", "ch": "d"}`
- **Required output:** `"dcbaefd"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a **0-indexed** string `word` and a character `ch`, **reverse** the segment of `word` that starts at index `0` and ends at the index of the **first occurrence** of `ch` (**inclusive**). If the character `ch` does not exist in `word`, do nothing.

The objective is to compute `"dcbaefd"` from `{"word": "abcdefd", "ch": "d"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Locate the exact reversal endpoint

`word.find(ch)` returns the index of the first occurrence of `ch`. That is exactly the endpoint specified by the problem. If the character is absent, Python returns -1.

The source stores this result in `i` and uses a conditional expression. When `i == -1`, it returns the original `word` unchanged. This explicit check is important because using -1 directly in slicing would refer to the last character rather than mean "not found."

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"word": "abcdefd", "ch": "d"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Reverse the inclusive prefix with a negative step

When `ch` is present, the prefix includes indices zero through `i`. Python slice

`word[i::-1]`

starts at index `i`, moves backward by one, and continues to the beginning because the stop is omitted. It therefore yields characters

`word[i], word[i - 1], ..., word[0]`.

The character `ch` itself appears first in this reversed prefix because the endpoint is inclusive.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Append the untouched suffix

`word[i + 1 :]` contains every character strictly after the first `ch` in its original order. Concatenating the reversed prefix and this suffix produces a string of the same length with exactly the requested segment changed.

For `word="abcdefd"` and `ch="d"`, `find` returns three. The first slice is `"dcba"` and the second is `"efd"`, producing `"dcbaefd"`. The later d does not affect the result because `find` chose the first occurrence.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"dcbaefd"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"word": "abcdefd", "ch": "d"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"dcbaefd"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Two-pointer character list:** Convert to a list, swap prefix endpoints inward, and join. It is explicit and linear but also uses $O(N)$ Python space.
- **Stack:** Push through the first target and pop to reverse, then append the suffix; more machinery for the same bounds.
- **Manual concatenation in a loop:** Repeated immutable-string addition can become $O(N^2)$ in Python.
- **Character absent:** Return `word`; do not use the -1 index as a real endpoint.
- **Character at index zero:** Reversing one character leaves the word unchanged.
- **Character at final index:** The entire word is reversed.
- **Repeated target character:** Only the first occurrence determines the prefix.
- **One-character word:** Both present and absent cases are handled.
- **Inclusive endpoint:** `word[i::-1]` includes `word[i]`.
- **Suffix preservation:** `word[i + 1 :]` keeps its original order.
- **Lowercase guarantee:** No case normalization or Unicode matching policy is needed.
- **Input preservation:** Strings are immutable and the method returns a newly constructed value when reversal occurs.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the word length. `find` scans up to $N$ characters. When the character is present, the two slices collectively copy $N$ characters and concatenation builds an $N$-character result. Total time is $O(N)$.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
