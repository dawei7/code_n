# Guided Example: Find Longest Awesome Substring

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "3242415"}`
- **Required output:** `5`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s`. An **awesome** substring is a non-empty substring of `s` such that we can make any number of swaps in order to make it a palindrome.

The objective is to compute `5` from `{"s": "3242415"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A palindrome depends on frequency parity

Characters may be rearranged arbitrarily inside the chosen substring. Their original order therefore does not determine whether a palindrome can be formed; only the counts matter.

Every character in an even-length palindrome appears an even number of times. In an odd-length palindrome, exactly one character may have an odd count and occupy the center. Thus a digit substring is awesome exactly when at most one of its ten digit counts is odd.

The solution represents these ten parities with a ten-bit mask. Bit `v` is one when digit `v` has appeared an odd number of times in the current prefix and zero when its count is even.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "3242415"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Update prefix parity with XOR

`st` starts at zero for the empty prefix because every digit count is even. Reading digit `v` executes `st ^= 1 << v`.

XOR toggles exactly bit `v`. The first occurrence changes its parity from even to odd; the next changes it back to even. Actual counts are unnecessary because only odd versus even affects palindrome feasibility.

For a substring ending at index `i` and beginning after an earlier prefix ending at `p`, its parity mask is the XOR of the two prefix masks. Bits equal in both prefixes cancel, leaving precisely the parities contributed by positions `p+1` through `i`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `st` starts at zero for the empty prefix because every digit... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Case one: every substring count is even

If the current `st` has appeared before at prefix index `p`, their XOR is zero. Therefore all digit counts in substring `s[p+1:i+1]` are even.

The dictionary `d` stores the earliest index for each observed mask. Using the earliest equal mask produces the longest substring ending at `i`, so the candidate length is `i - d[st]`.

The initialization `d = {0: -1}` represents the empty prefix before index zero. It allows a prefix beginning at the first character to be recognized. If the current mask is zero at index `i`, its length is `i - (-1) = i+1`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `5` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "3242415"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `5` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Enumerate all substrings:** Updating counts fo:** - **Enumerate all substrings:** Updating counts for every pair of endpoints costs at least $O(N^2)$.
- **Store full frequency vectors:** Prefix counts work but make comparisons heavier; a parity mask contains exactly the needed information.
- **Store latest mask index:** It is wrong for maximum length because later prefixes produce shorter candidates.
- **All counts even:** Equal prefix masks detect this case.
- **Exactly one odd count:** A one-bit-different prefix mask detects this case.
- **Two odd counts:** The substring cannot be rearranged into a palindrome and is intentionally ignored.
- **Single character:** It always has one odd count and is awesome, supporting initial answer one.
- **Entire string awesome:** The empty-prefix entry at negative one permits returning full length.
- **Leading zeros:** Character conversion treats zero as ordinary digit index zero.
- **Repeated digit:** Each occurrence toggles the same bit, so pairs cancel.
- **Nonempty input:** The contract guarantees at least one character; otherwise initializing answer to one would need adjustment.
- **Fixed digit alphabet:** Ten neighbor checks and at most 1024 states are constant only because input contains digits.
- **Rearrangement permission:** Without arbitrary swaps, parity alone would not characterize palindromic substrings.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be string length. For each character, the solution performs one mask update, one exact lookup, and ten neighbor lookups. Ten is fixed by the digit alphabet, so work per character is constant and total time is $O(N)$.
- **Auxiliary Space Complexity:** $O(2^D)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
