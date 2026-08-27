# Guided Example: Maximum Score After Splitting a String

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "011101"}`
- **Required output:** `5`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `s` of zeros and ones, *return the maximum score after splitting the string into two **non-empty** substrings* (i.e. **left** substring and **right** substring).

The objective is to compute `5` from `{"s": "011101"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Update the score when one character crosses the split

For a chosen split, the score is:

$$
\text{zeros in the left part} + \text{ones in the right part}.
$$

Checking every split independently would repeatedly recount almost the same characters. Moving a split one position to the right changes only one character: that character leaves the right substring and enters the left substring.

The solution tracks:

- `l`: the number of zeros currently in the left substring.
- `r`: the number of ones currently in the right substring.

Their sum is the score for the current split.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "011101"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Initialize an empty-left conceptual state

The code starts with:



Before processing any character, imagine that the left side is empty and the right side is the whole string. There are zero left zeros, while `r` equals every one in `s`.

That imaginary split is not legal because the left substring is empty. The algorithm does not score it. Instead, each loop iteration first moves one character into the left side and then evaluates the resulting legal split.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The code starts with:



Before processing any character, im... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Never move the final character

The loop scans `s[:-1]` rather than all of `s`. This slice contains every character except the last. After processing character at index `i`, the split lies between `i` and `i+1`.

If the last character were processed, the right substring would become empty, which the contract forbids. Because `s` has length at least two, `s[:-1]` contains at least one character and every legal split is visited exactly once.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `5` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "011101"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `5` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Explicit character branches:** Replace the XOR:** - **Explicit character branches:** Replace the XOR arithmetic with `if x == "0"` and `else`. It is more immediately readable and has identical complexity.
- **Prefix and suffix arrays:** Precompute zero counts from the left and one counts from the right. This answers each split quickly but uses $O(n)$ extra storage for information two counters can maintain.
- **Recount each split:** Scanning both substrings for every boundary takes $O(n^2)$ time.
- **One-pass algebraic variant:** Maximize left zeros minus left ones, then add total ones. It can avoid the separate initial count but needs careful handling of the final character.
- **All zeros:** `r` remains zero and `l` grows at each legal split, so the best split puts all but the final zero on the left.
- **All ones:** `l` remains zero and `r` decreases; the first split leaves the most ones on the right.
- **Length two:** The loop evaluates exactly the only legal split.
- **Score zero:** For `"10"`, neither the left contains a zero nor the right a one, so zero is correctly returned.
- **Nonempty constraint:** Excluding the final source character from the loop is essential; scoring after it would use an illegal empty right substring.
- **Binary-input guarantee:** The XOR trick relies on `int(x)` being exactly zero or one.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the string length. `s.count("1")` scans the string once in $O(n)$ time. The loop scans $n-1$ characters and performs constant work per character, so total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
