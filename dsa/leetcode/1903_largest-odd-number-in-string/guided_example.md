# Guided Example: Largest Odd Number in String

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"num": "52"}`
- **Required output:** `"5"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `num`, representing a large integer. Return *the **largest-valued odd** integer (as a string) that is a **non-empty substring** of *`num`*, or an empty string *`""`* if no odd integer exists*.

The objective is to compute `"5"` from `{"num": "52"}` while avoiding redundant calculations and unnecessary overhead.

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

**Oddness depends only on the last digit.** A decimal integer is odd exactly when its units digit is one of `1, 3, 5, 7, 9`. For any substring of `num`, only that substring's final character determines parity. The algorithm therefore searches for a suitable ending position rather than evaluating large numeric substrings.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"num": "52"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

**For a fixed ending, start at index zero.** Suppose an odd digit occurs at index `i`. Any substring ending there is odd. Among those substrings, `num[:i + 1]` has the greatest length because it starts at the beginning. The original number has no leading zeros, so this prefix represents an $(i+1)$-digit positive integer. Every later-starting substring has fewer digits and is therefore numerically smaller, regardless of its first digit.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | **For a fixed ending, start at index zero.** Suppose an odd ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

Even if leading zeros were present, adding them would not increase numeric value, but the stated no-leading-zero guarantee makes the length comparison direct and eliminates representational ambiguity for the chosen prefix.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"5"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"num": "52"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"5"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Forward scan remembering the last odd index:**:** - **Forward scan remembering the last odd index:** This also takes $O(n)$ time and returns the same prefix, but the reverse scan can return immediately.
- **Enumerate all substrings:** There are $O(n^2)$ candidates and parsing them is unnecessary because parity and length determine the answer structure.
- **Convert the full string to an integer:** The input may have $10^5$ digits and exceed practical numeric limits. Full conversion provides no useful information beyond the final digit.
- **Entire number odd:** The last digit succeeds and the whole string is returned.
- **All digits even:** No odd substring exists because every possible ending is even, so the empty string is correct.
- **Odd digit only at index zero:** The result is the first character, as in `"52"`.
- **Several odd digits:** Only the rightmost matters; its prefix strictly contains more digits than every earlier odd prefix.
- **No leading zeros:** This guarantees a longer chosen prefix is numerically larger in the usual decimal representation.
- **Output allocation:** The algorithmic working state is constant, but Python materializes `num[:i + 1]` as a new string.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of digits. In the worst case, the backward loop examines all $n$ positions, so search time is $O(n)$. Constructing the returned prefix copies up to $n$ characters in Python, also $O(n)$ time. Total time remains $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
